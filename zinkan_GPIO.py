#!/usr/bin/python3

from datetime import datetime
import time
import RPi.GPIO as GPIO
#import pigpio

# インターバル
INTERVAL = 3
# スリープタイム
SLEEPTIME = 5
# 使用するGPIO
GPIO_PIN = 18

#pi=pigpio.pi()
#pi.set_mode(LED_PIN,pigpio.IN)

#RPIモジュールをコメントアウト
#pigpioモジュール用に書き換え中
#ここから

def zinkan():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN, GPIO.IN)

        print ("処理キャンセル：CTRL+C")
        cnt = 1
        while True:
            # センサー感知
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
            #if(pi.write(GPIO_pin.pigpio.HIGH) == pigpio.HIGH):
                print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') +
                "：" + str("{0:05d}".format(cnt)) + "回目の人感知")
                cnt = cnt + 1
                time.sleep(SLEEPTIME)
                break
            else:
                print("感知中")
                time.sleep(INTERVAL)
                break
    except KeyboardInterrupt:
        print("終了処理中...")
        raise KeyboardInterrupt
    finally:
        GPIO.cleanup()
        #pi.stop()
        print("pigpio clean完了")

class zinkan:
    cnt = 0

    def __setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN, GPIO.IN)

    def is_detect():
        if (GPIO.input(GPIO_PIN) == GPIO.HIGH):
            now = datetime.now()strftime('%Y/%m/%d %H:%M:%S')
            print(f"{now}:{cnt:05d}回目の人感知")
            cnt += 1
        else:
            print("感知中")
        time.sleep(INTERVAL)

