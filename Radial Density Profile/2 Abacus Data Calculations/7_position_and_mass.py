from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog

file = 'halo_info_000'
cat = CompaSOHaloCatalog('/home/swaraj/Documents/Radial data/z2/halo_info/'+file+'.asdf', cleaned=False,subsamples=dict(A=True, B=True))
print(cat.halos['N','x_com'][:5])