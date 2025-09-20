

def radial_density_prof_halomod(particle_number, particle_mass, radius,so_radius,z,SOdensityL1):
    '''h=0.71
    Ob0 = 0.02237/h**2 #header value
    Ocdm0 = 0.12
    Onu0 = 0.0
    Om0 = Ocdm0 + Ob0 + Onu0
    n_s = 0.9649
    sigma_8 = 0.8'''

    h=0.6736
    Ob0 = 0.02237/h**2
    Om0 = 0.315192
    n_s = 0.9649
    sigma_8 = 0.807952

    hm = TracerHaloModel(z = z,
        halo_profile_model = 'NFW',
        cosmo_model = Planck18,
        sigma_8=sigma_8,
        n=n_s,
        mdef_model=mass_definitions.SOMean,
        halo_concentration_model='Ludlow16',
        mdef_params={'overdensity':SOdensityL1},
        cosmo_params = {
            'Om0': Om0,
            'H0': h*100,
            'Ob0':Ob0,
            'Tcmb0':2.7255,
            'Neff': 3.04,
        })
    #print(TracerHaloModel.parameter_info())

    r = np.logspace(np.min(np.log10(radius)), so_radius, 1000)
    for i in range(len(particle_number)):
        m= particle_mass*particle_number[i]
        indices = np.argsort(r)
        hm.halo_profile.rho(r=r[indices])
    plt.loglog()
    
    plt.plot(r[indices], hm.halo_profile.rho(r=r[indices], m=m))






radial_density_prof(particle_number,rad,so_radius[max_index],z)
radial_density_prof_halomod(particle_number, particle_mass, rad,so_radius[max_index],z,SOdensityL1)

plt.scatter(mass_pt, rad_density_comoving,label='Abacus Data')
plt.grid()
plt.legend()
plt.show()