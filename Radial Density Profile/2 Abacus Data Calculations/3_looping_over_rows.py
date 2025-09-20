from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10, 8), dpi = 100)

cat_path = '/home/swaraj/Documents/Radial data/z2/halo_info/halo_info_000.asdf'
cat = CompaSOHaloCatalog(cat_path, subsamples=dict(A=True), cleaned=False)

mass_A = cat.halos['N'].sum() * cat.header['ParticleSubsampleA']

position = cat.subsamples['pos']

x = []
y = []
z = []
for i in range(1000000):
    pos = position[i]
    x_pos = pos[0]
    y_pos = pos[1]
    z_pos = pos[2]
    x.append(x_pos)
    y.append(y_pos)
    z.append(z_pos)
plt.scatter(y,z, s=0.5, c=x)
plt.colorbar()
plt.show()