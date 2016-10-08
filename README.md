## fleets.json 和 ships.json ##

敌舰数据, 应该不需要解释

## load.py ##

将文本格式的战斗数据导入数据库

    python load.py [文件名1] [文件名2] ...

文件格式为一行请求 url 后面跟一行回复 json, 多次请求之间可以有空行. 例:

    GET /pve/spy/&t=......
    {"enemyVO":......
    
    GET /pve/deal/40308/4/2/......
    {"shipVO":[{"id":......

事实上本程序只处理 `/pve/deal` 这类请求, 其他数据的格式并不影响

## dump.py ##

我自用的解码工具, 可能不适用于其他抓包工具

    python dump.py [输入文件名] [输出文件名]

文件格式为一块 http 请求跟一块 http 回复. 例:

    GET /pve/getWarResult/0/......
    Accept-Encoding: identity
    ......
    Connection: Keep-Alive

    HTTP/1.1 200 OK
    Date: ......
    ......
    Set-Cookie: ......
    
    <第一段数据长度>
    <第一段数据>
    <第二段数据长度>
    <第二段数据>
    ......
    0
    
    GET /pve/newNext/......

## static.json ##

从 getInitConfigs 提取的静态数据, 一般不用管

## jsonformat.py ##

美化 json 输出的工具, 不用管
