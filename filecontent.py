#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import json

def countBypath(path):
	files = []
	dirs = os.listdir(path)
	for name in dirs:
		if name == '.DS_Store':continue
		full_path = os.path.join(path,name)
		isDir = os.path.isdir(full_path)
		if isDir:
			countBypath(full_path)
		else:
			print full_path
			exten = full_path.split('.')[-1]
			name = os.path.split(full_path)[1]
			size = os.path.getsize(full_path)
			super_folder_name = full_path.replace(path,'')
			files.append({'name':name,'exten':exten,'size':size,'super_folder_name':super_folder_name}) 
			#print '%s-%s-%s-%s-%s' % (exten,name,size,super_folder_name,full_path)
	return files

def writetojson(data):
    with open('/Users/junming/Desktop/Python/emojis.json','w+') as f:
        f.write(json.dumps(data))

file = countBypath('/Users/junming/Desktop/files')
#print file
#writetojson(file)