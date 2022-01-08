#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" NOTE
@member
_INTERVAL: 開錠してから施錠するまでの秒数
_is_locked: 施錠状態管理フラグ
_last_unlock: 最後に開錠した時間
_servo: サーボモータ操作用ラッパー

@method
__init__(servo_pin): 各種変数の初期化とスレッド処理の開始を行うコンストラクタ
unlock(): 開錠処理
lock(): 施錠処理
__autolock(): スレッド処理として常駐させ、開錠してから一定時間経過後に施錠処理を実行する
"""

from multiprocessing import Value
from threading import Thread
from time import time
from typing import NoReturn

from servo import Servo


class Autolock:
    _INTERVAL = 3

    def __init__(self, servo_pin) -> None:
        self._servo = Servo(servo_pin)

        # スレッドと共有する変数
        self._last_unlock = Value("d", 0.0)  # double型、初期値0.0
        self._is_locked = Value("b", False)  # bool型、初期値False

        # 常時autolockを走らせる
        # NOTE: 閉じっぱなしになるわけではない
        t = Thread(target=self.__autolock)
        t.setDaemon(True)
        t.start()

    def unlock(self) -> None:
        # print("解錠します")
        print("unlock")

        # スレッド
        self._last_unlock.value = time()
        self._is_locked.value = False
        self._servo.open()

    def lock(self) -> None:
        # print("施錠します")
        print("lock")

        self._is_locked.value = True
        self._servo.close()

    def __autolock(self) -> NoReturn:
        while True:
            if self._is_locked.value:
                continue

            if time() - self._last_unlock.value > self.__INTERVAL:
                self.lock()
                self._is_locked.value = True
