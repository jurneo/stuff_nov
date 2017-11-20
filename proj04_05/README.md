# Main Project 
## **Halucination for face from surveillance camera**

### **Main Idea**

- We have image scene captured from typical surveillance camera,

- There is person(s) of interest in the captured image

- The face of the person of interest does not have enough details or some details of the face parts are not good enough.

- We use super-resolution technique to improve the details

Therefore for this project we split into two parts: the first part has to do making a robust face detection using person detection (SSD method), and second part make use of the result from the first part to do face hallucination.

### **Dataset**

For the first part we use pre-trained model of inception, and the second part we use celeb-dataset and combined with dataset from cocos. 

### **Checklist**

1. Image Hallucination

    input : image low-res

    output : image high-res

2. Person Detection

3. Object Detection

### **TODO list**

- Test the train weight from my test, and compared them with what Sam has done in his example, and figure out the next step on this part.

- Test TensorFlow object detection API and see if we can run it on my machine

- Link up with face-detection from Dlib and see if they are sufficient for my purpose.

