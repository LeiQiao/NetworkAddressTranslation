# NATServer

简单的内网穿透服务器

将该程序部署在自己的服务器中。

## 部署

`NAT.py` 使用 Flask 实现一个接口的两个点用方式。

内网机器调用 `POST /nat` 接口时，接口解析请求头中的外网 IP 地址，并记录下来；在调用 `GET /nat`接口时返回。

### 设置 nginx

打开 `nginx.conf` 并将下一段粘贴进服务配置项
```config
location /nat {
    proxy_set_header  Host $host;
    proxy_set_header  X-Real-IP $remote_addr;
    proxy_set_header  X-Forwarded-Proto http;
    proxy_set_header  X-Forwarded-For $remote_addr;
    proxy_set_header  X-Forwarded-Host $remote_addr;
    proxy_pass http://127.0.0.1:5002;
}
```
保存后重启 nginx

### 启动 NAT 服务

```shell
./startup.sh
```



## 发送内网的 IP 接口

### HTTP Request

`POST /nat`

### 请求参数

使用 HTTP 基本认证方式，将用户名密码拼接在请求头中的 Authorization 字段。

Authorization 的计算方式：base64encode("username":"password")。

用户名密码可以随意设置，只是为了在 GET 接口中区分不同的用户。

### 返回值
当前网络的外网 IP

## 查询内网映射到外网的 IP 接口

### HTTP Request

`GET /nat`

### 请求参数

使用 HTTP 基本认证方式，将用户名密码拼接在请求头中的 Authorization 字段。

Authorization 的计算方式：base64encode("username":"password")。

用户名密码需要设置成发送时的用户名密码。

### 返回值
内网映射到外网的 IP 地址



