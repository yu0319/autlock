#!/usr/bin/python3

import time
from datetime import datetime

import RPi.GPIO as GPIO

INTERVAL = 3
SLEEPTIME = 5
GPIO_PIN = 18


class PirSensor:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN, GPIO.IN)
        self._pin = pin

    def __del__(self):
        GPIO.cleanup()

    def detect(self) -> bool:
        return GPIO.input(self._pin) == GPIO.HIGH


def PirSensor():
    try:

        print("処理キャンセル：CTRL+C")
        cnt = 1

        while True:
            # センサー感知
            if GPIO.input(GPIO_PIN) == GPIO.HIGH:
                print(
                    datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                    + "："
                    + str("{0:05d}".format(cnt))
                    + "回目の人感知"
                )
                cnt = cnt + 1
                time.sleep(SLEEPTIME)
                break
            else:
                print("感知中")
                time.sleep(INTERVAL)
                break
    except KeyboardInterrupt:
        print("終了処理中...")
    finally:
        GPIO.cleanup()
        # pi.stop()
        print("pigpio clean完了")


class zinkan:
    cnt = 0

    def __setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN, GPIO.IN)

    def is_detect(self):
        if GPIO.input(GPIO_PIN) == GPIO.HIGH:
            now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            print(f"{now}:{self.cnt:05d}回目の人感知")
            self.cnt += 1
        else:
            print("感知中")
        time.sleep(INTERVAL)
