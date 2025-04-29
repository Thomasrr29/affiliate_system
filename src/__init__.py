#We import the models to force the import of the entities in the execution process. 
from src.clients.models import Client, ClientCreate, ClientUpdate
from src.assets.models.balance import AssetBalance, AssetBalanceCreate
from src.wallets.models import Wallet
from src.sales.models import Sales, SalesCreate, SalesUpdate