function main
%% Fundmentals of digital image and video processing 

clear; clc;
%% Week 3

%% Question 8 


I = imread('E:\Fundamentals of Digital Image and Video Processing\week3.jpg'); 

I = im2double(I); % convert unit8 (8 bit ineger) to double (real number)

% low-pass filtering
filter = ones(3,3)/9; % create filter
I_filtered = imfilter(I, filter, 'replicate');

% down sampling
I_down = I_filtered(1:2:end, 1:2:end);
% [m, n] = size(I); % row, column
% I_down = [];
% for row = 1: floor(m/2)
%     for col = 1: floor(n/2)
%         r = row*2-1;
%         c = col*2-1;
%         I_down(row, col) = I(r, c);
%     end
% end
% I_down(floor(m/2)+1, floor(n/2)+1) = I(2*floor(m/2)+1, 2*floor(n/2)+1); % add the last column and row because the size of I is odd

% up sampling
up = zeros(359, 479);
up(1:2:end, 1:2:end) = I_down(1:end, 1:end);
% for i = 1: m
%     for j = 1:n
%         if rem(m/2,1)~= 0 & rem(n/2,1) ~= 0
%             up(i, j) = I_down(ceil(m/2), ceil(n/2));
%         end
%     end
% end
%up(m, n) = I_down(end);

filter2 = [0.25,0.5,0.25;
    0.5,1,0.5;
    0.25,0.5,0.25] ;
up_filtered = imfilter(up, filter2); % up-sampled image

% Calculate the PSNR
result = psnr(I, up_filtered, 1) % use maximum 1 instead of 255

    function r = psnr(i1, i2, m)
        mse = sum((i1(:)-i2(:)).^2) / prod(size(i1));
        r = 10*log10(m/mse);
    end

end