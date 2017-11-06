import os
import shutil
dirlist = os.listdir()
shosu = 3
if(os.path.exists('./conv/')):
    shutil.rmtree('./conv/')
for i in [m for m in dirlist if m.startswith('MOT')]:
    with open(i + '/seqinfo.ini') as info:
        imWidth = int(info.readlines()[5].rstrip().split('=')[1])
    with open(i + '/seqinfo.ini') as info:
        imHeight = int(info.readlines()[6].rstrip().split('=')[1])
    #with open(i + '/gt/gt.txt','r') as f:
    with open(i + '/det/det.txt','r') as f:
        if not(os.path.exists("./conv/")):
            #os.mkdir(i +"/conv")
            os.makedirs("./conv/")
        for row in f:
            element = row.rstrip().split(',')
            #for element[0] == str(frame):
            filename = '{0:06d}'.format(int(element[0]))
            #nf = open(i + '/conv/'+filename+'.txt','a')
            nf = open('./conv/'+i+filename+'.txt','a')
            x = (int(element[2]) + int(element[4])/2)/imWidth
            y = (int(element[3]) + int(element[5])/2)/imHeight
            #print("x:",x,"y:",y)
            width = int(element[4]) / imWidth
            height = int(element[5]) / imHeight
            nf.write("0"+" "+ str(round(x,shosu)) + " " + str(round(y,shosu)) 
                    + " " + str(round(width,shosu)) + " " + str(round(height,shosu)))
            nf.write('\n')

        nf.close()

print("finish!!")

