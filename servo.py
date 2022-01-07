#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pigpio


class Servo:
    _PULSE_OPEN = 776
    _PULSE_CLOSE = 1700

    _pi = pigpio.pi()

    def __init__(self, pin):
        self._pin = pin

    def open(self):
        self._pi.set_servo_pulsewidth(self._pin, self._PULSE_OPEN)

    def close(self):
        self._pi.set_servo_pulsewidth(self._pin, self._PULSE_CLOSE)
