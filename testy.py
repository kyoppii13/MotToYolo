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
    train_ys = cl.OrderedDict()
    test_ys  = cl.OrderedDict()
    #for i in [m for m in dirlist if m.startswith('MOT')]:
    fileDir = args[1]
    percentage_test = 30 # testデータの割合
    with open(fileDir + '/seqinfo.ini') as info:
        seqLen = int(info.readlines()[4].rstrip().split('=')[1])
        print("seqLength:{}".format(seqLen))
        #rects = [0 for j in range(seqLen)]
        f = open(fileDir + '/det/det.txt')
        lines = f.readlines()
        f.close()
        counter = 1
        index_test = round(100 / percentage_test) 

        for i in range(1, seqLen+1):
            rects = []
            #print(i)
            #for row in f: 
            for line in lines:
                element = line.rstrip().split(',')
                #element = ror.rstrip().split(',')
                if element[0] == str(i):
                # fname.append(string(filename))
                    rect = cl.OrderedDict()
                    rect["x1"] = int(float(element[2]))
                    rect["x2"] = int(float(element[2]) + float(element[4]))
                    rect["y1"] = int(float(element[3]))
                    rect["y2"] = int(float(element[3]) + float(element[5]))
                    #rect["x1"] = '{0:.1f}'.format(float(element[2]))
                    #rect["x2"] = '{0:.1f}'.format(float(element[2]) + float(element[4]))
                    #rect["y1"] = '{0:.1f}'.format(float(element[3]))
                    #rect["y2"] = '{0:.1f}'.format(float(element[3]) + float(element[5]))
                    #x1 = int(float(element[2]))
                    #y1 = int(float(element[3]))
                    #x2 = int(float(element[2])) + int(float(element[4]))
                    #y2 = int(float(element[3])) + int(float(element[5]))
                    #rect = cl.OrderedDict({"x1": x1, "y1": y1, "x2": x2, "y2": y2})
                    rects.append(rect)
    
            filename = '{0:06d}'.format(i) + '.jpg'
            print(filename)
            train_data = cl.OrderedDict()
            test_data = cl.OrderedDict()
            if counter == index_test:
                counter = 1
                test_data["image_path"] = 'test/'+fileDir+'/img1/'+filename
                test_data["rects"] = rects
            else:
                train_data["image_path"] = 'test/'+fileDir+'/img1/'+filename
                train_data["rects"] = rects
                counter = counter + 1
            train_ys[i] = train_data
            test_ys[i] = test_data
        f.close()
    fw = open(fileDir+'_train.json','w')
    json.dump(train_ys,fw,indent=2)
    fw.close()
    fw = open(fileDir+'_test.json','w')
    json.dump(test_ys,fw,indent=2)
    fw.close()
    num_lines_train = len(open(fileDir + '_train.json').readlines())
    num_lines_test = len(open(fileDir + '_test.json').readlines())
    fw_train = open(fileDir+'_train.json')
    fo_train = open('train/' + fileDir+'_train_fin.json','w')
    line_counter = 0
    for line in fw_train:
        line_counter += 1
        if line_counter == 1 or line_counter == num_lines_train:
            continue
        line = re.sub(r'"[0-9]+": ',"",line)
        line = re.sub(r'{}.?',"",line)
        line = re.sub(r'\s+\n',"",line)
        fo_train.write(line)
    fw_train.close()
    fo_train.close()

    fw_test = open(fileDir+'_test.json')
    fo_test = open('test/' + fileDir+'_test_fin.json','w')
    line_counter = 0
    for line in fw_test:
        line_counter += 1
        if line_counter == 1 or line_counter == num_lines_test:
            continue
        line = re.sub(r'"[0-9]+": ',"",line)
        line = re.sub(r'{}.?',"",line)
        line = re.sub(r'\s+\n',"",line)
        fo_test.write(line)
    fw_test.close()
    fo_test.close()

    print("finish!!")

if __name__=='__main__':
    main()
