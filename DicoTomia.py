#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import time
import re
import random
import os 
import shutil
os.system("title Dicotomia")
os.system("color a")
os.system("cls")
dir = "c:/Windows"
print("-------------------------------------------------")
print("*  Welcome to the wonderful world of Dicotomia  *")
print("-------------------------------------------------")
print("*  Target is to Find my Int between 0 & 1000    *")
print("*         You have only 10 tries...             *")
print("*    ...If you succeed, bsartek the goodie !!!! *")
print("-------------------------------------------------")
Step=0 #initial value
Goal=random.randint(0,1000)
time.sleep(1) 
while Step < 10: 
	Step=Step+1
	Value=input("input your choice ")
	if re.match("^\d+?", Value) is None:
		print("Faggot, a file is being deleted now, don't crash the command...")
		time.sleep(5)
		print("Random file deleted on your computer")
		Step=101
		break
	else:
		Value=float(Value)
	if Value>Goal:
		print("TOO BIG")
	if Value<Goal:
		print("too small")
	if Value==Goal:
		print("Clap CLap Clap")
		break
if Step<11:
	print("you broke the system in ", Step, "tries")
	files = [file for file in os.listdir(dir)if os.path.isfile(os.path.join(dir, file))]
	file = random.choice(files)
	shutil.copy(os.path.join(dir, file),'c:/env')
	print("and you won a file from somewhere!")
else:
	if Step<12:
		print("too many tries, sorry!")
	print("********* GAME OVER *********")

    
	
