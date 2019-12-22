import os
import pathlib
import datetime

DEST_DIR = "./img_dst/"

#os.system('ls')

p = pathlib.Path("./img_src/test.jpg")

dt = datetime.datetime.fromtimestamp(p.stat().st_ctime) 
day_string = dt.strftime('%Y-%m-%d')

dest_path = DEST_DIR + day_string

if os.path.exists(dest_path) :
    print("already exists")
else :
    make_dir = "mkdir " + dest_path
    os.system(make_dir)   