import os
import pathlib
import datetime

DEST_DIR = "./img_dst/"
SRC_DIR = "./img_src/"

def save_directory(idx):
    dt = datetime.datetime.fromtimestamp(idx.stat().st_birthtime) 
    return dt.strftime('%Y-%m-%d')
    
def count_files(dir):
    return len([1 for x in list(os.scandir(dir)) if x.is_file()])

def make_dir() :
    p = pathlib.Path(SRC_DIR)
    p = p.iterdir()

    for idx in p :
        #ファイル作成日
        day_string = save_directory(idx)
        #出力ディレクトリ
        dest_path = DEST_DIR + day_string
   
        if os.path.exists(dest_path) :
            print("already exists")
        else :
            #ディレクトリ作成
            make_dir = "mkdir " + dest_path
            os.system(make_dir)

def copy_img(ext) :
    copy_count = 0
    file_count = count_files(SRC_DIR)
    p = pathlib.Path(SRC_DIR)
    p = p.iterdir()
    for idx in p :
        #出力ディレクトリ
        day_string = save_directory(idx)
        #ファイル名
        basename = os.path.basename(idx)
        #拡張子
        root_ext_pair = os.path.splitext(idx)
        if ext == root_ext_pair[1] :
            dest_img_path = DEST_DIR + day_string + "/" + basename
            src_img_path = "./" + str(idx)
            copy_img = "cp " + src_img_path + " " + dest_img_path
            #print(copy_img)
            if not os.path.exists(dest_img_path) :
                print(dest_img_path)
                os.system(copy_img)
            else :
                print("already copied")

            copy_count += 1
            print(copy_count, "/", file_count, " files")
        else:
            print("skip file : ", idx)
            copy_count += 1
            print(copy_count, "/", file_count, " files")

if __name__ == '__main__' :
    make_dir()
    copy_img(".jpg")