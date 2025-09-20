from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import pandas as pd
import numpy as np
import glob
import os

def process_halo_file(file_path):
    box_size = 1000

    cat = CompaSOHaloCatalog(file_path, cleaned=False, subsamples=dict(A=True, B=True))
    cat.subsamples['pos'] += (box_size / 2)

    for halo_index, halo_N in enumerate(cat.halos['N']):
        if 61000 <= int(halo_N) <= 62000:
            halos = cat.halos[halo_index]
            data_A = cat.subsamples['pos'][halos['npstartA']:halos['npstartA'] + halos['npoutA']]
            data_B = cat.subsamples['pos'][halos['npstartB']:halos['npstartB'] + halos['npoutB']]

            # Ensure all arrays have the same length
            min_length = min(len(data_A), len(data_B))
            data_A, data_B = data_A[:min_length], data_B[:min_length]

            df_combined = pd.DataFrame({
                'Subsample_A_X': data_A[:, 0],
                'Subsample_A_Y': data_A[:, 1],
                'Subsample_A_Z': data_A[:, 2],
                'Subsample_B_X': data_B[:, 0],
                'Subsample_B_Y': data_B[:, 1],
                'Subsample_B_Z': data_B[:, 2]
            })

            file_name = os.path.splitext(os.path.basename(file_path))[0]
            df_combined.to_csv(f'{file_name}_subsample_data_{halo_N}.csv', index=False)

    del cat

def save_subsamples(halo_files):
    print('Reading Data')
    for file_path in halo_files:
        process_halo_file(file_path)
        print(f'Processed: {file_path}')

    print('Files Saved')

file_dir = '/home/swaraj/Documents/Radial data/High base/z0.8/halo_info/'
halo_files = glob.glob(os.path.join(file_dir, '*.asdf'))
save_subsamples(halo_files)
