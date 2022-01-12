import binascii
import sys
sys.path.insert(1,'home/pi/nfcpy')
import nfc

def connected(tag):tag;return False
clf = nfc.ContactlessFrontend('usb')

print ("学籍番号を入力してください。")
x = input()

print ("登録したい任意の鍵（学生証、スマホ）をかざしてください")

readidm = str(clf.connect(rdwr={'targets': ['212F', '424F'],'on-connect': connected}))
readidm = readidm.replace('=',' ')
#print (readidm)
readidm = readidm.split()
#print (readidm)

#IDを見つけだし次の値を見る
for index in range(len(readidm)):
	if readidm[index] == 'ID':
		index += 1
		break
print (readidm[index])

f = open('member_ID.txt','a')
f.write(x+"\n")
f.write(readidm[index]+"\n")
f.close()
print ("書き込み完了")
