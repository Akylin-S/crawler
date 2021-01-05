import os
import requests

url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)  # 获取英雄列表json文件
herolist_json = herolist.json()  # 转化为json格式
hero_name = list(map(lambda x: x['cname'], herolist.json()))  # 提取英雄的名字
hero_number = list(map(lambda x: x['ename'], herolist.json()))  # 提取英雄的编号


def download_pict():
    i = 0
    for j in hero_number:
        # 创建文件夹
        os.makedirs("D:\download\\wzry\\" + hero_name[i])
        # 进入文件夹
        os.chdir("D:\download\\wzry\\" + hero_name[i])
        for k in range(10):
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(
                j) + '-bigskin-' + str(k) + '.jpg'
            request = requests.get(onehero_link)  # 请求url
            if request.status_code == 200:#若有图片
                with open(str(k) + '.jpg', 'wb') as f:
                    f.write(request.content)
        print(str(hero_name[i]), "保存成功")
        i += 1


if __name__ == "__main__":
    download_pict()
