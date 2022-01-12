#!/usr/bin/python3
# -*- coding: utf-8 -*-

# NOTE: 参考資料
# 似たこと: https://qiita.com/depretiger/items/eb5c84faa59ee5743962
# 似たこと: https://qiita.com/irutack/items/61a783eb9d5c78d5a3f6
# gpiozero: https://gpiozero.readthedocs.io/en/stable/recipes.html#motion-sensor
# nfcpy: https://nfcpy.readthedocs.io/en/latest/index.html
# pythonでプロセス間の値の共有: https://qiita.com/t_okkan/items/4127a87177ed2b2db148
# 経過時間測定: https://note.nkmk.me/python-datetime-timedelta-measure-time/

""" NOTE: chart
@main
init
    prepare instances
    read saved idm list
if detect motion or read idm
    unlock door

@Autolock
if 15 seconds have passed since the last unlocking
    lock door
"""


import sys

from gpiozero import MotionSensor

# 自作モジュール読み込み
sys.path.insert(1, "/home/pi/nfcpy")
from autolock import Autolock
from card_reader import CardReader


def main():
    # gpio pins
    SERVO_PIN = 4
    PIR_PIN = 18

    # instance
    reader = CardReader()
    door = Autolock(SERVO_PIN)
    pir = MotionSensor(PIR_PIN)

    # 動体検知したら呼び出す関数
    def detected():
        print("detect motion")
        door.unlock()

    # 動体検知したら detected を呼び出す
    # NOTE: detected() ではなく detected
    pir.when_motion = detected

    # ファイルからidmを読み込み
    # TODO: .txt -> .json
    path = "/home/pi/Documents/new_autolock/member_ID.txt"

    
    with open(path) as f:
        # NOTE: 行ごとに読み込む、改行を取り除く、リストにする
        idms = [l.strip() for l in f.readlines()]

    while True:
        # IDm取得
        idm = reader.read_idm()
        idm = idm.upper()
        print(idm)

        # IDmが未知
        if idm not in idms:
            # print("未登録")
            print("unauthenticated")
            continue

        # 開錠
        # NOTE: 施錠は自動
        # print("認証")
        print("authenticated")
        door.unlock()


if __name__ == "__main__":
    main()
