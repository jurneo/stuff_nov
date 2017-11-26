## **Face hallucination**

The idea of the project is to investigate how deep learning can solve problem of face hallucination. The topic of this work was early investigated in 1999 by Baker and Kanade et al.

From Wikipedia, face hallucination refers to any superresolution technique which applies specifically to faces. It comprises techniques which take noisy or low-resolution facial images, and convert them into high-resolution images using knowledge about typical facial features.

This project explore the recent work of super-resolution method with deep learning to do face hallucination.

### **Dataset**

For training and evaluation, the training dataset is from  [**CelebA**](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) dataset from Liu et al. (CUHK).

### **Extended Part**

The second part of the project is to put this technique into a typical scenario of a scene from camera surveillance scene. 

To link up to our face hallucination of the first part of the project, we need to be able to detect the person and then the face (or the face directly) in the scene.

And, then preprocess them to be ready as the input to our face hallucination model for inference.

For face detection, in this part the object detection from tensorflow model is used for training and detection. 

The object detection method is based on SSD method.

https://1drv.ms/u/s!ArIKNjDOB13ch3EacToq2ZKle8Pn
