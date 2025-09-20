from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10,8), dpi=100)

file = 'halo_info_000'
cat = CompaSOHaloCatalog('/home/swaraj/Documents/Radial data/z2/halo_info/'+file+'.asdf', cleaned=False,subsamples=dict(A=True, B=True))

bighalo = cat.halos[123]
print(bighalo['N'])
print(bighalo['x_L2com'])

'''plt.scatter(bighalo['x_L2com'][0],bighalo['x_L2com'][1])
plt.show()'''

bighalo_subsamples = cat.subsamples[bighalo['npstartA'] : bighalo['npstartA'] + bighalo['npoutA']]
print(bighalo_subsamples['pos'].data)  # using .data just so all three columns are printed
