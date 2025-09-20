import zipfile
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def subsample_data_from_zip(file_path):
    particle_range = os.path.splitext(os.path.basename(file_path))[0]  # Extract particle range from file name
    print("Particle Range:", particle_range)
    outer_list = []
    
    with zipfile.ZipFile(file_path, 'r') as zip:
        csv_files = [name for name in zip.namelist() if name.endswith('.csv')]
        print("CSV Files in Zip:", csv_files)
        
        for csv_file in csv_files:
            with zip.open(csv_file) as csv:
                subsamples = pd.read_csv(csv)

                Subsample_A_X = subsamples['Subsample_A_X']
                Subsample_A_Y = subsamples['Subsample_A_Y']
                Subsample_A_Z = subsamples['Subsample_A_Z']

                Subsample_B_X = subsamples['Subsample_B_X']
                Subsample_B_Y = subsamples['Subsample_B_Y']
                Subsample_B_Z = subsamples['Subsample_B_Z']

                Subsample_X = np.vstack((Subsample_A_X, Subsample_B_X))
                Subsample_Y = np.vstack((Subsample_A_Y, Subsample_B_Y))
                Subsample_Z = np.vstack((Subsample_A_Z, Subsample_B_Z))

                x = [number for array in Subsample_X for number in array if not np.isnan(number)]
                y = [number for array in Subsample_Y for number in array if not np.isnan(number)]
                z = [number for array in Subsample_Z for number in array if not np.isnan(number)]

                outer_list.append((x, y, z))
                
    print("Total unique file locations processed:", len(outer_list))
    return outer_list

# Example usage:
file_path = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/Radial Density Profile/high base/z2/subsample data/averaging/35-89144.zip'
X_Y_Z_lists = subsample_data_from_zip(file_path)



plt.scatter(X_Y_Z_lists[1],X_Y_Z_lists[2])
plt.show()