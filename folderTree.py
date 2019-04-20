#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import json
import time,random
from xpinyin import Pinyin

def folders(path):
	folders = []
	for name in os.listdir(path):
		if name == '.DS_Store':continue
		share = random.randint(100,1000)
		save = random.randint(100,1000)
		timetsp = str(int(time.time())+random.randint(0,1000))
		data = {"name":name,"type_id":name,"share":share,"save":save,"timetsp":timetsp,"cover_url":"covers.jpg"}
		folders.append(data)
	return folders

def folder_tree(path):
	files = []
	dirs = os.listdir(path)
	for name in dirs:
		if name == '.DS_Store':continue
		next_path = os.path.join(path,name)
		sublist = []
		# type_id = getPinYin(name)
		if os.path.isdir(next_path):
			next_dirs = os.listdir(next_path)
			for next_name in next_dirs:
				if next_name == '.DS_Store':continue
				count = len(os.listdir(os.path.join(next_path,next_name)))
				fpath = os.path.join(name,next_name)
				share = random.randint(100,1000)
				save = random.randint(100,1000)
				timetsp = str(int(time.time())+random.randint(0,1000))
				data = {"name":next_name,"fpath":fpath,"share":share,"save":save,"timetsp":timetsp,"count":count}
				sublist.append(data)
				# print next_name
		files.append({"name":name,"folders":sublist})
	return files
	# return json.dumps(files)

def files_tree(path):
	files = []
	dirs = os.listdir(path)
	for name in dirs:
		if name == '.DS_Store':continue
		next_path = os.path.join(path,name)
		sublist = []
		if os.path.isdir(next_path):
			next_dirs = os.listdir(next_path)
			for next_name in next_dirs:
				if next_name == '.DS_Store':continue
				for file_name in os.listdir(os.path.join(next_path,next_name)):
					if file_name == '.DS_Store':continue
					fpath = name+"/"+next_name+"/"+file_name
					share = random.randint(100,1000)
					save = random.randint(100,1000)
					# 获取照片大小
					size = os.path.getsize(os.path.join(path,fpath))
					# print "size",str(size)
					download = random.randint(100,1000)
					timetsp = str(int(time.time())+random.randint(0,1000))
					data = {"name":file_name,"fpath":fpath,"type":next_name,"timetsp":timetsp,"author":"tony","share":share,"save":save,"size":size,"download":download}
					sublist.append(data)
				# print next_name
		files.append({"name":name,"folders":sublist})
	return files
	# return json.dumps(files)

def writetojson(data):
    with open('/Users/junming/Desktop/Python/emojis.json','w+') as f:
        f.write(json.dumps(data))

def getPinYin(coder):
	pin = Pinyin()
	test1 = pin.get_pinyin(coder," ")
	print test1
	return test1

if __name__ == "__main__":
	# pass
	# getPinYin(u"估计也要七点多之后了")
	# print files_tree('/Users/junming/Desktop/Source/Downloads/wallpaper')
	print folders('/Users/junming/Desktop/Source/Downloads/wallpaper')
	# folder_tree('/Users/junming/Desktop/Source/Downloads/wallpaper')
	#print file
	#writetojson(file)










