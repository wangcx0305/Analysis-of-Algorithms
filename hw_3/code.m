%%%%%%%%%%%Question 1%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

x = [1, 2, 3, 5, 7, 8, 10]';
y = [3, 5, 7, 11, 14, 15, 19]';
A1 = [x, ones(7, 1), -ones(7, 1)];
A2 = [-x, -ones(7, 1), -ones(7, 1)];
c = zeros(3, 1);
c(3) = 1;
A = [A1; A2];
a = [y; -y];

[xsol, fval, exitflag] = linprog(c, A, a);

plot(x, y, 'r*');
xlabel('x');
ylabel('y');
title('Question 1');
hold on 
xx = 0:0.5:10;
yx = xsol(1) * xx + xsol(2);
plot(xx, yx, '-k', 'LineWidth', 2);


%%%%%%%%%%%Question 2%%%%%%%%%%%%%%%%%%%%%%%%%%

d = csvread('day.csv');
t = csvread('temp.csv');
size(d); %22304
A1 = [ones(22304, 1), d, cos(2 * pi * d / 365.25), sin(2 * pi * d / 365.25), ...
       cos(2 * pi * d / (365.25 * 10.7)), sin(2 * pi * d / (365.25 * 10.7)), ...
       -ones(22304, 1)];

A2 = [-ones(22304, 1), -d, -cos(2 * pi * d / 365.25), -sin(2 * pi * d / 365.25), ...
       -cos(2 * pi * d / (365.25 * 10.7)), -sin(2 * pi * d / (365.25 * 10.7)), ...
       -ones(22304, 1)];
c = zeros(7, 1);
c(7) = 1;
A = [A1; A2];
a = [t; -t];


[xsol, fval, exitflag] = linprog(c, A, a)

plot(d, t, 'r*');
xlabel('day');
ylabel('temp');
title('Corvallis temp vs day');
hold on
td = xsol(1) + xsol(2) * d + xsol(3) * cos(2 * pi * d / 365.25) + ...
     xsol(4) * sin(2 * pi * d / 365.25) + xsol(5) * cos(2 * pi * d / (365.25 * 10.7)) + ...
     xsol(6) * sin(2 * pi * d / (365.25 * 10.7));
      
plot(d, td, '-k', 'LineWidth', 2);
hold on
tld = xsol(1) + xsol(2) * d;
plot(d, tld, '-k', 'LineWidth', 2);

change = xsol(2) * 365.25 * 100

%%%%%%%%%%%%%%%%%%%%Bonus%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
d = csvread('day_salem.csv');
t = csvread('temp_salem.csv');
size(d); %20820
A1 = [ones(20820, 1), d, cos(2 * pi * d / 365.25), sin(2 * pi * d / 365.25), ...
       cos(2 * pi * d / (365.25 * 10.7)), sin(2 * pi * d / (365.25 * 10.7)), ...
       -ones(20820, 1)];

A2 = [-ones(20820, 1), -d, -cos(2 * pi * d / 365.25), -sin(2 * pi * d / 365.25), ...
       -cos(2 * pi * d / (365.25 * 10.7)), -sin(2 * pi * d / (365.25 * 10.7)), ...
       -ones(20820, 1)];
c = zeros(7, 1);
c(7) = 1;
A = [A1; A2];
a = [t; -t];


[xsol, fval, exitflag] = linprog(c, A, a)

plot(d, t, 'r*');
xlabel('day');
ylabel('temp');
title('Salem temp vs day');
hold on
td = xsol(1) + xsol(2) * d + xsol(3) * cos(2 * pi * d / 365.25) + ...
     xsol(4) * sin(2 * pi * d / 365.25) + xsol(5) * cos(2 * pi * d / (365.25 * 10.7)) + ...
     xsol(6) * sin(2 * pi * d / (365.25 * 10.7));
      
plot(d, td, '-k', 'LineWidth', 2);
hold on
tld = xsol(1) + xsol(2) * d;
plot(d, tld, '-k', 'LineWidth', 2);

change = xsol(2) * 365.25 * 100

