from colossus.cosmology import cosmology

#adding a new cosmology
params = {'flat': True, 'H0': 67.36, 'Om0': 0.31, 'Ob0': 0.049, 'sigma8': 0.81, 'ns': 0.95}
cosmology.addCosmology('myCosmo', **params)
cosmo = cosmology.setCosmology('myCosmo')

