#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import json
import sqlite3
import folderTree

class imageFiles(object):
	def __init__(self,path):
		super(imageFiles, self).__init__()
		self.conne = sqlite3.connect(path)
		self.conne.text_factory = str
	# 插入专题item数据（获取item数据）
	def folder_sqlite(self,datas):
		for data in datas:
			name = data["name"]
			create = "create table if not exists %s (id integer primary key autoincrement, name text, fpath text, timetsp text, save integer,share integer,count integer,temp text)" % name
			curs = self.conne.cursor()
			curs.execute(create)
			folders = data["folders"]
			for dic in folders:
				datalist = [dic["name"],dic["fpath"],dic["timetsp"],dic["save"],dic["share"],dic["count"],"null"]
				try:
					insert = "insert into %s (name,fpath,timetsp,save,share,count,temp) values (?,?,?,?,?,?,?)" % name
					curs.execute(insert, datalist)
					self.conne.commit()
				except Exception as e:
					print '插入数据错误:%s' % e
		# step 4:close
		self.conne.close()
	# 插入专题item的详细数据（获取item详细）
	def files_sqlite(self,datas):
		for data in datas:
			name = data["name"]+"_data"
			create = "create table if not exists %s (id integer primary key autoincrement, name text, fpath text, type text, author text, timetsp text, download integer,size integer,save integer,share integer,temp text)" % name
			curs = self.conne.cursor()
			curs.execute(create)
			folders = data["folders"]
			for dic in folders:
				datalist = [dic["name"],dic["fpath"],dic["type"],dic["author"],dic["timetsp"],dic["download"],dic["size"],dic["save"],dic["share"],"null"]
				try:
					insert = "insert into %s (name, fpath, type, author, timetsp, download, size, save, share, temp) values (?,?,?,?,?,?,?,?,?,?)" % name
					curs.execute(insert, datalist)
					self.conne.commit()
				except Exception as e:
					print '插入数据错误:%s' % e
		# step 4:close
		self.conne.close()
	# 插入专题数据（获取item数据）
	def total_sqlite(self,datas):
		create = "create table if not exists wallpaper (id integer primary key autoincrement, name text, type_id text, timetsp text, cover_url integer,save integer,share integer,temp text)"
		curs = self.conne.cursor()
		curs.execute(create)
		for dic in datas:
			datalist = [dic["name"],dic["type_id"],dic["timetsp"],dic["cover_url"],dic["save"],dic["share"],""]
			try:
				insert = "insert into wallpaper (name, type_id, timetsp, cover_url, save, share, temp) values (?,?,?,?,?,?,?)"
				curs.execute(insert, datalist)
				self.conne.commit()
			except Exception as e:
				print '插入数据错误:%s' % e
				
		# step 4:close
		self.conne.close()

if __name__ == '__main__':
	ima = imageFiles("/Users/junming/Desktop/wallpaper.sqlite")
	# ima.readfiles("/Users/junming/Desktop/Source/upload/drew")
	# ima.writetojson("/Users/junming/Desktop/django.json")
	
	# 第三层文件树
	# files_datas = folderTree.files_tree('/Users/junming/Desktop/Source/Downloads/wallpaper')
	# ima.files_sqlite(files_datas)

	# 第二层文件树
	folder_datas = folderTree.folder_tree('/Users/junming/Desktop/Source/Downloads/wallpaper')
	ima.folder_sqlite(folder_datas)
	
	# 第一层文件树
	# total_datas = folderTree.folders('/Users/junming/Desktop/Source/Downloads/wallpaper')
	# ima.total_sqlite(total_datas)

































