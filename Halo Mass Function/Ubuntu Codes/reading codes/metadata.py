import abacusnbody.metadata

#meta = abacusnbody.metadata.get_meta('simname':'AbacusSummit_base_ph000_c000', 'redshift':2)
meta = abacusnbody.metadata.get_meta('AbacusSummit_base_c000_ph000', redshift=8)
print(meta['Om0'])