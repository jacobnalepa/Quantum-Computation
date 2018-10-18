%%PART A%%

%Defining the incoming state.
z=[1,0]';
%Defining the outgoing state.
x=[1/sqrt(2),1/sqrt(2)];

%Initializes the equivalent matrix for the total of the Stern-Gerlach 
%devices as an identity matrix.
SGtotal=[1,0;0,1];

%This loop creates a matrix that is equivalent to three Stern-Gerlach
%devices in a series, such that each succesive device is rotated by pi/4 
%from angle 0 to pi/2.
for theta=0:pi/4:pi/2
    SGn=[cos(theta/2),sin(theta/2);0,0];
    SGtotal=SGn*SGtotal;
end
AmplitudeA=x*SGtotal*z;
ProbabilityA=(AmplitudeA)^2;
fprintf('The probability for part A is : %.4f\n', ProbabilityA);

%%PART B%%

%Re-initializes the equivalent matrix for the total of the Stern-Gerlach 
%devices as an identity matrix so that the three SG devices from part A are
%not added to the 30 SG devices from part B.
SGtotal=[1,0;0,1];

%This loop creates a matrix that is equivalent to thirty Stern-Gerlach
%devices in a series, such that each succesive device is rotated
%incrementally from angle 0 to pi/2.
for theta=0:pi/58:29*pi/58
    SGn=[cos(theta/2),sin(theta/2);0,0];
    SGtotal=SGn*SGtotal;
end
AmplitudeB=x*SGtotal*z;
ProbabilityB=(AmplitudeB)^2;
fprintf('The probability for part B is : %.4f\n', ProbabilityB);

%%PART C%%

%Re-initializes the equivalent matrix for the total of the Stern-Gerlach 
%devices as an identity matrix so that Part A and B do not affect part C.
SGtotal=[1,0;0,1];

%This loop creates a matrix that is equivalent to 13 consecutive Stern-
%Gerlach devices progressively rotated from angle 0 to pi/2 where their 
%individual angles are given by the sequence 0,2,5,9,...90.
theta=-1; 
n=0; %initial conditions for the recurrence relation.
while n<13
theta=theta+n+1; %Recurrene relation for the sequence described above
SGn=[cos(deg2rad(theta/2)),sin(deg2rad(theta/2));0,0];
SGtotal=SGn*SGtotal;
n=n+1;
end
AmplitudeC=x*SGtotal*z;
ProbabilityC=(AmplitudeC)^2;
fprintf('The probability for part C is : %.4f\n', ProbabilityC);
