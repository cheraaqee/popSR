# popSR
We have provided a loss function for the task of single-image super-resolution. An implementation embedding the penalizer in the [SRCNN](https://github.com/tegg89/SRCNN-Tensorflow) is available here. Other necessary instructions for CNN-independent employment of the loss function will be subsequently provided.

Some results for the 2x, 3x, and 4x upscaling factors are represented with the respective order. The first column is the ground truth, second is the pure SRCNN, and the last column is the result of SRCNN employing our loss function.  
_2x:_
![temp_img_2x](https://user-images.githubusercontent.com/25932272/138225698-b56f5909-157e-4777-be75-7714e05da8d7.jpg)  
_3x:-  
![temp_img_3x](https://user-images.githubusercontent.com/25932272/138225710-e131532a-c4f6-4819-903c-46e2418749ce.jpg)  
_4x:_ 
![temp_img_4x](https://user-images.githubusercontent.com/25932272/138225735-f0477245-bdc3-4858-96c6-83af2f1d537d.jpg)
