import os
import glob

dir_path = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/csv data/z0.1'
files = glob.glob(os.path.join(dir_path,'*z*.csv'))

print(files)




