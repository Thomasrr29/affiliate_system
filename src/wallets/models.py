from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import Column, DateTime
from datetime import datetime, timezone
from pydantic import ConfigDict
from src.common.datetime_function import get_utc_now_function

if TYPE_CHECKING:
    from src.assets.models.balance import AssetBalance
    from src.clients.models import Client

class WalletBase(SQLModel):

    client_id: int = Field(foreign_key='client.id', unique=True) 
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False),
        default_factory=get_utc_now_function)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False),
        default_factory=get_utc_now_function)

class AssetBalanceForWallet(SQLModel): 

    asset_type: str = Field(default='POINTS')
    balance: float = Field(default=0)

class Wallet(WalletBase, table=True): 

    __tablename__ = 'wallet'
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: Optional[int] = Field(default=None, primary_key=True)
    client: Optional["Client"] = Relationship(back_populates="wallet")
    assets_balance: List["AssetBalance"] = Relationship(back_populates="wallet")

    