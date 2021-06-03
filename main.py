# %% [markdown]
# # Project C110
# %% [markdown]
# ## Getting Data

# %%
import random
import statistics

import pandas
import plotly.figure_factory as ff

data_frame = pandas.read_csv("data.csv")
reading_time_data = list(data_frame["reading_time"])

fig = ff.create_distplot([reading_time_data], ["Reading Time"])
fig.show()

population_mean = statistics.mean(reading_time_data)

print(f"Population Mean: {population_mean}")

# %% [markdown]
# ## Function for Sampling Mean

# %%
def sample_mean(counter: int, data: list):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

# %% [markdown]
# ## Getting Sample Mean

# %%
mean_list = []

for i in range(0, 100):
    set_of_means = sample_mean(10, reading_time_data)
    mean_list.append(set_of_means)

# %% [markdown]
# ## Showing Sample Mean

# %%
chart = ff.create_distplot([mean_list], ["Reading Time"])
chart.show()

sample_mean = statistics.mean(mean_list)
print(f"Sample Mean: {sample_mean}")


