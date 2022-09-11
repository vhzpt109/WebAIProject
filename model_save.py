import tensorflowjs as tfjs
from tensorflow.keras.applications import EfficientNetB0

if __name__ == "__main__":
    model = EfficientNetB0()
    model.summary()
    model.save("EfficientNetB0.h5")

    tfjs.converters.save_keras_model(model, "EfficientNetB0.js")