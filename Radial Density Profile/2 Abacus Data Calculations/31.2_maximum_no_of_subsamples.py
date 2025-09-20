from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import numpy as np
import glob
import os

'''file_chage = [str(i).zfill(2) for i in range(16)]
for i in file_chage:

    file_path =f'Radial data/High base/z0.8/halo_info/halo_info_0{i}.asdf'
    cat = CompaSOHaloCatalog(file_path, cleaned=False, subsamples=dict(A=True, B=True))
    for halo_index in range(0, len(cat.halos['N'])):
                if 61000 <= int(cat.halos['N'][halo_index]) <= 62000:
                        print([cat.halos['N'][halo_index]])
del cat
    #print(cat.halos['61788'])'''

file_dir = '/home/swaraj/Documents/Radial data/High base/z0.8/halo_info/'
halo_files = glob.glob(os.path.join(file_dir, '*.asdf'))

halo = []  # Define the list before the loop
for file_path in halo_files:
    colums = ['N']
    cat = CompaSOHaloCatalog(file_path, cleaned=False, subsamples=dict(A=True, B=True),fields=colums)
    halo_index = np.argmax(cat.halos['N'])
    halo.append(cat.halos['N'][halo_index])

print(halo)
