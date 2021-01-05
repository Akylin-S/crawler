import urllib.request
import urllib.parse
import json


def fanyi():
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15601659811655'
    data['sign'] = '78817b046452f9663a2b36604f220360'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTTIME'
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    print('翻译:%s' % (target['translateResult'][0][0]['tgt'])+'\n')


if __name__ == '__main__':

    while True:
        content = input('请输入你要翻译的文字:')
        fanyi()

