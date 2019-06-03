"""
种族-英雄
http://chess.uuu9.com/index.html?rid=15
"""
from bs4 import BeautifulSoup
import requests

session=requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Referer': 'https://kyfw.12306.cn/otn/login/init',
}


def read_write_web(racial,web,file):
    html=session.get(web,headers=headers).content.decode()
    Soup=BeautifulSoup(html,"lxml")
    soup=Soup.select(" body > div.sm_wrap > div.row > div.clearfix > div.sm_pic > ul.clearfix")[0]

    heros=soup.find_all('li')
    heros_name=''
    for hero in heros:
        hero_name=hero.find('p').contents
        trantab = str.maketrans("'[']", "    ")
        hero_name='{}'.format(hero_name).translate(trantab).replace(" ",'')
        heros_name+=(hero_name+',')
    heros_name=heros_name.rstrip(',')
    with open(file,'a') as f:
        f.write("{}#{}\n".format(racial,heros_name))
        print(racial,heros_name)
    return True
def raical_csv_G(file):
    racial_index={
        '神':15,
        "萨特":14,
        "矮人":13,
        "亡灵":12,
        "恶魔":11,
        "娜迦":10,
        "龙":9,
        "巨魔":8,
        "地精":7,
        "精灵":6,
        "食人魔":5,
        "元素":4,
        "兽人":3,
        "人类":2,
        "野兽":1,
    }
    base_web="http://chess.uuu9.com/index.html?rid={}"

    with open(file, 'w')as f:
        f.write('种族#英雄\n')
    for racial in racial_index:
        web=base_web.format(racial_index[racial])
        read_write_web(racial,web,file)
    return True

if __name__=='__main__':
    raical_csv_G(file="csv_files/raical.csv")
