from pptx import Presendtation
import win32com.client
import os
import util

def make_corpus_file_path(corpus_file_path):
    """
    corpus_file_path : 말뭉치가 있는 폴더 경로
    """
    current_path = os.getcwd()
    isNeedUpdate = True
    corpus_path_file = util.get_parent_path_name() + "\\CorpusPath.dat"
    if os.path.isfile(corpus_path_file):
        with open(corpus_path_file, "r", encoding = "utf-8") as f:
            if corpus_file_path in f.read():
                print(u"말뭉치 파일 경로 : 업데이트 필요 없음")
                isNeedUpdate = False
    if isNeedUpdate == True:
        with open(corpus_path_file,"w", encoding='UTF-8') as f:
            f.write(corpus_file_path)
            print(u"말뭉치 파일 경로 : 업데이트 완료 !!")

def create_corpus(file_name):
    """
    file_name : 찾을 파일 이름(path 미 포함)
    """
    current_path = os.getcwd()
    try:
        open_file = current_path + "\\" + file_name
        ppt_app = win32com.client.Dispatch('PowerPoint.Application')
        ppt_file = ppt_app.Presentations.Open(open_file, True)
        result = []
        text = ''

        # 말뭉치 파일 생성 : 현재폴더\corpus_상위폴더명\파일명.dat 이 형태로 저장
        make_dir_name = util.make_corpus_dir()
        save_file_name = current_path + '\\' + make_dir_name + '\\' + file_name + ".dat"
        
        with open(save_file_name, "w", encoding='UTF-8') as f:
            pages = 0
            for slide in ppt_file.slides:
                # page 저장
                pages = pages + 1
                result.append(str(pages) + u"pages ")
                for shape in slide.shapes:
                    if shape.HasTable:
                        col_cnt = shape.Table.Columns.Count
                        row_cnt = shape.Table.Rows.Count
                        for row_idx in range(1, row_cnt + 1):
                            for col_idx in range(1, col_cnt + 1):
                                text = shape.Table.Cell(row_idx, col_idx).Shape.TextFrame.TextRange.Text
                                text = text.replace('\r', ' ')
                                result.append(text)

                    if shape.HasTextFrame:
                        for paragraph in shape.TextFrame.TextRange.Paragraphs():
                            result.append(paragraph.text)
                for word in result:
                    f.write(word) # 파일쓰기
                f.write("\n")
                result.clear()

            if ppt_file:
                ppt_file.close()
            else:
                print("ppt_file null")
        return True
    except:
        print(u"생성 오류!")
    return False