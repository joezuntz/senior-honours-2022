"""
This is the script JZ used to make the data in the first place.

"""
import fitsio
import numpy as np

nbin = 6

filename = "/Users/jzuntz/src/des/y3-3x2pt-methods/cosmosis/data_vectors/fiducial_maglim_source_sompz_lens_sompz_hyperrank_nonu.fits"

nzs = []
with fitsio.FITS(filename) as f:
    for i in range(7, 2407):
        ext = f[i]
        data = ext.read()
        nz_i = [data[f'BIN{b}'] for b in range(1, nbin + 1)]
        nz_i = np.concatenate(nz_i)
        nzs.append(nz_i)
    z = f[7]['Z_MID'][:]

nzs = np.array(nzs)
nr, nf = nzs.shape
nz = z.size


np.savetxt("z.txt", z)
np.savetxt("nzs.txt", nzs)
