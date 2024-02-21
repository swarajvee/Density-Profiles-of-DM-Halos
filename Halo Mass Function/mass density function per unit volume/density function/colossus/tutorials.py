"""  *********  MY COSMOS ************
om0, omega_M, cosmological parameter= 0.315192
    H0, hubble constant= 67.36
    ob0,omega_b, baryon density= 0.02237
    sigma8, ZD_Pk_norm, power spectrum normalization= 8.0 
    ns, n_s, spectral index of the primordial power spectrum= 0.9649"""


from colossus.cosmology import cosmology

'''for k in cosmology.cosmologies:
    print(k)'''
contents = [planck18-only,planck18,planck15-only,planck15,planck13-only,planck13,WMAP9-only,WMAP9-ML,WMAP9,WMAP7-only,WMAP7-ML,WMAP7,WMAP5-only,WMAP5-ML,WMAP5,WMAP3-ML,WMAP3,WMAP1-ML,WMAP1,illustris,bolshoi,multidark-planck,millennium,EdS,powerlaw]

for i in contents:
    cosmo = cosmology.setCosmology('contents[i]')
    print(cosmo)