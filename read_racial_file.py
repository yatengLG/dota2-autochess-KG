import pandas as pd
from py2neo import *
import os
from racial import raical_csv_G

def racial_node_relationship_G(racial_csv,graph):

    if not os.path.exists(racial_csv):
        print('{} 文件不存在，正在爬取数据'.format(racial_csv))
        raical_csv_G(racial_csv)
        print("-------------------------------------------------------")
    df=pd.read_csv(racial_csv,'#')
    racials=df['种族']
    heros_names=df['英雄']

    for racial,heros_name in zip(racials,heros_names):
        if not graph.find_one(label='Racial',property_key='name',property_value=racial):
            racial_node=Node('Racial',
                   name=racial
                   )
            graph.create(racial_node)
            print('创建了新的结点：{}'.format(racial_node))

        for hero_name in heros_name.split(','):
            hero_node=graph.find_one(label='Hero',property_key='name',property_value=hero_name)
            racial_node=graph.find_one(label='Racial', property_key='name', property_value=racial)


            relationship=Relationship(hero_node,'种族',racial_node)
            graph.create(relationship)
            print('新建关系： {}'.format(relationship))
    return True


if __name__=='__main__':
    racial_csv='csv_files/racial.csv'
    graph = Graph(password="12311qq")
    racial_node_relationship_G(racial_csv,graph)