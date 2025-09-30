import imageio.v3 as iio
import os

filenames = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
images = [iio.imread(fn) for fn in filenames]

output_file = "team.gif"
iio.imwrite(output_file, images, duration=0.5, loop=0, format="GIF")

print("GIF saved to:", os.path.abspath(output_file))
print("Does it exist?", os.path.exists(output_file))
