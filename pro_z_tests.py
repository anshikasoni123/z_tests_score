import csv 
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv('School2.csv')
data = df['Math_score'].tolist()

def random_sets_of_mean(counter):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)

    mean = statistics.mean(data_set)
    return mean

mean_list = []
for i in range(0,1000):
    random_sets = random_sets_of_mean(30)
    mean_list.append(random_sets)

mean = statistics.mean(mean_list)
std_dev = statistics.stdev(mean_list)
print('Mean of sampling distribution is :- ',mean)
print('Standard deviation of sampling distribution is :- ',std_dev)

std_dev_start_1,std_dev_end_1 = mean-std_dev,mean+std_dev
std_dev_start_2,std_dev_end_2 = mean-(std_dev*2),mean+(std_dev*2)
std_dev_start_3,std_dev_end_3 = mean-(std_dev*3),mean+(std_dev*3)
print('Standard deviation 1 is :- ',std_dev_start_1,',',std_dev_end_1)
print('Standard deviation 2 is :- ',std_dev_start_2,',',std_dev_end_2)
print('Standard deviation 3 is :- ',std_dev_start_3,',',std_dev_end_3)

df = pd.read_csv('School_2_Sample.csv')
data = df['Math_score'].tolist()
mean_of_sample_2 = statistics.mean(data)
print('Mean of sample 2 is :- ',mean_of_sample_2)
fig = ff.create_distplot([mean_list],['MEAN LIST'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='MEAN'))
fig.add_trace(go.Scatter(x=[mean_of_sample_2,mean_of_sample_2],y=[0,0.17],mode='lines',name='MEAN OF SAMPLE 2'))
fig.add_trace(go.Scatter(x=[std_dev_start_1,std_dev_start_1],y=[0,0.17],mode='lines',name='STANDARD DEVIATION START 1'))
fig.add_trace(go.Scatter(x=[std_dev_end_1,std_dev_end_1],y=[0,0.17],mode='lines',name='STANDARD DEVIATION END 1'))
fig.add_trace(go.Scatter(x=[std_dev_start_2,std_dev_start_2],y=[0,0.17],mode='lines',name='STANDARD DEVIATION START 2'))
fig.add_trace(go.Scatter(x=[std_dev_end_2,std_dev_end_2],y=[0,0.17],mode='lines',name='STANDARD DEVIATION END 2'))
fig.add_trace(go.Scatter(x=[std_dev_start_3,std_dev_start_3],y=[0,0.17],mode='lines',name='STANDARD DEVIATION START 3'))
fig.add_trace(go.Scatter(x=[std_dev_end_3,std_dev_end_3],y=[0,0.17],mode='lines',name='STANDARD DEVIATION END 3'))
fig.show()

z_score = mean_of_sample_2-mean/std_dev
print('z score is :- ',z_score)