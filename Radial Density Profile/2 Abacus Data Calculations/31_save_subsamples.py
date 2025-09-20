from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import pandas as pd
import numpy as np
import glob
import os

def save_subsamples(halo_files,halo_min,halo_max):
    box_size = 1000

    print('Reading Data')
    for file_path in halo_files:
        colums = ['id','npstartA','npstartB','npoutA','npoutB','N']
        cat = CompaSOHaloCatalog(file_path, cleaned=False, subsamples=dict(A=True, B=True),fields=colums)
        cat.subsamples['pos'] += (box_size / 2)

        for halo_index in range(0, len(cat.halos['N'])):
                halo_N=cat.halos['N'][halo_index]
                if halo_min <= int(halo_N) <= halo_max:
                    halos=cat.halos[halo_index]
                    data_A = cat.subsamples['pos'][halos['npstartA']:halos['npstartA'] + halos['npoutA']]
                    data_B = cat.subsamples['pos'][halos['npstartB']:halos['npstartB'] + halos['npoutB']]

                    subsample_A_X = data_A[:, 0]
                    subsample_A_Y = data_A[:, 1]
                    subsample_A_Z = data_A[:, 2]

                    subsample_B_X = data_B[:, 0]
                    subsample_B_Y = data_B[:, 1]
                    subsample_B_Z = data_B[:, 2]

                    dfA = pd.DataFrame({
                        'Subsample_A_X': subsample_A_X,
                        'Subsample_A_Y': subsample_A_Y,
                        'Subsample_A_Z': subsample_A_Z
                    })
                    dfB = pd.DataFrame({
                        'Subsample_B_X': subsample_B_X,
                        'Subsample_B_Y': subsample_B_Y,
                        'Subsample_B_Z': subsample_B_Z
                    })

                    df_combined = pd.concat([dfA, dfB], ignore_index=True)
                    file_name = os.path.splitext(os.path.basename(file_path))[0]
                    df_combined.to_csv(f'{file_name}_subsample_data_{halo_N}.csv', index=False)

                    del dfA, dfB, df_combined
        print(f'Processed: {file_path}')
        del cat

halo_min=30000
halo_max=31000

file_dir = '/home/swaraj/Documents/Radial data/High base/z2/halo_info/'
halo_files = glob.glob(os.path.join(file_dir, '*.asdf'))

save_subsamples(halo_files,halo_min,halo_max)
print('Files Saved')
