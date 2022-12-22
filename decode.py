# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography
import os

total = 0
done = 0

directory = 'encoded'
# output = 'encoded'
# text = 'Nhom 8 - 22CLC06'


for filename in os.listdir(directory):
    total += 1
    f = os.path.join(directory, filename)

    if os.path.isfile(f):
        try:
            
            print("Decoding ",f)

            # hide text to image
            # path = f
            # output_path = os.path.join(output, filename)
            # Steganography.encode(path, output_path, text)

            # # read secret text from image
            secret_text = Steganography.decode(f)
            print('Noi dung an la', secret_text)
            done += 1
        except:
            print('anh thu ',total,' bi loi')
print(done,'/',total,' test success!!!!!')

os.system('pause')