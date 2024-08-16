from datetime import datetime

def checkTimeout(time:float,timeout:int=3600) -> bool:
    return datetime.now().timestamp() - time > timeout