import abacusnbody.metadata

file_path= '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/z8.000/halo_info/halo_info_000.asdf'
meta = abacusnbody.metadata.get_meta(file_path)
pk = meta['CLASS_power_spectrum']
print(pk)