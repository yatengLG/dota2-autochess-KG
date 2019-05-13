import pandas as pd
from py2neo import *
from profession import profession_csv_G
import os

def profession_node_relationshap_G(profession_file,graph):
    if not os.path.exists(profession_file):
        print('{} 文件不存在，正在爬取数据'.format(profession_file))
        profession_csv_G(profession_file)
        print("-------------------------------------------------------")

    df=pd.read_csv(profession_file,'#')
    professions=df['职业']
    heros_names=df['英雄']

    for profession,heros_name in zip(professions,heros_names):
        if not graph.find_one(label='Profession',property_key='name',property_value=profession):
            profession_node=Node('Profession',
                   name=profession
                   )
            graph.create(profession_node)
            print('创建了新的结点：{}'.format(profession_node))

        for hero_name in heros_name.split(','):
            hero_node=graph.find_one(label='Hero',property_key='name',property_value=hero_name)
            profession_node=graph.find_one(label='Profession', property_key='name', property_value=profession)

            relationship=Relationship(hero_node,'职业',profession_node)
            graph.create(relationship)
            print('新建关系： {}'.format(relationship))

if __name__=='__main__':
    racial_csv='csv_files/profession.csv'
    graph = Graph(password="12311qq")
    profession_node_relationshap_G(racial_csv,graph)
