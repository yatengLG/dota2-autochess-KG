"""
职业 - 英雄
"""
"""
http://chess.uuu9.com/index.html?jid=11
"""
from bs4 import BeautifulSoup
import requests

session=requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Referer': 'https://kyfw.12306.cn/otn/login/init',
}


def read_write_web(profession,web,file):
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
        f.write("{}#{}\n".format(profession,heros_name))
        print(profession,heros_name)
    return True


def profession_csv_G(file):
    profession_index={
        "牧师":11,
        "猎人":10,
        "骑士":9,
        "术士":8,
        "刺客":7,
        "萨满祭司":6,
        "工匠":5,
        "恶魔猎手":4,
        "德鲁伊":3,
        "战士":2,
        "法师":1,
    }
    base_web="http://chess.uuu9.com/index.html?jid={}"

    with open(file, 'w')as f:
        f.write('职业#英雄\n')
    for profession in profession_index:
        web=base_web.format(profession_index[profession])
        read_write_web(profession,web,file)


if __name__=='__main__':
    profession_csv_G(file="csv_files/profession.csv")