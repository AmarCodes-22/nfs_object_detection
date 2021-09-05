# Object detection
This project is a bare bones minimum base model trained from yolov3 tiny.  
The aim of the object detection model was to detect cars, trucks, and other objects in the game need for speed most wanted 2005.  
For the dataset, i recorded the gameplay footage and chose frames from the video that could be good data for the object detection model.  

Some of the detections from the model are:  
  
![](https://github.com/AmarCodes-22/nfs_object_detection/blob/main/detections/Screenshot%20from%202021-09-05%2022-41-17.png)
  
![](https://github.com/AmarCodes-22/nfs_object_detection/blob/main/detections/Screenshot%20from%202021-09-05%2022-41-32.png)  
  
![](https://github.com/AmarCodes-22/nfs_object_detection/blob/main/detections/Screenshot%20from%202021-09-05%2022-41-51.png)  

![](https://github.com/AmarCodes-22/nfs_object_detection/blob/main/detections/Screenshot%20from%202021-09-05%2022-42-10.png)  

![](https://github.com/AmarCodes-22/nfs_object_detection/blob/main/detections/Screenshot%20from%202021-09-05%2022-43-53.png)  

![](https://github.com/AmarCodes-22/nfs_object_detection/blob/main/detections/Screenshot%20from%202021-09-05%2022-44-11.png)  

**NOTE : **
1. I could have used more data. I only used ~350 images for 4 classes.
2. It is recommended to train the model for 8k iterations, but i only trained it for 2k.
3. Now in retrospect, my labelling wasn't very accurate when it comes to cars so that clearly affected the model. I Couldn't find a lot of good detections for cars.