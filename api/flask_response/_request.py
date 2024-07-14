from typing import Any
from werkzeug.datastructures import ImmutableDict

class MultiTypeDict:
    def __init__(self,_dict:dict) -> None:
        self._dict = _dict;
    
    def get(self,key,**kwrags):
        _default = kwrags.get("default") or None;
        _type = kwrags.get("type") or None;

        value = self._dict.get(key);

        if value == None:
            return _default;

        if callable(_type):
            try:
                return _type(value);
            except:
                return None
    
        return value;

    def update(self,key,value):
        self._dict[key] = value;
    
    def __str__(self) -> str:
        return "MultiTypeDict(%s)" % (self._dict);

    def __repr__(self) -> str:
        return "MultiTypeDict(%s)" % (self._dict);

class Loader:
    def __init__(self,request:ImmutableDict) -> None:
        self.args = request.args.to_dict();
        self.form = request.form.to_dict();

    def to_dict(self):
        return {
            "args": MultiTypeDict(self.args),
            "form": MultiTypeDict(self.form)
        };