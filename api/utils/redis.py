from flask import current_app,session
from redis.exceptions import ConnectionError


from .. import redisClient

def setHData(name,data:dict,time:int=3600) -> bool:
    session_name = current_app.config.get('SESSION_ID');
    session_id = session.get(session_name);
    if session_id == None:
        return False;
    redisId = current_app.import_name + session_id + name;
    try:
        for item,value in data.items():
            redisClient.hset(
                redisId,
                item,
                value
            )
        redisClient.expire(
            redisId,
            time
        );
    except ConnectionError as connectError:
        return False;
    
    return True;

def getHData(name,key,default=None):
    session_name = current_app.config.get('SESSION_ID');
    session_id = session.get(session_name);
    if session_id == None:
        return default;
    redisId = current_app.import_name + session_id + name;
    try:
        data = redisClient.hget(
            redisId,
            key
        );
        if data is None:
            return default;
        
    except ConnectionError as connectError:
        return default;

    return data;


def getttl(name) -> int:
    session_name = current_app.config.get('SESSION_ID');
    session_id = session.get(session_name);
    if session_id == None:
        return None;
    redisId = current_app.import_name + session_id + name;
    try:
        return redisClient.ttl(redisId);
    except ConnectionError as connectError:
        return None;