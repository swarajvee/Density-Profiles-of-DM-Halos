from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog

file = 'halo_info_000'
cat = CompaSOHaloCatalog('/home/swaraj/Documents/Radial data/z2/halo_info/'+file+'.asdf', cleaned=False,subsamples=dict(A=True, B=True))
h5 = cat.halos[4]
print(cat.subsamples['pos'][h5['npstartA']:h5['npstartA'] + h5['npoutA']])