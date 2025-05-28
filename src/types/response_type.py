from typing import Optional, TypeVar, List
from src.clients.enums import ClientType
from datetime import datetime 
from pydantic import BaseModel

T = TypeVar("T")

class PaginationResponse(BaseModel): 
    limit: int
    offset: int
    data: T

    class Config: 
        from_attributes: True

###SALES 
class ResponseClientInSales(BaseModel):

    id: int 
    name: str
    email: str 
    phone: str 
    client_type: ClientType

    class Config: 
        from_attributes = True

class ResponseSale(BaseModel): 

    id: int
    total_amount: float 
    sale_date: datetime 
    reference_sale_id: Optional[str] 
    buyer_client_id: int
    refering_affiliate_id: Optional[int]
    buyer_client: Optional[ResponseClientInSales] = None
    refering_affiliate: Optional[ResponseClientInSales] = None     

    class Config: 
        from_attributes = True

#CLIENT

class ResponseClient(BaseModel): 

    id: int
    client_id: Optional[str] = None
    name: str
    email: str
    phone: str  
    client_type: ClientType
    affiliate_code: Optional[str] = None
    updated_at: datetime
    created_at: datetime

    class Config: 
        from_attributes = True

##WALLET

class SalesPaginationResponse(PaginationResponse): 
    data: List[ResponseSale]

class ClientsPaginationResponse(PaginationResponse): 
    data: List[ResponseClient]

class WalletPaginationResponse(PaginationResponse): 
    pass 

class ResponseWallet(BaseModel): 
    pass 