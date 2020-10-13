
D=[2 0 0;0 2 0;0 0 2];
Dp=D^-1;

L=[0 -1  1 ;0  0  2 ;0 0 0];

U= [0 0 0; 2 0 0;-1 -1 0];

A=Dp*(L+U);

eigen= eig(A);

ratioConv = max(abs(eigen));

fprintf("Jacobi p radius:: " + ratioConv);




