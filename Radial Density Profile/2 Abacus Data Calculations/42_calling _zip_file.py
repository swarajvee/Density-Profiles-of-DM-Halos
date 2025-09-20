import zipfile

file_path='/Users/swarajv/Education/s10 MSc Major Project/Hubble data/Radial Density Profile/high base/z2/subsample data/averaging/35-89144.zip'

zip = zipfile.ZipFile(file_path)
print(zip.namelist())