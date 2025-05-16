function [ u_inc, u_sc, r_map, f ] = read_Fresnel(fileroute)
    % [ u_inc, u_sc, r_map, f ] = read_Fresnel(fileroute)
    % Reads a file from the Fresnel database at location "fileroute"
    % returns: 
    % - u_inc: N_F x N_M x N_E complex array with the incident field
    % - u_sc:  N_F x N_M x N_E complex array with the scattered field
    % - r_map:  N_M x N_E  integer array with the index of the receiving antenna
    % - f: N_F real array with the frequencies

    file_ID=fopen(fileroute); 
    for n=1:4
        line = fgetl(file_ID);
    end
    line = fgetl(file_ID);
    fclose(file_ID);
    
    N_F = str2num(line(27));


    N_E = 36;
    N_M = 49;

    
    [e_ID, r_map, f, uR, uI, u_incR, u_incI] = textread(fileroute,'%d %d %d %f %f %f %f','headerlines',10);
    shape = [ N_F, N_M, N_E]; 

    r_map = reshape(r_map, shape);
    f = reshape(f,shape);
    u = reshape(uR - 1j*uI, shape);
    u_inc = reshape(u_incR - 1j*u_incI, shape);
    u_sc = u - u_inc;
    f = double(f(:,1,1))*1E9;
    r_map = squeeze(r_map(1,:,:));
end 
