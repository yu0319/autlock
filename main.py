#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time

sys.path.insert(1, "/home/pi/nfcpy")

from card_reader import CardReader
from pir_sensor import PirSensor
from servo import Servo


def main():
    # ファイルからidmを読み込み
    # TODO: ファイル書式をjsonに変更
    path = "/home/pi/Documents/autolock/member_ID.txt"
    with open(path) as f:
        idms = [line.strip() for line in f.readlines()]

    reader = CardReader()
    sensor = PirSensor()
    door = Servo()

    while True:
        # idm取得
        idm = reader.read_idm()

        # idmが未知
        if idm not in idms:
            print("未登録")
            continue

        print("一致")

        print("解錠します")
        door.open()

        time.sleep(15)

        print("施錠します")
        door.close()


if __name__ == "__main__":
    main()
