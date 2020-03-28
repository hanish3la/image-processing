import numpy as np
from matplotlib import pyplot as plt
import cv2

#read BGR
im = cv2.imread('/home/hulk/PycharmProjects/sec_cv/j.png')
#convert image to gray
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# convert gray to binary
bw = gray>90
##generate image as in slides for dilation
# bw=np.zeros((7,5))
# bw[1:5,1:3]=1
# bw[4:6,2:4]=1
# print(bw)
#generate image as in slides for dilation
# bw=np.zeros((6,6))
# bw[1:5,2:6]=1
# bw[3,4]=0
# bw[0,1]=1
# bw[1,:2]=1
# bw[5,2:4]=1
# bw[4,1]=1
# print(bw)

selement = np.array([[1,1,1],[1,1,1],[1,1,1]])

def dilation(image,s):
    n , m = s.shape
    k = int (n / 2)
    # get index of 1's element
    indeces = list (zip (*np.where (s == 1)))
    # edit indeces
    for x in range (len (indeces)):
        indeces[x] = (indeces[x][0] - k , indeces[x][1] - k)

    # declare output image
    row , col = image.shape
    dilated = np.zeros (image.shape)
    #perform translation and union (dilation)
    for x in range (k , row - k):
        for y in range (k , col - k):
            if (image[x , y] == 1):
                for index in indeces:
                    dilated[x + index[0] , y + index[1]] = 1
    return dilated
# output = dilation(bw,selement)
# print (output)


def erosion(image,s):
    n , m = s.shape
    k = int (n / 2)
    # get index of 1's element
    indeces = list (zip (*np.where (s == 1)))
    # edit indeces
    for x in range (len (indeces)):
        indeces[x] = (indeces[x][0] - k , indeces[x][1] - k)
    
    # declare output image
    row , col = image.shape
    eroded = np.zeros (image.shape)
    for x in range(k,row-k):
        for y in range(k,col-k):
            if(image[x,y]==1):
                count =0
                for index in indeces:
                    if(image[x+index[0],y+index[1]] == 1):
                        count = count +1
                if(count == len(indeces)):
                    eroded[x,y] = 1
    return eroded

# output = erosion(bw,selement)
# print(output)

# #opening
# eroded = erosion(bw,selement)
# opened = dilation(eroded,selement)
# #closing
# dilated = dilation(bw,selement)
# closed = erosion(dilated,selement)

# #image edges
# dilated = dilation(bw,selement)
# edges = dilated - bw

# #morphological gradients
# dilated= dilation(bw,selement)
# eroded = erosion(bw,selement)
# mg  = dilated - eroded
#internal boundaries
eroded = erosion(bw,selement)
ib = bw-eroded
plt.imshow(bw,cmap='gray')
plt.axis('off')
plt.figure()
plt.imshow(eroded,cmap='gray')
plt.axis('off')
plt.figure()
plt.imshow(ib,cmap='gray')
plt.axis('off')
plt.show()


