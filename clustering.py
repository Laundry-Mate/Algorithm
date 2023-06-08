import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def color_clustering(dataset):
    # Extract the HSV color values
    hsv_data = dataset[['h', 's', 'v']]

    # Perform clustering with 1 cluster
    kmeans_1 = KMeans(n_clusters=1, random_state=42)
    cluster_labels_1 = kmeans_1.fit_predict(hsv_data)

    try:
        silhouette_score_1 = silhouette_score(hsv_data, cluster_labels_1)
    except ValueError:
        silhouette_score_1 = -1.0  # Set a low silhouette score for 1 cluster

    # Perform clustering with 2 clusters
    kmeans_2 = KMeans(n_clusters=2, random_state=42)
    cluster_labels_2 = kmeans_2.fit_predict(hsv_data)
    silhouette_score_2 = silhouette_score(hsv_data, cluster_labels_2)

    # Determine the optimal number of clusters
    if silhouette_score_1 > silhouette_score_2:
        num_clusters = 1
        cluster_labels = cluster_labels_1
    else:
        num_clusters = 2
        cluster_labels = cluster_labels_2

    # Add the cluster labels to the dataset
    dataset['cluster'] = cluster_labels

    # Visualize the clusters
    plt.figure(figsize=(8, 6))

    # Plot the clusters
    for cluster in range(num_clusters):
        cluster_points = hsv_data[cluster_labels == cluster]
        color = 'red' if cluster == 0 else 'blue'  # Change dot color based on cluster result
        plt.scatter(cluster_points['s'], cluster_points['v'], c=color,
                    label=f'Cluster {cluster + 1}')

    plt.xlabel('Saturation')
    plt.ylabel('Value')
    plt.title('HSV Color Clustering')
    plt.legend()
    plt.show()

    basket_0 = []
    basket_1 = []

    print("Cluster Results:")
    for index, row in dataset.iterrows():
        print(f"Data point {index}: Cluster {row['cluster']} - Fabric Type: {row['fabric_type']}")
        if row['cluster'] == 0:
            basket_0.append(row)
        else:
            basket_1.append(row)

    basket_0_df = pd.DataFrame(basket_0)
    basket_1_df = pd.DataFrame(basket_1)

    basket_0_df.to_csv('basket_0.csv', index=False)
    basket_1_df.to_csv('basket_1.csv', index=False)