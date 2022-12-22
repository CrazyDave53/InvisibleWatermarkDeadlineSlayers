# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography
import os

total = 0
done = 0

directory = 'input'
output = 'encoded'

text = 'Nhom 8 - 22CLC06'
print('Nhap thong diep can an giau trong anh: ', end = '')
text = input()



for filename in os.listdir(directory):
    total += 1
    f = os.path.join(directory, filename)

    if os.path.isfile(f):
        try:
            
            print("Encoding ",f)

            # hide text to image
            path = f
            output_path = os.path.join(output, filename)
            Steganography.encode(path, output_path, text)

            # # read secret text from image
            # secret_text = Steganography.decode(output_path)
            # print(secret_text)
            done += 1
            # print("Success!!!!!")
        except:
            print('anh thu ',total,' bi loi')
print(done,'/',total,' cases success!!!!!')

os.system('pause')