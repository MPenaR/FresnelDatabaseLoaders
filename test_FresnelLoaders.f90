program test_fresnel

        use FresnelLoaders, only: read_Fresnel, N_R, N_E

        integer, parameter :: N_F = 8
        
        real :: A(N_F,N_R,N_E)

        A = read_Fresnel("./Data/", "uTM_shaped.txt", N_F)


end program test_fresnel

