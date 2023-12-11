#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[17]:


#Question 1: Car Matrix Generation
import pandas as pd

def generate_car_matrix(dataframe):
    matrix = dataframe.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    for i in range(min(len(matrix.index), len(matrix.columns))):
        matrix.iloc[i, i] = 0

    return matrix


data = pd.read_csv('C:\\Users\\ayush\\Downloads\\dataset-1.csv')


result = generate_car_matrix(data)
result


# In[19]:


#Question 2: Car Type Count Calculation
import pandas as pd

def get_type_count(data):

    data['car_type'] = pd.cut(data['car'], bins=[-float('inf'), 15, 25, float('inf')],
                              labels=['low', 'medium', 'high'], right=False)
    type_counts = data['car_type'].value_counts().to_dict()
    type_counts = dict(sorted(type_counts.items()))
    return type_counts
file_path = 'C:\\Users\\ayush\\Downloads\\dataset-1.csv'
data = pd.read_csv(file_path)
result = get_type_count(data)
print(result)


# In[20]:


#Question 4: Route Filtering
import pandas as pd

def filter_routes(data):
    route_avg_truck = data.groupby('route')['truck'].mean()
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    filtered_routes.sort()
    return filtered_routes


file_path = 'C:\\Users\\ayush\\Downloads\\dataset-1.csv'
data = pd.read_csv(file_path)


result = filter_routes(data)
print(result)


# In[23]:


#Question 3: Bus Count Index Retrieval
import pandas as pd

def get_bus_indexes(data):
    bus_mean = data['bus'].mean()
    bus_indexes = data[data['bus'] > 2 * bus_mean].index.tolist()
    bus_indexes.sort()
    return bus_indexes
file_path = 'C:\\Users\\ayush\\Downloads\\dataset-1.csv'
data = pd.read_csv(file_path)
result = get_bus_indexes(data)
print(result)


# In[22]:


#Question 5: Matrix Value Modification
import pandas as pd
def multiply_matrix(data):
    def modify_value(value):
        if value > 20:
            return round(value * 0.75, 1)
        else:
            return round(value * 1.25, 1)
    modified_data = data.applymap(modify_value) 
    return modified_data
data = pd.read_csv('C:\\Users\\ayush\\Downloads\\dataset-1.csv')
result = generate_car_matrix(data)
result_modified = multiply_matrix(result)
print(result_modified)

