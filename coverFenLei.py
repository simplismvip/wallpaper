#!/usr/bin/python
# -*- coding:UTF-8 -*-
import sqlite3
import time,random
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def folder_saveDataToSqlite(data):
	sql = sqlite3.connect("/Users/junming/Desktop/wallpaper.sqlite")
	curs = sql.cursor()
	create = "create table if not exists 分类 (id integer primary key autoincrement, name text, fpath text, timetsp text, save integer,share integer,count integer,temp text)"
	curs.execute(create)
	for dic in data:
		datalist = [dic["name"],dic["fpath"],dic["timetsp"],dic["save"],dic["share"],dic["count"],"null"]
		try:
			curs.execute("insert into 分类 (name,fpath,timetsp,save,share,count,temp) values (?,?,?,?,?,?,?)", datalist)
			sql.commit()
		except Exception as e:
			print '插入数据错误:%s' % e
	sql.close()

def folder_queryData():
	sql = sqlite3.connect("/Users/junming/Desktop/Source/wallpappers/qiniuyunPic.sqlite")
	curs = sql.cursor()
	curs.execute('select * from 分类')
	datas = []
	for row in curs.fetchall():
		name = row[1]
		fpath = os.path.join("分类",name)
		share = random.randint(100,1000)
		save = random.randint(100,1000)
		count = row[3]
		timetsp = str(int(time.time())+random.randint(0,1000))
		data = {"name":name,"fpath":fpath,"share":share,"save":save,"timetsp":timetsp,"count":count}
		datas.append(data)
		# print data
	return datas
		

def fiels_saveDataToSqlite(data):
	sql = sqlite3.connect("/Users/junming/Desktop/wallpaper.sqlite")
	curs = sql.cursor()
	create = "create table if not exists 分类_data (id integer primary key autoincrement, name text, fpath text, type text, author text, timetsp text, download integer,size integer,save integer,share integer,temp text)"
	curs.execute(create)
	for dic in data:
		datalist = [dic["name"],dic["fpath"],dic["type"],dic["author"],dic["timetsp"],dic["download"],dic["size"],dic["save"],dic["share"],"null"]
		try:
			curs.execute("insert into 分类_data (name, fpath, type, author, timetsp, download, size, save, share, temp) values (?,?,?,?,?,?,?,?,?,?)", datalist)
			sql.commit()
		except Exception as e:
			print '插入数据错误:%s' % e
	sql.close()

def fiels_queryData():
	sql = sqlite3.connect("/Users/junming/Desktop/Source/wallpappers/qiniuyunPic.sqlite")
	curs = sql.cursor()
	curs.execute('select * from 分类_data')
	datas = []
	for row in curs.fetchall():
		name = row[2]
		type_id = row[1]
		fpath = "分类"+"/"+name
		share = random.randint(100,1000)
		save = random.randint(100,1000)
		size = 120
		download = random.randint(100,1000)
		timetsp = str(int(time.time())+random.randint(0,1000))
		data = {"name":name,"fpath":fpath,"type":type_id,"timetsp":timetsp,"author":"tony","share":share,"save":save,"size":size,"download":download}
		datas.append(data)
		# print name,fpath
	return datas
if __name__ == "__main__":
	# 生成分类外层文件数据树
	datas = folder_queryData()	
	folder_saveDataToSqlite(datas)

	# 生成分类内层文件数据树
	# datas = fiels_queryData()	
	# fiels_saveDataToSqlite(datas)








