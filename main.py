import os

from PIL import Image


def convert(file, output_dir):
    logo = Image.open(file)

    file = file.removesuffix("png")

    output_file = os.path.basename(file) + "ico"

    logo.save(output_dir + "\\" + output_file, format='ICO')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_path = "C:\\your\\input\\folder\\Icons"
    output_path = "C:\\your\\output\\folder\\Icons\\Converted"

    for file in os.listdir(input_path):
        if (file.endswith(".png")):
            convert(input_path+"\\"+file, output_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
