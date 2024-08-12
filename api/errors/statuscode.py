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

        #数据库错误
        DATABASEERROR = 1005

        ERRORDOC = {
            ERROR: "未知错误",
            PARAMERROR: "用户参数错误",
            REFUSE: "账号被封禁，无法登录",
            PASSWORDERROR: "用户名或密码错误",
            DATABASEERROR: "查询错误"
        }
        
    class LOGOUT:
        OK = 2000
        ERROR = 2001

    class REGISTER:
        OK = 3000
        ERROR = 3001
        EMAILERROR = 3002
        PASSWORDERROR = 3003
        PARAMERROR = 3004
        DATABASEERROR = 3005
        USEREXISTS = 3006
        ERRORDOC = {
            ERROR: "未知错误",
            EMAILERROR: "用户邮箱格式错误",
            PASSWORDERROR: "用户密码必须大于等于6位且同时包含英文和数字",
            PARAMERROR: "用户参数错误",
            DATABASEERROR: "查询错误",
            USEREXISTS: "用户已存在"
        }