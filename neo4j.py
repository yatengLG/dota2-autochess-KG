from py2neo import *
from read_chess_file import chess_node_G
from read_racial_file import racial_node_relationship_G
from read_profession_file import profession_node_relationshap_G
from read_equipment_file import equipment_node_relationship_G
from config import *
import time

chess_file = CHESS_FILE
racial_file = RACIAL_FILE
profession_file = PROFESSION_FILE
equipment_file = EQUIPMENT_FILE

neo4j_password=NEO4J_PASSWORD

# 连接Neo4j，默认是host="localhost"
print('请确认已经安装并打开了neo4j数据库')
time.sleep(3)

if not neo4j_password:
    neo4j_password=input('请输入neo4j数据库密码:')

graph = Graph(password="{}".format(neo4j_password))
graph.delete_all()
chess_node_G(chess_file, graph)
racial_node_relationship_G(racial_file, graph)
profession_node_relationshap_G(profession_file, graph)
equipment_node_relationship_G(equipment_file, graph)
# except:
#     print('连接失败，请确认数据库已打开且密码正确')