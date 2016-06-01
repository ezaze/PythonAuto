# 2016.6.1 
# 当监控到DNS服务器传输数据到本地后，执行本地的python文件，生成一个新的md文件，到网站的content目录下。
#

#!/bin/bash
inotify=/usr/local/inotify-tools/bin/inotifywait  #inotify的安装路径
dir1=/var/www/html/Raneto/example/python/  #要监控的目录
file1=wandoulabs.com.db
$inotify -mrq --timefmt '%y/%m/%d %H:%M' --format '%T %w%f' -e create,delete,close_write $dir1/$file1 \
| while read file   #监控结果通过管道给循环
do
    /bin/python3 /var/www/html/Raneto/example/python/R_md_create.py >>x.txt
        # sh -x 文件名 可以进入调试模式
done