import pandas as pd
from matplotlib import pylab as plt
import seaborn as sns

#data = pd.read_csv("/Users/mattia/Documents/Data_Visualization_Polishing/iris.csv") #  for mac
data =pd.read_csv(r'C:\Users\matti\OneDrive\Desktop\Data_Visualization_Polishing\iris.csv') #  for windows

# Simple Visualization, scattering x and y as pair thei class label which is hue
sns.set_style("whitegrid")
sns.FacetGrid(data, hue="Species", height=4) \
   .map(plt.scatter, "Sepal Length (cm)", "Sepal Width (cm)") \
   .add_legend()
plt.show()

