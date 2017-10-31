import os
import glob
dirlist = os.listdir()
os.mkdir("./result")
for i in [m for m in dirlist if m.startswith('MOT')]:
    imgs = glob.glob(i + '/img1/*.jpg')
    print(imgs)
    for img in imgs:
        os.rename(img, './result/' +i + os.path.basename(img))
