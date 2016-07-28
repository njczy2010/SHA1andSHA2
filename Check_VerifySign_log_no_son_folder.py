#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
#   This program is created to check VerifySign log
#   Author:         zhiyang_chen@trendmicro.com.cn
#   Created Date:   2015/11/12
#

import os
import time

## Below is the must 
import sys
import platform
import shutil
import subprocess
if 'function_used.py' not in sys.path:
    sys.path.append(os.getcwd() + 'function_used.py')
import function_used

##根据log中最后一行的 Count of valid signatures: ， 把结果分为4类：
##第1类 Count of valid signatures: 2 ； 
##第2类 Count of valid signatures: 1 （Primary signature verify success）；
##第3类 Count of valid signatures: 1 （Verify secondary signature Success!）；
##第4类 Count of valid signatures: 0

def main(report_path):

    print "Start Check_VerifySign_log.py"
    print "report_path : %s" % report_path
    flag = "local"

    ##modify remotedir,username,password if necessary
    remotedir = report_path
    username = "trend\\zhiyang_chen"
    password = "tre!##13"

    ##call connect_remote_path if report_path is a remote path
    if report_path.find('28') != -1:
        flag = "remote"
        
        ret = function_used.connect_remote_path(remotedir,username,password)
        if ret == 1:
            print '>> Connect remote path successfully %s' % remotedir
        else:
            raise AssertionError('>> Connect remote path failed: %s' % return_code)   

    rootdir = os.getcwd()
    print "rootdir : %s" % rootdir
    resultsfolder = rootdir + "\\" + "results"
    if flag == "local":
        resultsdir = resultsfolder + "\\" + flag
    else:
        position = report_path.rfind('\\')
        if position == -1:
            resultsdir = resultsfolder + "\\" + flag
        else:
            resultsdir = resultsfolder + "\\" + "results_afterhotfix_" + report_path[position+1:]

    ##record the sum results
    sum_result_path = resultsdir + "\\" + "sum_result.txt"

    ##record all the detail results
    detail_result_path = resultsdir + "\\" + "detail_result.txt"

    ##第1类 Count of valid signatures: 2 ； 
    both_success_result_path = resultsdir + "\\" + "both_success_result.txt"

    ##第2类 Count of valid signatures: 1 （Primary signature verify success）
    primary_success_result_path = resultsdir + "\\" + "primary_success_result.txt"

    ##第3类 Count of valid signatures: 1 （Verify secondary signature Success!）
    secondary_success_result_path = resultsdir + "\\" + "secondary_success_result.txt"

    ##第4类 Count of valid signatures: 0
    both_fail_result_path = resultsdir + "\\" + "both_fail_result.txt"

    total_count = 0
    both_success_count = 0
    primary_success_count = 0
    secondary_success_count = 0
    both_fail_count = 0

    total_log_name = []
    both_success_log_name = []
    primary_success_log_name = []
    secondary_success_log_name = []
    both_fail_log_name = []

    if not os.access(resultsfolder, os.F_OK):
        os.mkdir(resultsfolder)

    if not os.access(resultsdir, os.F_OK):
        os.mkdir(resultsdir)

    ##delete the old result files if exist
    if os.access(sum_result_path, os.F_OK):
        os.unlink(sum_result_path)

    if os.access(detail_result_path, os.F_OK):
        os.unlink(detail_result_path)

    if os.access(both_success_result_path, os.F_OK):
        os.unlink(both_success_result_path)

    if os.access(primary_success_result_path, os.F_OK):
        os.unlink(primary_success_result_path)

    if os.access(secondary_success_result_path, os.F_OK):
        os.unlink(secondary_success_result_path)

    if os.access(both_fail_result_path, os.F_OK):
        os.unlink(both_fail_result_path)

    ##write the introductions into the result files
    function_used.file_append(sum_result_path,"This file record the sum results\n")
    function_used.file_append(detail_result_path,"This file record all the detail results\n")
    function_used.file_append(both_success_result_path,"This file record first classification -- Count of valid signatures: 2\n")
    function_used.file_append(primary_success_result_path,"This file record second classification -- Count of valid signatures: 1 (Primary signature verify success!)\n")
    function_used.file_append(secondary_success_result_path,"This file record third classification -- Count of valid signatures: 1 (Verify secondary signature Success!)\n")
    function_used.file_append(both_fail_result_path,"This file record forth classification -- Count of valid signatures: 0\n")

    ## to classify the logs
    print "\tStart to classify the logs"
    for x in os.listdir(report_path):
        ##if exist son folder
        temp = os.path.join(report_path, x)
        if os.path.isdir(temp):
            report_son_path = os.path.join(report_path, x)

            for y in os.listdir(report_son_path):
                file_path = os.path.join(report_son_path, y)
                with open(file_path,'r') as f:
                    contents = []
                    line_count = 0
                    for line in f.readlines():
                        contents.append(line)
                        line_count += 1

                    total_count += 1
                    total_log_name.append(y)
                    if contents[line_count - 1].find('Count of valid signatures: 2') != -1:
                        both_success_count += 1
                        both_success_log_name.append(y)
                        function_used.file_append(detail_result_path,"%s -- Count of valid signatures: 2" % y)

                    elif contents[line_count - 1].find('Count of valid signatures: 1')!= -1:
                        if contents[1].find('Primary signature verify success!')!= -1:
                            primary_success_count += 1
                            primary_success_log_name.append(y)
                            function_used.file_append(detail_result_path,"%s -- Count of valid signatures: 1 (Primary signature verify success!)" % y)

                        else:
                            secondary_success_count += 1
                            secondary_success_log_name.append(y)
                            function_used.file_append(detail_result_path,"%s -- Count of valid signatures: 1 (Verify secondary signature Success!)" % y)

                    else:
                        both_fail_count += 1
                        both_fail_log_name.append(y)
                        function_used.file_append(detail_result_path,"%s -- Count of valid signatures: 0" % y)
        ##if x is a file
        else:
            file_path = os.path.join(report_path, x)
            with open(file_path,'r') as f:
                contents = []
                line_count = 0
                for line in f.readlines():
                    contents.append(line)
                    line_count += 1

                total_count += 1
                total_log_name.append(x)
                if contents[line_count - 1].find('Count of valid signatures: 2') != -1:
                    both_success_count += 1
                    both_success_log_name.append(x)
                    function_used.file_append(detail_result_path,"%s -- Count of valid signatures: 2" % x)

                elif contents[line_count - 1].find('Count of valid signatures: 1')!= -1:
                    if contents[1].find('Primary signature verify success!')!= -1:
                        primary_success_count += 1
                        primary_success_log_name.append(x)
                        function_used.file_append(detail_result_path,"%s -- Count of valid signatures: 1 (Primary signature verify success!)" % x)

                    else:
                        secondary_success_count += 1
                        secondary_success_log_name.append(x)
                        function_used.file_append(detail_result_path,"%s -- Count of valid signatures: 1 (Verify secondary signature Success!)" % x)

                else:
                    both_fail_count += 1
                    both_fail_log_name.append(x)
                    function_used.file_append(detail_result_path,"%s -- Count of valid signatures: 0" % x)
    
    print "\tend classify the logs"

    ## write results
    print "\tStart to write results"
    function_used.file_append(sum_result_path,"total_count : %s" % total_count)
    function_used.file_append(sum_result_path,"both_success_count : %s" % both_success_count)
    function_used.file_append(sum_result_path,"primary_success_count : %s" % primary_success_count)
    function_used.file_append(sum_result_path,"secondary_success_count : %s" % secondary_success_count)
    function_used.file_append(sum_result_path,"both_fail_count : %s" % both_fail_count)

    function_used.file_append(sum_result_path,"\nboth_success_count : %s\n" % both_success_count)
    if both_success_count != 0:
        function_used.file_append(sum_result_path,"\tlog names are:")
        for log_name in both_success_log_name:
            function_used.file_append(sum_result_path,"\t\t%s" % log_name)

    function_used.file_append(sum_result_path,"\nprimary_success_count : %s\n" % primary_success_count)
    if primary_success_count != 0:
        function_used.file_append(sum_result_path,"\tlog names are:")
        for log_name in primary_success_log_name:
            function_used.file_append(sum_result_path,"\t\t%s" % log_name)

    function_used.file_append(sum_result_path,"\nsecondary_success_count : %s\n" % secondary_success_count)
    if secondary_success_count != 0:
        function_used.file_append(sum_result_path,"\tlog names are:")
        for log_name in secondary_success_log_name:
            function_used.file_append(sum_result_path,"\t\t%s" % log_name)

    function_used.file_append(sum_result_path,"\nboth_fail_count : %s\n" % both_fail_count)
    if both_fail_count != 0:
        function_used.file_append(sum_result_path,"\tlog names are:")
        for log_name in both_fail_log_name:
            function_used.file_append(sum_result_path,"\t\t%s" % log_name)

    function_used.file_append(detail_result_path,"\n")
    function_used.file_append(detail_result_path,"total_count : %s" % total_count)
    function_used.file_append(detail_result_path,"both_success_count : %s" % both_success_count)
    function_used.file_append(detail_result_path,"primary_success_count : %s" % primary_success_count)
    function_used.file_append(detail_result_path,"secondary_success_count : %s" % secondary_success_count)
    function_used.file_append(detail_result_path,"both_fail_count : %s" % both_fail_count)
    function_used.file_append(detail_result_path,"\n")

    function_used.file_append(both_success_result_path,"both_success_count : %s\n" % both_success_count)
    if both_success_count != 0:
        function_used.file_append(both_success_result_path,"\tlog names are:")
        for log_name in both_success_log_name:
            function_used.file_append(both_success_result_path,"\t\t%s" % log_name)

    function_used.file_append(primary_success_result_path,"primary_success_count : %s\n" % primary_success_count)
    if primary_success_count != 0:
        function_used.file_append(primary_success_result_path,"\tlog names are:")
        for log_name in primary_success_log_name:
            function_used.file_append(primary_success_result_path,"\t\t%s" % log_name)

    function_used.file_append(secondary_success_result_path,"secondary_success_count : %s\n" % secondary_success_count)
    if secondary_success_count != 0:
        function_used.file_append(secondary_success_result_path,"\tlog names are:")
        for log_name in secondary_success_log_name:
            function_used.file_append(secondary_success_result_path,"\t\t%s" % log_name)

    function_used.file_append(both_fail_result_path,"both_fail_count : %s\n" % both_fail_count)
    if both_fail_count != 0:
        function_used.file_append(both_fail_result_path,"\tlog names are:")
        for log_name in both_fail_log_name:
            function_used.file_append(both_fail_result_path,"\t\t%s" % log_name)

    print "\tend to write results"
    print "end Check_VerifySign_log.py"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        para_num = len(sys.argv) - 1
        print 'Error!! Param Number should be 1,not %d' % para_num
        print 'Usage:'
        print '      Check_VerifySign_log.py [report_path]\nExample:Check_VerifySign_log.py \\10.204.16.28\Home\DCE\Zhiyang_chen\SHA1andSHA2\TestSuite\report'
    else:
        report_path = sys.argv[1]
        main(report_path) 
