#!/opt/python3/bin/python3
# 1. 从/bind/zone/ 里自动抓取数据，对获得的A、NS、CNAME记录重新整理排序。 （完成）
# 2. 生成 .md 文件的表单，并自动更新到Ranote平台。（完成）
# 2. 根据Serial判断更新，并进行信息同步。
# 3. 自动匹配申请人信息、申请时间和备注至Ranote平台。


import os
def w_dns_data(labs_db):
    try:
        with open(labs_db) as ddb,open('./ranote/DNS/wandoulabs_dns.md', 'w') as wandlabs_md:
            name_top1 = "| 主机域名     |  记录类型  |  记录值  | 需求提交日期 | 需求提交人 | 备注 |"
            name_top2 = "|-----------|:------|:----|:------|:----------|:----------:|"
            temp1_s = []
            temp2_s = []
            temp3_s = []
            ddb_s = sorted(ddb)
            for n in ddb_s:
                    if not n.find('Serial') == -1:
                            (d_sn,d_temp) = n.strip().split('; Serial')
                    elif not n.find('\tA\t') == -1:
                            temp1_s.append(n)
                    elif not n.find('\tNS\t') == -1:
                            temp2_s.append(n)                          
                    elif not n.find('\tCNAME\t') == -1:
                            temp3_s.append(n)                 
                    else:
                            print('',end='')
                            

                            
                            
            print('####最后更新时间：' + d_sn,file=wandlabs_md)
            print('\n',file=wandlabs_md)
            print(name_top1,file=wandlabs_md)
            print(name_top2,file=wandlabs_md)
            temp1_e = sorted(temp1_s)
            temp2_e = sorted(temp2_s)
            temp3_e = sorted(temp3_s)
            
            for ppp in temp1_e:
                (d_name_a, d_a) = ppp.strip().split('\tA\t')
                print('| ' + d_name_a + ' | A | ' + d_a + ' | - | - |   -   | ',file=wandlabs_md)
            
            for ppp in temp2_e:
                (d_name_ns, d_ns) = ppp.strip().split('\tNS\t')
                print('| ' + d_name_ns + ' | NS | ' + d_ns + ' | - | - |   -   | ',file=wandlabs_md)
            
            for ppp in temp3_e:
                (d_name_cname, d_cname) = ppp.strip().split('\tCNAME\t')
                print('| ' + d_name_cname + ' | CNAME | ' + d_cname + ' | - | - |   -   | ',file=wandlabs_md)
              
                            
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)


print(w_dns_data('w.db'))
