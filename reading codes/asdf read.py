from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import pandas as pd

#h = 0.6736 = hubblepara/100set
def readdata(file_name):
        h = 0.6736
        box_size = 500/h
        part_mass = 2.109081520453063e+09/h
        clms  = ['N', 'SO_central_particle']

        print("Reading the data")

        cat = CompaSOHaloCatalog(file_name,cleaned=False)
        data = cat.halos[clms]
        data['N'] = data['N'].astype('float')*part_mass
        data['SO_central_particle'] += (box_size/2) # correcting the box coordinates origin
        data['X'] =data['SO_central_particle'][:,0]
        data['Y'] =data['SO_central_particle'][:,1]
        data['Z'] =data['SO_central_particle'][:,2]
        del cat
        return data[['N', 'X', 'Y', 'Z']].to_pandas().to_csv('output.csv')
    
location = '/home/swaraj/Documents/s10 MSc Major Projects/mass density function per unit volume/mass density function per unit volume/Hubble data/z5.000/halo_info/halo_info_000.asdf'

readdata(location)
print("file saved")