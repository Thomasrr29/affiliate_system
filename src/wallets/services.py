from sqlalchemy.ext.asyncio import AsyncSession 
from src.assets.services import AssetsService
from src.clients.models import Client
from src.clients.enums import ClientType
from sqlalchemy.orm import selectinload
from fastapi.encoders import jsonable_encoder
from src.wallets import Wallet
from fastapi import HTTPException
from typing import TYPE_CHECKING
from datetime import datetime
from sqlmodel import select


###
# SERVICES WITHIN TRANSACTIONS PROCESS (TRANSACTIONS OF A LOT PROCESS WITH A SAME SESSION)
# CreateWalletWithBalances
# Create wallet 
# ###    

WALLET_BALANCES_FOR_CLIENT = {
    ClientType.CLIENT: ["POINTS"],
    ClientType.AFFILIATE: ["POINTS", "MONEY"],
    ClientType.ATHLETE: ["POINTS", "MONEY"]
}


class WalletsService():

    async def GetAllWallets(db: AsyncSession, limit: int = 10, offset: int = 0): 
        
        result = await db.execute(
            select(Wallet)
            .limit(limit)
            .offset(offset)
            .options(selectinload(Wallet.client)))
        db_wallets = result.scalars().all()

        if not db_wallets:
            raise HTTPException(status_code=404, detail="Wallets not found")
        
        return jsonable_encoder(db_wallets)

    async def GetWalletByClientId(db: AsyncSession, client_id: int): 

        result = await db.execute(
            select(Wallet)
            .where(Wallet.client_id == client_id)
            .options(selectinload(Wallet.client)))
        db_wallet = result.scalar_one_or_none()

        if not db_wallet: 
             raise HTTPException(status_code=404, detail=f'wallet wasnt found with the id: {client_id}')
        
        wallet_dict = jsonable_encoder(db_wallet)

        # Manually ensure client data is included
        if db_wallet.client:
            wallet_dict["client"] = jsonable_encoder(db_wallet.client)
            # Remove client's wallet to prevent circular references
            if "wallet" in wallet_dict["client"]:
                del wallet_dict["client"]["wallet"]
        
        return wallet_dict

    async def CreateWallet(db: AsyncSession, client_id: int): 

        result = await db.execute(select(Wallet).where(Wallet.client_id == client_id))
        wallet_existence = result.scalar_one_or_none()

        if wallet_existence:
            raise HTTPException(status_code=401, detail=f'Wallet for the client {client_id} already exists')
        
        wallet_data = {
            "client_id": client_id,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        
        wallet_create = Wallet.model_validate(wallet_data)

        db.add(wallet_create)
        await db.flush()
        await db.refresh(wallet_create)

        return jsonable_encoder(wallet_create, exclude="client")

    async def CreateWalletWithBalances(db: AsyncSession, client_id: int):

        assets_created = []

        try: 

            db_client = await db.get(Client, client_id)

            if not db_client: 
                raise HTTPException(status_code=400, detail="Issue creating client before wallet creation")

            wallet_created = await WalletsService.CreateWallet(db, db_client.id)
            assets_client = WALLET_BALANCES_FOR_CLIENT.get(db_client.client_type, "CLIENT")

            for asset_type in assets_client:

                asset_balance_data = {

                    #We return like a dictionary so we need access like a dictionary
                    "wallet_id": wallet_created['id'],
                    "asset_type": asset_type,
                    "balance": 0,
                    "created_at": datetime.now(),
                    "updated_at": datetime.now()
                } 

                asset_created = await AssetsService.create_asset_balance(db, asset_balance_data)
                assets_created.append(asset_created)

            return {
                "wallet": wallet_created,
                "assets": assets_created
            }
            
        except Exception as e: 

            raise HTTPException(status_code=500, detail=f'Error creating wallet: {e}')

    async def DeleteWallet(db: AsyncSession, wallet_id: int): 

        db_wallet = await db.get(Wallet, wallet_id)

        if not db_wallet: 
            raise HTTPException(status_code=404, detail=f'Wallet wasnt found with the id: {wallet_id}')

        await db.delete(db_wallet)
        await db.commit()

        return {
            "message": f"Wallet with the id: {wallet_id} was deleted successfully"
        }

