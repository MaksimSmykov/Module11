from pprint import pprint

from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np
import requests

#pillow
image1 = Image.open('cat.jpg')
cropped = image1.crop((400, 80, 1800, 1200)) #изменение размера изображения
cropped.save('./cat_resize.jpg')

image2 = Image.open('Eiffel_Tower.jpeg')
blurred = image2.filter(ImageFilter.BLUR) #применение эффект размытия
blurred.save('./Eiffel_Tower_blur.png') #сохранение в другом формате

image3 = Image.open('nature.jpg')
grayscale = image3.convert('L') #конвертация в черно-белом цвете
grayscale.save('./nature_gray.png') #сохранение в другом формате


# matplotlib
x = np.linspace(0, 2, 100)
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3], [0, 1, 4, 9], label='quadratic')   # график №1
ax.plot(x, x**3, label='cubic') #график №2
ax.set_xlabel('x') # подпись оси x
ax.set_ylabel('y') # подпись оси y
ax.set_title("plots") # подпись заголовка
plt.legend() # показать легенду
plt.show()


#requests
response = requests.get('https://github.com')
print('Заголовки:', response.headers)
print('http-код состояния =', response.status_code)

print('URL:', response.url)

get_params = {'q': 'mp3', 'type': 'repositories'}
response = requests.get('https://github.com/search', params=get_params)
print('URL:', response.url)
