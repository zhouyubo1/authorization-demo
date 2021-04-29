# authorization-demo
一个用户身份验证的demo

demo项目使用flask框架，mysql数据库进行开发，没有做模型类映射，使用原生sql语句查询

app/
	目录下的blueprint为蓝图，处理业务
	目录下的checks做简单参数校验
	目录下的utils是简单工具，验证密码

manage.py 文件问项目启动文件
settings.py 文件为加载环境变量文件