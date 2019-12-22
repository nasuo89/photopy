import os
import pathlib
import datetime

DEST_DIR = "./img_dst/"

#os.system('ls')

p = pathlib.Path("./img_src/")
p = p.iterdir()

for idx in p :
    dt = datetime.datetime.fromtimestamp(idx.stat().st_birthtime) 
    day_string = dt.strftime('%Y-%m-%d')
    print(day_string)
    dest_path = DEST_DIR + day_string
    
    if os.path.exists(dest_path) :
        print("already exists")
    else :
        make_dir = "mkdir " + dest_path
        os.system(make_dir)   