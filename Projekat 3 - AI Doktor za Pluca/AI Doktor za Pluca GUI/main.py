import tensorflow as tf
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

import numpy as np
import matplotlib.pyplot as plt
import cv2

if __name__ == '__main__':
    root = Tk()
    root.title("AI Doktor za Pluca")

    def ai_odg(IMG_LOCATION):
        KATEGORIJE = ['ZDRAV', 'VIRUS', 'BAKTERIJA', 'STREPTOCOCCUS', 'COVID-19', 'ARDS', 'SARS']
        IMG_SIZE = 400
        model = tf.keras.models.load_model('saved_model\\0-dense---32-nodes---1-conv---accuracy-95_08')
            # kod za ucitavanje modela koji se nalazi u folderu saved_model koji sadrzi folder 0-dense---32-nodes---1-conv---accuracy-95_08
        test_slika = cv2.imread(IMG_LOCATION, cv2.IMREAD_GRAYSCALE)
        test_slika = cv2.resize(test_slika, dsize=(IMG_SIZE, IMG_SIZE), interpolation=cv2.INTER_CUBIC)
        plt.imshow(test_slika, cmap='gray')

        test_slika = np.array(test_slika)
        test_slika = (np.expand_dims(test_slika, 0))
        test_slika = (np.expand_dims(test_slika, -1))

        prediction = model.predict(test_slika)
        return "Model je misli da je u pitanju {}".format(KATEGORIJE[int(np.argmax(prediction[0]))])

    def open():
        global my_image
        root.filename = filedialog.askopenfilename(title="Odaberite x-ray sliku vasih pluca", filetypes=[
            ('Slike', ('.png', '.jpg', '.jpeg', '.webp')),
            ('Svi fajlovi', '.*'),
        ])
        my_label = Label(root, text=ai_odg(root.filename)).pack()
        my_image = ImageTk.PhotoImage(Image.open(root.filename))
        my_image_label = Label(image=my_image).pack()


    my_btn = Button(root, text="Otvori", command=open).pack()

    root.mainloop()
