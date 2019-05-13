"""
获取装备数据，保存csv文件
http://chess.uuu9.com/equip/{}.html   2-45  共44件装备
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
    equipment_name=soup.find('dt').find('p').contents[0]   # 装备名称
    content=soup.find('dd')
    introduce=content.find("p").contents   # 装备介绍
    hecheng=content.find_all('h5')[1:]
    hecheng_list=content.find_all('ul')
    composes_from_contents=''
    composes_to_contents=''
    for hecheng ,hecheng_list in zip(hecheng,hecheng_list):
        if hecheng.contents[0]=='合成公式':
            composes_from=hecheng_list.find_all('li')
            for compose_from in composes_from:
                try:
                    compose_from=compose_from.find('p').contents[0]
                    composes_from_contents += '{}+'.format(compose_from)
                except:
                    pass

        if hecheng.contents[0]=='进阶合成物品':
            composes_to=hecheng_list.find_all('li')
            for compose_to in composes_to:
                compose_to=compose_to.find('p').contents[0]
                composes_to_contents += '{}+'.format(compose_to)
    composes_from_contents=composes_from_contents.rstrip('+')
    composes_to_contents=composes_to_contents.rstrip('+')
    # print(equipment_name)
    # print(introduce)
    # print('合成公式',composes_from_contents)a
    # print('进阶合成物品',composes_to_contents)
    # print("------------------------------------")

    with open(file,'a')as f:
        trantab = str.maketrans("'[']", "    ")
        write_contents="{}#{}#{}#{}\n".format(equipment_name,introduce,composes_from_contents,composes_to_contents).translate(trantab).replace(" ",'')

        f.write(write_contents)
    return True

def equipment_csv_G(file):
    base_web="http://chess.uuu9.com/equip/{}.html"

    with open(file, 'w')as f:
        f.write('名字#介绍#合成公式#进阶合成物品\n')
    for i in range(2,46):
        web=base_web.format(i)
        read_write_web(web,file)

if __name__=='__main__':
    equipment_csv_G(file="csv_files/equipment.csv")