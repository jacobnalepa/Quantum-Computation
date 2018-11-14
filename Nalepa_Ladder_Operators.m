%Finds the overlap between any two states, for any ladder operator input.

%Initializes an 's by s' matrix of zeros for the x operator matrix.
s=100;
x = zeros(s);
i=sqrt(-1);

%Fills the in values to create the x operator matrix, m = w = hbar = 1.
for c = 1:s
    x(c,c+1) = sqrt(c);
end

for c = 1:s
    x(c+1,c) = sqrt(c);
end

x = sqrt(0.5).*x;

%Initializes an 's by s' matrix of zeros for the p operator matrix.
p = zeros(s);

%Fills in values to create the p operator matrix, m = w = hbar = 1.
for c = 1:s
    p(c,c+1) = sqrt(c);
end

for c = 1:s
    p(c+1,c) = -sqrt(c);
end
p = -i.*sqrt(0.5).*p;

%Creates a matrix containg all of the vectors for each possible state.
%The jth column corresponds to psi_(j-1); The first column is psi_0.
psi_n = eye(s+1);

%Prompts the user to enter the states and operator.
prompt = 'What is the value of m? ';
m = input(prompt);
prompt = 'What is the value of n? ';
n = input(prompt);
prompt = 'What is ladder operator? (ex: x^2, p^2, x^2*p^2) ';
op = input(prompt);

%Calculates and displays the desired overlap
overlap = psi_n(:,m+1)'*op*psi_n(:,n+1);
fprintf('The overlap is: %.4f\n', overlap);



