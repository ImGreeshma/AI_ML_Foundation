import numpy as np
data = np.array([[22.5, 19.0, 31.2, 28.7, 25.1],
                 [17.3, 22.8, 30.5, 26.4, 21.9],
                 [33.1, 29.6, 18.4, 24.0, 27.8],
                 [20.2, 23.5, 31.9, 28.1, 22.6]])
# Print the shape of data
print (data.shape) 

# Then compute and print the mean temperature per station (one value per row)
mean_data = np.mean(data, axis = 1)
print (mean_data.reshape (4, 1))

# Using a boolean mask, extract all temperature readings above 28.0°C 
# Print them as a 1D array
high_temperature = data[data > 28.0]
print (high_temperature)

#  Normalize the entire data array to the range [0, 1] using the formula below 
#  normalized = (data - data.min()) / (data.max() - data.min())
# Print the result rounded to 2 decimal places:
normalized = (data - data.min()) / (data.max() - data.min())
print (np.round(normalized, 2))