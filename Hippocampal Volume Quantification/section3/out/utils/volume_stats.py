"""
Contains various functions for computing statistics over 3D volumes
"""
import numpy as np

def Dice3d(a, b):
    """
    This will compute the Dice Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks -
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Dice3D. If you completed exercises in the lessons
    # you should already have it.
    # <YOUR CODE HERE>
    a1 = (a == 1).astype(np.int)
    b1 = (b == 1).astype(np.int)
    intersection1 = np.sum(a1*b1)
    volumes1 = np.sum(a1) + np.sum(b1)
    dsc1 = -1
    if volumes1 > 0:
        dsc1 = 2.*float(intersection1) / float(volumes1)

    a2 = (a == 2).astype(np.int)
    b2 = (b == 2).astype(np.int)
    intersection2 = np.sum(a2*b2)
    volumes2 = np.sum(a2) + np.sum(b2)
    dsc2 = -1
    if volumes2 > 0:
        dsc2 = 2.*float(intersection2) / float(volumes2)
    dsc = (dsc1 + dsc2) / 2
    return dsc

def Jaccard3d(a, b):
    """
    This will compute the Jaccard Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Jaccard similarity coefficient. Please do not use 
    # the Dice3D function from above to do the computation ;)
    # <YOUR CODE GOES HERE>

    a1 = (a == 1).astype(np.int)
    b1 = (b == 1).astype(np.int)
    intersection1 = np.sum(a1*b1)
    union1 = np.sum(a1) + np.sum(b1) - intersection1
    jsc1 = -1
    if union1 > 0:
        jsc1 = float(intersection1) / float(union1)

    a2 = (a == 2).astype(np.int)
    b2 = (b == 2).astype(np.int)
    intersection2 = np.sum(a2*b2)
    union2 = np.sum(a2) + np.sum(b2) - intersection2
    jsc2 = -1
    if union2 > 0:
        jsc2 = float(intersection2) / float(union2)
    jsc = (jsc1 + jsc2) / 2

    return jsc