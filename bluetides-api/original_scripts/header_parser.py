import glob

import numpy as np
from astropy.cosmology import FlatLambdaCDM
from bigfile import BigFile

cosmo = FlatLambdaCDM(H0=69.7, Om0=0.2814, Ob0=0.0464)
files = '/bluetides3/PIG_*'

# Yueying: The snapshot is written in bigfile.
# The header file can be used to extract the general information of the PIG file.
# Here is the script I use to make that info table for you.
for f in sorted(glob.glob(files)):
    pig = BigFile(f)
    z = 1. / pig.open('Header').attrs['Time'][0] - 1  # redshift
    Nfof = pig.open('Header').attrs['NumFOFGroupsTotal'][0]  # Number of FOF Groups
    Npgt = pig.open('Header').attrs['NumPartInGroupTotal']  # Number of particles in the group
    t = np.array(cosmo.age(z))  # age of the universe
    print(f[-7:])
    print("Age (Gyr): %.3f" % t, "Redshift (z): %.2f" % z, "Dark matter in group [#]: %s" % Npgt[0],
          "Gas in group [#]: %s" % Npgt[1], "Stars [#]: %s" % Npgt[4], "Black holes [#]: %s" % Npgt[5],
          "FoF Groups [#]: %s" % Nfof, )
