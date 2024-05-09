class UserStatus:
    class LOGIN:   
        # 正常返回
        OK = 1000
        
        #未知错误
        ERROR = 1001

        #参数错误
        PARAMERROR = 1002

        #拒绝登录
        REFUSE = 1003

        #口令错误
        PASSWORDERROR = 1004

        ERRORDOC = {
            ERROR: "未知错误",
            PARAMERROR: "用户参数错误",
            REFUSE: "账号被封禁，无法登录",
            PASSWORDERROR: "用户名或密码错误"
        }
        

        
    class LOGOUT:
        OK = 2000
        ERROR = 2001
