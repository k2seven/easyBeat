# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 13:57:01 2021

@author: liuxuemin
"""

import os
import shutil
from pydub import AudioSegment
import librosa
import re

if not os.path.isdir("Res") or not os.path.exists("Res") :
    print("缺少资源文件")
    exit()
if not os.path.exists("OutPut"):
    os.mkdir("OutPut")
if not os.path.exists("TempRes"):
    os.mkdir("TempRes")
    
filenameList = os.listdir("Res")
for filename in filenameList:
    filepath = "Res\\"+filename
    temppath = re.sub(r"\..*",".ogg", "TempRes\\"+filename)
    if os.path.exists(filepath):  
        print(filepath)
        if os.path.exists(temppath):
            os.remove(temppath)
        #转换格式
        print(re.search(".mp3", filepath))
        if re.search(".mp3", filepath):
            song = AudioSegment.from_mp3(filepath)
            song.export(temppath, format="ogg")
        elif re.search(".ogg", filepath): 
            shutil.copyfile(filepath,temppath)
        else:
            print("仅支持ogg与MP3，请删除其他格式文件重试")
            exit()
            
        outputpath = re.sub(r"\..*",".txt", "OutPut\\"+filename)
        if os.path.exists(outputpath):
            os.remove(outputpath)
    
        #输出beat
        y, sr = librosa.load(temppath , duration=120)
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        array1 = librosa.frames_to_time(beats, sr=sr)
        fp = open(outputpath,"a")
        fp.write(str(array1))
        fp.close()
        