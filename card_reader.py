#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" NOTE
@member
_idm: カードから読み込んだIDm

@method
__on_connect(tag): カードを読み込んだ際に実行され、IDmを抜き出す
read_idm(): カードからIDmを読み込む
read(): 上2つをまとめたやつ
"""

import binascii
import sys

sys.path.insert(1, "/home/pi/nfcpy")
import nfc


class CardReader:
    def __on_connect(self, tag) -> bool:
        self._idm = binascii.hexlify(tag.idm).decode("utf-8")
        # NOTE: もとはFalse
        return True

    def read_idm(self) -> str:
        # NOTE: options for reader/writer(rd/wr)
        rdwr = {
            "targets": [
                "212F",
                "424F",
            ],
            "on-connect": self.__on_connect,
        }

        with nfc.ContactlessFrontend("usb") as clf:
            clf.connect(rdwr=rdwr)

        return self._idm

    # NOTE: これでいけるかも。要検証
    # def read(self) -> str:
    #     with nfc.ContactlessFrontend("usb") as clf:
    #         tag = clf.connect(rdwr={"targets": ["212F", "424F"]})
    #     return binascii.hexlify(tag.idm).decode("utf-8")
