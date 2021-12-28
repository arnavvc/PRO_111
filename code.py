import pandas as bear
import statistics as stats
import random
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = bear.read_csv("medium_data.csv")

# SOME DATA TYPE NAMES:
# claps (not bell curve)
# responses (not working for some reason)
# reading_time
#data_name = str(input("Enter the data type name: "))
data_name = "reading_time"
data = df[data_name].tolist()
population_mean = stats.mean(data)

def sample_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    mean_sample = stats.mean(dataset)

    return mean_sample

def plot_graph(mean_list, list_mean, s1, s2, s3, e1, e2, e3, nlm):
    df = mean_list
    fig = ff.create_distplot([df], [f"Average of Sample Means of {data_name}"], show_hist=False)
    fig.add_trace(go.Scatter(x=[list_mean, list_mean], y=[0, 1], mode="lines", name="Sample Mean"))
    fig.add_trace(go.Scatter(x=[nlm, nlm], y=[0, 1], mode="lines", name="Intervention Mean"))

    fig.add_trace(go.Scatter(x=[s1, s1], y=[0, 1], mode="lines", name="Sample Stdev1 Start"))
    fig.add_trace(go.Scatter(x=[e1, e1], y=[0, 1], mode="lines", name="Sample Stdev1 End"))
    fig.add_trace(go.Scatter(x=[s2, s2], y=[0, 1], mode="lines", name="Sample Stdev2 Start"))
    fig.add_trace(go.Scatter(x=[e2, e2], y=[0, 1], mode="lines", name="Sample Stdev2 End"))
    fig.add_trace(go.Scatter(x=[s3, s3], y=[0, 1], mode="lines", name="Sample Stdev3 Start"))
    fig.add_trace(go.Scatter(x=[e3, e3], y=[0, 1], mode="lines", name="Sample Stdev3 End"))

    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_mean = sample_mean(30)
        mean_list.append(set_of_mean)
    list_mean = stats.mean(mean_list)
    list_stdev = stats.stdev(mean_list) 

    stdev_s1, stdev_e1 = list_mean-list_stdev, list_mean+list_stdev 
    stdev_s2, stdev_e2 = list_mean-2*list_stdev, list_mean+2*list_stdev
    stdev_s3, stdev_e3 = list_mean-3*list_stdev, list_mean+3*list_stdev

    new_mean_list = []
    for j in range(0,100):
        new_set_of_mean = sample_mean(30)
        new_mean_list.append(new_set_of_mean)
    new_list_mean = stats.mean(new_mean_list)


    plot_graph(mean_list, list_mean, stdev_s1, stdev_s2, stdev_s3, stdev_e1, stdev_e2, stdev_e3, new_list_mean)

    zscore = (new_list_mean - list_mean) / list_stdev
    print(zscore)

setup()
