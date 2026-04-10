from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer

# 1. 创建作者器（账号管理）
authorizer = DummyAuthorizer()

# 2. 添加一个用户：用户名、密码、根目录、权限
# 权限 elradfmwMT 表示完整权限，你可以改
authorizer.add_user("ftpuser", "123456", "./ftp_root", perm="elradfmwMT")

# 3. 允许匿名用户（可选）
# authorizer.add_anonymous("./ftp_root")

# 4. 配置 FTP 处理类
handler = FTPHandler
handler.authorizer = authorizer

# 5. 启动服务器
server = FTPServer(("192.168.31.145", 21), handler)
print("FTP 服务器已启动：192.168.31.145:21")
server.serve_forever()
