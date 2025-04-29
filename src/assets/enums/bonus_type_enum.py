from enum import Enum 

class BonusType(str, Enum): 

    SALE = "SALE"
    STREAK = "STREAK"
    AFFILIATE = "AFFILIATE"
    ACHIEVEMENT = "ACHIEVEMENT"


#THIS ARE INFORMATION THAT LET US CALCULATE THE BONUS AMOUNT
class CalculateBonusAmount(str, Enum): 

    AMOUNT = "amount"
    DAYS = "days"
    LEVEL = "level"