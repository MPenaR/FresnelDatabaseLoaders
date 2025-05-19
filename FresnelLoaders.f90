module FresnelLoaders

        integer, parameter :: N_E = 36
        integer, parameter :: N_R = 72
        integer, parameter :: N_M = 49

        contains

                function read_Fresnel( folder, file, N_F ) result(A)
                        character(len=*), intent(in) :: folder 
                        character(len=*), intent(in) :: file 
                        real :: A(N_F,N_R,N_E)

                        A = 0
                end function



end module
