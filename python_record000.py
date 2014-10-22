########宣告utf8↓↓↓擇一#############
# coding=UTF-8
# -*- coding:utf-8
#coding: utf-8 -*-
########################################
########輸入輸出##################
a=(raw_input("想說的話"))  #輸入字串
a=(input("想說的話"))	#輸入整數,算式會被計算。
print a,"*",b,"=",'%2 d'%(a*b),";",  #用 , 結尾，才不會被自動換行
########################################
########讀寫檔案##################
filename = raw_input('檔名：')
f = open(filename, 'r')
b_str = f.read()
f.close()

import os
x = os.getcwd()  #取得這個檔案的目錄
########################################
########變數、算式##################
a =['cat', 'windows', 'defenestdfsd']  #一個變數存好幾個字串 
9**2	#9的平方，**代表次方
a = "a"
b = a + "b" # 字串連接， b 會等於 "ab"
c = a*4   # 字串重複， c 會等於 "aa"
########################################
########判斷##################
if a > 9:	print "大於9"
elif a == 8: 	print "等於8"  #elif!!!!
else : print "7以下"
########################################
#########Object,class###############################
class Demo:
	def __init__(self,a,b): #python2的一開始要用__init__
		self.a =a
		self.b =b
#######################################

############MYSQL###########################
# 打开数据库连接
db = MySQLdb.connect("localhost","root","123","testdb" )
##############################################################################
#######################################
list.append(obj);   #添加新對象  
str.join(sequence)  #連接新字串
locals()
Update and return a dictionary representing the current local symbol table.
# Free variables are returned by locals() when it is called in function blocks, but not in class blocks.

#######################################