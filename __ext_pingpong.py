#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------
# COPYRIGHT (C) 2014-2021 Mitsuo KONDOU.
# This software is released under the MIT License.
# https://github.com/konsan1101
# Thank you for keeping the rules.
# ------------------------------------------------



import sys
import os
import time
import datetime
import codecs
import glob



# 共通ルーチン
import  _v6__qFunc
qFunc = _v6__qFunc.qFunc_class()



if __name__ == '__main__':

    # パラメータ
    imgPath = '_icons/'
    imgFile = 'detect_face.png'

    if (len(sys.argv) >= 2):
        imgPath = str(sys.argv[1])
        if (imgPath[:-1] != '/'):
            imgPath += '/'
    if (len(sys.argv) >= 3):
        imgFile  = str(sys.argv[2])

    # 音声再生
    qFunc.guideSound(filename='_pingpong', sync=True)

    # メッセージ
    time.sleep(0.50)



