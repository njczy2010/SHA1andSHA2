# SHA1andSHA2
统计文件签名(Microsoft,Trend Micro)

工程项目:编写统计文件签名（Microsoft,Trend Micro）的程序
简要介绍:编写程序，统计不同平台上、相关文件是否带有所需签名（Microsoft,Trend Micro）
所用语言：python,批处理脚本
时间:2015/11/11 - 2015/11/13
*个人贡献:1）独立编写VerifySign_all.bat，VerifySign_once.bat 和 Collect_VerifySign_log.bat，在各台虚拟机上运行，收集相关文件的签名（Microsoft,Trend Micro），整理汇总并上传至服务器。
2）独立编写Check_VerifySign_log.py和function_used.py，分析某个路径下的签名汇总结果，对于虚拟机上传的签名整理结果，根据文件的签名个数分类，给出总的分类结果以及每类的文件信息。2个python，3个.bat代码量共528行。

This program is created for VerifySign operations
Author:         zhiyang_chen@trendmicro.com.cn
Created Date:   2015/11/

run VerifySign_all.bat >VerifySign_all.log

VerifySign_all.bat：
    主程序，枚举 dce,dre,ssapi,tmebc文件夹，按要求执行 VerifySign_32.exe or VerifySign_64.exe
    调用 VerifySign_once.bat 和 Collect_VerifySign_log.bat

    需要修改的参数：
    rootdir,the path you put this bat
         
    dce_dir,dre_dir,ssapi_dir,tmebc_dir,the path you put these folders

VerifySign_once.bat：
    run VerifySign_32.exe or VerifySign_64.exe once

Collect_VerifySign_log.bat：
    collect VerifySign log from local computer to a remote path 

    需要修改的参数：
    remotedir,username,password
    PS: 目前使用的是：

    remotedir=\\10.204.16.28\Home\DCE\Zhiyang_chen
    username=trend\zhiyang_chen
    password=tre!##13

    remote_report_dir=%remotedir%\VerifySign_log ， 即 \\10.204.16.28\Home\DCE\Zhiyang_chen\VerifySign_log

This program is created to check VerifySign log
Author:         zhiyang_chen@trendmicro.com.cn
Created Date:   2015/11/

主程序Check_VerifySign_log.py，函数库：function_used.py
run Check_VerifySign_log.py [report_path]
Example:
    Check_VerifySign_log.py \\10.204.16.28\Home\DCE\Zhiyang_chen\SHA1andSHA2\TestSuite\report
    Check_VerifySign_log.py C:\Users\zhiyang_chen\Desktop\SHA1andSHA2\TestSuite\report

结果放在 rootdir\results\remote 或 rootdir\results\local内

sum_result_path record the sum results

detail_result_path record all the detail results

both_success_result_path record first classification -- Count of valid signatures: 2

primary_success_result_path record second classification -- Count of valid signatures: 1 (Primary signature verify success!)

secondary_success_result_path record third classification -- Count of valid signatures: 1 (Verify secondary signature Success!)

both_fail_result_path record forth classification -- Count of valid signatures: 0