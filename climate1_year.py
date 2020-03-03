
# coding: utf-8

# In[14]:


import pandas as pd
import random
data= pd.read_csv("DV_Data.csv")
data.total_cases = data.total_cases.astype(int)

from bokeh.models import ColumnDataSource,HoverTool
from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.models.widgets import Select,Panel,Tabs
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.layouts import layout
from bokeh.io import curdoc
import pandas as pd

from bokeh.embed import components
from bokeh.resources import CDN


precip_amt1=list(data[data.year==2002].precip_amt)
humidity1=list(data[data.year==2002].humidity)
avg_temp1=list(data[data.year==2002].avg_temp)
Total_cases_2002=list(data[data.year==2002].total_cases)

precip_amt2=list(data[data.year==2003].precip_amt)
humidity2=list(data[data.year==2003].humidity)
avg_temp2=list(data[data.year==2003].avg_temp)
Total_cases_2003=list(data[data.year==2003].total_cases)

precip_amt3=list(data[data.year==2004].precip_amt)
humidity3=list(data[data.year==2004].humidity)
avg_temp3=list(data[data.year==2004].avg_temp)
Total_cases_2004=list(data[data.year==2004].total_cases)

d1 = {'precip_amt' : precip_amt1,
      'humidity':humidity1,
      'avg_temp':avg_temp1,
        'y'   : Total_cases_2002,
       
       }
d2 = {'precip_amt' : precip_amt2,
      'humidity':humidity2,
      'avg_temp':avg_temp2,
        'y'   : Total_cases_2003,
       
       }

d3 = {'precip_amt' : precip_amt3,
      'humidity':humidity3,
      'avg_temp':avg_temp3,
        'y'   : Total_cases_2004,
       
       }

source1 = ColumnDataSource(d1)
source2 = ColumnDataSource(d2)
source3 = ColumnDataSource(d3)

p = figure(plot_width=400, plot_height=450, title="Total Dengue cases recorded in 2002 for the given climate values",
           toolbar_location=None, tools="")
p.circle(x='precip_amt', y='y',color="red",legend="precipitation",source=source1)
p.circle(x='humidity', y='y',color="green",legend="humdity",source=source1)
p.circle(x='avg_temp', y='y',color="blue",legend="average temp",source=source1)


p1 = figure(plot_width=400, plot_height=450, title="Total Dengue cases recorded in 2003 for the given climate values",
           toolbar_location=None, tools="")
p1.circle(x='precip_amt', y='y',color="red",legend="precipitation",source=source2)
p1.circle(x='humidity', y='y',color="green",legend="humdity",source=source2)
p1.circle(x='avg_temp', y='y',color="blue",legend="average temp",source=source2)

p2 = figure(plot_width=400, plot_height=450, title="Total Dengue cases recorded in 2004 for the given climate values",
           toolbar_location=None, tools="")
p2.circle(x='precip_amt', y='y',color="red",legend="precipitation",source=source3)
p2.circle(x='humidity', y='y',color="green",legend="humdity",source=source3)
p2.circle(x='avg_temp', y='y',color="blue",legend="average temp",source=source3)

myLayout=layout(row(p, p1, p2))
curdoc().add_root(myLayout)
js2, div2 = components(myLayout)

cdn_js2 =CDN.js_files[0]
cdn_css2 =CDN.css_files[0]
'''
tab1 = Panel(child=p, title="2002")
tab2 = Panel(child=p1, title="2003")
tab3 = Panel(child=p2, title="2004")

tabs = Tabs(tabs=[tab1,tab2,tab3])
myLayout = layout([[tabs]])
curdoc().add_root(myLayout)
show(tabs)
'''

