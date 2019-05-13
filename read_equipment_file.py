import pandas as pd
from py2neo import *
import os
from equipment import equipment_csv_G



def equipment_node_relationship_G(file,graph):

    if not os.path.exists(file):
        print('{} 文件不存在，正在爬取数据'.format(file))
        equipment_csv_G(file)

    df=pd.read_csv(file,'#')
    names=df['名字']
    intros=df['介绍']
    compose_froms=df['合成公式']
    compose_tos=df['进阶合成物品']
    for name,intro,compose_from in zip(names,intros,compose_froms):

        equipment_node=Node('Equipment',
                       name=name,
                       intro=intro,
                       composes_froms=compose_from,
                       )
        if not graph.find_one(label='Equipment',property_key='name',property_value=name):
            graph.create(equipment_node)
            print('创建了新 结点 ： {}'.format(equipment_node))
    for name,compose_to in zip(names,compose_tos):
        if compose_to == compose_to:    # 判nan
            for compose in compose_to.split('+'):
                start_node=graph.find_one(label='Equipment',property_key='name',property_value=name)
                end_node=graph.find_one(label='Equipment',property_key='name',property_value=compose)

                relationship=Relationship(start_node,'合成',end_node)
                graph.create(relationship)
                print('新建关系： {}'.format(relationship))
if __name__=='__main__':
    graph = Graph(password="12311qq")
    equipment_file = 'csv_files/equipment.csv'
    equipment_node_relationship_G(equipment_file,graph)