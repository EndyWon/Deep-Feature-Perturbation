import argparse
import os
import numpy as np
from PIL import Image,ImageChops,ImageStat

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-d','--dir', type=str, default='./', help='the directory of the image pairs to compute the average pixel distance')

opt = parser.parse_args()

# compute the average pixel distance of all image pairs within a directory
files = os.listdir(opt.dir)

print(r'---------------------------------')
print(r'Start computing pixel distance...')
dists = []

number = 0
ignored_number = 0

for (ff,file0) in enumerate(files[:-1]):
    img0 = Image.open(os.path.join(opt.dir,file0))

    for (gg,file1) in enumerate(files[ff+1:]):
        img1 = Image.open(os.path.join(opt.dir,file1))
        if img1.size[0]== img0.size[0] and img1.size[1]== img0.size[1]:
	    # Compute pixel distance
            diff = ImageChops.difference(img0,img1)
            stat = ImageStat.Stat(diff)
            dist0 = stat.sum
            dist1 = sum(dist0)
            dist01 = dist1/255.0/(img0.size[0]*img0.size[1]*3)
            dists.append(dist01)
            number += 1
        else:
            print (r"Ignored!"+ r"The size of image "+ file0+ r"("+ str(img0.size[0])+ r","+ str(img0.size[1])+ r")"+ r" is not the same as "+ file1+ r"("+ str(img1.size[0])+ r","+ str(img1.size[1])+ r").")
            ignored_number += 1
	

dist_mean = np.mean(np.array(dists))
print(r'---------------------------------')
print(r"Total number of image pairs: %d, Tested: %d, Ignored: %d"%(number+ignored_number, number, ignored_number))
print(r"Average pixel distance of %d image pairs: %.5f"%(number, dist_mean))
