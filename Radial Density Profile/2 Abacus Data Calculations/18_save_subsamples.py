from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import pandas as pd
import numpy as np

file = 'halo_info_000'
file_dir = '/home/swaraj/Documents/Radial data/z2/halo_info/'

def save_subsamples(file, file_dir):
    box_size = 1000

    print('Reading Data')
    cat = CompaSOHaloCatalog(file_dir + file + '.asdf', cleaned=False, subsamples=dict(A=True, B=True))

    halo_index = np.argmax(cat.halos['N'])
    halos = cat.halos[halo_index]
    column=['pos']
    data_subsamples = cat.subsamples[column]

    cat.subsamples['pos'] += (box_size / 2)
    data_A = cat.subsamples['pos'][halos['npstartA']:halos['npstartA'] + halos['npoutA']]
    data_B = cat.subsamples['pos'][halos['npstartB']:halos['npstartB'] + halos['npoutB']]
    del cat

    subsample_A_X = data_A[:,0]
    subsample_A_Y = data_A[:,1]
    subsample_A_Z = data_A[:,2]

    subsample_B_X = data_B[:,0]
    subsample_B_Y = data_B[:,1]
    subsample_B_Z = data_B[:,2]

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
    return df_combined.to_csv(file + '_subsample_data.csv', index=False)
    
save_subsamples(file, file_dir)
print('File Saved')