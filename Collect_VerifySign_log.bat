@echo off
rem   This bat is created to collect VerifySign log from local computer to a remote path 
rem   Author:         zhiyang_chen@trendmicro.com.cn
rem   Created Date:   2015/11/12
echo Start Collect_VerifySign_log.bat

	rem modify remotedir,username,password if necessary
	set remotedir=\\10.204.16.28\Home\DCE\Zhiyang_chen
	set username=trend\zhiyang_chen
	set password=tre!##13
	
	set remote_report_dir=%remotedir%\VerifySign_log
	set report_dir=%1
	
	rem for /f "tokens=4" %%a in ('route print^|findstr 0.0.0.0.*0.0.0.0') do (
	rem 	set IP=%%a
	rem )
		
	rem net use \\10.204.16.28\Home\DCE\Zhiyang_chen "Etslab_123" /user:dce
	rem net use \\10.204.16.28\Home\DCE\Zhiyang_chen /user:trend\zhiyang_chen tre!##13
	rem net use \\10.204.16.28\Home\DCE\Zhiyang_chen /user:dce Etslab_123
	net use %remotedir% /user:%username% %password%

	rem create remote report dir
	if not exist %remote_report_dir% (
		md %remote_report_dir%
	)
	
	set remote_thispc_report_dir=%remote_report_dir%\%computername%
	
	rem delete and then create remote_thispc_report_dir
	if exist %remote_thispc_report_dir% (
		rd /s /q %remote_thispc_report_dir%
	)
	
	md %remote_thispc_report_dir%
	
	rem copy file from remote_thispc_report_dir
	
	rem xcopy c:\1.txt \\10.204.16.28\Home\DCE\Zhiyang_chen
	if exist %report_dir% (
		FOR /r %report_dir% %%C IN (*?) DO xcopy %%C %remote_thispc_report_dir%
	)
	
echo End Collect_VerifySign_log.bat