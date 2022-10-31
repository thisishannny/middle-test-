import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

%matplotlib inline    

iris = sns.load_dataset('iris')
iris

iris.groupby('species').size()

iris.describe()

type(iris)

# seaborn
sns.pairplot(iris)
plt.title("Iris Data Analysis")

# kde plotÀ» Àû¿ë
sns.pairplot(iris, hue="species", diag_kind='kde')

sns.boxplot(x='species', y="petal_length", data=iris)

sns.boxplot(x='species', y="petal_width", data=iris)

# pandas box plot
iris.boxplot(by="species", figsize=(16,8))