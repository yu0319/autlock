#!/usr/bin/python3
# -*- coding: utf-8 -*-

import binascii
import sys
sys.path.insert(1,'home/pi/nfcpy')
import nfc
import pigpio
import time
import zinkan_GPIO

def connected(tag):tag;return False

clf = nfc.ContactlessFrontend('usb')

#ファイルからidmをリストに格納
with open('/home/pi/Documents/autolock/member_ID.txt','r') as f:
    idmlist = f.readlines()

#GPIOを使うためのインスタンスを作成
pi = pigpio.pi()

while True:

	#リーダーから読み取り,文字列処理
	readidm = str(clf.connect(rdwr={'targets': ['212F', '424F'],'on-connect': connected}))
	#time.sleep(3)
	readidm = readidm.replace('=',' ')
	print (readidm)
	readidm = readidm.split()
	#print (readidm)

	#IDを見つけだし次の値を見る
	for index in range(len(readidm)):
		if readidm[index] == 'ID':
			index += 1
			break
	#print (readidm[index])
	m = 0
	#idmから一致するか調べる
	for i in idmlist:
		#print ('検査')
		if readidm[index] == i.rstrip('\n'):
			print ('一致')
			print ('解錠します')
			pi.set_servo_pulsewidth(4, 776)

			time.sleep(15)

			print ('施錠します')
			pi.set_servo_pulsewidth(4, 1700)
			#time.sleep(2)
			#pi.set_servo_pulsewidth(4, 0)
			
		else:
			zinkan_GPIO.zinkan()
			
			#time.sleep(15)

			print ('施錠します')
			pi.set_servo_pulsewidth(4, 1700)
			#time.sleep(2)
			#pi.set_servo_pulsewidth(4, 0)

			break

		#elif readidm[index] != i.rstrip('\n'):
			#time.sleep(3)
			#m += 1
			#print (m)

