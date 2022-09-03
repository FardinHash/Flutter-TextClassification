import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_keras_model(model)  #converter for the model
tflite_model = converter.convert()

with open("model.tflite", 'wb') as f:  
  f.write(tflite_model) 
