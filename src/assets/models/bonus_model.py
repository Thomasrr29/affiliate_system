from pydantic import BaseModel
from typing import Optional

# Modelo base para todas las bonificaciones
class BonusBase(BaseModel):
    wallet_id: int
    reference_id: Optional[int] = None

# Modelos específicos para cada tipo de bonificación
class SaleBonusData(BonusBase):
    amount: float
    sale_id: int

class StreakBonusData(BonusBase):
    days: int

class AchievementBonusData(BonusBase):
    name: str
    level: int = 1

class AffiliateBonusData(BonusBase):
    amount: float
    sale_id: int