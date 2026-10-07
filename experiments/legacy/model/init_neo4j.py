# 导入所需的库
from py2neo import Graph, Node
import pandas as pd


def init_py2neo():
    # 读取Excel文件(rel.xlsx)中的数据，并去除重复项，选择前87787行数据
    t1 = pd.read_excel('rel.xlsx').drop_duplicates().iloc[:106705]
    # 创建一个Graph对象，连接到本地Neo4j数据库，使用用户名和密码进行认证
    import os
    g = Graph(
        os.getenv("NEO4J_URL", "http://127.0.0.1:7474"),
        auth=(os.getenv("NEO4J_USERNAME", "neo4j"), os.getenv("NEO4J_PASSWORD", "")),
        name=os.getenv("NEO4J_DATABASE", "neo4j"),
    )
    # 清空数据库中的所有节点和关系
    g.delete_all()
    # 用于存储已创建的节点名称
    is_create = []

    # 遍历't1'中的'sub_type'和'sub_name'列
    for index, i in t1[['sub_type', 'sub_name']].iterrows():
        # 如果'sub_name'不在'is_create'列表中，表示该节点还未创建过
        if i['sub_name'] not in is_create:
            is_create.append(i['sub_name'])
            # 创建一个Node对象，设置节点标签为'sub_type'，节点属性为'name'
            node = Node(i['sub_type'], name=i['sub_name'])
            # 在图数据库中创建该节点
            g.create(node)

    # 遍历't1'中的'obj_type'和'obj_name'列
    for index, i in t1[['obj_type', 'obj_name']].iterrows():
        # 如果'obj_name'不在'is_create'列表中，表示该节点还未创建过
        if i['obj_name'] not in is_create:
            is_create.append(i['obj_name'])
            # 创建一个Node对象，设置节点标签为'obj_type'，节点属性为'name'
            node = Node(i['obj_type'], name=i['obj_name'])
            # 在图数据库中创建该节点
            g.create(node)

    # 遍历't1'中的每一行数据
    for index, i in t1.iterrows():
        # 构建一个Cypher查询语句，用于创建节点之间的关系
        query = "MATCH (p:%s), (q:%s) WHERE p.name='%s' AND q.name='%s' CREATE (p)-[rel:%s{name:'%s'}]->(q)" % (
            i['sub_type'], i['obj_type'], i['sub_name'], i['obj_name'], i['rel_type'], i['rel_name'])
        print(query)
        try:
            # 执行查询语句，在图数据库中创建关系
            g.run(query)
        except Exception as e:
            print(e)


# 调用初始化函数
init_py2neo()
