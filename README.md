# webchat
You know, chat!

# 环境
python 3.6

# 安装依赖
pip install -r requirements.txt

# 启动
    首次启动前运行以下两条命令： 
        python manage.py makemigrations
        python manage.py migrate
    启动：
        python manage.py runserver
    访问：
        浏览器访问： http://localhost:8000/index


# 接口
### 状态码说明
    请求成功： 200
    后台错误： 500
    请求方式错误： 405
    请求参数错误： 400
    
#### 1.登录
    接口地址：/user/login
    请求方式：post
    请求参数：username, password
    返回结果：{"statusCode": 200, "message": "登录成功", "data": ""}
    
    
#### 2.注册
    接口地址：/user/register
    请求方式：post
    请求参数： username, password, password2, email
    返回结果：{"statusCode": 200, "message": "注册成功", "data": ""}
  
    
