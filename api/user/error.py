from ..errors.errors import BaseError


class getUserInfoError(BaseError):
    NOUSER = 1000
    ERROR = 1001
    
    def __init__(self, *args, **kwargs) -> None:
        self.ERRORDOC = {
            self.ERROR : '查询错误',
            self.NOUSER: '没有该用户'
        }
        super().__init__(*args, **kwargs);