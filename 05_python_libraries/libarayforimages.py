import imageio.v3 as iio

filenames = ['my_image_1.jpg', 'my_image_2.jpg']
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

for image in images:
    print(image)

iio.imwrite("team.gif", images, duration = 1000, loop = 0)