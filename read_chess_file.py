import pandas as pd
from py2neo import *
import os
from chess import chess_csv_G



def chess_node_G(file,graph):

    if not os.path.exists(file):
        print('{} 文件不存在，正在爬取数据'.format(file))
        chess_csv_G(file)

    df=pd.read_csv(file,'#')
    names=df['名字']
    intros=df['介绍']
    skills=df['技能']
    attrs=df['属性']
    for name,intro,skill,attr in zip(names,intros,skills,attrs):
        attr=attr.split(',')
        attr_list=[]
        for i in attr:
            try:
                a=float(i)
                attr_list.append(a)
            except:
                pass

        hero_node=Node('Hero',
                       name=name,
                       intro=intro,
                       skills=skill,
                       attr=attr_list,
                       )
        if not graph.find_one(label='Hero',property_key='name',property_value=name):
            graph.create(hero_node)
            print('创建了新 结点 ： {}'.format(hero_node))

if __name__=='__main__':
    graph = Graph(password="12311qq")
    chess_file = 'csv_files/chess.csv'
    chess_node_G(chess_file,graph)