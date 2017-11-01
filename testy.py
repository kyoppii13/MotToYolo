# Convert to TensorBox from MOT
"""
[
  {
    "image_path": "images/1/abc.jpg",
    "rects":
      [
        {"x1": 0, "y1": 0, "x2": 100, "y2": 100},
        {"x1": 200, "y1": 150, "x2": 220, "y2": 300}
      ]
  },
  {
    "image_path": "images/2/klm.jpg",
    "rects":
      [
        {"x1": 200, "y1": 0, "x2": 300, "y2": 100}
      ]
  },
]
"""
import os
import shutil
import json
import collections as cl
import re
import sys

def main():
    
    args = sys.argv
    dirlist = os.listdir()
    ys = cl.OrderedDict()
    #for i in [m for m in dirlist if m.startswith('MOT')]:
    #for fileDir in ["MOT17-02-FRCNN"]:
    fileDir = args[1]
    with open(fileDir + '/seqinfo.ini') as info:
        seqLen = int(info.readlines()[4].rstrip().split('=')[1])
        print("seqLength:{}".format(seqLen))
        #rects = [0 for j in range(seqLen)]
        f = open(fileDir + '/gt/gt.txt')
        lines = f.readlines()
        f.close()

        for i in range(1, seqLen+1):
            rects = []
            #print(i)
            #for row in f: 
            for line in lines:
                element = line.rstrip().split(',')
                #element = ror.rstrip().split(',')
                if element[0] == str(i):
                # fname.append(string(filename))
                    x1 = (int(element[2]))
                    y1 = (int(element[3]))
                    x2 = int(element[2]) + int(element[4])
                    y2 = int(element[3]) + int(element[5])
                    rect = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
                    rects.append(rect)
    
            filename = '{0:06d}'.format(i) + '.jpg'
            print(filename)
            data = cl.OrderedDict()
            data["image_path"] = '~/ml/MOT17/train/'+fileDir+'/'+filename
            #print(rects)
            data["rect"] = rects
            ys[i] = data
        f.close()
    fw = open(fileDir+'.json','w')
    json.dump(ys,fw,indent=4)
    fw.close()
    fw = open(fileDir+'.json')
    fo = open(fileDir+'_fin.json','w')

    for conv_line in fw:
        conv_line = re.sub(r'"[0-9]+": ',"",conv_line)
        fo.write(conv_line)
    fw.close()
    fo.close()
    

    print("finish!!")

if __name__=='__main__':
    main()
