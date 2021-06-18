#importing the fft and inverse fft functions from fftpackage
from scipy.fftpack import fft
import numpy as np
#create an array with random n numbers
x = np.array([1.0,2.0,1.0,-1.0,1.5])

#applying th fft function
y = fft(x)
print(y)