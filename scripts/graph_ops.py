import numpy as np

"""
Graph operations
"""

def connection_matrix(A : np.typing.NDArray[np.float64], k : int):
    """
    Args:
        A (np.typing.NDArray[np.float64]): adjacency matrix
        k (int): length of the walk
    """
    
    if len(A.shape) != 2:
        raise ValueError("Input must be a 2D array")
    if A.shape[0] != A.shape[1]:
        raise ValueError("Input must be a square matrix")
    n = A.shape[0]
    
    B_k = ((np.linalg.matrix_power(A,k) + np.identity(n))>1).astype(np.float64) - np.identity(n)
    
    return B_k

def connection_matrix_l(A : np.typing.NDArray[np.float64], l : int):
    """
    Args:
        A (np.typing.NDArray[np.float64]): adjacency matrix
        l (int): max length of the walk
    """
    if len(A.shape) != 2:
        raise ValueError("Input must be a 2D array")
    if A.shape[0] != A.shape[1]:
        raise ValueError("Input must be a square matrix")
    n = A.shape[0]

    B_1_l = np.zeros_like(A)
    for i in range(1,l+1):
        B_1_l += connection_matrix(A,i)
    B_1_l = (B_1_l>1).astype(np.float64)
    return B_1_l


    
    

    
    
    


