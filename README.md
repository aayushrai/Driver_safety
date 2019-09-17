# Driver_safety

This project can help to save lives and prevent accidents using deep learning. when a driver does not sleep properly or sleep while driving it gives a warning and start alarm which can prevent accidents. A camera in front of the driver face which detects the driver's face and using deep learning identify the driver eyes closed or opened with the help of this data system identify sleeping or not.

**Convolutional Neural Network** used for classification of the images, rather person eye in image close or open.**Keras API** used for building a CNN. A Convolutional Neural Network (ConvNet/CNN) is a Deep Learning algorithm which can take in an input image, assign importance (learnable weights and biases) to various aspects/objects in the image and be able to differentiate one from the other. The pre-processing required in a ConvNet is much lower as compared to other classification algorithms. While in primitive methods filters are hand-engineered, with enough training, ConvNets have the ability to learn these filters/characteristics.

**Haar Cascade classifier** used for face detection and then extract the face from image. After the face extraction from image we provide this image to train CNN classifier which classify the eyes in the image of the face is close or open. Haar Cascade is a machine learning object detection algorithm used to identify objects in an image or video and based on the concept of feature.Haar Cascade classifier is based on the Haar Wavelet technique to analyse pixels in the image into squares by function.

# Awake
![image](https://github.com/aayushrai/Driver_safety/blob/master/s3.jpg)

# Not slept properly
![image](https://github.com/aayushrai/Driver_safety/blob/master/s1.jpg)

# Slept
![image](https://github.com/aayushrai/Driver_safety/blob/master/s2.jpg)

## Installation

A step by step series of examples that tell you how to get a development env running:-

First install python3 

```
https://www.python.org/downloads/this 
```

Then install opencv module in python3 

```
https://pypi.org/project/opencv-python/
pip install opencv-python
```

Then install numpy module in python3

```
https://pypi.org/project/numpy/
pip install numpy
```
And then install keras python3 deep learning library

```
https://pypi.org/project/Keras/
pip install Keras
```


