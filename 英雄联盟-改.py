import json
import os
import shutil
import time
import requests


def DownloadLOLSkin():
    url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    req = requests.get(url,verify=False).content
    req = json.loads(req.decode())
    hero_list = req['hero']
    i = 0
    for hero in hero_list:
        i += 1
        url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/' + hero['heroId'] + '.js'
        req = requests.get(url,verify=False).content
        req = json.loads(req.decode())
        req = req['skins']
        print('一共' + str(len(hero_list)) + '个英雄，正在下载第' + str(i) + '个英雄皮肤')
        print('英雄： ' + hero['name']+' '+hero['title'])
        if os.path.exists(".\\lol改\\" + hero['name']):              # 如果存在
            shutil.rmtree(".\\lol改\\" + hero['name'])               # 删除再建立
            os.makedirs(".\\lol改\\" + hero['name'])
        else:
            os.makedirs(".\\lol改\\" + hero['name'])
        os.chdir(".\\lol改\\" + hero['name'])
        for skin in req:
            url_skin = skin['mainImg']
            if url_skin == '':
                continue
            req_hero = requests.get(url_skin)
            if req_hero.status_code == 200:                         # 若有图片
                print('皮肤： '+skin['name'])
                with open(skin['name'].replace('/','／') .replace('\\','＼') + '.jpg', 'wb') as f:        # 打开文件 若不存在则创建,里面有转义字符的话，半角转全角
                    f.write(req_hero.content)
                    f.close()                                       # 打开文件后一定要关闭
            time.sleep(2)
        os.chdir('..//..//')


if __name__ == "__main__":
    DownloadLOLSkin()
