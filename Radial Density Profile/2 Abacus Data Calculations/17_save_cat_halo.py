from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import pandas as pd

file = 'halo_info_015'
file_dir = '/home/swaraj/Documents/Radial data/z2/halo_info/'

def save_halo(file,file_dir):
    print('Reading Data')
    cat = CompaSOHaloCatalog(file_dir+file+'.asdf', cleaned=False,subsamples=dict(A=True, B=True))
    box_size = cat.header['BoxSize']
    
    colums = ['id','npstartA','npstartB','npoutA','npoutB','N','x_L2com','x_com','SO_central_particle','SO_L2max_central_particle','SO_radius','r100_L2com']
    data = cat.halos[colums]

    data['x_L2com'] += (box_size/2)
    data['x_L2com_X']=data['x_L2com'][:,0]
    data['x_L2com_Y']=data['x_L2com'][:,1]
    data['x_L2com_Z']=data['x_L2com'][:,2]

    data['x_com'] += (box_size/2)
    data['x_com_X']=data['x_com'][:,0]
    data['x_com_Y']=data['x_com'][:,1]
    data['x_com_Z']=data['x_com'][:,2]
    
    data['SO_central_particle'] += (box_size/2)
    data['SO_central_particle_X'] =data['SO_central_particle'][:,0]
    data['SO_central_particle_Y'] =data['SO_central_particle'][:,1]
    data['SO_central_particle_Z'] =data['SO_central_particle'][:,2]

    data['SO_L2max_central_particle'] += (box_size/2)
    data['SO_L2max_central_particle_X']=data['SO_L2max_central_particle'][:,0]
    data['SO_L2max_central_particle_Y']=data['SO_L2max_central_particle'][:,1]
    data['SO_L2max_central_particle_Z']=data['SO_L2max_central_particle'][:,2]
    
    del cat
    return data[['id','npstartA','npstartB','npoutA','npoutB','N','x_L2com_X','x_L2com_Y','x_L2com_Z','x_com_X','x_com_Y','x_com_Z','SO_central_particle_X','SO_central_particle_Y','SO_central_particle_Z','SO_L2max_central_particle_X','SO_L2max_central_particle_Y','SO_L2max_central_particle_Z','SO_radius','r100_L2com']].to_pandas().to_csv(file+'.csv')

save_halo(file, file_dir)
print('File Saved')