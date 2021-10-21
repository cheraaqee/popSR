import numpy as np
import cv2 as cv
#quantizationsad = np.load('quantizationMatrix.npy')
#quantization1 = quantization/2

jpeg = np.array([[16,11,10,16,24,40,51,61],[12,12,14,19,26,58,60,55],[14,13,16,24,40,57,69,56],[14,17,22,29,51,87,80,62],[18,22,37,56,68,109,103,77],[24,35,55,64,81,104,113,92],[49,64,78,87,103,121,120,101],[72,92,95,98,112,100,103,99]])
jpeg = jpeg.astype(np.float)
jpeg1 = cv.resize(jpeg,None, fx=2.625 , fy=2.625 , interpolation = cv.INTER_LINEAR)
jpeg1 = jpeg1.astype(np.uint8)

b = np.repeat(jpeg1[:, :, np.newaxis], 128, axis=2)
#b = b.astype(np.uint8)

np.save('quantizationMatrix.npy',b)