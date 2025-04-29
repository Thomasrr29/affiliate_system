from typing import Optional, TYPE_CHECKING
from sqlalchemy import Column, DateTime
from datetime import datetime, timezone
from ..enums import AssetType
from sqlmodel import Field, SQLModel, UniqueConstraint, Relationship

if TYPE_CHECKING: 
    from wallets.models import Wallet

class AssetBalanceBase(SQLModel): 
    
    wallet_id: int = Field(foreign_key='wallet.id', index=True)
    asset_type: AssetType = Field(default=AssetType.POINTS)
    balance: float = Field(default = 0)
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False),
        default_factory= lambda: datetime.now(timezone=timezone.utc))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False),
        default_factory= lambda: datetime.now(timezone=timezone.utc))
    
    __table_args__ = (
        UniqueConstraint('wallet_id', 'asset_type', name='uix_wallet_asset'),
    )

class AssetBalance(AssetBalanceBase, table=True):

    __tablename__ = 'asset_balance'

    id: Optional[int] = Field(default=None, primary_key = True)
    wallet: "Wallet" = Relationship(back_populates='assets_balance')

class AssetBalanceCreate(AssetBalanceBase): 
    pass 

class AssetBalanceUpdate(SQLModel): 

    wallet_id: Optional[int] = None
    asset_type: Optional[AssetType] = None
    balance: Optional[float] = None



