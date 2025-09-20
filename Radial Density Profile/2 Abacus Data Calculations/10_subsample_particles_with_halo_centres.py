from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10,8), dpi=100)

file = 'halo_info_000'
cat = CompaSOHaloCatalog('/home/swaraj/Documents/Radial data/z2/halo_info/'+file+'.asdf', cleaned=False,subsamples=dict(A=True, B=True))

L = cat.header['BoxSize']
#ax.set_aspect('equal')
ax.scatter(cat.subsamples['pos'][:,0], cat.subsamples['pos'][:,1],
    s=10., label='Subsample particles')
ax.scatter(cat.halos['x_L2com'][:,0], cat.halos['x_L2com'][:,1],
    s=1., label='Halo centers')
ax.set_xlabel('$x$ [Mpc/$h$]')
ax.set_ylabel('$y$ [Mpc/$h$]')

ax.set_xlim(-L/2,L/2)
ax.set_ylim(-L/2,L/2)

ax.legend(loc='upper right')
plt.show()