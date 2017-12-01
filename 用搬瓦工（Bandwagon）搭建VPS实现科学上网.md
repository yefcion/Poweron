##写在前面
1. FQ是为了学习交流、使用工具
2. 以国为荣，不惹事端
###起因
网面上所有hosts（以[老D博客](https://laod.cn/hosts/2017-google-hosts.html)为例）不能用，各种VPN被封，导致我所使用的Google系列产品无法使用。最近看到一个朋友的技术贴，觉得FQ这种技术活掌握在手里也挺好，所以我也开始尝试了。
###介绍
这项活动不难，`按部就班`即可完成。当然，我的做法可能比较小白，无法发掘VPS全部功能，但是就我的初衷`顺利FQ`而言，完美稳定。
简单介绍一下梗概：
1. 购买搬瓦工（Bandwagon）VPS
2. 配置VPS
3. 配置终端，PC/Android/IOS客户端
4. 科学上网

###1. 购买VPS
    知名VPS服务商有：Bandwagon、Vultr 、 Linode。
    我使用Bandwagon，原因很简单：便宜，可支付宝。
    KVM、$25.99 USD包年、USCA_2
    可以几个人合买哦，因为配置完之后理论上是没有使用人数限制的，只不过就像宽带一样，人多了速度自然就会慢了
   1.1 登录[搬瓦工](https://bwh1.net/index.php)网址

[![](./_image/2017-12-01-13-49-45.jpg)]
1.2 选择套餐，加入购物车：

[![](./_image/2017-12-01-13-50-52.jpg)]
本着价格优先和稳定够用的原则，我选了第二便宜的套餐（最便宜的套餐常年断货）
至于`KVM`还是`OVZ`，推荐KVM，这是一番比较之后的结果。看过的文章忘记保存，以后有机会的话放网址。
之后是套餐内容：
![](./_image/2017-12-01-13-55-19.jpg)
选择时长和服务器位置：包月、包年；洛杉矶、加拿大、日本等
我选择了`包年`、`洛杉矶_2`
1.3 确认订单与付款
![](./_image/2017-12-01-13-57-47.jpg)
这里可以填优惠码，用了会打折扣（和国内软件邀请机制一样，双方都有优惠），然后checkout
如果是新用户的话需要注册，要填的信息如下：姓名、邮件、地址、电话。这里可以选择支付宝(Alipay)付款，最后complete order完成。
![](./_image/2017-12-01-14-04-47.jpg)
购买成功后，邮箱收到三封邮件，里面有重要信息（SSH port、VPS IP、root 临时密码）需要记录。之后有用。
以上VPS的购买完成，下面进入配置。
###2. 配置VPS
2.1 返回home，进入client area，找到service，`my services`,进入`KiwiVM`控制面板
![](./_image/2017-12-01-14-09-36.jpg)
![](./_image/2017-12-01-14-11-46.jpg)
![](./_image/2017-12-01-14-13-33.jpg)
2.2 配置KiwiVM(核心在这里)

    面板中要用到的面板选项下图标出：
![](./_image/2017-12-01-14-21-04.jpg)
    - main controls(主控中心)
    - install OS(安装系统)
    - root password modification(根密码修改)
    - KiwiVM password modification(KiwiVM密码修改)
    - Shadowsocks serve(Shadowsocks服务)
    - ShadowsocksR serve(ShadowsocksR服务)
1) 首先，可以修改用户名，这个就是个人喜好的问题，可以不改，之后配置没什么用。（ ~~但如果你用 putty 的话，这个就是登陆的名字，由于这个教程面向我这种小白用户，所以这段话可以忽略~~）
![](./_image/2017-12-01-14-29-50.jpg)
2) 重装系统。
这里本来是默认装了CentOS的系统，但是清洁起见还是重装一下。
Main controls面板，单击Stop，然后Install new OS 这里，选择 CentOS-6-x86_64-bbr，勾选 I agree， 点击 Reload。然后看密码，或者修改。
	• Root password modification 这个是装系统之后，搬瓦工随机分配的密码，自己不能修改，`记录这里的信息`（邮箱里也会收到） 
	• KiwiVM password modification 是登陆账号的密码，直接写新密码。这样的话最开始邮件收到的密码就可以不用了。从这步开始购买VPS时的邮件内容就不用了。
3）安装 ShadowsocksR Server和Shadowsocks serve
本来可以只安装一个ShadowsocksR Server，但是后来测试必须要把Shadowsocks serve也安装上才能正确上网所以这里我们一步到位。另外这里建议使用ShadowsocksR，因为安全。
两个服务都是自动安装，自动装好之后记录显示的消息，用客户端FQ就`靠这些信息`了。
![](./_image/2017-12-01-14-43-52.jpg)
以上VPS配置工作就完成了，只要在终端登录就可以实现科学上网了
###3. 配置终端
客户端下载，点击关键词即可下载。
- PC
    [SSR-4.7.0](https://cache.cdn.bydisk.com/ShadowsocksR-4.7.0-win.7z)
- IOS
    [Wingy](https://itunes.apple.com/us/app/wingy-http-s-socks5-proxy-utility/id1178584911)
    [shadowrocket](https://itunes.apple.com/us/app/shadowrocket/id932747118)
- Android
    [SSR-3.4.0.5](https://qiniucloud.download.storage.bydisk.com/ssr-3.4.0.5.apk)
- MAC
    [ShadowrocksX-NG-R](https://github.com/qinyuhang/ShadowsocksX-NG-R/releases)
    [electron-ssr](https://github.com/erguotou520/electron-ssr/releases)

配置案例：
1. 以win为例：
把ShadowsocksR Server的信息填到客户端，完成单击确定即可。
![](./_image/2017-12-01-14-58-39.jpg)
2. 以IOS客户端Wing为例：
把ShadowsocksR Server的信息填到客户端，完成单击确定即可。
![](./_image/2017-12-01-15-03-56.jpg)

测试网页：
[Google](www.google.com.hk/?hl=zh-cn)
[Facebook](https://www.facebook.com/)














