"""
http://chess.uuu9.com/hero/66.html
获取棋子数据，保存生成csv文件
"""
from bs4 import BeautifulSoup
import requests

session=requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Referer': 'https://kyfw.12306.cn/otn/login/init',
}



def read_write_web(web,file):
    html=session.get(web,headers=headers).content.decode()
    Soup=BeautifulSoup(html,"lxml")
    soup=Soup.select(" body > div.sm_wrap > div.row > div.sm_box > dl ")[0]
    hero_name=soup.find('dt').find('p').contents
    content=soup.find('dd')
    introduce=content.find("p").contents
    Hero_skills=content.find('div',{"class":'sm_jn_con'}).find('div').find('p').contents
    attribute_table=content.find('div',{'class':'sm_table'}).find('table')
    attributes=attribute_table.find_all('tr')[1::2]
    attrs_list=[]
    for i,attr in enumerate(attributes):
        attr=attr.find_all('td')
        cost,sell,blood,arm,magic,recovery,min_attack,max_attack,attack_speed,attack_distance=attr
        cost,sell,blood,arm,magic,recovery,min_attack,max_attack,attack_speed,attack_distance=\
            cost.contents,sell.contents,blood.contents,arm.contents,magic.contents,recovery.contents,min_attack.contents,max_attack.contents,attack_speed.contents,attack_distance.contents
        attrs_list.append([cost,sell,blood,arm,magic,recovery,min_attack,max_attack,attack_speed,attack_distance])
    print(hero_name)
    print(introduce)
    print(Hero_skills)

    with open(file,'a')as f:
        trantab = str.maketrans("'[']", "    ")
        write_contents="{}#{}#{}#{}\n".format(hero_name,introduce,Hero_skills,attrs_list).translate(trantab).replace(" ",'')

        f.write(write_contents)
    return True

def chess_csv_G(file):
    base_web="http://chess.uuu9.com/hero/{}.html"

    with open(file, 'w')as f:
        f.write('名字#介绍#技能#属性\n')
    for i in range(3,67):
        web=base_web.format(i)
        read_write_web(web,file)

if __name__=='__main__':
    chess_csv_G(file="csv_files/chess.csv")