import tensorflowjs as tfjs
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications import MobileNetV2

if __name__ == "__main__":
    model = EfficientNetB0()
    # model = MobileNetV2()
    model.summary()

    tfjs.converters.save_keras_model(model, "EfficientNetB0")
    # tfjs.converters.save_keras_model(model, "MobileNetV2")