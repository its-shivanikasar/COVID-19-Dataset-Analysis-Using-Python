# -*- coding: utf-8 -*-
"""covid19 data analysis notebook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-8sCfpZ_SLTEsUekaK1aHFxZijx0IKYS

# Covid19 Data Analysis Notebook
------------------------------------------

### Import the modules
"""

import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')

"""## Task 2

### Task 2.1: importing covid19 dataset
"""

corona_dataset_csv = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset_csv.head()

"""#### Check the shape of the dataframe"""

corona_dataset_csv.shape

"""### Task 2.2: Delete the useless columns"""

corona_dataset_csv = corona_dataset_csv.drop(["Lat","Long"],axis=1)

corona_dataset_csv.head(10)

"""### Task 2.3: Aggregating the rows by the country"""

corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()

corona_dataset_aggregated.head()

corona_dataset_aggregated.shape

"""### Task 2.4: Visualizing data related to a country for example China"""

corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
corona_dataset_aggregated.loc["Spain"].plot()
plt.legend()

"""### Task3: Calculating a good measure 
we need to find a good measure reperestend as a number, describing the spread of the virus in a country.
"""

corona_dataset_aggregated.loc['China'].plot()

corona_dataset_aggregated.loc["China"][:3].plot()

"""### task 3.1: caculating the first derivative of the curve"""

corona_dataset_aggregated.loc["China"].diff().plot()

"""### task 3.2: find maxmimum infection rate for China"""

corona_dataset_aggregated.loc["China"].diff().max()

corona_dataset_aggregated.loc["Italy"].diff().max()

corona_dataset_aggregated.loc["Spain"].diff().max()

"""### Task 3.3: find maximum infection rate for all of the countries."""

countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for c in countries:
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["max_infection_rate"] = max_infection_rates

corona_dataset_aggregated.head()

"""### Task 3.4: create a new dataframe with only needed column"""

corona_data = pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])

corona_data.head()

"""### Task4: 
- Importing the WorldHappinessReport.csv dataset
- selecting needed columns for our analysis 
- join the datasets 
- calculate the correlations as the result of our analysis

### Task 4.1 : importing the dataset
"""

happiness_report_csv = pd.read_csv("Datasets/worldwide_happiness_report.csv")

happiness_report_csv.head()

"""### Task 4.2: drop the useless columns"""

useless_cols = ["Overall rank","Score","Generosity","Perceptions of corruption"]

happiness_report_csv.drop(useless_cols,axis=1,inplace=True)
happiness_report_csv.head()

"""### Task 4.3: changing the indices of the dataframe"""

happiness_report_csv.set_index("Country or region",inplace=True)

happiness_report_csv.head()

"""### Task4.4: now join two datasets that we have prepared

#### Corona Dataset :
"""

corona_data.head()

corona_data.shape

"""#### world happiness report Dataset :"""

happiness_report_csv.head()

happiness_report_csv.shape

data = corona_data.join(happiness_report_csv,how="inner")
data.head()

"""### Task 4.5: correlation matrix"""

data.corr()

"""### Task 5: Visualization of the results"""

data.head()

"""### Task 5.1: Plotting GDP vs maximum Infection rate"""

x = data["GDP per capita"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))

"""### Task 5.2: Plotting Social support vs maximum Infection rate"""

x = data["Social support"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))

"""### Task 5.3: Plotting Healthy life expectancy vs maximum Infection rate"""

x = data["Healthy life expectancy"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))

"""### Task 5.4: Plotting Freedom to make life choices vs maximum Infection rate"""

x = data["Freedom to make life choices"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))