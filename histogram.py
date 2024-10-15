import imageio
import numpy as np
import matplotlib.pyplot as plt


image_path = "C:\\Users\\ASUS VIVOBOOK GO14\\Pictures\\histogram\\1.jpg"
image = imageio.imread(image_path)


if len(image.shape) < 3 or image.shape[2] != 3:
    print("Format gambar harus RGB")
    exit()


red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]


histogram_red = np.zeros(256, dtype=int)
histogram_green = np.zeros(256, dtype=int)
histogram_blue = np.zeros(256, dtype=int)


for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        histogram_red[red[i, j]] += 1
        histogram_green[green[i, j]] += 1
        histogram_blue[blue[i, j]] += 1


plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.bar(range(256), histogram_red)
plt.title("Histogram Merah")
plt.xlabel("Intensitas")
plt.ylabel("Jumlah Piksel")

plt.subplot(1, 3, 2)
plt.bar(range(256), histogram_green)
plt.title("Histogram Hijau")
plt.xlabel("Intensitas")
plt.ylabel("Jumlah Piksel")

plt.subplot(1, 3, 3)
plt.bar(range(256), histogram_blue)
plt.title("Histogram Biru")
plt.xlabel("Intensitas")
plt.ylabel("Jumlah Piksel")

plt.tight_layout()
plt.show()

# Menghitung total piksel
total_pixels = image.shape[0] * image.shape[1]

# Menampilkan hasil total piksel dan intensitas dominan
print("Total piksel:", total_pixels)