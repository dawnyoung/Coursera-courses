%% Fundamentals of digital image and video processing

%% week 4

%% question 3

b1 = [1 1 2 2;
    1 1 2 2;
    2 2 3 4;
    2 2 5 6];
b2 = [2 2 1 1;
    2 2 2 2;
    2 2 6 4;
    2 2 5 3];

mse = sum((b1(:)-b2(:)).^2)/prod(size(b1));

%% question 4

clear;clc;

bx = [10 20 10 10;
    20 40 10 10;
    30 40 20 20;
    50 60 20 20];
b1 = [10 20 10 10;
    20 40 10 10;
    20 20 30 40;
    20 20 50 60];
b2 = [20 30 20 20;
    30 50 20 20;
    40 50 30 30;
    60 70 30 30];
b3 = [10 20 30 40;
    20 40 50 60;
    10 10 20 20;
    10 10 20 20];
b4 = [1 2 1 1;
    2 4 1 1;
    3 4 2 2;
    5 6 2 2];

mae((bx-b1))
mae((bx-b2))
mae((bx-b3))
mae((bx-b4))

%% question 8 & 9
clear; clc;

% block matching

frame1 = imread('E:\Fundamentals of Digital Image and Video Processing\week4_1.jpg');
I1 = im2double(frame1); % previous frame

frame2 = imread('E:\Fundamentals of Digital Image and Video Processing\week4_2.jpg');
I2 = im2double(frame2); % current frame

Btarget = I2(65:96, 81:112);

% position = [0, 0];
diff = [];
for i = 1:288-31
    for j = 1:352-31
        diff(i, j) = mae(Btarget-I1(i:i+31, j:j+31));
        %diff(i, j) = sum(sum(abs(Btarget-I1(i:i+31,j:j+31))))/(32*32);
        %diff = mae(Btarget, I1(i:i+31, j:j+31));
    end
end

d = min(diff(:));
[a, b] = find(diff == d); 
a+b % question 8

d*255 % question 9
