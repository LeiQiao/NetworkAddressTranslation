# NetworkAddressTranslation
简单的内网穿透服务器及客户端程序


准备：

1. 一台服务器用于记录内网的 IP 地址（如果没有自己的服务器可以使用下面的连接 https://www.doomga.com/nat ）
2. 一台内网的电脑用于定时向服务器发送当前内网映射到外网的 IP

`/NATServer` 部署在服务器上的 python 程序，用来识别内网电脑发过来的请求。

`Mac` 部署在内网的电脑上，利用电脑的定时任务来向服务器发送当前的网络 IP。



