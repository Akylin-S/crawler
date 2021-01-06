# crawler
## 爬虫学习

### 最简单的爬虫学习

####**DAY1**

1.**有道翻译**

2.**王者荣耀皮肤**

###**DAY2**

3.**~~英雄联盟皮肤~~**

    看改进版的就行

4.**英雄联盟皮肤-改进**
     
####**Ⅰ.改进**

        相比较第一次爬取皮肤，第一次图片网站是通过经验拼接出来的，第二次是解决第一次一直解码的错误，后来发现用GBK解码便可解决，所以便可以找到英雄皮肤列表及图片地址实现爬取
####**Ⅱ.访问太多，ssl证书验证错误**
        爬取次数太多，出现了SSL证书验证错误，这可能要用到最简单的反爬技术
        1. 代理池法
		import requests 

		proxy = { 
			"http": "http://12.13.1.10:1234",
			 "https": "http://12.11.2.15:2048", 
			 } 
		response = requests.get(url, proxies=proxy).content.decode())
		print(response) 
        2.SSL证书验证错误
            import requests 

            url = "https://www.baidu.com/"
            response = requests.get(url,verify=False).content.decode()     # 默认解码方式为UTF-8
            print(response)
        3.User Agent中文名为用户代理，是Http协议中的一部分，属于头域的组成部分，User Agent也简称UA。它是一个特殊字符串头，是一种向访问网站提供你所使用的浏览器类型及版本、操作系统及版本、浏览器内核、等信息的标识。通过这个标识，用户所访问的网站可以显示不同的排版从而为用户提供更好的体验或者进行信息统计；例如用手机访问谷歌和电脑访问是不一样的，这些是谷歌根据访问者的UA来判断的。UA可以进行伪装。

          浏览器的UA字串的标准格式：浏览器标识 (操作系统标识; 加密等级标识; 浏览器语言) 渲染引擎标识版本信息。但各个浏览器有所不同。
            
            from fake_useragent import UserAgent
            import requests 

            url = 'https://www.baidu.com/'
            ua = UserAgent().random
            header = {
                'User-Agent': ua
            }
            response = requests.get(url, headers=header, verify=False).content.decode()
            print(response)
        4.  “HTTP
            Referer是header的一部分，当浏览器向web服务器发送请求的时候，一般会带上Referer，告诉服务器我是从哪个页面链接过来的，服务器籍此可以获得一些信息用于处理。”
            url = 'https://www.baidu.com/'
            ua = UserAgent().random
            header = {
		        'Referer': 'https://www.baidu.com/',
                'User-Agent': ua
            }
            response = requests.get(url, headers=header, verify=False).content.decode()
            print(response)
        5. time 休眠
####**Ⅲ 创建文件时，出现/**
    创建文件时出现了转义字符，半角用全角替换
    string.replace('/','／') .replace('\\','＼')
    或者 replace('/',unichr(ord('/')+65248)).replace('\\',unichr(ord('\\')+65248))
    除了空格 其它半角+65248=全角 另外注意\的转意 所以用\\
    
5.**书籍网站**
