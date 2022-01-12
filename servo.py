#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" NOTE
@member
_PULSE_OPEN: ドアロックを開錠角度にする際にサーボモータにセットする周波数
_PULSE_CLOSE: ドアロックを施錠角度にする際にサーボモータにセットする周波数
_pin: サーボモータ接続ピン番号
_pi: pigpioインスタンス?

@method
__init__(pin): コンストラクタ
__set_pulse(pulse): pulseをサーボモータへの送信周波数に設定
open(): ドアロックを開錠角度にする
close(): ドアロックを施錠角度にする
"""

import pigpio


class Servo:
    _PULSE_OPEN = 776
    _PULSE_CLOSE = 1700

    def __init__(self, pin):
        self._pin = pin
        self._pi = pigpio.pi()

    def __set_pulse(self, pulse):
        self._pi.set_servo_pulsewidth(self._pin, pulse)

    def open(self):
        self.__set_pulse(self._PULSE_OPEN)

    def close(self):
        self.__set_pulse(self._PULSE_CLOSE)
