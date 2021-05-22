import pandas
import numpy
import re
import matplotlib.pyplot as mplt 
import seaborn as sns
class scatter_plot:
    def __init__(self, df):
        self.data = df

    def scatter_plot(self):
        a = self.df
    
    def line_plot(self):
        aa = self.df
    
    def plot_another(self):
        a = self.df
    
    def multiple_line_chart(self):
        # multiple line plot
        #print(self.data)
        mplt.plot( 'time', 'algo', data=self.data, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
        mplt.plot( 'time', 'algo', data=self.data, marker='', color='olive', linewidth=2)
        mplt.plot( 'time', 'algo', data=self.data, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")
        mplt.plot( 'time', 'algo', data=self.data, marker='o', markerfacecolor='red', markersize=12, color='skyblue', linewidth=4)
        mplt.plot( 'time', 'algo', data=self.data, marker='', color='green', linewidth=2)
        mplt.plot( 'time', 'algo', data=self.data, marker='', color='grey', linewidth=2, linestyle='dashed', label="toto")
        mplt.show()
    def bar_plot(self):
        #self.data.plot(kind='bar', figsize=(17, 10), color=['lightgray', 'gray', 'black', 'olive', 'green', 'blue'], rot=0)                                       
        #mplt.title("Algorithm Runtime chart", y=1.013, fontsize=22)
        #mplt.xlabel("Name (Instance)", labelpad=16)
        #mplt.ylabel("time", labelpad=16)
        #mplt.show()
        d = self.data
        sns.lineplot(x='name',y='time',data=d,hue='algo')
        mplt.show()
    
    def heat_map_plot(self):
        #uniform_data = numpy.random.rand(10, 12)
        sns.heatmap(self.data)
        mplt.show()
