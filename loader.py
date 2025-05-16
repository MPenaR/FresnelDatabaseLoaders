import numpy as np 
from pathlib import Path
from enum import Enum
#from collections import namedtuple




# list of original filenames
class FresnelFile(Enum):
    U = "uTM_shaped.txt"
    ONE_DIEL8 = "dielTM_dec8f.txt"
    ONE_DIEL4 = "dielTM_dec4f.txt"
    RECT_CENT = "rectTM_cent.txt"
    RECT_OFF  = "rectTM_dece.txt"
    TWO_DIEL8 = "twodielTM_8f.txt"
    TWO_DIEL4 = "twodielTM_4f.txt"


freqs = {FresnelFile.TWO_DIEL4 : 4, 
         FresnelFile.TWO_DIEL8 : np.linspace(1,8,8),
         FresnelFile.U         : np.linspace(2,16,8),
         FresnelFile.ONE_DIEL4 : 4,
         FresnelFile.ONE_DIEL8 : 8,
         FresnelFile.RECT_OFF  : 8,
         FresnelFile.RECT_CENT : 4}



N_E = 36
N_M = 49
N_R = 72


def load_file( filename : FresnelFile, folder = Path('./Data') ):
    file_route = folder / filename.value

# with open(file_route) as f:
#         for n in range(5):
#             line = f.readline()
#    freq_info = line.split(" : ")[1].split(" ")
#     N_F = int(freq_info[0])
#    print(freq_info)
    print(freqs[filename])


    N_F = len(freqs[filename])

    print(f"loading file {filename} located at {filename.value}, with {N_F} frecuencies ... ")
    
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

if __name__ == "__main__":
    load_file(FresnelFile.U)
