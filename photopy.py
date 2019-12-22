import os
import pathlib
import datetime

DEST_DIR = "./img_dst/"
SRC_DIR = "./img_src/"

def make_dir() :
    p = pathlib.Path(SRC_DIR)
    p = p.iterdir()

    for idx in p :
        dt = datetime.datetime.fromtimestamp(idx.stat().st_birthtime) 
        day_string = dt.strftime('%Y-%m-%d')
        dest_path = DEST_DIR + day_string
   
        if os.path.exists(dest_path) :
            print("already exists")
        else :
            make_dir = "mkdir " + dest_path
            os.system(make_dir)

def copy_img(ext) :
    p = pathlib.Path(SRC_DIR)
    p = p.iterdir()
    for idx in p :
        dt = datetime.datetime.fromtimestamp(idx.stat().st_birthtime) 
        day_string = dt.strftime('%Y-%m-%d')
        basename = os.path.basename(idx)
        root_ext_pair = os.path.splitext(idx)
        if ext == root_ext_pair[1] :
            dest_img_path = DEST_DIR + day_string + "/" + basename
            src_img_path = "./" + str(idx)
            copy_img = "cp " + src_img_path + " " + dest_img_path
            #print(copy_img)
            os.system(copy_img)
    

if __name__ == '__main__' :
    make_dir()
    copy_img(".jpg")