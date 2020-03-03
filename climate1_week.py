import pandas as pd
import random
data= pd.read_csv("DV_Data.csv")
data.total_cases = data.total_cases.astype(int)

from bokeh.models import ColumnDataSource,HoverTool,Div
from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.models.widgets import Select,Panel,Tabs
from bokeh.io import curdoc
from bokeh.layouts import column, row,widgetbox
from bokeh.layouts import layout
from bokeh.io import curdoc
import pandas as pd
from bokeh.models import NumeralTickFormatter, Range1d, LinearAxis

from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.models.ranges import Range1d
    
    
precip_amt1_2002=list(data[(data.year==2002) & (data.city=="New_London")].precip_amt)
humidity1_2002=list(data[(data.year==2002) & (data.city=="New_London")].humidity)
avg_temp1_2002=list(data[(data.year==2002) & (data.city=="New_London")].avg_temp)
Total_cases1_2002=list(data[(data.year==2002) & (data.city=="New_London")].total_cases)
weekofyear1_2002=list(data[(data.year==2002) & (data.city=="New_London")].weekofyear)



d1 = {'precip_amt' : precip_amt1_2002,
      'humidity':humidity1_2002,
      'avg_temp':avg_temp1_2002,
        'y'   : Total_cases1_2002,
        'y1' :weekofyear1_2002
       
       }


source = ColumnDataSource(d1)



p2 = figure(plot_width=400, plot_height=450, title="Total Lyme cases recorded in 2004 for the given climate values",
           toolbar_location=None, tools="")

p2.extra_y_ranges = {'y1': Range1d(start=0, end=52)} 
p2.add_layout(LinearAxis(y_range_name='y1'), 'right')

p2.circle(x='precip_amt', y='y',color="red",legend="precipitation",source=source,size=7)
p2.circle(x='humidity', y='y',color="green",legend="humdity",source=source,size=7)
p2.circle(x='avg_temp', y='y',color="blue",legend="average temp",source=source,size=7)

p2.circle(x='precip_amt', y='y1',color="red",legend="precipitation",source=source,size=7)
p2.circle(x='humidity', y='y1',color="green",legend="humdity",source=source,size=7)
p2.circle(x='avg_temp', y='y1',color="blue",legend="average temp",source=source,size=7)

p2.yaxis[0].axis_label = "Total Cases"
p2.yaxis[1].axis_label = "Week Of Year"
p2.xaxis.axis_label = "Climate Variables"

# layout1 = column(row(select1, width=400), p)
# layout2 = column(row(select2, width=400), p1)
# layout3 = column(row(select3, width=400), p2)

# mylayout=row(layout1, layout2,layout3)


curdoc().add_root(p2) 


