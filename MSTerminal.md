## Features

**winget** exposes the following commands and options for the preview.

- **install** Installs the given application
- **show** Shows info about an application
- **source** Manage sources of applications
- **search** Find and show basic info of apps
- **hash** Helper to hash installer files
- **validate** Validates a manifest file
- **--help** Provides command line help
- **--info** Provides addition data, helpful for troubleshooting
- **--version** Provides the version of the client



```bash
Windows Package Manager v0.1.41331 预览
Copyright (c) Microsoft Corporation. All rights reserved.

WinGet 命令行实用工具可从命令行安装应用程序。

usage: winget [<command>] [<options>]

下列命令有效:
  install   安装指定的应用程序
  show      显示关于应用的信息
  source    管理应用源
  search    查找并显示应用的基本信息
  hash      哈希安装程序的帮助程序
  validate  验证清单文件

如需特定命令的更多详细信息，请向其传递帮助参数。 [-?]

下列选项可用：
  -v,--version  显示工具的版本
  --info        显示工具的常规信息

可在此找到更多帮助： https://aka.ms/winget-command-help
```



Winget 下载地址：

官方 Github：https://github.com/microsoft/winget-cli/releases

搬运地址：https://www.jianguoyun.com/p/Dd8JlckQn7KEBxjXx5sD 



## Powershell 修改主题

首先安装 `oh-my-posh`

```powershell
Install-Module -Name oh-my-posh
```

然后参考这个开源项目的介绍 https://gitee.com/yefcion/oh-my-posh

安装 `posh-git` 和 `oh-my-posh`

```powershell
Install-Module posh-git -Scope CurrentUser
Install-Module oh-my-posh -Scope CurrentUser
```

（非必要）如果要编辑 PowerShell 配置文件，输入如下命令：

```powershell
if (!(Test-Path -Path $PROFILE )) { New-Item -Type File -Path $PROFILE -Force }
notepad $PROFILE
```

将以下行追加到 PowerShell 配置文件中：

```powershell
Import-Module posh-git
Import-Module oh-my-posh
Set-Theme Paradox
```



之后就可以设置主题了



```powershell
# 查看当前设置
$ThemeSettings
```

