from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10, 8), dpi = 100)
import pandas as pd
import numpy as np 

file = 'halo_info_004'
cat_path = '/home/swaraj/Documents/Radial data/z2/halo_info/'+file+'.asdf'
print('reading data')

def save_csv(cat_path):
    cat = CompaSOHaloCatalog(cat_path, subsamples=dict(A=True), cleaned=False)
    position = cat.subsamples['pos']
    velocity = cat.subsamples['vel']

    x = []
    y = []
    z = []
    v_x = []
    v_y = []
    v_z = []
    
    #pos_chunk = 

    for i in range(len(position)):
        pos = position[i]
        vel = velocity[i]

        x_pos = pos[0]
        y_pos = pos[1]
        z_pos = pos[2]

        vx = vel[0]
        vy = vel[1]
        vz = vel[2]

        x.append(x_pos)
        y.append(y_pos)
        z.append(z_pos)
        v_x.append(vx)
        v_y.append(vy)
        v_z.append(vz)
    
    data_out = pd.DataFrame({
        'x': x,
        'y': y,
        'z': z,
        'v_x': v_x,
        'v_y': v_y,
        'v_z': v_z
    })
    
    data_out.to_csv(f'{file}.csv')
    return data_out

save_csv(cat_path)
print('file saved')