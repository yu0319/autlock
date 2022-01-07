#!/usr/bin/python3
# -*- coding: utf-8 -*-

import binascii
import sys

sys.path.insert(1, "/home/pi/nfcpy")

import nfc


class CardReader:
    def __on_connect(self, tag) -> bool:
        self._idm = binascii.hexlify(tag.idm).decode("utf-8")
        return True

    def read_idm(self) -> str:
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
