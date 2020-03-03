
# coding: utf-8

# In[1]:


import pandas as pd
import random
from bokeh.models import (
    GeoJSONDataSource,
    HoverTool,
    LinearColorMapper,
    LogColorMapper,
    ColorBar,
    LogTicker
)
import json
import numpy as np
from bokeh.plotting import figure, show,output_file,output_notebook
from bokeh.models import Range1d
from bokeh.models.widgets import Panel, Tabs
from bokeh.layouts import layout
from bokeh.io import curdoc

from bokeh.palettes import Purples9 as palette1
from bokeh.palettes import YlGn9 as palette2

 


# In[2]:




with open(r'Hospitals_2002.geojson', 'r') as f:
    geo_source1 = GeoJSONDataSource(geojson=f.read())
    
with open(r'Hospitals_2003.geojson', 'r') as f:
    geo_source2 = GeoJSONDataSource(geojson=f.read())

with open(r'Hospitals_2004.geojson', 'r') as f:
    geo_source3 = GeoJSONDataSource(geojson=f.read())


# In[3]:


TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
custom_colors = ['#f2f2f2', '#fee5d9', '#fcbba1', '#fc9272', '#fb6a4a', '#de2d26']
mapper1 = LinearColorMapper(palette=custom_colors, low=450, high=3500) 
mapper2 = LinearColorMapper(palette=palette1, low=100, high=4000) 
mapper3 = LinearColorMapper(palette=palette2, low=600, high=3600) 

color_bar1 = ColorBar(color_mapper=mapper1, ticker=LogTicker(),
                     label_standoff=12, border_line_color=None, location=(0,0))
color_bar2 = ColorBar(color_mapper=mapper2, ticker=LogTicker(),
                     label_standoff=12, border_line_color=None, location=(0,0))
color_bar3 = ColorBar(color_mapper=mapper3, ticker=LogTicker(),
                     label_standoff=12, border_line_color=None, location=(0,0))

palette1.reverse()
palette2.reverse()
p = figure(title="Connecticut Dengue Cases recorded in Year 2002", tools=TOOLS, x_axis_location=None, y_axis_location=None, width=800, height=500)
p.grid.grid_line_color = None
p.patches('xs', 'ys', fill_alpha=1.0, 
          fill_color={'field': 'Total_Cases_2002', 'transform': mapper1},
          line_color='red', line_width=0.5, source=geo_source1)
hover1 = HoverTool( tooltips=[("Name","@name"), ("Yale Hospital","@Yale_Hospital"),
                              ("Bristol Hospital","@Bristol_Hospital"),("Gaylord Hospital","@Gaylord_Hospital"),
                             ("Total cases","@Total_Cases_2002")] )
p.add_tools(hover1)
p.add_layout(color_bar1, 'right')

p1 = figure(title="Connecticut Dengue Cases recorded in Year 2003", tools=TOOLS, x_axis_location=None, y_axis_location=None, width=800, height=500)
p1.grid.grid_line_color = None
p1.patches('xs', 'ys', fill_alpha=1.0, 
          fill_color={'field': 'Total_Cases_2003', 'transform': mapper2},
          line_color='red', line_width=0.5, source=geo_source2)
hover2 = HoverTool( tooltips=[("Name","@name"), ("Yale Hospital","@Yale_Hospital"),("Bristol Hospital","@Bristol_Hospital"),("Gaylord Hospital","@Gaylord_Hospital"),
                             ("Total cases","@Total_Cases_2003")] )
p1.add_tools(hover2)
p1.add_layout(color_bar2, 'right')


p2 = figure(title="Connecticut Dengue Cases recorded in Year 2004", tools=TOOLS, x_axis_location=None, y_axis_location=None, width=800, height=500)
p2.grid.grid_line_color = None
p2.patches('xs', 'ys', fill_alpha=1.0, 
          fill_color={'field': 'Total_Cases_2004', 'transform': mapper3},
          line_color='red', line_width=0.5, source=geo_source3)
hover3 = HoverTool( tooltips=[("Name","@name"), ("Yale Hospital","@Yale_Hospital"),("Bristol Hospital","@Bristol_Hospital"),("Gaylord Hospital","@Gaylord_Hospital"),
                             ("Total cases","@Total_Cases_2004")] )
p2.add_tools(hover3)
p2.add_layout(color_bar3, 'right')


tab1 = Panel(child=p, title="2002")
tab2 = Panel(child=p1, title="2003")
tab3 = Panel(child=p2, title="2004")

tabs = Tabs(tabs=[tab1,tab2,tab3])
myLayout = layout([[tabs]])
curdoc().add_root(myLayout)
show(tabs)

   

