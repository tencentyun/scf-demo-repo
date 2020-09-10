# -*- coding: utf8 -*-
from datetime import datetime
from elasticsearch import Elasticsearch
import curator

esServer = "10.16.16.137:9200"  # 修改爲 es server 網址+端口
esPrefix = "cron-"              # 查找的 index 索引前綴
esCuratorTimeStr = "%Y%m%d%H"   # 索引中的時間格式
esCuratorTimeUnit = "hours"     # 過濾清理的時間單位,days,months
esCuratorTimeCount = 8          # 時間間隔

# 如上範例可以清理 索引格式類似爲 index-2018101113 ，當前時間的8個小時前的索引

ESServer = Elasticsearch(esServer)

def clean_index():
    ilo = curator.IndexList(ESServer)
    ilo.filter_by_regex(kind='prefix', value=esPrefix)
    ilo.filter_by_age(source='name', direction='older', timestring=esCuratorTimeStr, unit=esCuratorTimeUnit, unit_count=esCuratorTimeCount)
    try:
        ilo.empty_list_check()
    except Exception,e:
        print(e)
        print("list is empty")
        return
    delete_indices = curator.DeleteIndices(ilo)
    print(delete_indices.do_action())

def main_handler(event,context):
    clean_index()