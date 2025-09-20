import glob
import os



z= 0.1
file_dir=f'/Users/swarajv/Education/s10 MSc Major Project/Hubble data/HMFcsvdata_(all_at_once)'
file_path = glob.glob(os.path.join(file_dir,'**',f'*z{z}.csv'))


