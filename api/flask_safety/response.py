from flask import make_response

from random import randint


class StatusCode:
    OK = 200
    ERROR = 500

class Server:
    ServerName = ("Apache","nginx","Microsoft-IIS","LiteSpeed","Apache-Coyote","Node.js","Express","Cherokee","Jetty","Caddy","IBM_HTTP_Server","Hiawatha","uWSGI")

    @staticmethod
    def getRandomServer(version=True) -> str:
        '''
            if version is True , we will return a random server name with version 
            example:
                Apache/20.3.5
        '''
        namelist = Server.ServerName
        length = len(namelist) - 1

        if not version:
            return namelist[randint(0,length)]
        
        randlist = [randint(0,length) if i == 0 else str(randint(0,20)) for i in range(4)]
        
        prefix = namelist[randlist[0]]
        vers = '.'.join(randlist[1:])
        return f'{prefix}/{vers}'


class StatusCode:
    OK = 200
    BADREQUEST = 400
    NOTFOUNT = 404
    SERVERERROR = 500


class ServerResponse:
    def __init__(self,content,status_code=None,RandomServer=True) -> None:
        self.content = content
        self.status_code = StatusCode.OK
        self.header = {
            "Server" : Server.ServerName[0]
        }

        if status_code:
            self.status_code = status_code

        if RandomServer:
            self.header["Server"] = Server.getRandomServer()
    

    def response(self) -> tuple:
        header = []
        for key in self.header:
            value = self.header.get(key)
            if not value:
                continue
            header.append(
                (key,value)
            )
        return (
            self.content,
            self.status_code,
            header
        )