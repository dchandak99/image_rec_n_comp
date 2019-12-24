import numpy as np
def reconstruct_from_noisy_patches(input_dict, shape):
    """
    input_dict: 
    key: 4-tuple: (topleft_row, topleft_col, bottomright_row, bottomright_col): location
     of the patch
    in the original image. topleft_row, topleft_col are inclusive but bottomright_row, bottomright_col 
    are exclusive. i.e. if M is the reconstructed matrix.
    M[topleft_row:bottomright_row, topleft_col:bottomright_col]will give the patch.

    value: 2d numpy array: the image patch.

    shape: shape of the original matrix.
    """
    # Initialization: Initialise M, black_count, mid_count, white_count, mid_total
    M=np.zeros(shape,dtype=int)
    black_count=np.zeros(shape,dtype=int)
    mid_count=np.zeros(shape,dtype=int)
    white_count=np.zeros(shape,dtype=int)
    mid_total=np.zeros(shape,dtype=int)
    appear=np.zeros(shape,dtype=int)
    
    for topleft_row, topleft_col, bottomright_row, bottomright_col in input_dict: # no loop except this!
        tlr, tlc, brr, brc = topleft_row, topleft_col, bottomright_row, bottomright_col
        patch = input_dict[(tlr, tlc, brr, brc)]
        black= np.copy(patch==0)
        white = np.copy(patch==255)
        mid1=np.copy(patch>0)
        mid2=np.copy(patch<255)
        mid = np.multiply(mid1,mid2)
        patchc=np.copy(patch)

        appear[tlr:brr,tlc:brc]=1
        
        black_count[tlr:brr,tlc:brc]=black+black_count[tlr:brr,tlc:brc]
        white_count[tlr:brr,tlc:brc]=white+white_count[tlr:brr,tlc:brc]
        mid_count[tlr:brr,tlc:brc]=mid+mid_count[tlr:brr,tlc:brc]
        mid_total[tlr:brr,tlc:brc]=patchc*mid+mid_total[tlr:brr,tlc:brc]
        
        # change black_count, mid_count, white_count, mid_total here
    # Finally change M here
    mid_bool=mid_count!=0
    mid_notbool=mid_count==0
    M[mid_bool]=np.around(mid_total[mid_bool]/mid_count[mid_bool],decimals=0)

    not_app=appear!=0

    black_minus_white=np.subtract(black_count,white_count)
    bo_in=black_minus_white<=0
    bo_in_final=np.multiply(bo_in,mid_notbool)
    fin=np.multiply(bo_in_final,not_app)
    M[fin]=255

    return M # You have to return the reconstructed matrix (M).

