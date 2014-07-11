#coding:utf-8

# http://docs.python-requests.org/en/latest/    requests包

import requests,re,json
import sys

#2句话解决 UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-78
reload(sys)
sys.setdefaultencoding('utf8')

s = requests.session()
login_data = {'email':'######','password':'#####'}

s.post('http://www.zhihu.com/login',login_data)

r = s.get('http://www.zhihu.com/people/kaifulee/followers')

# print r.url


# 想要得到followers列表，所以我下一步要实现页面点击“更多”按钮的功能
# 必须要对信息headers和params进行伪装
global header_info
header_info = {
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1581.2 Safari/537.36',
'Host':'www.zhihu.com',
'Origin':'http://www.zhihu.com',
'Connection':'keep-alive',
'Referer':'http://www.zhihu.com/people/zihaolucky/followers',
'Content-Type':'application/x-www-form-urlencoded',
}

# form data
data =  r.text    # 相当于urllib.urlopen(url).read()
raw_hash_id = re.findall('hash_id(.*)',data)
hash_id = raw_hash_id[0][14:46]    # hash_id
# raw_hash_id[0][0:46]
# &quot;: &quot;043ff01e5d03c529c268d50f388012c2
# print hash_id
# 043ff01e5d03c529c268d50f388012c2

raw_xsrf = re.findall('xsrf(.*)',data)
_xsrf = raw_xsrf[0][9:-3]          # _xsrf

# print _xsrf
# 1a08f2721bd649f583cb59aaa8f26c06
# print  raw_xsrf[0][:]
# " value="1a08f2721bd649f583cb59aaa8f26c06"/>
#  print _xsrf

offsets = 20
# 由于返回的是json数据,所以用json处理parameters.
params = json.dumps({"hash_id":hash_id,"order_by":"created","offset":offsets,})
payload = {"method":"next","params":params,"_xsrf":_xsrf}

# 发送这个请求了
click_url = 'http://www.zhihu.com/node/ProfileFollowersListV2'
r = s.post(click_url,data=payload,headers=header_info)

print r.text

print type(r.text)
f = open('1.txt','w')
f.write(str( r.text) )
f.close()