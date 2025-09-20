import abacusnbody
from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import asdf
import matplotlib.pyplot as plt 
from abacusnbody.data.read_abacus import read_asdf


#redshift = 2
filepath = '/home/swaraj/Documents/Radial data/z2/halo_info/halo_info_000.asdf'
cat = CompaSOHaloCatalog(filepath, cleaned=False)
#read = read_asdf(filepath, colname='N')
#print(read)
#print(cat.halos['N','x_com'])

N = cat.halos['N']
x = cat.halos['x_com']

#h5= cat.halos[5]

print(cat)

'''plt.plot(x, y)
plt.show()'''
