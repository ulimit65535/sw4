import json
import sys
import simplejson
import urllib.request
from etc import settings


def gettoken(corpid,corpsecret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    try:
        token_file = urllib.request.urlopen(gettoken_url)
    except urllib.request.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))
        sys.exit()
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token


def senddata(subject,content):
    try:
        corpid = settings.corpid
        corpsecret = settings.corpsecret
        touser = settings.wechat_user
    except:
        return

    access_token = gettoken(corpid,corpsecret)

    send_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + access_token

    send_values = {
        "touser":touser,
        #"toparty":"1",
        "msgtype":"text",
        "agentid":"1000003",
        "text":{
            "content":subject + '\n' + content
        },
        "safe":"0"
    }
    #send_data = json.dumps(send_values, ensure_ascii=False)
    send_data = simplejson.dumps(send_values, ensure_ascii=False).encode('utf-8')
    send_request = urllib.request.Request(send_url, send_data)
    response = json.loads(urllib.request.urlopen(send_request).read())
    print(str(response))


if __name__ == '__main__':
    user = str(sys.argv[1])
    subject = str(sys.argv[2])
    content = str(sys.argv[3])

    senddata(subject,content)
