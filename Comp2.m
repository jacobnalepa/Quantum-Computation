%%PART A%%

%Defining the incoming state.
z=[1,0]';
%Defining the relative angle between each Stern-Gerlach device
theta=pi/4;
%Defines the first Stern-Gerlach Device, SGz.
SGz=[cos(0),sin(0);,0,0];
%Calculates the probability of the +z state passing through a SGz device
% out of the +z side and initializes the total probability as 1.
P_total=(SGz*z)'*(SGz*z);

%This loop updates the total probability of transmission through the series
%of 2 SGn devices following the 1 SGz device.
for i=1:2
    SGn=[cos(theta/2),sin(theta/2);0,0];
    P=(SGn*z)'*(SGn*z);
    P_total=P_total*P;
end
fprintf('The probability for part A is : %.4f\n', P_total);

%%Part B%%

%Defining the relative angle between each Stern-Gerlach device
theta=pi/58;
%Calculates the probability of the +z state passing through the first of 30
%Stern Gerlach devices, an SGz device. Also initializes the total 
%probability as 1.
P_total=(SGz*z)'*(SGz*z);

%This loop updates the total probability of transmission through the series
%of 29 SGn devices following the 1 SGz device.
for i=1:29
    SGn=[cos(theta/2),sin(theta/2);0,0];
    P=(SGn*z)'*(SGn*z);
    P_total=P_total*P;
end
fprintf('The probability for part B is : %.4f\n', P_total);

%%Part C%%

%Calculates the probability of the +z state passing through the first of a
%series of Stern Gerlach devices, an SGz device. Also initializes the 
%total probability as 1.
P_total=(SGz*z)'*(SGz*z);

%Sets the first rotated Stern-Gerlach device to an angle of 2 degrees from
%the z axis.
theta=2;

%This loop updates the total probability of transmission through the series
%of 12 SGn devices following the 1 SGz device.
for i=1:12
    SGn=[cos(deg2rad(theta)/2),sin(deg2rad(theta)/2);0,0];
    P=(SGn*z)'*(SGn*z);
    P_total=P_total*P;
    theta=theta+1;
end
fprintf('The probability for part C is : %.4f\n', P_total);



