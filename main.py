import os

from PIL import Image

import tkinter as tk
from tkinter import filedialog

def convert(file, output_dir):
    logo = Image.open(file)

    file = file.removesuffix("png")

    output_file = os.path.basename(file) + "ico"

    logo.save(output_dir + "\\" + output_file, format='ICO')


def convert_batch(input_path, output_path):
    for file in os.listdir(input_path):
        if (file.endswith(".png")):
            convert(input_path + "\\" + file, output_path)


if __name__ == '__main__':
    input_path = filedialog.askdirectory(initialdir="C:\\Users\\bloch\\Desktop")
    output_path = filedialog.askdirectory(initialdir="C:\\Users\\bloch\\Desktop")

    convert_batch(input_path, output_path)

