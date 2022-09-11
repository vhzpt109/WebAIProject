import cv2
import numpy as np
from PIL import Image
from tensorflow.keras.applications import EfficientNetB0

if __name__ == "__main__":
    model = EfficientNetB0()
    model.summary()
    model.save("EfficientNetB0.h5")
    # Model Inference
    # image = Image.open("Cat.jpg")
    # image = cv2.imread("Cat.jpg")
    # image = np.reshape(image, [1, 224, 224, 3])
    # print(image.shape)

    # predict = model.predict(image)

    # print(np.argmax(predict, axis=1))