import cv2
import os
import numpy as np

path0 = 'D:/data/fddb/train.txt'
with open(path0,'r') as f:
    fl = f.readlines()

with open('out.csv','w') as fo:
    i = 0
    for fname in fl:
        i = i + 1
        fs = fname.strip()
        fw = fs.replace('.jpg','.txt').replace('JPEGImages','labels')
        with open(fw,'r') as f:
            s = f.readlines()
        img2 = cv2.imread(fs)
        h, w, c = img2.shape
        q = []
        for l in s:
            l = l.strip()
            v = l.split(' ')
            z = [float(x) for x in v]
            z = z[1:5]
            q.append(z)
        for r in q:        
            b = [int(r[0]*w), int(r[1]*h), int(r[2]*w), int(r[3]*h)]
            pt1 = [int(b[0]-b[2]/2), int(b[1]-b[3]/2)]
            pt2 = [int(b[0]+b[2]/2), int(b[1]+b[3]/2)]
            if (pt1[0]<0):  pt1[0] = 0
            if (pt1[1]<0):  pt1[1] = 0
            if (pt2[0]>w):  pt2[0] = w
            if (pt2[1]>h):  pt2[1] = h            
            fo.write(fs + ', ' + str(pt1[0]) + ', ' + str(pt1[1]) + ', ' + str(pt2[0]) + ', ' + str(pt2[1]) + ', ' + 'face\n')

print('total: ', i)

# cv2.rectangle(img2, pt1, pt2, (0, 0, 255), 1)
# cv2.imshow('test',img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()