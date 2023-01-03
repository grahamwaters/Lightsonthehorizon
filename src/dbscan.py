import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import pdist, squareform

# Read in the data
df = pd.read_csv("./data/processed/ufos_processed.csv", low_memory=False, on_bad_lines= 'skip')

# Convert the latitude and longitude to radians
df['latitude_rad'] = np.radians(df['latitude'])
df['longitude_rad'] = np.radians(df['longitude'])

# Convert the latitude and longitude to cartesian coordinates
df['x'] = np.cos(df['latitude_rad']) * np.cos(df['longitude_rad']) # x = r * cos(lat) * cos(long)
df['y'] = np.cos(df['latitude_rad']) * np.sin(df['longitude_rad']) # y = r * cos(lat) * sin(long)
df['z'] = np.sin(df['latitude_rad']) # z = r * sin(lat)

# Create a matrix of the x, y, and z coordinates
X = df[['x', 'y', 'z']].values

print(f'The shape of the matrix is: {X.shape}')
# Scale the data to have a mean of 0 and a standard deviation of 1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f'Calculating the distance matrix...')
# Calculate the condensed distance matrix
distances = pdist(X_scaled)

# Calculate the distance to the kth nearest neighbor for each point
k = 5
print(f'Calculating the distance to the {k}th nearest neighbor for each point...')
neigh = NearestNeighbors(n_neighbors=k)
nbrs = neigh.fit(X_scaled)
distances_k, indices_k = nbrs.kneighbors(X_scaled)
distances_k = distances_k[:, k-1]

# Plot a histogram of the distances to the kth nearest neighbor
plt.hist(distances_k, bins=50)
plt.xlabel('Distance')
plt.ylabel('Frequency')
plt.title('Histogram of Distances to the 5th Nearest Neighbors')
# save the figure as a .png file in the project_folder/reports folder with the name 'knn_histogram.png'
plt.savefig('./reports/knn_histogram.png')
plt.show()

# Choose a value for eps
eps = 0.5

# Run the DBSCAN algorithm
db = DBSCAN(eps=eps, min_samples=2, metric='precomputed')
db.fit(squareform(distances))

# Calculate the silhouette score
score = silhouette_score(squareform(distances), db.labels_)

# Calculate the Calinski-Harabasz score
score = calinski_harabasz_score(squareform(distances), db.labels_)

# Print the cluster labels
print(db.labels_)