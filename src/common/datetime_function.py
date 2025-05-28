from datetime import datetime, timezone

def get_utc_now_function(): 

    return datetime.now(timezone.utc)

