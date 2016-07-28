@echo off
rem   This bat is created for VerifySign operations
rem   Author:         zhiyang_chen@trendmicro.com.cn
rem   Created Date:   2015/11/12
echo Start VerifySign_all.bat
rem if  exist "c:\\StartVerifySign.txt" goto end
	
	rem type nul>c:\\StartVerifySign.txt
	
	rem modify rootdir,the path you put this bat
	set rootdir=C:\Users\zhiyang_chen\Desktop\SHA1andSHA2\TestSuite
	echo %rootdir%
		
	rem modify dce_dir,dre_dir,ssapi_dir,tmebc_dir,the path you put these folders
	set dce_dir=%rootdir%\dce
	set dre_dir=%rootdir%\dre
	set ssapi_dir=%rootdir%\ssapi
	set tmebc_dir=%rootdir%\tmebc
		
	set report_dir=%rootdir%\report
	rem echo %report_dir%
	set Logs_dir=%rootdir%\Logs
	rem echo %Logs_dir%
	
	set VerifySign_32_path=%rootdir%\VerifySign_32.exe
	set VerifySign_64_path=%rootdir%\VerifySign_64.exe
	
	set dce_32_dir=%dce_dir%\32
	set dce_64_dir=%dce_dir%\64
	
	set dre_32_dir=%dre_dir%\32
	set dre_64_dir=%dre_dir%\64
	
	set ssapi_32_dir=%ssapi_dir%\32
	set ssapi_64_dir=%ssapi_dir%\64
	
	set tmebc_32_dir=%tmebc_dir%\32
	set tmebc_64_dir=%tmebc_dir%\64

	cd %rootdir%
	
	rem delete and then create report_dir and Logs_dir
	if exist %report_dir% (
		rd /s /q %report_dir%
		rem echo success mkdir report!
	)
	
	md %report_dir%

	if exist %Logs_dir% (
		rd /s /q %Logs_dir%
	)
	
	md %Logs_dir%
	
	rem start to run VerifySign_32.exe and VerifySign_64.exe
	
	rem ETS给的tool Primary signature是SHA1, second signature是SHA2.
	rem 收集log
	rem 在x86上验证2次
	rem VerifySign_X86.exe PE_X86 
	rem VerifySign_X86.exe PE_X64

	rem 在x64验证4次
	rem VerifySign_X86.exe PE_X86
	rem VerifySign_X86.exe PE_X64	
	rem VerifySign_X64.exe PE_X86
	rem VerifySign_X64.exe PE_X64
	if exist %dce_dir% (
	
		rem 所有机子都要跑VerifySign_32.exe
		
		rem FOR /R [[drive:]path] %%variable IN (set) DO command [command-parameters]
		rem 检查以 [drive:]path 为根的目录树，指向每个目录中的FOR语句
		rem 如果在 /R后没有指定目录，则使用当前目录。如果集仅为一个单点(.)字符，则枚举该目录树。
		FOR /r %dce_32_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_32.exe %%C %report_dir%
		FOR /r %dce_64_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_32.exe %%C %report_dir%

		rem 如果是X64,需要再跑VerifySign_64.exe
		if exist "c:\\program files (x86)" (			
		FOR /r %dce_32_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_64.exe %%C %report_dir%
		FOR /r %dce_64_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_64.exe %%C %report_dir%
		)
	)
	
	if exist %dre_dir% (
		FOR /r %dre_32_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_32.exe %%C %report_dir%
		FOR /r %dre_64_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_32.exe %%C %report_dir%

		if exist "c:\\program files (x86)" (			
		FOR /r %dre_32_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_64.exe %%C %report_dir%
		FOR /r %dre_64_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_64.exe %%C %report_dir%
		) 
	)
	
	if exist %ssapi_dir% (
		FOR /r %ssapi_32_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_32.exe %%C %report_dir%
		FOR /r %ssapi_64_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_32.exe %%C %report_dir%

		if exist "c:\\program files (x86)" (			
		FOR /r %ssapi_32_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_64.exe %%C %report_dir%
		FOR /r %ssapi_64_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_64.exe %%C %report_dir%
		) 
	)
	
	if exist %tmebc_dir% (
		FOR /r %tmebc_32_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_32.exe %%C %report_dir%
		FOR /r %tmebc_64_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_32.exe %%C %report_dir%

		if exist "c:\\program files (x86)" (			
		FOR /r %tmebc_32_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_64.exe %%C %report_dir%
		FOR /r %tmebc_64_dir% %%C IN (*?) DO call VerifySign_once.bat VerifySign_64.exe %%C %report_dir%
		) 
	)
	
	call Collect_VerifySign_log.bat %report_dir%

 :end
 echo end VerifySign_all.bat