## fleets.json 和 ships.json ##

敌方编队和敌舰属性

编队数据中 `Cx-y` 表示战役, 比如 `C2-2` 表示巡洋困难

其他的应该不需要解释

## load.py ##

将文本格式的战斗数据导入 `fleets.json` 和 `ships.json`

    python load.py [文件名1] [文件名2] ...

文件格式为一行请求 url 后面跟一行回复 json, 多次请求之间可以有空行. 例:

    GET /pve/spy/&t=......
    {"enemyVO":......
    
    GET /pve/deal/40308/4/2/......
    {"shipVO":[{"id":......

本程序只处理 `/pve/newNext/`(索敌), `/pve/deal`(白天战斗), `/campaign/challenge`(战役) 这几类请求, 其他数据的格式并不影响

## decode.py ##

为 packet capture 导出格式做的解码工具, 可能不适用于其他抓包工具

    python decode.py [输入文件名] [输出文件名]

输入文件格式为一块 http 请求跟一块 http 回复. 例:

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

## wiki.py ##

将 `ships.json` 和 `fleets.json` 的内容转换成 wiki module 用的格式

    python wiki.py

生成的 `enemy.lua` 内容复制粘贴至[模块:敌舰数据](http://www.zjsnrwiki.com/wiki/模块:敌舰数据)

建议更新 wiki 前先与 [github](https://github.com/zjsnrwiki/enemy) merge 数据

## run.sh ##

给 *nix 系统用的一键式脚本, 假设 dump 的数据保存在 android 设备上的 download 目录

    ./run.sh <文件名>

## static.json ##

从 getInitConfigs 提取的静态数据, 一般不用管

## jsonformat.py ##

美化 json 输出的工具, 不用管
