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


frequencies = {FresnelFile.TWO_DIEL4 : np.linspace(4,16,4), 
         FresnelFile.TWO_DIEL8 : np.linspace(1,8,8),
         FresnelFile.U         : np.linspace(2,16,8),
         FresnelFile.ONE_DIEL4 : np.linspace(4,16,4),
         FresnelFile.ONE_DIEL8 : np.linspace(1,8,8),
         FresnelFile.RECT_OFF  : np.linspace(2,16,8),
         FresnelFile.RECT_CENT : np.linspace(4,16,4)}



N_E = 36
N_M = 49
N_R = 72


def load_file( filename : FresnelFile | str, folder = Path('./Data'), 
              positive_exponent = True, 
              zero_completed = True,
              verbose = False):
    """
    """

    if isinstance(filename,str):
        filename = FresnelFile(filename)

    folder = Path(folder)

    file_route = folder / filename.value
    
    f = frequencies[filename]*1E9

    N_F = len(f)

    if verbose:
        print(f"loading file {filename} located at {filename.value},\n with frecuencies:\n")
        print(", ".join([f'{v:.1f} GHz' for v in frequencies[filename]] ))
    
    data = np.loadtxt(fname=file_route,skiprows=10)
    shape = (N_F, N_M, N_E)
    U_inc = ( data[:,3] - 1j*data[:,4]).reshape(shape,order="F")
    U_tot = ( data[:,5] - 1j*data[:,6]).reshape(shape,order="F")
    
    if positive_exponent:
        U_inc = np.conjugate(U_inc)
        U_tot = np.conjugate(U_tot)

    A_near = U_tot - U_inc
    r_ID = data[:,1].astype(int).reshape(shape,order="F") - 1
    A = np.zeros((N_F,N_R, N_E), dtype=np.complex128)
    U = np.zeros((N_F,N_R, N_E), dtype=np.complex128)
   
    if zero_completed:
        for f in range(N_F):
            for e in range(N_E):
                A[f,r_ID[f,:,e],e] = A_near[f,:,e]
                U[f,r_ID[f,:,e],e] = U_inc[f,:,e]

    return A, U, f

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--verbose', action="store_true")
    parser.add_argument(
        "--file",
        type=str,
        choices=[f.value for f in FresnelFile],  # shows up in help
        help=f"Choose a file from: {[f.value for f in FresnelFile]}")


    args = parser.parse_args()
    
    A, U, f =  load_file(args.file, verbose=args.verbose)
