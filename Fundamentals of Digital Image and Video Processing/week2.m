%% Fundmentals of digital image and video processing 
%% Week 2

clear; clc;

I = imread('E:\Fundamentals of Digital Image and Video Processing\week2.gif'); % load the image

I = im2double(I); % convert unit8 (8 bit ineger) to double (real number)

% use filer
% - step 1: create a filter
% - step 2: apply the filter
f3 = fspecial('average',... % type of the filter
    [3,3]);            % parameters of the filter
% alternative way:
% ones(3,3)/9

f5 = fspecial('average', [5,5]);

I_filtered3 = imfilter(I, f3, 'replicate'); % apply the filter
I_filtered5 = imfilter(I, f5, 'replicate');

mse3 = sum((I(:)-I_filtered3(:)).^2) / prod(size(I));
mse5 = sum((I(:)-I_filtered5(:)).^2) / prod(size(I));

psnr3 = 10*log10(1/mse3) 
psnr5 = 10*log10(1/mse5)
% why 1 not 255?
% im2double function maps all the pixel values from the range 0-255 to the 
% range 0-1. So the maximum value a pixel can now have is 1. 
