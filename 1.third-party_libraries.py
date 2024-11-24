from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np
import requests

#pillow
image1 = Image.open('cat.jpg')
cropped = image1.crop((400, 80, 1800, 1200))
cropped.save('./cat_resize.jpg')

image2 = Image.open('Eiffel_Tower.jpeg')
blurred = image2.filter(ImageFilter.BLUR)
blurred.save('./Eiffel_Tower.png')

image3 = Image.open('nature.jpg')
grayscale = image3.convert('L')
grayscale.save('./nature_gray.png')


# matplotlib
x = np.linspace(0, 2, 100)
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([0, 1, 2, 3], [0, 1, 4, 9], label='quadratic')  # Plot some data on the Axes.
ax.plot(x, x**3, label='cubic')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title("plots")
plt.legend()
plt.show()


#requests
BASE_URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.608826,  # широта Липецка
    "longitude": 39.599229,  # долгота Липецка
    "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum",
    # минимальная и максимальная температура, сумма осадков
    "timezone": "Europe/Moscow"  # временная зона для Липецка
}
response = requests.get(BASE_URL, params=params)
if response.status_code == 200:
    data = response.json()
    # Поскольку индекс 0 представляет собой данные на текущий день, индекс 1 будет представлять данные на завтра
    tomorrow_temp_min = data['daily']['temperature_2m_min'][1]
    tomorrow_temp_max = data['daily']['temperature_2m_max'][1]
    tomorrow_precipitation = data['daily']['precipitation_sum'][1]

    print(f"Прогноз погоды в Липецке на завтра:")
    print(f"Минимальная температура: {tomorrow_temp_min}°C")
    print(f"Максимальная температура: {tomorrow_temp_max}°C")
    print(f"Ожидаемое количество осадков: {tomorrow_precipitation} мм")
else:
    print(f"Ошибка {response.status_code}: {response.text}")