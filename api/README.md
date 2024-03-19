# Flask-Server

> Python 3.8.18

This folder is Qickstudy's Server

### 服务端安装前配置

> 编辑 当前目录下的 .env 文件
> 开启了 debug 模式下的 secret_key 默认为 QickStudy


| 参数 | 参数类型 | 默认值 | 可选值 | 说明 |
| ---- | --------| ------ | ------| ---- |
| app_mode       | `str` | build | build、debug |flask是否处于调试模式 |
| ADMIN_PASSWORD | `str` | admin@QickStudy | 任意 | 管理员初始密码 |
| MAIL_SERVER    | `str` | None | 任意 | 平台邮箱服务地址 |
| MAIL_PORT      | `str` | None | 任意 | 平台邮箱服务地址端口 |
| MAIL_USERNAME  | `str` | None | 任意 | 平台邮箱服务邮箱账号 |
| MAIL_PASSWORD  | `str` | None | 任意 | 平台邮箱服务邮箱对应密钥 |
| SQL_PORT       | `str` | 3306 | 任意 | 平台数据库端口 |
| SQL_USER       | `str` | root | 任意 | 平台数据库用户 |
| SQL_PASSWORD   | `str` | 123456|任意 | 平台数据库密码 |
| SQL_SCHEMA     | `str` | qickstudy_db| 任意 | 平台所使用的数据库 |
