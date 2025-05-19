FC=gfortran -c
FL=gfortran

FresnelLoaders.o : FresnelLoaders.f90
	$(FC) $<
test_FresnelLoaders.o : test_FresnelLoaders.f90 FresnelLoaders.o
	$(FC) $<
test_FresnelLoaders : test_FresnelLoaders.o FresnelLoaders.o
	$(FL) $^ -o $@

.PHONY: clean

clean:
	rm *.o *.mod
