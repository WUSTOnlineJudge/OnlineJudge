武汉科技大学 OnlineJudge 后端
--------

### 技术栈
- Django
- Django Rest Framework 


### 进度
- [ ] 账号
    - [x] 构建账号数据库
    - [ ] 注册/登录账号
    - [ ] 权限控制

- [ ] Problem
    - [x] 构建数据库
    - [x] 增删查改题目
    - [ ] 提交题目

### 运行
- 设置环境变量`ENV=dev`后开启debug模式
- 使用`python manage.py runserver`运行服务器

### api
```json
{
    "accounts": "http://127.0.0.1:8000/accounts/",
    "problems": "http://127.0.0.1:8000/problems/"
}
```

