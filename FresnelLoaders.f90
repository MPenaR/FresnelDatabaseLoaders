module FresnelLoaders

        implicit none

        integer, parameter :: N_E = 36
        integer, parameter :: N_R = 72
        integer, parameter :: N_M = 49

        contains

                function read_Fresnel( folder, file, N_F ) result(NF)
                        character(len=*), intent(in) :: folder 
                        character(len=*), intent(in) :: file 
                        integer, intent(in) :: N_F
                        complex :: NF(N_F,N_R,N_E)
                        
                        integer :: f_unit, io_stat, n_records, i
                        character(len=:), allocatable :: file_route
                        real :: data(N_M*N_F*N_E, 4), tmp
                        complex :: A(N_F, N_M, N_E), U(N_F, N_M, N_E)

                        file_route = folder // file 
                        print*, "reading ", file_route, " ..."
                        open( file=file_route, status="old", action="read", newunit=f_unit, iostat=io_stat )
                        if (io_stat == 0) print*, "in unit ", f_unit

                        do i = 1, 10
                                read(unit=f_unit,fmt=*)
                        end do

                        n_records = N_F*N_M*N_E
                        do i = 1, n_records
                                read(unit=f_unit, fmt=*) tmp, tmp, tmp, data(i,1), data(i,2), data(i,3), data(i,4)
                        end do

                        U = cmplx( reshape( data(:,1), shape=[N_F,N_M,N_E]), -reshape( data(:,2), shape=[N_F,N_M,N_E]) )
                        A = cmplx( reshape( data(:,3), shape=[N_F,N_M,N_E]), -reshape( data(:,4), shape=[N_F,N_M,N_E]) )

                        






                end function



end module
