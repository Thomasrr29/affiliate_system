from fastapi import APIRouter
from src.clients.routes import router as clients_router
from src.assets.routes import router as assets_router
from src.sales.routes import router as sales_router 
from src.wallets.routes import router as wallets_router 

api_router = APIRouter()

api_router.include_router(clients_router)
api_router.include_router(assets_router)
api_router.include_router(sales_router)
api_router.include_router(wallets_router)