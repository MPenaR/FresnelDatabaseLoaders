function [F_full] = complete_with_zeros(F, r_map)
    % [F_full] = complete_with_zeros(F, r_map)
    % Given the partial data in F  ( N_F x N_M x N_E) completes the array to 
    % form a ( N_F x N_M x N_E) array where the missing data is set to zero.
    % Inputs:
    % - F: ( N_F x N_M x N_E) complex array containing the partial data
    % - r_map: (N_M x N_E) integer array maping each data to its global index
    % Outputs:
    % - F_full: ( N_F x N_R x N_E) complex array containing the zero-extrapolated data

    N_F = size(F,1);
    N_E = size(F,3);
    N_R = 2*N_E;
    N_M = size(F,2);
    
    F_full = zeros(N_F,N_R,N_E);
    for f_ID=1:N_F
        for e_ID=1:N_E
            for r_ID=1:N_M
                F_full( f_ID, r_map( r_ID, e_ID ), e_ID) = F(f_ID,r_ID,e_ID);
            end 
        end 
    end 
end 
