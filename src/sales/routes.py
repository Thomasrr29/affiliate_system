from fastapi import APIRouter, Query, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import get_db
from src.types import SalesPaginationResponse
from .models import SalesUpdate, SalesWithBonusData
from .services import SalesService

router = APIRouter()

@router.get('/sales',
    response_model=SalesPaginationResponse,
    tags=['Sales'],
    summary='Get all sales')
async def get_all_sales(
    db: AsyncSession = Depends(get_db),
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0)
): 

    return await SalesService.get_all_sales(db, limit, offset)

@router.get('/sales/{client_id}',
    tags=['Sales'],
    summary='Get sale by client ID')
async def get_sale_by_client_id(client_id: int, db: AsyncSession = Depends(get_db)):

    return await SalesService.GetSalesByClientId(db, client_id)

@router.get('/sales/affiliate/{affiliate_id}',
    tags=['Sales'],
    summary='Get sale by affiliate id')
async def get_sale_by_affiliate_id(affiliate_id: int, db: AsyncSession = Depends(get_db)): 

    return await SalesService.GetSalesByAffilate(db, affiliate_id)

@router.post('/sales/create',
    tags=['Sales'],
    summary='Create sale')
async def create_sale(create_sale_data: SalesWithBonusData = Body(), db: AsyncSession = Depends(get_db)): 

    return await SalesService.CreateSaleAndApplyBonusWallet(db, create_sale_data)

@router.patch('/sales/update/{sale_id}',
    tags=['Sales'],
    summary='Updates sale')
async def update_sale(sale_id: int, update_sale_data: SalesUpdate = Body(), db: AsyncSession = Depends(get_db)):

    return await SalesService.UpdateSale(db, sale_id, update_sale_data)

@router.delete('/sales/delete/{sale_id}',
    tags=['Sales'],
    summary='Deletes sale')
async def delete_sale(sale_id: int, db: AsyncSession = Depends(get_db)): 

    return await SalesService.DeleteSale(db, sale_id)