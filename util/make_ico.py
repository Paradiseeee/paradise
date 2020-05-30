# -*- coding: utf-8 -*-
import os
from PythonMagick import Image


class ICOGenerator():
    '''图片转为 ICO'''

    def __init__(self, filename, path='./'):
        '''Initializing'''
        self.path = './'
        self.filename = filename
    
    def generate(self):
        os.chdir(self.path)
        img = Image(self.filename)
        img.sample("128x128")
        name = self.filename.split('.')[0]
        img.write(name + '.ico')
        print(f'>>> 成功写出文件：{self.path + name}.ico')


if __name__ == "__main__":

    path = input("请输入图片路径及文件名：\n")
    generator = ICOGenerator(path)
    generator.generate()
