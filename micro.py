

import pandas as pd
import numpy as np
import random
from bokeh.models import ColumnDataSource, HoverTool, PanTool, ResetTool
from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.models import Range1d

from bokeh.embed import components
from bokeh.resources import CDN

data= pd.read_csv("DV_Data.csv")
data.total_cases = data.total_cases.astype(int)
data.weekofyear = data.weekofyear.astype('category')

def yearly_pattern(city, year):
    weekofyear = list((data[((data.year==year) & (data.city==city))].weekofyear))
    data1=data[((data.year==year) & (data.city==city))].total_cases
    N=len(data1)
    x = np.random.random(size=N) * 100
    y = np.random.random(size=N) * 100
    colors = [
    "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
    ]
    f=figure(width=1000,height=450)
    f.title.text = 'Total dengue cases recored each week of the Year'
    f.xaxis.axis_label = 'Week of the Year'
    f.yaxis.axis_label = "Total cases"

    f.vbar(x=weekofyear,top=data1,width=0.5, fill_color=colors,fill_alpha=0.6)
    hover = HoverTool( tooltips=[("Week of year",'@x'), ("total cases","@top")] )
    f.add_tools(hover) 
    js, div = components(f)

    cdn_js =CDN.js_files[0]
    cdn_css =CDN.css_files[0]
    
yearly_pattern('New_London', 2002)    


