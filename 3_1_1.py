# import urllib.request
#
# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
##################################################################################################################
# import urllib.request
#
# response = urllib.request.urlopen('https://www.python.org')
# print(type(response))
##################################################################################################################
# import urllib.request
#
# response = urllib.request.urlopen('https://www.python.org')
# # 前两个输出分别输出了响应的状态码和响应的头信息，
# # 最后一个输出通过调用getheader()方法并传递一个参数Server获取了响应头中的Server值，
# # 结果是nginx，意思是服务器是用Nginx搭建的。
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

##################################################################################################################
# import urllib.parse
# import urllib.request
# # 这里我们传递了一个参数word，值是hello。它需要被转码成bytes（字节流）类型。
# # 其中转字节流采用了bytes()方法，该方法的第一个参数需要是str（字符串）类型，
# # 需要用urllib.parse模块里的urlencode()方法来将参数字典转化为字符串；
# # 第二个参数指定编码格式，这里指定为utf8
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# # 这里请求的站点是httpbin.org，它可以提供HTTP请求测试。
# # 本次我们请求的URL为http://httpbin.org/post，这个链接可以用来测试POST请求，
# # 它可以输出请求的一些信息，其中包含我们传递的data参数。
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())
##################################################################################################################
# import urllib.request
# # 这里我们设置超时时间是0.1秒
# response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# print(response.read())

##################################################################################################################
# import socket
# import urllib.request
# import urllib.error
# # 这里我们请求了http://httpbin.org/get测试链接，
# # 设置超时时间是0.1秒，然后捕获了URLError异常，
# # 接着判断异常是socket.timeout类型（意思就是超时异常），
# # 从而得出它确实是因为超时而报错，打印输出了TIME OUT
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

##################################################################################################################
# import urllib.request
#
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))


##################################################################################################################
# from urllib import request, parse
#
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))
##################################################################################################################


##################################################################################################################


# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
# # 这里使用了ProxyHandler，其参数是一个字典，
# # 键名是协议类型（比如HTTP或者HTTPS等），键值是代理链接，可以添加多个代理。
# proxy_handler = ProxyHandler({
#     # 这里我们在本地搭建了一个代理，它运行在8000端口上
#     'http': 'http://127.0.0.1:8000',
#     'https': 'https://127.0.0.1:8000'
# })
# # 利用这个Handler及build_opener()方法构造一个Opener，之后发送请求即可
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)
##################################################################################################################
# import http.cookiejar, urllib.request
# # 必须声明一个CookieJar对象。
# cookie = http.cookiejar.CookieJar()
# # 利用HTTPCookieProcessor来构建一个Handler
# handler = urllib.request.HTTPCookieProcessor(cookie)
# # 利用build_opener()方法构建出Opener
# opener = urllib.request.build_opener(handler)
# # 执行open()函数即可
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name + "=" + item.value)
##################################################################################################################
# import http.cookiejar, urllib.request
# filename = 'cookies.txt'
# # 这时CookieJar就需要换成MozillaCookieJar，它在生成文件时会用到，是CookieJar的子类，
# # 可以用来处理Cookies和文件相关的事件，比如读取和保存Cookies，可以将Cookies保存成Mozilla型浏览器的Cookies格式。
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)
##################################################################################################################
# import http.cookiejar, urllib.request
# filename = 'cookies1.txt'
# # 文件保存成LWP格式的Cookies文件
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)
##################################################################################################################
import http.cookiejar, urllib.request
cookie = http.cookiejar.LWPCookieJar()
# 这里调用load()方法来读取本地的Cookies文件，
# 获取到了Cookies的内容。不过前提是我们首先生成了LWPCookieJar格式的Cookies，
# 并保存成文件，然后读取Cookies之后使用同样的方法构建Handler和Opener即可完成操作。
cookie.load('cookies1.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
# 运行结果正常的话，会输出百度网页的源代码。
print(response.read().decode('utf-8'))