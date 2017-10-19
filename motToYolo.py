import os
dirlist = os.listdir()
imHeight = 1080
imWidth = 1920
shosu = 3
#filenumber = 1
#filename = '{0:06d}'.format(filenumber)
#nf = open(filename+'.txt','w')
for i in [m for m in dirlist if m.startswith('MOT')]:
    with open(i + '/gt/gt.txt','r') as f:
        if not(os.path.exists(i+"/conv")):
            os.mkdir(i +"/conv")
        for row in f:
            element = row.rstrip().split(',')
            #for element[0] == str(frame):
            filename = '{0:06d}'.format(int(element[0]))
            nf = open(i + '/conv/'+filename+'.txt','a')
            x = (int(element[2]) + int(element[4])/2)/imWidth
            y = (int(element[3]) + int(element[5])/2)/imHeight
            #print("x:",x,"y:",y)
            width = int(element[4]) / imWidth
            height = int(element[5]) / imHeight
            #s = ','.join(element)
            nf.write("0"+","+ str(round(x,shosu)) + "," + str(round(y,shosu)) 
                    + "," + str(round(width,shosu)) + "," + str(round(height,shosu)))
            nf.write('\n')

        nf.close()

print("finish!!")

