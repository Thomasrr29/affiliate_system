from fastapi import APIRouter, Query, Body, Depends
from src.core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from src.wallets.models import Wallet
from typing import List
from .services import WalletsService

router = APIRouter()

@router.get('/wallet',
    response_model=None,
    tags=['Wallets'],
    summary='Get All wallets')
async def get_all_wallets(limit: int = Query(10, ge=1), offset: int = Query(0, ge=0), db: AsyncSession = Depends(get_db)): 

    return await WalletsService.GetAllWallets(db, limit, offset)

@router.get('/wallet/{client_id}',
    response_model=None,
    tags=['Wallets'],
    summary='Get wallet by client id')
async def get_wallet_by_id(client_id: int, db: AsyncSession = Depends(get_db)): 

    return await WalletsService.GetWalletByClientId(db, client_id)

@router.post('/wallet/wallet-with-balances/{client_id}', 
    tags=['Wallets'],
    summary='Create wallet with balances')
async def create_wallet_with_balances(client_id: int, db: AsyncSession = Depends(get_db)):

    return await WalletsService.CreateWalletWithBalances(db, client_id)

@router.delete('/wallet/{wallet_id}',
    tags=['Wallets'],
    summary='Deletes wallet')
async def delete_wallet(wallet_id: int, db: AsyncSession = Depends(get_db)): 

    return await WalletsService.DeleteWallet(db, wallet_id)