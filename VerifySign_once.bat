@echo off
rem   This bat is created to run VerifySign_32.exe or VerifySign_64.exe once
rem   Author:         zhiyang_chen@trendmicro.com.cn
rem   Created Date:   2015/11/12
	
	rem VerifySign_32.exe or VerifySign_64.exe
	set tool=%1
	
	rem get 32 or 64
	rem 从%tool%的倒数第6位开始截取2位
	set bit=%tool:~-6,2%
	
	rem the file path, for example: C:\Users\zhiyang_chen\Desktop\SHA1andSHA2\TestSuite\dce\32\tsc.exe
	set file_path=%2
	rem set osname=%3
	
	rem the report dir, for example: C:\Users\zhiyang_chen\Desktop\SHA1andSHA2\TestSuite\report
	set report_dir=%3
	
	rem get file name,for example: tsc
	set file_name=%~n2
	
	rem get file attr,for example: exe
	set file_attr=%~x2
	
	rem for /f "tokens=4" %%a in ('route print^|findstr 0.0.0.0.*0.0.0.0') do (
	rem 	set IP=%%a
	rem )
	
	rem the log name,for example: tscexe_32_Win7X86.log
	set log=%report_dir%\%file_name%%file_attr:~1%_%bit%_%computername%.log

echo 	Start VerifySign_once.bat %file_name%.%file_attr%	
	rem VerifySign_32.exe C:\Users\zhiyang_chen\Desktop\SHA1andSHA2\TestSuite\dce\32\tsc.exe >tscexe_32_Win7X86.log
	
	rem run VerifySign_32.exe or VerifySign_64.exe once
	%tool% %file_path% >%log%

 :end
 echo 	end VerifySign_once.bat %file_name%.%file_attr%