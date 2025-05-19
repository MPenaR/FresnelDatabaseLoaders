# FresnelDatabaseLoaders
A repository with a couple of loaders in different languages for the [Institut Fresnel two dimensional experimental database](https://iopscience.iop.org/article/10.1088/0266-5611/17/6/301). The original files can be downloaded from the sumplementary data section. 

In [1] all the signals are assumed to have time-harmonic dependency, i.e. $u(\mathbf{x},t)=U(\mathbf{x})e^{i\omega t}$. However. to the best of oure knowledege, a time dependency of the form $e^{-i\omega t}$ seems to be more popular, hence in this loaders all the measurements are conjugated by default. 

## Python

The python loader returns two `numpy.NDarray`  objects containing the incident field and the scattered field per each batch of experiments.


## MATLAB

### GNU-Octave
All the MATLAB code is also valid for octave, with the exception that octave has no implementation of a `pdist2`function.


## Fortran


## References

1. Belkebir H., Saillard M. 2001 Special section: Testing inversion algorithms against experimental data. _Inverse problems_ 17 1565-1571 




