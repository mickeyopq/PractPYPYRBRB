# -*- coding:utf-8
# import os;

while a <= 9:
	b = 1
	while b <= 9:
		print a,"*",b,"=",'%2d'%(a*b),";",  #用 , 結尾，才不會被自動換行
		b+=1
	print ""    #為了換行
	if a%3 == 0:
		print ""	#為了換行
	a+=1	