import csv
import glob
import os

from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog

file = 'halo_info_000'
file_dir = '/home/swaraj/Documents/Radial data/High base/z0.8/halo_info/'

def save_subsamples(file, file_dir):
    box_size = 1000

    print('Reading Data')

    header = ['Number_of_Particles']
    output_filename = 'no_of_particles.csv'
    with open(output_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)

    files = glob.glob(os.path.join(file_dir, '*.asdf'), recursive=True)
    for file_path in files:
        cat = CompaSOHaloCatalog(file_path, cleaned=False, subsamples=dict(A=True, B=True))

        with open(output_filename, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for halo_index in range(0, len(cat.halos['N'])):
                if 61000 <= int(cat.halos['N'][halo_index]) <= 62000:
                    csvwriter.writerow([cat.halos['N'][halo_index]])
        
        del cat
        
    print("Data written to", output_filename)

save_subsamples(file, file_dir)
print('File Saved')
