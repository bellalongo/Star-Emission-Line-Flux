import astropy.io.fits as fits
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from scipy.signal import find_peaks, peak_widths
import astropy.units as u
import numpy as np
import pandas as pd
from collections import defaultdict
import math
from astropy.table import QTable, Table, Column
from astropy.modeling import models, fitting


# Have both fits files be in the same array
data1 = fits.getdata('hlsp_muscles_hst_cos_gj849_g130m_v23_component-spec.fits')
data2 = fits.getdata('hlsp_muscles_hst_cos_gj832_g160m_v22_component-spec.fits')

# Iterate and see if there are duplicates, if so get rid of the g130m?
fits = defaultdict(list)

# 1428 1393 -> use data 1 up to 1393 1393.568834375207 use data up to 1393.56295 for data1
# for i in range(0,20):
#     print(data2['Wavelength'][i])

for data in data1:
    fits['Wavelength'].append(data['Wavelength'])
    fits['Flux'].append(data['Flux'])
    fits['Error'].append(data['Error'])

    if data['Wavelength'] == 1393.56295:
        # Exit
        break

for data in data2:
    fits['Wavelength'].append(data['Wavelength'])
    fits['Flux'].append(data['Flux'])
    fits['Error'].append(data['Error'])

data_array = []
for i in range(0, len(fits['Wavelength'])):
    data_array.append({"Wavelength" : fits["Wavelength"][i], "Flux" : fits["Flux"][i], "Error": fits["Error"][i]})

# Make into fits file
t = Table(rows=data_array)
t.write("gj832.fits", overwrite=True) 



