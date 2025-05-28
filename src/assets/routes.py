from src.assets.models import AssetTransactionCreate, AssetBalanceCreate, AssetTransaction, AssetBalance
from sqlalchemy.ext.asyncio import AsyncSession
from src.assets.services import AssetsService
from src.assets.enums import AssetType
from fastapi import APIRouter, Depends
from src.core.db import get_db
from typing import List 



router = APIRouter()

##TRANSACTIONS 
# @router.post('/assets/transactions/create',
#     tags=['Assets'],
#     summary='Create asset transaction')
# async def create_asset_transaction(createAssetTransactionData: AssetTransactionCreate, db: AsyncSession = Depends(get_db)):
    
#     return await AssetsService.create_asset_transaction(db, createAssetTransactionData)

@router.get('/assets/transactions/wallet/{wallet_id}',
    tags=['Assets'],
    summary='Get all wallet transactions')
async def get_asset_transactions_by_wallet_id(wallet_id: int, db: AsyncSession = Depends(get_db)):
    
    return await AssetsService.get_asset_transactions_by_wallet_id(db, wallet_id)


@router.get('/assets/transactions/reference_id/{reference_id}',
    tags=['Assets'],
    summary='Get all transactions by reference id')
async def get_asset_transactions_by_reference_id(reference_id: int, db: AsyncSession = Depends(get_db)):
    return await AssetsService.get_asset_transactions_by_reference_id(db, reference_id)

@router.get('/assets/transactions/wallet/{wallet_id}/type/{asset_type}',
    tags=['Assets'],
    summary='Get all wallet transactions by asset type')
async def get_wallet_transactions_by_asset_type(wallet_id: int, asset_type: str, db: AsyncSession = Depends(get_db)):
    
    return await AssetsService.get_wallet_transactions_by_asset_type(db, wallet_id, asset_type)

#BALANCES
@router.post('/assets/balances/create',
    tags=['Assets'],
    summary='Create assets balance for synchronize with the wallet')
async def create_asset_balance(createAssetBalanceData: AssetBalanceCreate, db: AsyncSession = Depends(get_db)):
    
    return await AssetsService.create_asset_balance(db, createAssetBalanceData)

@router.get('/assets/balances/wallet/{wallet_id}/asset/{asset_type}',
    tags=['Assets'],
    summary='Get wallet balance by asset type')
async def get_asset_balance_by_wallet_id_and_asset_type(wallet_id: int, asset_type: str, db: AsyncSession = Depends(get_db)):
    
    return await AssetsService.get_asset_balance_by_wallet_id_and_asset_type(db, wallet_id, asset_type)

@router.patch('/assets/balances/recalculate/{wallet_id}/type/{asset_type}',
    tags=['Assets'],
    summary='Recalculate the wallet asset balance')
async def recalculate_asset_balance(wallet_id: int, asset_type: AssetType, db: AsyncSession = Depends(get_db)):
    
    return await AssetsService.recalculate_asset_balance(db, wallet_id, asset_type)

@router.get('/assets/balances/wallet/{wallet_id}', 
    tags=['Assets'],
    summary='Get all wallet balances')
async def get_all_wallet_balances(wallet_id: int, db: AsyncSession = Depends(get_db)):
    return await AssetsService.get_asset_balance_by_wallet_id(db, wallet_id)