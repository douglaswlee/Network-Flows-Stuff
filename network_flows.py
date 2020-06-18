import numpy as np

def make_adjmatrix_from_edgelist(n_vertices, edges, directed=True):
    '''
        Given:
            n_vertices, the number of vertices in the network,
            edges, an edge list dictionary representing the network
            directed, a flag denoting whether the network is directed or not
        Return:
            an n_vertices x n_vertices adjacency matrix representation of the same network as edges
    '''
    # initialize adjacency matrix as n_vertices x n_vertices array of zeros
    adj = np.zeros([n_vertices, n_vertices])
    
    # iterate through edge list to populate adjacency matrix
    for e, w in edges.items():
        adj[e[0], e[1]] = w
        
    # symmetrize and return adjacency matrix if undirected else return as-is 
    return adj + np.tril(adj.T) if not directed else adj

def make_edgelist_from_adjmatrix(adj, directed=True):
    '''
        Given:
            adj, an adjacency matrix representation of the network
            directed, a flag denoting whether the network is directed or not
        Return:
            edgelist, an edge list dicitonary representing a network of the same network as adj
    '''
    # initialize an empty edge list
    edgelist = {}
    
    # get edges from indices of non-zero elements of the adjacency matrix
    # if directed, look at all non-zero elements, else all non-zero in upper triangular adjacency matrix
    if directed:
        indices = np.nonzero(adj)
    else:
        indices = np.nonzero(np.triu(adj))
    
    # populate edge list
    for e1, e2 in zip(indices[0].tolist(), indices[1].tolist()):
        edgelist[(e1, e2)] = adj[e1, e2]
    return edgelist