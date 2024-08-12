from flask import current_app,session
from redis.exceptions import ConnectionError
from .. import redisClient

def setHData(key,data:dict,time:int=3600) -> bool:
    session_name = current_app.config.get('SESSION_ID');
    session_id = session.get(session_name);
    if session_id == None:
        return False;
    redisId = current_app.import_name + session_id + key;
    try:
        for item in 
    except ConnectionError as connectError:
        return False;

    redisClient.expire(
        redisId,
        time
    );
    return True;

def getData(key,default=None):
    session_name = current_app.config.get('SESSION_ID');
    session_id = session.get(session_name);
    if session_id == None:
        return default;
    redisId = current_app.import_name + session_id + key;
    try:
        data = redisClient.hget(
            redisId,
            key
        );
        if not data:
            return default;
        
    except ConnectionError as connectError:
        return default;

    return data;