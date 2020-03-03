
import pandas as pd
import random
data= pd.read_csv("DV_Data.csv")
data.total_cases = data.total_cases.astype(int)
data2=data.groupby(['city','year'])['total_cases'].sum()
data2=pd.DataFrame(data2.reset_index(level=[0,1]))

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.models.widgets import Select
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.palettes import Spectral8
import pandas as pd

Spectral8.reverse()
cities = list(data2['city'].unique())
years = list(data2['year'].unique())
data_2002=list(data2[data2.year==2002].total_cases)
data_2003=list(data2[data2.year==2003].total_cases)
data_2004=list(data2[data2.year==2004].total_cases)

color=Spectral8


d1 = {'cities' : cities,
        'y'   : data_2002,
       'color' :color
       }
d2 = {'cities' : cities,
        'y'   : data_2003,
      'color' :color
       }

d3= {'cities' : cities,
        'y'   : data_2004,
      'color' :color
    }

source = ColumnDataSource(d1)

p = figure(x_range=cities, y_range=(0, 5000),plot_width=800, plot_height=450, title="Total Dengue cases recorded each year in  Colorado Counties",
           toolbar_location=None, tools="")
p.vbar(x='cities', top='y',width=0.5,source = source,color='color',legend="cities")
select = Select(title="Year",  options=['2002','2003','2004'])

p.legend.location = "top_right"
p.legend.orientation = "vertical"
p.yaxis.axis_label = "Total Dengue Cases Recorded"
p.xaxis.axis_label = "Cities"
new_legend = p.legend[0]
p.legend[0].plot = None
p.add_layout(new_legend, 'right')

def update_plot(attrname, old, new):
    if select.value == '2002':
        newSource = d1  # changed this to the dict
    if select.value == '2003':
        newSource = d2  # changed this to the dict
    if select.value == '2004':
        newSource = d3  # changed this to the dict
    
    source.data =  newSource 


select.on_change('value', update_plot)
layout = column(row(select, width=400), p)
curdoc().add_root(layout)





