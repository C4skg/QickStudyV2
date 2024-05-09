from .statuscode import UserStatus

class ParamError(Exception):
    def __init__(self, **kwargs) -> None:
        self.args = kwargs.keys()
        self.values = list(kwargs.values())

    def __str__(self) -> str:
        _errorInfo = []
        for index,key in enumerate(self.args):
            _info = f"The parameter `{key}` couldn't bt `{self.values[index]}`";
            _errorInfo.append(_info)
        return '\n'.join(_errorInfo)
    

class LoginError(Exception):
    def __init__(self, *args,**kwargs) -> None:
        self.code = kwargs.get('code');
        self.message = args;
        if not self.code:
            self.code = UserStatus.LOGIN.ERROR

        if len(self.message) == 0:
            self.findMessageByDoc();
        else:
            self.message = args;
        
        self.message = self.__str__();
        

    def findMessageByDoc(self):
        DOC = UserStatus.LOGIN.ERRORDOC;
        self.message = DOC.get(self.code);
        if not self.message:
            self.message = ''

    def __str__(self) -> str:
        return self.message if type(self.message) == str else '\n'.join(self.message);