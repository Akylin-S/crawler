import json
import os
import shutil
import time
import requests


def DownloadLOLSkin():
    url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    req = requests.get(url).content
    req = json.loads(req.decode())
    hero_list = req['hero']
    i=0
    for hero in hero_list:
        i+=1
        print('一共'+str(len(hero_list))+'个英雄，正在下载第'+str(i)+'个英雄皮肤')
        k = 0
        j = 0
        if os.path.exists(".\\lol\\" + hero['name']):
            shutil.rmtree(".\\lol\\" + hero['name'])  # 删除再建立
            os.makedirs(".\\lol\\" + hero['name'])
        else:
            os.makedirs(".\\lol\\" + hero['name'])
        os.chdir(".\\lol\\" + hero['name'])
        while k <= 30:

            if k < 10:
                url_hero = 'https://game.gtimg.cn/images/lol/act/img/skin/big' + str(
                    hero['heroId'] + '00' + str(k) + '.jpg')
                req_hero = requests.get(url_hero.encode('utf-8'))
                k = k + 1
                if req_hero.status_code == 200:  # 若有图片
                    print('正在下载' + hero['name'] + '第' + str(k - j) + '个皮肤')
                    with open(str(k - j) + '.jpg', 'wb') as f:
                        f.write(req_hero.content)
                else:
                    j = j + 1
            if k >= 10:
                url_hero = 'https://game.gtimg.cn/images/lol/act/img/skin/big' + str(
                    hero['heroId'] + '0' + str(k) + '.jpg')
                req_hero = requests.get(url_hero.encode('utf-8'))
                k = k + 1
                if req_hero.status_code == 200:  # 若有图片
                    print('正在下载' + hero['name'] + '第' + str(k - j) + '个皮肤')
                    with open(str(k - j) + '.jpg', 'wb') as f:
                        f.write(req_hero.content)
                else:
                    j = j + 1
            time.sleep(2)
        os.chdir('..//..//')


if __name__ == "__main__":
    DownloadLOLSkin()
