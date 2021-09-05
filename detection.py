import cv2
import numpy as np
import os
import random

paths = {
    'images_dir': os.path.join(os.getcwd(), 'data', 'images'),
    'videos_dir': os.path.join(os.getcwd(), 'data', 'videos'),
    # 'class_names': os.path.join(os.getcwd(), 'data', 'obj.names'),
    'tiny_yolo_config': os.path.join(os.getcwd(), 'trained_models', 'yolov3_tiny.cfg'),
    'tiny_yolo_weights': os.path.join(os.getcwd(), 'trained_models', 'yolov3_tiny_training_2000.weights')
}

classes_names = ['navigation', 'car', 'misc', 'truck']

net = cv2.dnn.readNetFromDarknet(paths['tiny_yolo_config'], paths['tiny_yolo_weights'])
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

def pick_random_image(images_dir:str) -> str:
    images = os.listdir(images_dir)
    chosen_image = random.sample(images, 1)
    image_path = os.path.join(paths['images_dir'], chosen_image[0])
    return image_path

def find_objects(outputs, image:np.ndarray):
    height, width, color_channels = image.shape
    bbox = list()
    class_ids = list()
    confs = list()
    
    for output in outputs:
        for det in output:
            scores = det[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                w, h = int(det[2]*width), int(det[3]*height)
                x, y = int((det[0]*width) - w/2), int((det[1]*height) - h/2)
                bbox.append([x, y, w, h])
                class_ids.append(class_id)
                confs.append(float(confidence))
    print(len(bbox))
    indices = cv2.dnn.NMSBoxes(bbox, confs, 0.5, 0.3)
    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow('Output', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

img = cv2.imread(pick_random_image(paths['images_dir']))

blob = cv2.dnn.blobFromImage(img, 1/255, (320, 320), [0,0,0], 1, crop=False)
net.setInput(blob)

layer_names = net.getLayerNames()
output_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

outputs = net.forward(output_names)
find_objects(outputs, img)

# print(output[0].shape)
# print(output_names)
# print(layer_names)