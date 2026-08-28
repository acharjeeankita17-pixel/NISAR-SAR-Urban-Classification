#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os

print("Current folder:")
print(os.getcwd())

print("\nFiles in this folder:")
for f in os.listdir():
    print(f)


# In[4]:


import os

downloads = r"C:\Users\Ankita\Downloads"

h5_files = []

for root, dirs, files in os.walk(downloads):
    for file in files:
        if file.lower().endswith(".h5"):
            h5_files.append(os.path.join(root, file))

print("H5 files found:")

for f in h5_files:
    print(f)


# In[5]:


import h5py

file_path = r"C:\Users\Ankita\Downloads\NISAR_S2_PR_GCOV_025_170_A_013_3700_DHNA_A_20260719T232918_20260719T232955_P00500_M_F_I_001.h5"

with h5py.File(file_path, "r") as f:
    print("NISAR H5 file opened successfully!")
    print("\nFile structure:\n")
    f.visit(print)


# In[6]:


import h5py

file_path = r"C:\Users\Ankita\Downloads\NISAR_S2_PR_GCOV_025_170_A_013_3700_DHNA_A_20260719T232918_20260719T232955_P00500_M_F_I_001.h5"

with h5py.File(file_path, "r") as f:
    for layer in ["HHHH", "HHHV", "HVHV"]:
        d = f[f"science/SSAR/GCOV/grids/frequencyA/{layer}"]
        print(layer)
        print("Shape:", d.shape)
        print("Data type:", d.dtype)
        print()


# In[7]:


import h5py

file_path = r"C:\Users\Ankita\Downloads\NISAR_S2_PR_GCOV_025_170_A_013_3700_DHNA_A_20260719T232918_20260719T232955_P00500_M_F_I_001.h5"

with h5py.File(file_path, "r") as f:
    d = f["science/SSAR/GCOV/grids/frequencyA/HHHH"]

    print("Shape:", d.shape)
    print("Data type:", d.dtype)
    print("Minimum:", d[:].min())
    print("Maximum:", d[:].max())


# In[9]:


import h5py

file_path = r"C:\Users\Ankita\Downloads\NISAR_S2_PR_GCOV_025_170_A_013_3700_DHNA_A_20260719T232918_20260719T232955_P00500_M_F_I_001.h5"

with h5py.File(file_path, "r") as f:
    d = f["science/SSAR/GCOV/grids/frequencyA/HHHH"]

    sample = d[0:1000, 0:1000]

    print("Sample shape:", sample.shape)
    print("Minimum:", sample.min())
    print("Maximum:", sample.max())


# In[10]:


import h5py
import numpy as np

file_path = r"C:\Users\Ankita\Downloads\NISAR_S2_PR_GCOV_025_170_A_013_3700_DHNA_A_20260719T232918_20260719T232955_P00500_M_F_I_001.h5"

with h5py.File(file_path, "r") as f:
    d = f["science/SSAR/GCOV/grids/frequencyA/HHHH"]

    sample = d[0:1000, 0:1000]

    valid = sample[np.isfinite(sample)]

    print("Total pixels:", sample.size)
    print("Valid pixels:", valid.size)

    if valid.size > 0:
        print("Minimum valid value:", valid.min())
        print("Maximum valid value:", valid.max())
        print("Mean valid value:", valid.mean())
    else:
        print("No valid values found in this sample.")


# In[11]:


import h5py
import numpy as np

file_path = r"C:\Users\Ankita\Downloads\NISAR_S2_PR_GCOV_025_170_A_013_3700_DHNA_A_20260719T232918_20260719T232955_P00500_M_F_I_001.h5"

with h5py.File(file_path, "r") as f:
    d = f["science/SSAR/GCOV/grids/frequencyA/HHHH"]

    rows = [0, 8000, 16000, 24000, 32000]
    cols = [0, 8000, 16000, 24000, 33000]

    for r, c in zip(rows, cols):
        sample = d[r:r+500, c:c+500]
        valid = sample[np.isfinite(sample)]

        print(f"Position ({r}, {c}) -> Valid pixels: {valid.size}")

        if valid.size > 0:
            print("  Min:", valid.min())
            print("  Max:", valid.max())


# In[12]:


import h5py

file_path = r"C:\Users\Ankita\Downloads\NISAR_S2_PR_GCOV_025_170_A_013_3700_DHNA_A_20260719T232918_20260719T232955_P00500_M_F_I_001.h5"

with h5py.File(file_path, "r") as f:
    base = "science/SSAR/GCOV/grids/frequencyA"

    print("Projection:")
    print(f[f"{base}/projection"][()])

    print("\nX coordinate spacing:")
    print(f[f"{base}/xCoordinateSpacing"][()])

    print("\nY coordinate spacing:")
    print(f[f"{base}/yCoordinateSpacing"][()])

    print("\nX coordinates:")
    print(f[f"{base}/xCoordinates"][0:5])

    print("\nY coordinates:")
    print(f[f"{base}/yCoordinates"][0:5])


# In[13]:


from pyproj import Transformer

# Kolkata approximate centre
lat = 22.5726
lon = 88.3639

transformer = Transformer.from_crs(
    "EPSG:4326",
    "EPSG:32645",
    always_xy=True
)

x, y = transformer.transform(lon, lat)

print("Kolkata UTM X:", x)
print("Kolkata UTM Y:", y)


# In[14]:


import h5py

file_path = r"C:\Users\Ankita\Downloads\NISAR_S2_PR_GCOV_025_170_A_013_3700_DHNA_A_20260719T232918_20260719T232955_P00500_M_F_I_001.h5"

with h5py.File(file_path, "r") as f:
    base = "science/SSAR/GCOV/grids/frequencyA"

    x = f[f"{base}/xCoordinates"]
    y = f[f"{base}/yCoordinates"]

    print("X range:")
    print("Minimum:", x[0])
    print("Maximum:", x[-1])

    print("\nY range:")
    print("Maximum:", y[0])
    print("Minimum:", y[-1])


# In[15]:


import h5py
from pyproj import Transformer

file_path = r"C:\Users\Ankita\Downloads\NISAR_S2_PR_GCOV_025_170_A_013_3700_DHNA_A_20260719T232918_20260719T232955_P00500_M_F_I_001.h5"

# Kolkata centre
lat = 22.5726
lon = 88.3639

# Convert Kolkata lat/lon to NISAR projection
transformer = Transformer.from_crs(
    "EPSG:4326",
    "EPSG:32645",
    always_xy=True
)

kolkata_x, kolkata_y = transformer.transform(lon, lat)

# AOI = 20 km x 20 km
half_size = 10000  # 10 km from centre

xmin = kolkata_x - half_size
xmax = kolkata_x + half_size
ymin = kolkata_y - half_size
ymax = kolkata_y + half_size

with h5py.File(file_path, "r") as f:

    base = "science/SSAR/GCOV/grids/frequencyA"

    x = f[f"{base}/xCoordinates"]
    y = f[f"{base}/yCoordinates"]

    # Find pixel indices
    col_start = int((xmin - x[0]) / 10)
    col_end   = int((xmax - x[0]) / 10)

    row_start = int((y[0] - ymax) / 10)
    row_end   = int((y[0] - ymin) / 10)

    print("Kolkata UTM:")
    print("X =", kolkata_x)
    print("Y =", kolkata_y)

    print("\nAOI:")
    print("X:", xmin, "to", xmax)
    print("Y:", ymin, "to", ymax)

    print("\nPixel range:")
    print("Rows:", row_start, "to", row_end)
    print("Columns:", col_start, "to", col_end)

    print("\nSubset size:")
    print("Rows:", row_end - row_start)
    print("Columns:", col_end - col_start)


# In[17]:


import h5py
import numpy as np
import rasterio
from rasterio.transform import from_origin

file_path = r"C:\Users\Ankita\Downloads\NISAR_S2_PR_GCOV_025_170_A_013_3700_DHNA_A_20260719T232918_20260719T232955_P00500_M_F_I_001.h5"

output_file = r"C:\Users\Ankita\Downloads\NISAR_Kolkata_HHHH.tif"

row_start = 17946
row_end = 19946
col_start = 11397
col_end = 13397

with h5py.File(file_path, "r") as f:

    base = "science/SSAR/GCOV/grids/frequencyA"

    d = f[f"{base}/HHHH"]

    subset = d[row_start:row_end, col_start:col_end]

    x = f[f"{base}/xCoordinates"]
    y = f[f"{base}/yCoordinates"]

    xmin = float(x[col_start])
    ymax = float(y[row_start])

print("Subset shape:", subset.shape)
print("Upper-left X:", xmin)
print("Upper-left Y:", ymax)

subset = np.where(
    np.isfinite(subset),
    subset,
    -9999
).astype("float32")

transform = from_origin(
    xmin,
    ymax,
    10,
    10
)

with rasterio.open(
    output_file,
    "w",
    driver="GTiff",
    height=subset.shape[0],
    width=subset.shape[1],
    count=1,
    dtype="float32",
    transform=transform,
    nodata=-9999
) as dst:

    dst.write(subset, 1)

print("GeoTIFF created successfully!")
print(output_file)


# In[ ]:




