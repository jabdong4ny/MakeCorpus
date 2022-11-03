#### -*- coding: utf-8 -*-
from time import time
import multiprocessing
import util
import os
import sys
import multi_processing as mp
import create_corpus as cc

def make_corpus():
    print("=============")
    print(" create corpus !! ")
    print("=============")

    # 현재 폴더 위치
    print(os.getcwd())
    file_path = os.getcwd()

    print("=====file list========") 
    file_list = []
    file_types = ('.doc','docx','ppt',pptx')
    for f in os.listdir(file_path):
        if f.startswith('~$'):
            continue
        if f.endswith(file_types):
            print(f)
            file_list.append(f)

    print("=============")
    print(u"말뭉치 생성 시작...")
    print("~~~~~~")
    start_time = time()

    if len(sys.argv ) != 2:
        # 하나 열어서 검색
        print(u"하나씩 생성!")
        for fa in file_list:
            cc.create_corpus(fa)

    elif('m' == sys.argv[1]):
        # 멀티로 검색
        print(u"멀티로 생성!")
        mp.multi_make(file_list)
    else:
        print(u"관리자에게 문의 바랍니다.")
        sys.exit()

    print("~~~~~~~")
    end_time = time()
    print(u"말뭉치 생성 소요시간 : ",end_time - start_time)
    print("======== end!!!")

    # 말뭉치 파일 경로 업데이트 체크
    cc.make_curpus_file_path(file_path + '\\' + util.get_curpus_dir_name())
    return True

if __name__ == "__main__":
    multiprocessing.freeze_support() # for multiprocessing other process on windows
    print("=============")
    print(u" make_corpus v0.9 ")
    print("=============")
    sys.stdout = open('output.log', 'w')
    make_corpus()