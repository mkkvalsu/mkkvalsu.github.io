import numpy as np
from numpy.fft import fft2,ifft2,fftshift
import matplotlib.pyplot as plt
from imageio import imread
from scipy.signal import convolve2d

# Making a tiny version of cow.png, can be fully ignored
cow = imread("cow.png", as_gray=True)
N,M = cow.shape
h = np.zeros((N,M))
n = 6
h[int(N/2-n):int(N/2+n), int(M/2-n):int(M/2+n)] = 1/(2*n*2*n)
F = np.fft.fft2(cow)
H = abs(np.fft.fft2(h))
Res = F*H
res = np.real(np.fft.ifft2(Res))
tiny_cow = res[::8,::8]

plt.imsave("tiny_cow.jpg", tiny_cow, cmap="gray")
