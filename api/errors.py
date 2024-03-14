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