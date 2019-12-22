import os
import pathlib
import datetime

DEST_PATH = "./img_dst/"

#os.system('ls')

p = pathlib.Path("./img_src/test.jpg")

dt = datetime.datetime.fromtimestamp(p.stat().st_ctime) 
day_string = dt.strftime('%Y-%m-%d')

make_dir = "mkdir " + DEST_PATH + day_string
os.system(make_dir)