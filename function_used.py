#
#   This Library is created to check VerifySign log
#   Author:         zhiyang_chen@trendmicro.com.cn
#   Created Date:   2015/11/12
#

import os
import sys
import subprocess
import platform
import time
import glob
import filecmp
import hashlib
import shutil
  
def connect_remote_path(remotedir,username,password):
    """ connect remote path using username and password
        
    @Param:
        
    remotedir:  the remote path to connect

    username:   

    password: 

    Example:
    |Connect Remote Path | \\10.204.16.28\Home\DCE\Zhiyang_chen | trend\zhiyang_chen | tre!##13 |
                
    """
    connect_command = 'net use %s /user:%s %s' % (remotedir,username,password)
    process = subprocess.Popen(connect_command, shell = True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    return_code = process.stdout.read()
    if 'The command completed successfully.' in return_code:
        return 1
        #print '>> Connect remote path successfully'
    else:
        #raise AssertionError('>> Connect remote path failed: %s' % return_code) 
        return 0
            
def file_append(filepath,contents):
    """ append content to the file
        
    @Param:
        
    filepath:  the file path 

    contents:  the content to be append

    Example:
    |File Append | C:\Users\zhiyang_chen\Desktop\SHA1andSHA2\TestSuite\results\sum_result.txt | This file record all the detail results |
                
    """
    with open(filepath, 'a') as f:
        f.write(contents+'\n')
    
  
