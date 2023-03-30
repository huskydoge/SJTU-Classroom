import uvicorn
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from elasticsearch import Elasticsearch

import multiPlot
import wordcount
import heatMap



# !es的索引 index命名时只能是小写字母！
es = Elasticsearch([{'host': "127.0.0.1", 'port': 9200}])
app = FastAPI()

# 请求的api地址进行分类
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 通配符
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 用于搜索返回多个条目，单个条目用sql
@app.get("/classroomInfo/")
async def getClassInfo(classname: str):
    query = {
        "query": {
            "bool": {
                "should": [
                    {"match": {"教室名": classname}}
                ]
            }
        }
    }
    result = es.search(index="classroom", body=query)
    return result["hits"]["hits"]


# 其实不用，直接从数据库检索返回就够了
@app.get("/classroomCharacter/")
async def getClassCharacter(classname: str):
    query = {
        "query": {
            "bool": {
                "should": [
                    {"match": {"教室名": classname}}
                ]
            }
        }
    }
    result = es.search(index="classroomcharacter", body=query)
    return result["hits"]["hits"]


@app.get("/getLostItem/")
async def searchLostItem(context: str):
    query = {
        "query": {
            "bool": {
                "should": [
                    {"match": {"classroomname": context}},
                    {"match": {"lostitem": context}},
                    {"match": {"username": context}},
                    {"match": {"context": context}}
                ]
            }
        }
    }
    result = es.search(index="lostitem", body=query)
    return result["hits"]["hits"]


@app.get("/getFoundItem")
async def searchLostItem(context: str):
    query = {
        "query": {
            "bool": {
                "should": [
                    {"match": {"classroomname": context}},
                    {"match": {"lostitem": context}},
                    {"match": {"username": context}},
                    {"match": {"context": context}}
                ]
            }
        }
    }
    result = es.search(index="founditem", body=query)
    return result["hits"]["hits"]


@app.get("/getCommentCloud")
async def getCommentCloud():
    return wordcount.getCommentCloud()


@app.get("/getCommentCloudByCLassroom")
async def getCommentCloudByClassroom(classroom):
    return wordcount.getCommentCloudByClassRoom(classroom)


@app.get("/getHeatMap")
async def getHeatMap(classname: str, datatype: str):
    return heatMap.getHeatMapData(classname, datatype)

@app.get("/getPlotData")
async def getAverageWeekData(classname: str):
    return multiPlot.getPlotData(classname)

if __name__ == "__main__":
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True)
