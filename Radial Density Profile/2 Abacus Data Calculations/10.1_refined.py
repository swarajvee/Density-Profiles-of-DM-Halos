from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10,8), dpi=150)

file = 'halo_info_000'
cat = CompaSOHaloCatalog('/home/swaraj/Documents/Radial data/z2/halo_info/'+file+'.asdf', cleaned=False,subsamples=dict(A=True, B=True))

L = cat.header['BoxSize']



#fig, ax = plt.subplots(dpi=150)
ax.set_aspect('equal')
ax.set_xlim(-L/2,L/2)
ax.set_ylim(-L/2,L/2)
ax.set_xlabel('$x$ [Mpc/$h$]')
ax.set_ylabel('$y$ [Mpc/$h$]')
subsamp_densorder = cat.subsamples[cat.subsamples['density'].argsort()]

sc = ax.scatter(subsamp_densorder['pos'][:,0], subsamp_densorder['pos'][:,1], s=4.,
    c=subsamp_densorder['density'],
    norm=matplotlib.colors.LogNorm()
)
cbar = fig.colorbar(sc)
cbar.set_label('Density / cosmic mean')