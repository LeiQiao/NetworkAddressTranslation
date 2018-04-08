# Mac
简单的 Mac 客户端程序

## 修改定时任务脚本
编辑 `com.LoveC.NAT.plist` 文件
```plist
<key>ProgramArguments</key>
<array>
    <string>/usr/bin/curl</string>
    <string>-X</string>
    <string>POST</string>
    <string>--user</string>
    <string>用户名:密码（例如：abc:123）</string>
    <string>服务器的地址（如果没有自己的服务器可以设置成：http://www.doomga.com/nat）</string>
</array>
```
设置间隔时间，电信的网络每两天更新依次外网 IP （或更短时间）
```plist
<key>StartInterval</key>
<integer>更新时间间隔（秒，例如：600）</integer>
```

### 运行

```shell
cp com.LoveC.NAT.plist ~/Library/LaunchAgents/ # 将定时任务拷贝到启动目录中
launchctl load ~/Library/LaunchAgents/com.LoveC.NAT.plist # 加载任务并定时启动
```
