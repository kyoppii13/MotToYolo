import os
import cv2
import sys
import numpy as np

def main():
    args = sys.argv
    #images = os.listdir('../' + args[1])
    for j in [m for m in os.listdir('../') if m.startswith('MOT') and not m.startswith('MOT17-05')]:
        images = os.listdir('../' + j + '/img1/')
        for i in images:
            print(j + i)
            img = cv2.imread('../' + j + '/img1/' + i)
            height,width = img.shape[:2]
            # 貼り付け用ブランクimg
            cols = width
            rows = height + 8
            new_img = np.zeros((rows, cols, 3),np.uint8)
            for x in range(1,width):
                for y in range(1,height):
                    new_img[y, x] = img[y, x]
            
            if not os.path.exists(j + '/img1'):
                os.makedirs(j + '/img1')

            cv2.imwrite(j + '/img1/' + i,new_img)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()

if __name__=='__main__':
    main()
