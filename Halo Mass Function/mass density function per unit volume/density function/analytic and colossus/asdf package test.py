"""python commands for reading asdf files"""
import asdf
from colossus.cosmology import cosmology
'''import matplotlib.pyplot as plt
fig =plt.figure(figsize=(10,8),dpi=100)'''
#from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog

def ASDF(file_path):

    """  *********  MY COSMOS ************
    om0, omega_M, cosmological parameter= 0.315192
    H0, hubble constant= 67.36
    ob0,omega_b, baryon density= 0.02237
    sigma8, ZD_Pk_norm, power spectrum normalization= 8.0 
    ns, n_s, spectral index of the primordial power spectrum= 0.9649"""


    af= asdf.open(file_path)
    af.info(max_rows=None,max_cols=None)
    SO_central_particle= af['data']['SO_central_particle']
    print(SO_central_particle)

'''#adding a new cosmology
params = {'flat': True, 'H0': 67.36, 'Om0': 0.315192, 'Ob0': 0.02237, 'sigma8': 8, 'ns': 0.9649}
cosmology.addCosmology('myCosmo', **params)
cosmo = cosmology.setCosmology('myCosmo')'''

file_path= '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/z8.000/halo_info/halo_info_000.asdf'
ASDF(file_path)