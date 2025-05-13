import numpy as np 
from pathlib import Path
from enum import Enum 


N_F = 8
N_M = 49
def load_file( filename : str | Path):
    folder = Path('../Fresnel_Data')
    file_route = folder / filename
    data = np.loadtxt(fname=file_route,skiprows=10)
    shape = (N_F, N_M, N_E)
    U_inc = ( data[:,3] - 1j*data[:,4]).reshape(shape,order="F")
    U_tot = ( data[:,5] - 1j*data[:,6]).reshape(shape,order="F")
    A_near = U_tot - U_inc
    r_ID = data[:,1].astype(int).reshape(shape,order="F") - 1
    A = np.zeros((N_F,N_R, N_E), dtype=np.complex128)
    U = np.zeros((N_F,N_R, N_E), dtype=np.complex128)
    for f in range(N_F):
        for e in range(N_E):
            A[f,r_ID[f,:,e],e] = A_near[f,:,e]
            U[f,r_ID[f,:,e],e] = U_inc[f,:,e]

    return A, U
