import time
import keras_cv
import matplotlib.pyplot as plt

from tensorflow import keras
from translate import Translator

if __name__ == "__main__":
    model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)

    translator = Translator(from_lang="ko", to_lang="en")

    translation = translator.translate(input().rstrip())

    images = model.text_to_image(translation, batch_size=3)

    plt.figure(figsize=(20, 20))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.axis("off")
        plt.tight_layout()