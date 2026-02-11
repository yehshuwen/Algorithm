#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SHU-WEN YEH


# Function to perform Kruskal's algorithm for single link k-clustering
def greedy_clustering_kruskal(distance_matrix, k):
    n = len(distance_matrix)

    # (weight, u, v)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append((distance_matrix[i][j], i, j))

    edges.sort()

    parent = list(range(n))
    size = [1]*n
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry  = find(x), find(y)
        if rx == ry: return False
        if size[rx] < size[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        size[rx]  += size[ry]
        return True
    
    components = n
    for w, u, v in edges:
        if components == k:
            break
        if union(u, v):
            components -= 1

    clusters = {}
    for node in range(n):
        r = find(node)
        clusters.setdefault(r, []).append(node)

    return list(clusters.values())  # Return the clusters


# Use this input 
distance_matrix = [
    [0, 38, 17, 28, 88, 59, 13],
    [38, 0, 52, 49, 83, 91, 59],
    [17, 52, 0, 46, 34, 77, 80],
    [28, 49, 46, 0, 5, 53, 62],
    [88, 83, 34, 5, 0, 43, 33],
    [59, 91, 77, 53, 43, 0, 27],
    [13, 59, 80, 62, 33, 27, 0]
]

# Set k=2 for number of clusters
k = 2  
clusters = greedy_clustering_kruskal(distance_matrix, k)

# Print the resulting clusters
print("Resulting Clusters:", clusters)