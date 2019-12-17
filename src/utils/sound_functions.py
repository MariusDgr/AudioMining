import numpy as np

def range_map(x, inp_range, out_range):
    return (x - inp_range[0]) * (out_range[1] - out_range[0]) / (inp_range[1] - inp_range[0]) + out_range[0]

def add_tow_samples(s1, s2, padding="right", padding_value=0):
    """Add vectors s1 and s2
    Is used to overlap two signals
    When one sample is longer than the other, the shorter vectr is padded.
    
    Args: 
        s1: first vector
            array-like
        s2: second vector
            array-like
        padding: Specifies if padding should be added to the left or to the right
            "right"(default), "left"  
        padding_value: specifies the value of the padding 
            0 (default) adds zero vector to left or right

    """
    pass

def mix_samples(samples_list):
    """Add up the vectors given as input to generate mixed samples.
    The samples need to have the same sampling rate."""
    pass
