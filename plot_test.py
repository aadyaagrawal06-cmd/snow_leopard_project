import pandas as pd
import rasterio
import numpy as np
import matplotlib.pyplot as plt

# 1. Load occurrence data
pts = pd.read_csv("data/occurrences_thinned.csv")
print(len(pts), "points")

# 2. Open raster dataset
with rasterio.open("data/bio/wc2.1_10m_bio_1.tif") as src:
    arr = src.read(1, masked=True)
    ext = [src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top]

print("Raster shape:", arr.shape)

# 3. Clean masked nodata values for Matplotlib
arr_clean = arr.filled(np.nan)

# 4. Plot map
fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(arr_clean, extent=ext, cmap="coolwarm")

ax.scatter(pts["decimalLongitude"], pts["decimalLatitude"], s=8, c="black")
ax.set_xlim(65, 110)
ax.set_ylim(25, 50)
ax.set_title("Snow leopard records on mean annual temperature")

fig.colorbar(im, label="Mean annual temperature (°C)")
fig.savefig("first_map.png", dpi=100)
print("saved successfully!")