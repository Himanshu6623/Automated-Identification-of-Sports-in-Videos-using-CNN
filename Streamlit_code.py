from google.colab.patches import cv2_imshow
import cv2
import tensorflow as tf
import numpy as np
import keras
def predict(model, resize, pridicted_class):
   img_array =keras.utils.img_to_array(resize)
   img_array = tf.expand_dims(img_array, 0)
   predictions = model.predict(img_array)
   predict = class_names[np.argmax(predictions[0])]
   pridicted_class.append(predict)
def frames_from_video_file(video_path,pridicted_class):
  src = cv2.VideoCapture(video_path)
  ret,frame = src.read()
  i=0
  while True:
    ret, frame = src.read()
    if ret:
      if i%10==0:
        image=tf.image.resize(frame,(256,256))
        predict(model,image,pridicted_class)
        cv2_imshow(frame)
    i=i+1
    if(i==1000):
      break
pridicted_class=[]
path="/content/drive/MyDrive/correct_prediction/v_Archery_g01_c01.avi"
frames_from_video_file(path,pridicted_class)
print(pridicted_class)
occurances = {}
for value in pridicted_class:
    if value in occurances:
        occurances[value] += 1
    else:
        occurances[value] = 1

max_value = max(occurances, key=lambda x: occurances[x])

print(max_value)
