#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------
# COPYRIGHT (C) 2014-2022 Mitsuo KONDOU.
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

import queue
import threading
import subprocess

import pyautogui
if (os.name == 'nt'):
    import ctypes

import random
#import cv2

#print(os.path.dirname(__file__))
#print(os.path.basename(__file__))
#print(sys.version_info)



# インターフェース
qCtrl_control_player     = 'temp/control_player.txt'
qCtrl_control_self       = qCtrl_control_player



# 共通ルーチン
import  _v6__qRiKi
qRiKi = _v6__qRiKi.qRiKi_class()
import  _v6__qFunc
qFunc = _v6__qFunc.qFunc_class()
import  _v6__qLog
qLog  = _v6__qLog.qLog_class()
#import  _v6__qGuide
#qGuide= _v6__qGuide.qGuide_class()

qPLATFORM        = qRiKi.getValue('qPLATFORM'        )
qRUNATTR         = qRiKi.getValue('qRUNATTR'         )
qHOSTNAME        = qRiKi.getValue('qHOSTNAME'        )
qUSERNAME        = qRiKi.getValue('qUSERNAME'        )
qPath_controls   = qRiKi.getValue('qPath_controls'   )
qPath_pictures   = qRiKi.getValue('qPath_pictures'   )
qPath_videos     = qRiKi.getValue('qPath_videos'     )
qPath_cache      = qRiKi.getValue('qPath_cache'      )
qPath_sounds     = qRiKi.getValue('qPath_sounds'     )
qPath_icons      = qRiKi.getValue('qPath_icons'      )
qPath_fonts      = qRiKi.getValue('qPath_fonts'      )
qPath_log        = qRiKi.getValue('qPath_log'        )
qPath_work       = qRiKi.getValue('qPath_work'       )
qPath_rec        = qRiKi.getValue('qPath_rec'        )
qPath_recept     = qRiKi.getValue('qPath_recept'     )

qPath_s_ctrl     = qRiKi.getValue('qPath_s_ctrl'     )
qPath_s_inp      = qRiKi.getValue('qPath_s_inp'      )
qPath_s_wav      = qRiKi.getValue('qPath_s_wav'      )
qPath_s_jul      = qRiKi.getValue('qPath_s_jul'      )
qPath_s_STT      = qRiKi.getValue('qPath_s_STT'      )
qPath_s_TTS      = qRiKi.getValue('qPath_s_TTS'      )
qPath_s_TRA      = qRiKi.getValue('qPath_s_TRA'      )
qPath_s_play     = qRiKi.getValue('qPath_s_play'     )
qPath_v_ctrl     = qRiKi.getValue('qPath_v_ctrl'     )
qPath_v_inp      = qRiKi.getValue('qPath_v_inp'      )
qPath_v_jpg      = qRiKi.getValue('qPath_v_jpg'      )
qPath_v_detect   = qRiKi.getValue('qPath_v_detect'   )
qPath_v_cv       = qRiKi.getValue('qPath_v_cv'       )
qPath_v_photo    = qRiKi.getValue('qPath_v_photo'    )
qPath_v_msg      = qRiKi.getValue('qPath_v_msg'      )
qPath_v_recept   = qRiKi.getValue('qPath_v_recept'   )
qPath_d_ctrl     = qRiKi.getValue('qPath_d_ctrl'     )
qPath_d_play     = qRiKi.getValue('qPath_d_play'     )
qPath_d_prtscn   = qRiKi.getValue('qPath_d_prtscn'   )
qPath_d_movie    = qRiKi.getValue('qPath_d_movie'    )
qPath_d_upload   = qRiKi.getValue('qPath_d_upload'   )

qBusy_dev_cpu    = qRiKi.getValue('qBusy_dev_cpu'    )
qBusy_dev_com    = qRiKi.getValue('qBusy_dev_com'    )
qBusy_dev_mic    = qRiKi.getValue('qBusy_dev_mic'    )
qBusy_dev_spk    = qRiKi.getValue('qBusy_dev_spk'    )
qBusy_dev_cam    = qRiKi.getValue('qBusy_dev_cam'    )
qBusy_dev_dsp    = qRiKi.getValue('qBusy_dev_dsp'    )
qBusy_dev_scn    = qRiKi.getValue('qBusy_dev_scn'    )
qBusy_s_ctrl     = qRiKi.getValue('qBusy_s_ctrl'     )
qBusy_s_inp      = qRiKi.getValue('qBusy_s_inp'      )
qBusy_s_wav      = qRiKi.getValue('qBusy_s_wav'      )
qBusy_s_STT      = qRiKi.getValue('qBusy_s_STT'      )
qBusy_s_TTS      = qRiKi.getValue('qBusy_s_TTS'      )
qBusy_s_TRA      = qRiKi.getValue('qBusy_s_TRA'      )
qBusy_s_play     = qRiKi.getValue('qBusy_s_play'     )
qBusy_v_ctrl     = qRiKi.getValue('qBusy_v_ctrl'     )
qBusy_v_inp      = qRiKi.getValue('qBusy_v_inp'      )
qBusy_v_QR       = qRiKi.getValue('qBusy_v_QR'       )
qBusy_v_jpg      = qRiKi.getValue('qBusy_v_jpg'      )
qBusy_v_CV       = qRiKi.getValue('qBusy_v_CV'       )
qBusy_v_recept   = qRiKi.getValue('qBusy_v_recept'   )
qBusy_d_ctrl     = qRiKi.getValue('qBusy_d_ctrl'     )
qBusy_d_inp      = qRiKi.getValue('qBusy_d_inp'      )
qBusy_d_QR       = qRiKi.getValue('qBusy_d_QR'       )
qBusy_d_rec      = qRiKi.getValue('qBusy_d_rec'      )
qBusy_d_telework = qRiKi.getValue('qBusy_d_telework' )
qBusy_d_play     = qRiKi.getValue('qBusy_d_play'     )
qBusy_d_browser  = qRiKi.getValue('qBusy_d_browser'  )
qBusy_d_upload   = qRiKi.getValue('qBusy_d_upload'   )
qRdy__s_force    = qRiKi.getValue('qRdy__s_force'    )
qRdy__s_fproc    = qRiKi.getValue('qRdy__s_fproc'    )
qRdy__s_sendkey  = qRiKi.getValue('qRdy__s_sendkey'  )
qRdy__v_mirror   = qRiKi.getValue('qRdy__v_mirror'   )
qRdy__v_reader   = qRiKi.getValue('qRdy__v_reader'   )
qRdy__v_sendkey  = qRiKi.getValue('qRdy__v_sendkey'  )
qRdy__d_reader   = qRiKi.getValue('qRdy__d_reader'   )
qRdy__d_sendkey  = qRiKi.getValue('qRdy__d_sendkey'  )

# フォント
qFONT_default = {'file':qPath_fonts + '_vision_font_ipaexg.ttf','offset':8}



import _v6__qRiKi_key

config_file = '_v6__sub_player_key.json'

qRiKi_key = _v6__qRiKi_key.qRiKi_key_class()
res, dic = qRiKi_key.getCryptJson(config_file=config_file, auto_crypt=False, )
if (res == False):
    dic['_crypt_']            = 'none'
    dic['engine']             = 'ffplay'
    dic['path_winos']         = 'C:/Users/Public/'
    dic['path_macos']         = '/Users/Shared/'
    dic['path_linux']         = '/users/kondou/Documents/'
    dic['play_folder_00']     = '_動画_AppleTV'
    dic['play_folder_01']     = '_m4v__Clip/Perfume'
    dic['play_folder_02']     = '_m4v__Clip/BABYMETAL'
    dic['play_folder_03']     = '_m4v__Clip/OneOkRock'
    dic['play_folder_04']     = '_m4v__Clip/きゃりーぱみゅぱみゅ'
    dic['play_folder_05']     = '_m4v__Clip/etc'
    dic['play_folder_06']     = '_m4v__Clip/SekaiNoOwari'
    dic['play_folder_07']     = '_動画_AppleTV'
    dic['play_folder_08']     = '_m4v__Clip/Perfume'
    dic['play_folder_09']     = '_m4v__Clip/BABYMETAL'
    dic['play_volume']        = 100
    dic['bgm_changeSec']      = 1800
    dic['bgm_folder']         = 'BGM'
    dic['bgm_volume']         = 50
    dic['bgm_stopByMouseSec'] = 300
    dic['bgv_changeSec']      = 0
    dic['bgv_folder']         = '_動画_AppleTV'
    dic['bgv_volume']         = 0
    dic['bgv_stopByMouseSec'] = 300
    dic['dayStart']           = '06:25:00'
    dic['dayEnd']             = '18:05:00'
    dic['lunchStart']         = '12:00:00'
    dic['lunchEnd']           = '13:00:00'
    res = qRiKi_key.putCryptJson(config_file=config_file, put_dic=dic, )



#runMode = 'debug'
runMode = 'bgm'
#runMode = 'bgv'

overPath   = ''
overFolder = ''



def qFFplay(id='qFFplay', file='', vol=100, order='normal', left=100, top=100, width=320, height=240, fps=5, overText='', limitSec=0, stopByMouseSec=0, ):

    #ffplay -i test_input.flv -volume 100 -window_title "test_input.flv" -noborder -autoexit -x 320 -y 240
    #ffplay -i test_input.flv -volume 100 -window_title "test_input.flv" -noborder -autoexit -fs
    #ffplay -f lavfi "amovie=test_sample.mp3,asplit[out0],showspectrum[out1]"
    #ffplay -f lavfi "amovie=test_sample.mp3,asplit[out0],showwaves[out1]"
    #ffplay -f lavfi "amovie=test_sample.mp3,asplit=3[out1][a][b]; [a]showwaves=s=320x100[waves]; [b]showspectrum=s=320x100[spectrum]; [waves][spectrum] vstack[out0]"

    if (stopByMouseSec != 0):
        (x, y) = pyautogui.position()
        last_mouse_x = x
        last_mouse_y = y

    vf = 'fps=' + str(fps)
    if (overText != ''):
        vf += ',drawtext=fontfile=' + qFONT_default['file'] + ':fontsize=256:fontcolor=white:text=' + overText

    if (file[-4:].lower() == '.wav') \
    or (file[-4:].lower() == '.mp3') \
    or (file[-4:].lower() == '.m4a'):
            ffplay = subprocess.Popen(['ffplay', '-i', file, \
                                        '-volume', str(vol), \
                                        '-window_title', str(id), \
                                        '-noborder', '-autoexit', \
                                        '-left', str(left), '-top', str(top), \
                                        '-x', str(width), '-y', str(height), \
                                        '-loglevel', 'warning', \
                        ], )
                        #], stdout=subprocess.PIPE, stderr=subprocess.PIPE, )
    else:
        if (width != 0) or (height != 0):
            ffplay = subprocess.Popen(['ffplay', '-i', file, \
                                        '-vf', vf, \
                                        '-volume', str(vol), \
                                        '-window_title', str(id), \
                                        '-noborder', '-autoexit', \
                                        '-left', str(left), '-top', str(top), \
                                        '-x', str(width), '-y', str(height), \
                                        '-loglevel', 'warning', \
                        ], )
                        #], stdout=subprocess.PIPE, stderr=subprocess.PIPE, )
        else:
            w, h = pyautogui.size()
            ffplay = subprocess.Popen(['ffplay', '-i', file, \
                                        '-vf', vf, \
                                        '-volume', str(vol), \
                                        '-window_title', str(id), \
                                        '-noborder', '-autoexit', \
                                        #'-fs', \
                                        '-left', str(left), '-top', str(top), \
                                        '-x', str(w), '-y', str(h), \
                                        '-loglevel', 'warning', \
                        ], )
                        #], stdout=subprocess.PIPE, stderr=subprocess.PIPE, )

    time.sleep(1.00)

    z_order = 0
    if (order == 'top'):
        z_order = -1

    if (os.name == 'nt'):
        hwnd = 0
        chktime = time.time()
        while (hwnd == 0) and ((time.time() - chktime) < 8):
            hwnd = ctypes.windll.user32.FindWindowW(None, str(id))
            time.sleep(0.10)

        if (hwnd != 0):
            if (width != 0) or (height != 0):
                ctypes.windll.user32.SetWindowPos(hwnd,z_order,int(left),int(top),0,0,1)

    if (file[-4:].lower() == '.wav') \
    or (file[-4:].lower() == '.mp3') \
    or (file[-4:].lower() == '.m4a') \
    or (file[-4:].lower() == '.mp4') \
    or (file[-4:].lower() == '.m4v') \
    or (file[-4:].lower() == '.mov'):
        if (int(limitSec) == 0):
            ffplay.wait()
        else:
            #ffplay.wait(timeout=int(limitSec))
            checkTime = time.time()
            while (ffplay.poll() is None) and ((time.time() - checkTime) <= int(limitSec)):
                if (stopByMouseSec != 0):
                    (x, y) = pyautogui.position()
                    if (abs(last_mouse_x-x) >= 50) or (abs(last_mouse_y-y) >= 50):
                        last_mouse_x = x
                        last_mouse_y = y
                        print('★ Stop Play By Mouse Move. Waiting sec = ' + str(stopByMouseSec) + 's ')
                        break
                    last_mouse_x = x
                    last_mouse_y = y
                time.sleep(0.25)

    else:
            time.sleep(1.00)
            #ffplay.wait()
    ffplay.terminate()
    ffplay = None

    return True



def panelPlay(panel, runMode, path, vol, order, loop, overtext, limitSec, stopByMouseSec, dayStart, dayEnd, lunchStart, lunchEnd, ):

    #print('★panelPlay', path)

    qCtrl_control_player2 = qCtrl_control_player
    qCtrl_control_self2   = qCtrl_control_self
    if (runMode == 'bgv'):
        qCtrl_control_player2 = qCtrl_control_player.replace('.txt', '_bgv.txt')
        qCtrl_control_self2   = qCtrl_control_player2

    if (stopByMouseSec != 0):
        (x, y) = pyautogui.position()
        last_mouse_x = x
        last_mouse_y = y
        last_mouse_time = time.time() - stopByMouseSec

    #black_screen = 'off'
    #black_time   = None

    count = 0
    while (loop > 0):

        # --------------
        # ファイル指定実行
        # --------------
        if (os.path.isfile(path)):
            fn = path
            p  = panel

            if (runMode == 'bgm') or (runMode == 'bgv'):
                fps = 30
            else:
                fps = 15
                if (vol == 0):
                    if (p=='0') or (p=='0-') or (p=='5'):
                        fps = 5
                    else:
                        fps = 2

            if (fn[-4:].lower() == '.wav') \
            or (fn[-4:].lower() == '.mp3') \
            or (fn[-4:].lower() == '.m4a'):
                if (p=='0') or (p=='0-'):
                    p = '5+'

            # play
            left, top, width, height = qFunc.getPanelPos(p,)
            res = qFFplay(p, fn, vol, order, left, top, width, height, fps, overtext, limitSec, stopByMouseSec, )
            count += 1

            txts, txt = qFunc.txtsRead(qCtrl_control_self2)
            if (txts != False):
                if (txt == '_end_') or (txt == '_stop_'):
                    loop = 0

            if (loop < 9):
                loop -= 1

        # --------------
        # フォルダ指定実行
        # --------------
        if (os.path.isdir(path)):
            files = glob.glob(path + '/*.*')
            random.shuffle(files)
            for fn in files:
                p = panel
                if (panel == '1397'):
                    p = panel[(count % 4):(count % 4)+1] + '-'
                if (panel == '19'):
                    p = panel[(count % 2):(count % 2)+1] + '-'
                if (panel == '28'):
                    p = '82'[(count % 2):(count % 2)+1] + '-'
                if (panel == '37'):
                    p = panel[(count % 2):(count % 2)+1] + '-'
                if (panel == '46'):
                    p = '64'[(count % 2):(count % 2)+1] + '-'

                if (runMode == 'bgm') or (runMode == 'bgv'):
                    fps = 30
                else:
                    fps = 15
                    if (vol == 0):
                        if (p=='0') or (p=='0-') or (p=='5'):
                            fps = 5
                        else:
                            fps = 2

                if (fn[-4:].lower() == '.wav') \
                or (fn[-4:].lower() == '.mp3') \
                or (fn[-4:].lower() == '.m4a'):
                    if (p=='0') or (p=='0-'):
                        p = '5+'

                # Wait! Pass!
                nowTime = datetime.datetime.now()
                nowYYMMDD = nowTime.strftime('%Y-%m-%d')
                nowHHMMSS = nowTime.strftime('%H:%M:%S')
                nowHHMM   = nowTime.strftime('%H:%M')
                nowYOUBI  = nowTime.strftime('%a')

                # 開始判断
                playFlag  = True
                limitSec2 = limitSec

                # マウス操作による再生スキップ
                if (playFlag == True):
                    if (stopByMouseSec != 0):
                        if ((time.time() - last_mouse_time) < stopByMouseSec):
                            playFlag  = False
                        (x, y) = pyautogui.position()
                        if (abs(last_mouse_x-x) >= 50) or (abs(last_mouse_y-y) >= 50):
                            last_mouse_time = time.time()
                        last_mouse_x = x
                        last_mouse_y = y

                # 曜日による再生スキップ
                if (playFlag == True):
                    if (dayStart != '00:00:00') \
                    or (dayEnd   != '00:00:00'):
                        if  (nowYOUBI == 'Sat') \
                        or  (nowYOUBI == 'Sun') \
                        or  (nowYOUBI == '土') \
                        or  (nowYOUBI == '日'):
                            playFlag = False
                            #print('★曜日による再生スキップ')

                # 再生時間帯で短縮再生
                if (playFlag == True):
                    if (dayStart != '00:00:00') \
                    or (dayEnd   != '00:00:00'):
                        if (nowHHMMSS < dayStart) \
                        or (nowHHMMSS > dayEnd):
                            playFlag = False
                            #print('★再生時間帯によるスキップ')
                        else:
                            # 終了時間で短縮再生
                            dayEnd2 = dayEnd
                            if (dayEnd2 == '00:00:00'):
                                dayEnd2 = '23:59:59'
                            endTime = datetime.datetime.strptime(nowYYMMDD + ' ' + dayEnd2, '%Y-%m-%d %H:%M:%S')
                            limitSecX = endTime - nowTime
                            if (limitSecX.total_seconds() > 0) and (limitSecX.total_seconds() < limitSec2):
                                limitSec2 = int(limitSecX.total_seconds())
                                print('☆再生時間帯で短縮再生=', limitSec2)

                # ランチ時間で短縮再生
                if (playFlag == True):
                    if (lunchStart != '00:00:00') \
                    or (lunchEnd   != '00:00:00'):
                        if (nowHHMMSS  >= lunchStart) \
                        and (nowHHMMSS <= lunchEnd):
                            playFlag = False
                            #print('★ランチ時間帯によるスキップ')
                        else:
                            # ランチ時間で短縮再生
                            endTime = datetime.datetime.strptime(nowYYMMDD + ' ' + lunchStart, '%Y-%m-%d %H:%M:%S')
                            limitSecX = endTime - nowTime
                            if (limitSecX.total_seconds() > 0) and (limitSecX.total_seconds() < limitSec2):
                                limitSec2 = int(limitSecX.total_seconds())
                                print('☆ランチ時間帯で短縮再生=', limitSec2)

                # Mouse Position
                if (stopByMouseSec != 0):
                    (x, y) = pyautogui.position()
                    last_mouse_x = x
                    last_mouse_y = y

                ## BLACK OFF
                #if (playFlag != True):
                #    if (runMode == 'bgv'):
                #        if (black_screen == 'on'):
                #            if (black_time != None):
                #                if ((time.time() - black_time) > 2):
                #                    try:
                #                        qGuide.close()
                #                        qGuide.terminate()
                #                    except:
                #                        pass
                #                    black_screen = 'off'
                #                    black_time   = None

                # play
                if (playFlag == True):
                    ## BLACK ON
                    #if (runMode == 'bgv'):
                    #    img = cv2.imread(qPath_icons + '__black.png')
                    #    qGuide.init(panel='0+', title='black', image=img,)
                    #    qGuide.open()
                    #    black_screen  = 'on'
                    #    black_time    = None

                    # play
                    left, top, width, height = qFunc.getPanelPos(p,)
                    res = qFFplay(p, fn, vol, order, left, top, width, height, fps, overtext, limitSec2, stopByMouseSec, )
                    count += 1

                    ## BLACK OFF START
                    #if (runMode == 'bgv'):
                    #    #try:
                    #    #    qGuide.close()
                    #    #    qGuide.terminate()
                    #    #except:
                    #    #    pass
                    #    #black_screen = 'off'
                    #    black_time = time.time()

                # Mouse Move ?
                if (stopByMouseSec != 0):
                    (x, y) = pyautogui.position()
                    if (abs(last_mouse_x-x) >= 50) or (abs(last_mouse_y-y) >= 50):
                        last_mouse_time = time.time()
                    last_mouse_x = x
                    last_mouse_y = y

                txts, txt = qFunc.txtsRead(qCtrl_control_self2)
                if (txts != False):
                    if (txt == '_end_') or (txt == '_stop_'):
                        loop = 0

        if (loop < 9):
            loop -= 1



class main_player:

    def __init__(self, name='thread', id='0', runMode='debug', overPath='', overFolder='', ):
        self.runMode   = runMode
        self.overPath  = overPath
        self.overFolder= overFolder

        self.breakFlag = threading.Event()
        self.breakFlag.clear()
        self.name      = name
        self.id        = id
        self.proc_id   = '{0:10s}'.format(name).replace(' ', '_')
        self.proc_id   = self.proc_id[:-2] + '_' + str(id)
        if (runMode == 'debug'):
            self.logDisp = True
        else:
            self.logDisp = False
        qLog.log('info', self.proc_id, 'init', display=self.logDisp, )

        self.proc_s    = None
        self.proc_r    = None
        self.proc_main = None
        self.proc_beat = None
        self.proc_last = None
        self.proc_step = '0'
        self.proc_seq  = 0

        self.play_max  = 10
        self.play_proc = {}
        self.play_id   = {}
        self.play_path = {}
        for i in range(1, self.play_max+1):
            self.play_proc[i] = None
            self.play_id[i]   = None
            self.play_path[i] = None

        # 構成情報
        json_file = '_v6__sub_player_key.json'
        self.engine             = 'ffplay'
        self.path_winos         = 'C:/Users/Public/'
        self.path_macos         = '/Users/Shared/'
        self.path_linux         = '/users/kondou/Documents/'
        self.play_folder        = {}
        self.play_folder['00']  = '_動画_AppleTV'
        self.play_folder['01']  = '_m4v__Clip/Perfume'
        self.play_folder['02']  = '_m4v__Clip/BABYMETAL'
        self.play_folder['03']  = '_m4v__Clip/OneOkRock'
        self.play_folder['04']  = '_m4v__Clip/きゃりーぱみゅぱみゅ'
        self.play_folder['05']  = '_m4v__Clip/etc'
        self.play_folder['06']  = '_m4v__Clip/SekaiNoOwari'
        self.play_folder['07']  = '_m4v__Clip/GB'
        self.play_folder['08']  = '_m4v__Clip/Perfume'
        self.play_folder['09']  = '_m4v__Clip/BABYMETAL'
        self.play_volume        = 100
        self.bgm_changeSec      = 3000
        self.bgm_folder         = 'BGM'
        self.bgm_volume         = 30
        self.bgm_stopByMouseSec = 300
        self.bgv_changeSec      = 0
        self.bgv_folder         = '_動画_AppleTV'
        self.bgv_volume         = 0
        self.bgv_stopByMouseSec = 300
        self.dayStart           = '06:25:00'
        self.dayEnd             = '18:05:00'
        self.lunchStart         = '12:00:00'
        self.lunchEnd           = '13:00:00'
        res, json_dic = qRiKi_key.getCryptJson(config_file=json_file, auto_crypt=False, )
        if (res == True):
            self.engine             = json_dic['engine']
            self.path_winos         = json_dic['path_winos']
            self.path_macos         = json_dic['path_macos']
            self.path_linux         = json_dic['path_linux']
            self.play_folder['00']  = json_dic['play_folder_00']
            self.play_folder['01']  = json_dic['play_folder_01']
            self.play_folder['02']  = json_dic['play_folder_02']
            self.play_folder['03']  = json_dic['play_folder_03']
            self.play_folder['04']  = json_dic['play_folder_04']
            self.play_folder['05']  = json_dic['play_folder_05']
            self.play_folder['06']  = json_dic['play_folder_06']
            self.play_folder['07']  = json_dic['play_folder_07']
            self.play_folder['08']  = json_dic['play_folder_08']
            self.play_folder['09']  = json_dic['play_folder_09']
            self.play_volume        = json_dic['play_volume']
            self.bgm_changeSec      = json_dic['bgm_changeSec']
            self.bgm_folder         = json_dic['bgm_folder']
            self.bgm_volume         = json_dic['bgm_volume']
            self.bgm_stopByMouseSec = json_dic['bgm_stopByMouseSec']
            self.bgv_changeSec      = json_dic['bgv_changeSec']
            self.bgv_folder         = json_dic['bgv_folder']
            self.bgv_volume         = json_dic['bgv_volume']
            self.bgv_stopByMouseSec = json_dic['bgv_stopByMouseSec']
            self.dayStart           = json_dic['dayStart']
            self.dayEnd             = json_dic['dayEnd']
            self.lunchStart         = json_dic['lunchStart']
            self.lunchEnd           = json_dic['lunchEnd']

        if (self.overPath != ''):
            self.path_winos        = self.overPath
            self.path_macos        = self.overPath
            self.path_linux        = self.overPath

        if (self.overFolder != ''):
            self.play_folder['00'] = self.overFolder
            self.play_folder['01'] = self.overFolder
            self.play_folder['02'] = self.overFolder
            self.play_folder['03'] = self.overFolder
            self.play_folder['04'] = self.overFolder
            self.play_folder['05'] = self.overFolder
            self.play_folder['06'] = self.overFolder
            self.play_folder['07'] = self.overFolder
            self.play_folder['08'] = self.overFolder
            self.play_folder['09'] = self.overFolder
            self.bgm_folder        = self.overFolder
            self.bgv_folder        = self.overFolder

        self.path_play = {}
        for id in self.play_folder:
            if (os.name == 'nt'):
                self.path_play[id] = self.path_winos + self.play_folder[id]
            elif (qPLATFORM == 'darwin'):
                self.path_play[id] = self.path_macos + self.play_folder[id]
            else:
                self.path_play[id] = self.path_linux + self.play_folder[id]

        self.path_bgm = ''
        self.path_bgv = ''
        if (os.name == 'nt'):
            self.path_bgm = self.path_winos + self.bgm_folder
            self.path_bgv = self.path_winos + self.bgv_folder
        elif (qPLATFORM == 'darwin'):
            self.path_bgm = self.path_macos + self.bgm_folder
            self.path_bgv = self.path_macos + self.bgv_folder
        else:
            self.path_bgm = self.path_linux + self.bgm_folder
            self.path_bgv = self.path_linux + self.bgv_folder

        self.qCtrl_control_player = qCtrl_control_player
        self.qCtrl_control_self   = qCtrl_control_self
        if (runMode == 'bgv'):
            self.qCtrl_control_player = qCtrl_control_player.replace('.txt', '_bgv.txt')
            self.qCtrl_control_self   = self.qCtrl_control_player
        pyautogui.FAILSAFE = False

    def __del__(self, ):
        qLog.log('info', self.proc_id, 'bye!', display=self.logDisp, )

    def begin(self, ):
        #qLog.log('info', self.proc_id, 'start')

        self.fileRun = qPath_work + self.proc_id + '.run'
        self.fileRdy = qPath_work + self.proc_id + '.rdy'
        self.fileBsy = qPath_work + self.proc_id + '.bsy'
        qFunc.statusSet(self.fileRun, False)
        qFunc.statusSet(self.fileRdy, False)
        qFunc.statusSet(self.fileBsy, False)

        self.proc_s = queue.Queue()
        self.proc_r = queue.Queue()
        self.proc_main = threading.Thread(target=self.main_proc, args=(self.proc_s, self.proc_r, ), daemon=True, )
        self.proc_beat = time.time()
        self.proc_last = time.time()
        self.proc_step = '0'
        self.proc_seq  = 0
        self.proc_main.start()

    def abort(self, waitMax=5, ):
        qLog.log('info', self.proc_id, 'stop', display=self.logDisp, )

        self.breakFlag.set()
        chktime = time.time()
        while (not self.proc_beat is None) and ((time.time() - chktime) < waitMax):
            time.sleep(0.25)
        chktime = time.time()
        while (os.path.exists(self.fileRun)) and ((time.time() - chktime) < waitMax):
            time.sleep(0.25)

    def put(self, data, ):
        self.proc_s.put(data)
        return True

    def checkGet(self, waitMax=5, ):
        chktime = time.time()
        while (self.proc_r.qsize() == 0) and ((time.time() - chktime) < waitMax):
            time.sleep(0.10)
        data = self.get()
        return data

    def get(self, ):
        if (self.proc_r.qsize() == 0):
            return ['', '']
        data = self.proc_r.get()
        self.proc_r.task_done()
        return data

    def main_proc(self, cn_r, cn_s, ):
        # ログ
        qLog.log('info', self.proc_id, 'start', display=self.logDisp, )
        qFunc.statusSet(self.fileRun, True)
        self.proc_beat = time.time()

        # 初期設定
        self.proc_step = '1'

        txts, txt = qFunc.txtsRead(self.qCtrl_control_self)
        if (txts != False):
            if (txt == '_end_'):
                qFunc.remove(self.qCtrl_control_self)

        # 待機ループ
        self.proc_step = '5'

        onece = True
        last_alive = time.time()

        last_menu  = 0

        while (self.proc_step == '5'):
            self.proc_beat = time.time()

            # 終了確認
            control = ''
            txts, txt = qFunc.txtsRead(self.qCtrl_control_self)
            if (txts != False):
                qLog.log('info', self.proc_id, '' + str(txt))
                if (txt == '_end_'):
                    break

                if (txt == '_stop_'):
                    self.sub_proc('_stop_', )
                    time.sleep(2.00)

                qFunc.remove(self.qCtrl_control_self)
                control = txt

            # 停止要求確認
            if (self.breakFlag.is_set()):
                self.breakFlag.clear()
                self.proc_step = '9'
                break

            # 活動メッセージ
            if  ((time.time() - last_alive) > 30):
                qLog.log('debug', self.proc_id, 'alive', display=True, )
                last_alive = time.time()

            # キュー取得
            if (cn_r.qsize() > 0):
                cn_r_get  = cn_r.get()
                inp_name  = cn_r_get[0]
                inp_value = cn_r_get[1]
                cn_r.task_done()
            else:
                inp_name  = ''
                inp_value = ''

            if (cn_r.qsize() > 1) or (cn_s.qsize() > 20):
                qLog.log('warning', self.proc_id, 'queue overflow warning!, ' + str(cn_r.qsize()) + ', ' + str(cn_s.qsize()))

            # レディー設定
            if (qFunc.statusCheck(self.fileRdy) == False):
                qFunc.statusSet(self.fileRdy, True)

            # ステータス応答
            if (inp_name.lower() == '_status_'):
                out_name  = inp_name
                out_value = '_ready_'
                cn_s.put([out_name, out_value])

            # 活動Ｑ検査
            if (os.path.exists(self.fileBsy)):
                self.sub_alive()

            # 選択アナウンス
            if (control.find(u'動画') >=0) and (control.find(u'メニュー') >=0):
                last_menu = time.time()
            if (control.lower() >= '01') and (control.lower() <= '09'):
                last_menu = 0

            if (last_menu != 0):
                if ((time.time() - last_menu) > 120):
                    if (onece == True):
                        onece = False

                        speechs = []
                        speechs.append({ 'text':u'画面表示位置を指定して再生はいかがですか？', 'wait':0, })
                        qRiKi.speech(id='speech', speechs=speechs, lang='', )

            # 処理
            if (control != ''):
                self.sub_proc(control, )

            # アイドリング
            slow = False
            if  (qFunc.statusCheck(qBusy_dev_cpu) == True):
                slow = True
            if  (qFunc.statusCheck(qBusy_dev_mic) == True):
                slow = True

            if (slow == True):
                time.sleep(1.00)
            else:
                if (cn_r.qsize() == 0):
                    time.sleep(0.50)
                else:
                    time.sleep(0.25)

        # 終了処理
        if (True):

            # レディー解除
            qFunc.statusSet(self.fileRdy, False)

            # 停止
            self.sub_proc('_stop_', )

            # ビジー解除
            qFunc.statusSet(self.fileBsy, False)
            if  (self.runMode != 'bgm') \
            and (self.runMode != 'bgv'):
                if (str(self.id) == '0'):
                    qFunc.statusSet(qBusy_d_play, False)

            # キュー削除
            while (cn_r.qsize() > 0):
                cn_r_get = cn_r.get()
                cn_r.task_done()
            while (cn_s.qsize() > 0):
                cn_s_get = cn_s.get()
                cn_s.task_done()

            # ログ
            qLog.log('info', self.proc_id, 'end', display=self.logDisp, )
            qFunc.statusSet(self.fileRun, False)
            self.proc_beat = None



    # 処理
    def sub_proc(self, proc_text, ):
        if (proc_text.find(u'リセット') >=0):
            #self.sub_stop(proc_text, )
            self.sub_stop('_stop_', )

        elif (proc_text.lower() == '_stop_'):
            #self.sub_stop(proc_text, )
            self.sub_stop('_stop_', )

        elif (proc_text.lower() == '_start_'):
            pass

        elif (proc_text.lower() == '_demo0-'):
            #self.sub_stop('_stop_', )
            self.sub_start(proc_text, self.path_play['01'], panel='0' , vol=0  , order='normal', loop=1, limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['01'], panel='0-', vol=int(self.play_volume), order='top'   , loop=1, limitSec=0, stopByMouseSec=0, )

        elif (proc_text.lower() == '_demo1397'):
            #self.sub_stop('_stop_', )
            self.sub_start(proc_text, self.path_play['00'], panel='0'   , vol=0  , order='normal', loop=99, limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['01'], panel='1397', vol=int(self.play_volume), order='top'   , loop=99, limitSec=0, stopByMouseSec=0, )

        elif (proc_text.lower() == '_demo1234'):
            #self.sub_stop('_stop_', )
            self.sub_start(proc_text, self.path_play['05'], panel='0' , vol=int(self.play_volume), order='normal', loop=99, limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['01'], panel='19', vol=0  , order='normal', loop=99, limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['02'], panel='28', vol=0  , order='normal', loop=99, limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['03'], panel='37', vol=0  , order='normal', loop=99, limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['04'], panel='46', vol=0  , order='normal', loop=99, limitSec=0, stopByMouseSec=0, )

        elif (proc_text.lower() == '_bgm_'):
            #self.sub_stop('_stop_', )
            self.sub_start(proc_text, self.path_bgm, panel='9' , vol=int(self.bgm_volume), order='normal', loop=99, limitSec=int(self.bgm_changeSec), stopByMouseSec=self.bgm_stopByMouseSec, )

        elif (proc_text.lower() == '_bgv_'):
            #self.sub_stop('_stop_', )
            self.sub_start(proc_text, self.path_bgv, panel='0' , vol=int(self.bgv_volume), order='normal', loop=99, limitSec=int(self.bgv_changeSec), stopByMouseSec=self.bgv_stopByMouseSec, )

        elif ((proc_text.find(u'動画') >=0) and (proc_text.find(u'メニュー') >=0)) or (proc_text.lower() == '_test_'):
            #self.sub_stop('_stop_', )
            self.sub_start(proc_text, self.path_play['00'], panel='0' , vol=0  , order='normal', loop=99, overtext='', limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['01'], panel='1-', vol=0  , order='normal', loop=99, overtext='01', limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['02'], panel='2-', vol=0  , order='normal', loop=99, overtext='02', limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['03'], panel='3-', vol=0  , order='normal', loop=99, overtext='03', limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['04'], panel='4-', vol=0  , order='normal', loop=99, overtext='04', limitSec=0, stopByMouseSec=0, )
            if (proc_text.find(u'動画') >=0) and (proc_text.find(u'メニュー') >=0):
                self.sub_start(proc_text, self.path_play['05'], panel='5-', vol=0  , order='normal', loop=99, overtext='05', limitSec=0, stopByMouseSec=0, )
            if (proc_text.lower() == '_test_'):
                self.sub_start(proc_text, self.path_play['05'], panel='5-', vol=int(self.play_volume), order='top'   , loop=99, overtext='05', limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['06'], panel='6-', vol=0  , order='normal', loop=99, overtext='06', limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['07'], panel='7-', vol=0  , order='normal', loop=99, overtext='07', limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['08'], panel='8-', vol=0  , order='normal', loop=99, overtext='08', limitSec=0, stopByMouseSec=0, )
            self.sub_start(proc_text, self.path_play['09'], panel='9-', vol=0  , order='normal', loop=99, overtext='09', limitSec=0, stopByMouseSec=0, )

        elif (proc_text.lower() >= '01') and (proc_text.lower() <= '09'):
            #self.sub_stop('_stop_', )
            self.sub_start(proc_text, self.path_play[proc_text], panel='0-', vol=int(self.play_volume), order='top' , loop=99, limitSec=0, stopByMouseSec=0, )

        else:
            proc_path = qFunc.txtFilePath(proc_text)
            if (proc_path != False):
                #self.sub_stop('_stop_', )
                self.sub_start(proc_text, proc_path, panel='0-', vol=int(self.play_volume), order='top', loop=1, limitSec=0, stopByMouseSec=0, )



    # 活動Ｑ検査
    def sub_alive(self, ):
        hit = -1
        for i in range(1, self.play_max+1):
            if (not self.play_proc[i] is None):
                #try:
                    if (not self.play_proc[i].is_alive()):
                        #self.play_proc[i].terminate()
                        del self.play_proc[i]
                        self.play_proc[i] = None
                        self.play_id[i]   = ''
                        self.play_path[i] = ''
                #except Exception as e:
                #        self.play_proc[i] = None
                #        self.play_id[i]   = ''
                #        self.play_path[i] = ''
            if (not self.play_proc[i] is None):
                hit = i
                break
        if (hit == -1):
            # ビジー解除
            qFunc.statusSet(self.fileBsy, False)
            if  (self.runMode != 'bgm') \
            and (self.runMode != 'bgv'):
                if (str(self.id) == '0'):
                    qFunc.statusSet(qBusy_d_play, False)
            return False
        else:
            # ビジー設定
            if (qFunc.statusCheck(self.fileBsy) == False):
                qFunc.statusSet(self.fileBsy, True)
                if  (self.runMode != 'bgm') \
                and (self.runMode != 'bgv'):
                    if (str(self.id) == '0'):
                        qFunc.statusSet(qBusy_d_play, True)
            return True

    # 開始
    def sub_start(self, proc_text, proc_path, panel='0-', vol=100, order='normal', loop=1, overtext='', limitSec=0, stopByMouseSec=0, ):

        # ログ
        qLog.log('info', self.proc_id, 'open ' + proc_path, display=True,)

        # 空きＱ検索
        hit = -1
        for i in range(1, self.play_max+1):
            if (not self.play_proc[i] is None):
                #try:
                    if (not self.play_proc[i].is_alive()):
                        #self.play_proc[i].terminate()
                        del self.play_proc[i]
                        self.play_proc[i] = None
                        self.play_id[i]   = ''
                        self.play_path[i] = ''
                #except Exception as e:
                #        self.play_proc[i] = None
                #        self.play_id[i]   = ''
                #        self.play_path[i] = ''
            if (self.play_proc[i] is None):
                hit = i
                break

        # オープン
        if (hit >= 0):

            # ビジー設定
            if (qFunc.statusCheck(self.fileBsy) == False):
                qFunc.statusSet(self.fileBsy, True)
                if  (self.runMode != 'bgm') \
                and (self.runMode != 'bgv'):
                    if (str(self.id) == '0'):
                        qFunc.statusSet(qBusy_d_play, True)

            i = hit
            self.play_id[i]   = panel
            self.play_path[i] = proc_path
            self.play_proc[i] = threading.Thread(target=panelPlay, args=(
                self.play_id[i], self.runMode, self.play_path[i], vol, order, loop, overtext, limitSec, stopByMouseSec,
                self.dayStart, self.dayEnd, self.lunchStart, self.lunchEnd,
                #), daemon=True, )
                ))
            self.play_proc[i].start()

            time.sleep(2.00)

    # 停止
    def sub_stop(self, proc_text, ):

        # リセット
        #qFunc.kill('ffplay', )
        qFunc.kill(self.engine, )

        # 全Ｑリセット
        for i in range(1, self.play_max+1):
            if (not self.play_proc[i] is None):
                #try:
                    #self.play_proc[i].terminate()
                    del self.play_proc[i]
                    self.play_proc[i] = None
                    self.play_id[i]   = ''
                    self.play_path[i] = ''
                #except Exception as e:
                #    self.play_proc[i] = None
                #    self.play_id[i]   = ''
                #    self.play_path[i] = ''

        # リセット
        #qFunc.kill('ffplay', )
        qFunc.kill(self.engine, )

        # ビジー解除
        self.sub_alive()



# シグナル処理
import signal
def signal_handler(signal_number, stack_frame):
    print(os.path.basename(__file__), 'accept signal =', signal_number)

#signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGINT,  signal.SIG_IGN)
signal.signal(signal.SIGTERM, signal.SIG_IGN)



if __name__ == '__main__':
    main_name = 'player'
    main_id   = '{0:10s}'.format(main_name).replace(' ', '_')

    # 共通クラス
    qRiKi.init()
    qFunc.init()

    # ログ
    nowTime  = datetime.datetime.now()
    filename = qPath_log + nowTime.strftime('%Y%m%d.%H%M%S') + '.' + os.path.basename(__file__) + '.log'
    qLog.init(mode='logger', filename=filename, )

    qLog.log('info', main_id, 'init')
    qLog.log('info', main_id, 'exsample.py runMode, ')

    # 初期設定
    if (len(sys.argv) >= 2):
        runMode    = str(sys.argv[1]).lower()
    qCtrl_control_player2 = qCtrl_control_player
    qCtrl_control_self2   = qCtrl_control_self
    if (runMode == 'bgv'):
        qCtrl_control_player2 = qCtrl_control_player.replace('.txt', '_bgv.txt')
        qCtrl_control_self2   = qCtrl_control_player2

    if (True):

        txts, txt = qFunc.txtsRead(qCtrl_control_self2)
        if (txts != False):
            if (txt == '_end_'):
                qFunc.remove(qCtrl_control_self2)

        qFunc.kill('ffplay')

    # パラメータ

    if (True):

        if (len(sys.argv) >= 2):
            runMode    = str(sys.argv[1]).lower()
        if (len(sys.argv) >= 3):
            overPath   = str(sys.argv[2])
        if (len(sys.argv) >= 4):
            overFolder = str(sys.argv[3])

        qLog.log('info', main_id, 'runMode    = ' + str(runMode   ))
        qLog.log('info', main_id, 'overPath   = ' + str(overPath  ))
        qLog.log('info', main_id, 'overFolder = ' + str(overFolder))

    # 起動

    if (True):

        qLog.log('info', main_id, 'start')

        id = '0'
        if   (runMode == 'bgv'):
            id = '1'

        main_core = main_player(main_name, id, runMode=runMode, overPath=overPath, overFolder=overFolder, )
        main_core.begin()

        main_start = time.time()
        onece      = True

    # 待機ループ

    while (True):

        # 終了確認
        txts, txt = qFunc.txtsRead(qCtrl_control_self2)
        if (txts != False):
            if (txt == '_end_'):
                break

        # デバッグ
        if (runMode == 'debug'):

            # テスト開始
            if  ((time.time() - main_start) > 1):
                if (onece == True):
                    onece = False
                    #t = u'C:/Users/Public/_m4v__Clip/Perfume/Perfume_FLASH.m4v'
                    #t = u'C:/Users/Public/_m4v__Clip/Perfume'
                    #t = u'_demo0-'   # base + center
                    #t = u'_demo1397' # base + 1,3,9,7
                    #t = u'_demo1234' # base + 1234,6789
                    t = u'_test_'      # base + 1-9
                    qLog.log('debug', main_id, t, )
                    qFunc.txtsWrite(qCtrl_control_self2 ,txts=[t], encoding='utf-8', exclusive=True, mode='w', )

            # テスト終了
            if  ((time.time() - main_start) > 120):
                    qLog.log('debug', main_id, '_stop_', )
                    qFunc.txtsWrite(qCtrl_control_self2 ,txts=['_stop_'], encoding='utf-8', exclusive=True, mode='w', )
                    time.sleep(5.00)
                    qLog.log('debug', main_id, '_end_', )
                    qFunc.txtsWrite(qCtrl_control_self2 ,txts=['_end_'], encoding='utf-8', exclusive=True, mode='w', )

        # BGM モード
        if (runMode == 'bgm'):

            # テスト開始
            if  ((time.time() - main_start) > 1):
                if (onece == True):
                    onece = False
                    qFunc.txtsWrite(qCtrl_control_self2 ,txts=['_bgm_'], encoding='utf-8', exclusive=True, mode='w', )

        # BGV モード
        if (runMode == 'bgv'):

            # テスト開始
            if  ((time.time() - main_start) > 1):
                if (onece == True):
                    onece = False
                    qFunc.txtsWrite(qCtrl_control_self2 ,txts=['_bgv_'], encoding='utf-8', exclusive=True, mode='w', )

        # アイドリング
        slow = False
        if   (qFunc.statusCheck(qBusy_dev_cpu) == True):
            slow = True
        elif (qFunc.statusCheck(qBusy_dev_mic) == True):
            slow = True

        if (slow == True):
            time.sleep(1.00)
        else:
            time.sleep(0.50)

    # 終了

    if (True):

        qLog.log('info', main_id, 'terminate')

        main_core.abort()
        del main_core

        qFunc.kill('ffplay', )

        qLog.log('info', main_id, 'bye!')

        sys.exit(0)


