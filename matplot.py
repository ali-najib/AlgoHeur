import numpy as np

#make this example reproducible.
np.random.seed(1)

#create numpy array with 1000 values that follow normal dist with mean=10 and sd=2
data = np.random.normal(size=1000, loc=10, scale=2)

#view first five values

print(data[:5])