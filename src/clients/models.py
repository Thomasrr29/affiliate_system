from typing import Optional, TYPE_CHECKING
from pydantic import ConfigDict
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column, DateTime
from datetime import datetime, timezone
from .enums import ClientType

if TYPE_CHECKING: 
    from src.wallets.models import Wallet

class ClientBase(SQLModel): 

    #Client id for external platform (Siigo, or other bill application)
    client_id: Optional[str] = Field(default=None, nullable=True)
    name: str
    email: str
    phone: str  
    client_type: ClientType
    affiliate_code: Optional[str] = Field(default=None, nullable=True)
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False),
        default_factory= lambda: datetime.now(timezone=timezone.utc))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False),
        default_factory= lambda: datetime.now(timezone=timezone.utc))

class Client(ClientBase, table=True): 

    __tablename__ = 'client'
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: Optional[int] = Field(default=None, primary_key=True)   
    wallet: Optional["Wallet"] = Relationship(back_populates="client")

class ClientCreate(ClientBase): 
    pass 

class ClientUpdate(SQLModel): 

    siigo_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None 
    phone: Optional[str] = None
    client_type: Optional[str] = None
    affiliate_code: Optional[str] = None


    