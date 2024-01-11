from colossus.cosmology import cosmology

#adding a new cosmology
params = {'flat': True, 'H0': 67.36, 'Om0': 0.315192, 'Ob0': 0.02237, 'sigma8': 8, 'ns': 0.9649}
cosmology.addCosmology('myCosmo', **params)
cosmo = cosmology.setCosmology('myCosmo')

"""om0, omega_M, cosmological parameter= 0.315192
    H0, hubble constant= 67.36
    ob0,omega_b, baryon density= 0.02237
    sigma8, ZD_Pk_norm, power spectrum normalization= 8.0 
    ns, n_s, spectral index of the primordial power spectrum= 0.9649"""