#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json

class readjson(object):
	"""读取json文件内容"""
	def __init__(self, json_path):
		super(readjson, self).__init__()
		self.json_path = json_path

	def openjson(self):
		with open(self.json_path) as js:
			diclist = json.load(js)
			return diclist
	def function():
		pass

def openjson(json_path):
	with open(json_path) as js:
		diclist = json.load(js)
		return diclist


j = readjson("/Users/junming/Desktop/emoji_items.json")
print j.openjson()
#print openjson("/Users/junming/Desktop/emoji_items.json")