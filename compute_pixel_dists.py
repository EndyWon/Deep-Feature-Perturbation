import argparse
import os
import numpy as np
from PIL import Image,ImageChops,ImageStat

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-d','--dir', type=str, default='./', help='the directory of the image pairs to compute the average pixel distance')

opt = parser.parse_args()

# compute the average pixel distance of all image pairs within a directory
files = os.listdir(opt.dir)

print(r'start computing pixel distance...')
dists = []

number = 0
for (ff,file0) in enumerate(files[:-1]):
    img0 = Image.open(os.path.join(opt.dir,file0))

    for (gg,file1) in enumerate(files[ff+1:]):
        img1 = Image.open(os.path.join(opt.dir,file1))

	# Compute pixel distance
        diff = ImageChops.difference(img0,img1)
        stat = ImageStat.Stat(diff)
        dist0 = stat.sum
        dist1 = sum(dist0)
        dist01 = dist1/255.0/(img0.size[0]*img0.size[1]*3)
        dists.append(dist01)
        number+=1
	

dist_mean = np.mean(np.array(dists))
print('Average pixel distance of %d image pairs: %.5f'%(number, dist_mean))
