# Example: Using 'del' to remove references

def process_data(data):
    # Some data processing code here
    print("Processing data:", data)

# Create a list of data
data_list = [1, 2, 3, 4, 5]

# Pass the data_list to the function
process_data(data_list)

# Remove the reference to data_list using 'del'
del data_list

# Attempting to access data_list after deletion will result in an error
# Uncomment the following line to see the NameError
# print(data_list)
