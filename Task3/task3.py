import numpy as np
import matplotlib.pyplot as plt 
import argparse
from scipy.cluster.vq import kmeans2

inp = argparse.ArgumentParser()
inp.add_argument('--input')
inp.add_argument('--k')
inp.add_argument('--output')
args = inp.parse_args()

path = vars(args)['input']
k = vars(args)['k']
k=int(k)
out =  vars(args)['output']


img = plt.imread(path)
img = img[:,:,:3]
img = img.astype(float)
img1 = img.reshape(img.shape[0]*img.shape[1],3)

centroid,label = kmeans2(img1,k,minit='++')
img2 = np.array([centroid[i].tolist() for i in label])
img3 = img2.reshape(img.shape[0],img.shape[1],3)
#print(img3)
#print(img3.shape)
img3 = img3.astype("uint8")
plt.imshow(img3)
plt.imsave(out,img3)

#plt.savefig(str(out)+"/task3_result.png")

#plt.show()
#plt.imsave(out,img3)

#img = img[:,:,:3]
#print(img1)
#print(img1.shape)
#print(centroid)
#print(label)

