#!/opt/python3/bin/python3
# -*- coding: utf-8 -*-
#
# 2016.6.1
# 等待R_inotify_dns_md.sh发现.md变化时，自动运行，并检测关键字'add,'或'del,'变化。
# 将结果保存到go_info.db和go_dns.db 以用作
#
def w_dns_data(labs_db):
    try:
        with open(labs_db) as ddb,open('../python/go_info.db', 'w') as go_info_db,open('../python/go_dns.db', 'w') as go_dns_db:
            for n in ddb:
                    if not n.find('add,') == -1:
                            (add_temp,add_name,add_type,add_IP,add_date,add_user,add_other) = n.strip().split(',')
                            print(add_name + '\t' + add_type + '\t' + add_IP,file=go_dns_db)
                            print(add_date + '\t' + add_user + '\t' + add_other,file=go_info_db)
                    elif not n.find('del,') == -1:
                            (del_temp,del_name,del_type,del_IP,del_date,del_user,del_other) = n.strip().split(',')
                            print(del_name + '\t' + del_type + '\t' + del_IP,file=go_dns_db)
                            print(del_date + '\t' + del_user + '\t' + del_other,file=go_info_db)
                    else:
                            print('',end='')
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)


print(w_dns_data('../content/IT公开数据/办公网域名解析记录查询.md'))