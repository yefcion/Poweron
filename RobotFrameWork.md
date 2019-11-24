python3 安装 ride

1、安装python3

下载安装包，安装

2、安装 python 相关库

	# robotframework RF
	python -m pip install robotframework -i http://mirrors.zte.com.cn/pypi/simple/ --trusted-host mirrors.zte.com.cn
	
	# robotframework-seleniumlibrary 关键字驱动用例时使用
	python -m pip install robotframework-seleniumlibrary -i http://mirrors.zte.com.cn/pypi/simple/ --trusted-host mirrors.zte.com.cn
	
	# wxpython
	python -m pip install wxpython -i http://mirrors.zte.com.cn/pypi/simple/ --trusted-host mirrors.zte.com.cn
	
	# pygments 代码高亮相关库，运行ride需要
	python -m pip install pygments -i http://mirrors.zte.com.cn/pypi/simple/ --trusted-host mirrors.zte.com.cn
	
	# pywin32 安装ride需要
	python -m pip install pywin32 -i http://mirrors.zte.com.cn/pypi/simple/ --trusted-host mirrors.zte.com.cn
	
	# robotframework-ride 安装 ride
	python -m pip install robotframework-ride -i http://mirrors.zte.com.cn/pypi/simple/ --trusted-host mirrors.zte.com.cn
	
	下面的选择性安装，可以不装
	# pycryptodome 需要在安装sshlibrary库前安装
	# robotframework-sshlibrary
	# robotframework-requests
	# robotframework-databaselibrary
	# robotframework-appiumlibrary
	
3、启动 ride
	
	到 python 安装目录下 用 python 执行 py373\Scripts\ride.py
	可以写一个 bat 脚本执行放到桌面作为启动 ride 的快捷方式（注：脚本中的路径填自己的）
	```
		@echo off
		echo ***************************
		echo ****  ride 启动中...  *****
		echo ***************************
		::timeout /T 3
		echo 耐心等待
		echo Ride 启动后别关 cmd 窗口
		cd /d D:\Program Files\Python\py373\Scripts
		python ride.py
	```
	