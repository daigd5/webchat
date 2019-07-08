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

## 用户相关接口

#### 1.登录
    接口地址：/user/login
    请求方式：post
    请求参数：username, password
    返回结果：{"statusCode": 200, "message": "登录成功", "data": {"userId": xxx}}
    
    
#### 2.注册
    接口地址：/user/register
    请求方式：post
    请求参数： username, password, password2, email
    返回结果：{"statusCode": 200, "message": "注册成功", "data": ""}
    
    
#### 3.用户修改信息
    接口地址：/user/update
    请求方式：post
    请求参数：userId, username, password, password2, email
    返回结果： {"statusCode": 200, "message": "修改成功", "data": ""}
  

## 组相关接口  

#### 1.添加组
    接口地址： /group/addGroup
    请求方式：post
    请求参数： groupName, description
    返回结果： {"statusCode": 200, "message": "注册成功", "data": {"groupId": xxx}}
    

#### 2.更新组
    接口地址： /group/updateGroup
    请求方式： post
    请求参数：groupId, groupName, description
    返回结果： {"statusCode": 200, "message": "修改成功", "data": ""}
    
    
#### 3.删除组（单个）
    接口地址：/group/deleteGroup
    请求方式： get
    请求参数：groupId
    返回结果：{"statusCode": 200, "message": "删除成功", "data": ""}
    
    
#### 4.删除组（批量）
    接口地址： /group/deleteGroups
    请求方式： psot
    请求参数：groupIdList(类型：数组， 示例: [1, 3, 4])
    返回结果： {"statusCode": 200, "message": "删除成功", "data": ""}
    
    