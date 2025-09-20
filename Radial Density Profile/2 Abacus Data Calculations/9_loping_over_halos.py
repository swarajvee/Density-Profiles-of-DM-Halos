from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog

file = 'halo_info_000'
cat = CompaSOHaloCatalog('/home/swaraj/Documents/Radial data/z2/halo_info/'+file+'.asdf', cleaned=False,subsamples=dict(A=True, B=True))

positions = cat.subsamples['pos']
position = []
print(len(positions))
'''for i in range(len(positions)):
    halo = cat.halos[i]'''
    #pos_slice = cat.subsamples['pos'][halo['npstartA']:halo['npstartA'] + halo['npoutA']]
    #position.append(pos_slice)

#working on next step ....will be comming back to this one later