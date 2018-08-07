import pymongo

client = pymongo.MongoClient(host='localhost',port=27017)
db = client.test
collection = db.students
#插入一条数据
# student = {
    # 'id' : '20170101',
    # 'name': 'whyz',
    # 'age' : 20,
    # 'gender':'male'
# }
# result = collection.insert(student)
# print(result)
#插入多条数据
# student1 = {
    # 'id' : '20170101',
    # 'name': 'jond',
    # 'age' : 21,
    # 'gender':'male'
# }
# student2 = {
    # 'id' : '2133444',
    # 'name': 'mike',
    # 'age': 22,
    # 'gender':'female'
# }
# result2 = collection.insert([student1,student2])
# print(result2)
#查询一条数据
# result = collection.find_one({'name':'whyz'})
# print(type(result))
# print(result)
#查询多条数据
# res = collection.find({'name':'whyz'})
# print(type(res))
# for r in res:
#     print(r)
#高级查询
# res = collection.find({'age':{'$gt':20}})
# for r in res :
    # print(r)

