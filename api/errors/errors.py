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
    
class BaseError(Exception):
    def __init__(self, *args,**kwargs) -> None:
        self.code = kwargs.get('code');
        del kwargs['code'];
        
        self.message = args;
        self.kwrags = kwargs;
        if not self.code:
            self.code = UserStatus.LOGIN.ERROR

        if len(self.message) == 0:
            self.findMessageByDoc();
        else:
            self.message = args;
        
        self.message = self.__str__();
        

    def findMessageByDoc(self,DOC=None):
        if DOC == None:
            DOC = UserStatus.LOGIN.ERRORDOC;
        self.message = DOC.get(self.code);
        if not self.message:
            self.message = ''

    def __str__(self) -> str:
        return self.message if type(self.message) == str else '\n'.join(self.message);


class LoginError(Exception):
    def __init__(self, *args,**kwargs) -> None:
        self.code = kwargs.get('code');
        del kwargs['code'];
        
        self.message = args;
        self.kwrags = kwargs;
        if not self.code:
            self.code = UserStatus.LOGIN.ERROR

        if len(self.message) == 0:
            self.findMessageByDoc();
        else:
            self.message = args;
        
        self.message = self.__str__();
        

    def findMessageByDoc(self,DOC=None):
        if DOC == None:
            DOC = UserStatus.LOGIN.ERRORDOC;
        self.message = DOC.get(self.code);
        if not self.message:
            self.message = ''

    def __str__(self) -> str:
        return self.message if type(self.message) == str else '\n'.join(self.message);


class RegisterError(LoginError):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs);

    def findMessageByDoc(self):
        super().findMessageByDoc(
            UserStatus.REGISTER.ERRORDOC
        )
    
    def __str__(self) -> str:
        return super().__str__();

class CaptchaError(LoginError):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs);

    def findMessageByDoc(self):
        super().findMessageByDoc(
            UserStatus.CAPTCHA.ERRORDOC
        )
    
    def __str__(self) -> str:
        return super().__str__();