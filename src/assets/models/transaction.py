from sqlmodel import SQLModel, Field
from src.assets.enums import AssetType, AssetTransactionCategory
from src.common.datetime_function import get_utc_now_function
from sqlalchemy import Column, DateTime
from typing import Optional 
from datetime import datetime, timezone

class AssetTransactionBase(SQLModel):

    wallet_id: int = Field(foreign_key="wallet.id", index=True)
    amount: float
    description: str
    asset_type: AssetType
    category: AssetTransactionCategory
    reference_id: Optional[int] = Field(default=None)
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), nullable=False),
        default_factory=get_utc_now_function)
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), nullable=False),
        default_factory=get_utc_now_function)
    
class AssetTransaction(AssetTransactionBase, table=True): 

    __tablename__ = 'asset_transaction'

    id: Optional[int] = Field(default=None, primary_key=True)

class AssetTransactionCreate(AssetTransactionBase): 
    pass 

class AssetTransactionUpdate(SQLModel): 

    wallet_id: Optional[int] = None
    asset_type: Optional[AssetType] = None
    amount: Optional[float] = None
    category: Optional[str] = None
    reference_id: Optional[int] = None
    description: Optional[str] = None

    

