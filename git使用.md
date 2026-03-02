# git使用

## 1. 本地库初始化

### 1.1 git仓库初始化

```
git init    初始化一个空的git仓库
```

### 1.2 设置签名

```
git config user.name Angel
git config user.email 1551854934@qq.com
```

### 1.3 状态查看

```
git status
```

### 1.4 暂存区操作

```
git add .    将当前目录所有内容全部添加到暂存区
```

### 1.5 提交操作

```
git commit -m "提交的信息(需要自己描述)"
```

## 2. 创建远程仓库

### 2.1 推送操作

```
git remote -v	查看是否有远程仓库地址
git remote add origin https://github.com/ilkrx/AI_STUDY_CODE.git	添加远程库地址

git push (-u) origin master    将代码推送到远程库(第一次推送要加-u)

```

### 2.2 git配置代理

```
git config --global https.proxy http://127.0.0.1:7890 设置HTTPS代理（端口号为7890）
```

