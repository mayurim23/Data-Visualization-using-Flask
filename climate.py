import pandas as pd
import random
data= pd.read_csv("DV_Data.csv")
data.total_cases = data.total_cases.astype(int)

from bokeh.models import ColumnDataSource,HoverTool
from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.models.widgets import Select,Panel,Tabs
from bokeh.io import curdoc
from bokeh.layouts import column, row,widgetbox
from bokeh.layouts import layout
from bokeh.io import curdoc
import pandas as pd


from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.models import LinearAxis, Range1d

from bokeh.models import NumeralTickFormatter, Range1d, LinearAxis    
    
precip_amt1_2002=list(data[(data.year==2002) & (data.city=="New_London")].precip_amt)
humidity1_2002=list(data[(data.year==2002) & (data.city=="New_London")].humidity)
avg_temp1_2002=list(data[(data.year==2002) & (data.city=="New_London")].avg_temp)
Total_cases1_2002=list(data[(data.year==2002) & (data.city=="New_London")].weekofyear)

precip_amt2_2002=list(data[(data.year==2002) & (data.city=="Hartford")].precip_amt)
humidity2_2002=list(data[(data.year==2002) & (data.city=="Hartford")].humidity)
avg_temp2_2002=list(data[(data.year==2002) & (data.city=="Hartford")].avg_temp)
Total_cases2_2002=list(data[(data.year==2002) & (data.city=="Hartford")].weekofyear)


precip_amt3_2002=list(data[(data.year==2002) & (data.city=="Middlesex")].precip_amt)
humidity3_2002=list(data[(data.year==2002) & (data.city=="Middlesex")].humidity)
avg_temp3_2002=list(data[(data.year==2002) & (data.city=="Middlesex")].avg_temp)
Total_cases3_2002=list(data[(data.year==2002) & (data.city=="Middlesex")].weekofyear)

precip_amt4_2002=list(data[(data.year==2002) & (data.city=="Fairfield")].precip_amt)
humidity4_2002=list(data[(data.year==2002) & (data.city=="Fairfield")].humidity)
avg_temp4_2002=list(data[(data.year==2002) & (data.city=="Fairfield")].avg_temp)
Total_cases4_2002=list(data[(data.year==2002) & (data.city=="Fairfield")].weekofyear)

precip_amt5_2002=list(data[(data.year==2002) & (data.city=="Litchfield")].precip_amt)
humidity5_2002=list(data[(data.year==2002) & (data.city=="Litchfield")].humidity)
avg_temp5_2002=list(data[(data.year==2002) & (data.city=="Litchfield")].avg_temp)
Total_cases5_2002=list(data[(data.year==2002) & (data.city=="Litchfield")].weekofyear)

precip_amt6_2002=list(data[(data.year==2002) & (data.city=="Tolland")].precip_amt)
humidity6_2002=list(data[(data.year==2002) & (data.city=="Tolland")].humidity)
avg_temp6_2002=list(data[(data.year==2002) & (data.city=="Tolland")].avg_temp)
Total_cases6_2002=list(data[(data.year==2002) & (data.city=="Tolland")].weekofyear)


precip_amt7_2002=list(data[(data.year==2002) & (data.city=="Windham")].precip_amt)
humidity7_2002=list(data[(data.year==2002) & (data.city=="Windham")].humidity)
avg_temp7_2002=list(data[(data.year==2002) & (data.city=="Windham")].avg_temp)
Total_cases7_2002=list(data[(data.year==2002) & (data.city=="Windham")].weekofyear)

precip_amt8_2002=list(data[(data.year==2002) & (data.city=="New_Haven")].precip_amt)
humidity8_2002=list(data[(data.year==2002) & (data.city=="New_Haven")].humidity)
avg_temp8_2002=list(data[(data.year==2002) & (data.city=="New_Haven")].avg_temp)
Total_cases8_2002=list(data[(data.year==2002) & (data.city=="New_Haven")].weekofyear)


#################2003#########################################################################
precip_amt1_2003=list(data[(data.year==2003) & (data.city=="New_London")].precip_amt)
humidity1_2003=list(data[(data.year==2003) & (data.city=="New_London")].humidity)
avg_temp1_2003=list(data[(data.year==2003) & (data.city=="New_London")].avg_temp)
Total_cases1_2003=list(data[(data.year==2003) & (data.city=="New_London")].weekofyear)

precip_amt2_2003=list(data[(data.year==2003) & (data.city=="Hartford")].precip_amt)
humidity2_2003=list(data[(data.year==2003) & (data.city=="Hartford")].humidity)
avg_temp2_2003=list(data[(data.year==2003) & (data.city=="Hartford")].avg_temp)
Total_cases2_2003=list(data[(data.year==2003) & (data.city=="Hartford")].weekofyear)


precip_amt3_2003=list(data[(data.year==2003) & (data.city=="Middlesex")].precip_amt)
humidity3_2003=list(data[(data.year==2003) & (data.city=="Middlesex")].humidity)
avg_temp3_2003=list(data[(data.year==2003) & (data.city=="Middlesex")].avg_temp)
Total_cases3_2003=list(data[(data.year==2003) & (data.city=="Middlesex")].weekofyear)

precip_amt4_2003=list(data[(data.year==2003) & (data.city=="Fairfield")].precip_amt)
humidity4_2003=list(data[(data.year==2003) & (data.city=="Fairfield")].humidity)
avg_temp4_2003=list(data[(data.year==2003) & (data.city=="Fairfield")].avg_temp)
Total_cases4_2003=list(data[(data.year==2003) & (data.city=="Fairfield")].weekofyear)

precip_amt5_2003=list(data[(data.year==2003) & (data.city=="Litchfield")].precip_amt)
humidity5_2003=list(data[(data.year==2003) & (data.city=="Litchfield")].humidity)
avg_temp5_2003=list(data[(data.year==2003) & (data.city=="Litchfield")].avg_temp)
Total_cases5_2003=list(data[(data.year==2003) & (data.city=="Litchfield")].weekofyear)

precip_amt6_2003=list(data[(data.year==2003) & (data.city=="Tolland")].precip_amt)
humidity6_2003=list(data[(data.year==2003) & (data.city=="Tolland")].humidity)
avg_temp6_2003=list(data[(data.year==2003) & (data.city=="Tolland")].avg_temp)
Total_cases6_2003=list(data[(data.year==2003) & (data.city=="Tolland")].weekofyear)


precip_amt7_2003=list(data[(data.year==2003) & (data.city=="Windham")].precip_amt)
humidity7_2003=list(data[(data.year==2003) & (data.city=="Windham")].humidity)
avg_temp7_2003=list(data[(data.year==2003) & (data.city=="Windham")].avg_temp)
Total_cases7_2003=list(data[(data.year==2003) & (data.city=="Windham")].weekofyear)

precip_amt8_2003=list(data[(data.year==2003) & (data.city=="New_Haven")].precip_amt)
humidity8_2003=list(data[(data.year==2003) & (data.city=="New_Haven")].humidity)
avg_temp8_2003=list(data[(data.year==2003) & (data.city=="New_Haven")].avg_temp)
Total_cases8_2003=list(data[(data.year==2003) & (data.city=="New_Haven")].weekofyear)

###########################20004#########################################################################

precip_amt1_2004=list(data[(data.year==2004) & (data.city=="New_London")].precip_amt)
humidity1_2004=list(data[(data.year==2004) & (data.city=="New_London")].humidity)
avg_temp1_2004=list(data[(data.year==2004) & (data.city=="New_London")].avg_temp)
Total_cases1_2004=list(data[(data.year==2004) & (data.city=="New_London")].weekofyear)

precip_amt2_2004=list(data[(data.year==2004) & (data.city=="Hartford")].precip_amt)
humidity2_2004=list(data[(data.year==2004) & (data.city=="Hartford")].humidity)
avg_temp2_2004=list(data[(data.year==2004) & (data.city=="Hartford")].avg_temp)
Total_cases2_2004=list(data[(data.year==2004) & (data.city=="Hartford")].weekofyear)


precip_amt3_2004=list(data[(data.year==2004) & (data.city=="Middlesex")].precip_amt)
humidity3_2004=list(data[(data.year==2004) & (data.city=="Middlesex")].humidity)
avg_temp3_2004=list(data[(data.year==2004) & (data.city=="Middlesex")].avg_temp)
Total_cases3_2004=list(data[(data.year==2004) & (data.city=="Middlesex")].weekofyear)

precip_amt4_2004=list(data[(data.year==2004) & (data.city=="Fairfield")].precip_amt)
humidity4_2004=list(data[(data.year==2004) & (data.city=="Fairfield")].humidity)
avg_temp4_2004=list(data[(data.year==2004) & (data.city=="Fairfield")].avg_temp)
Total_cases4_2004=list(data[(data.year==2004) & (data.city=="Fairfield")].weekofyear)

precip_amt5_2004=list(data[(data.year==2004) & (data.city=="Litchfield")].precip_amt)
humidity5_2004=list(data[(data.year==2004) & (data.city=="Litchfield")].humidity)
avg_temp5_2004=list(data[(data.year==2004) & (data.city=="Litchfield")].avg_temp)
Total_cases5_2004=list(data[(data.year==2004) & (data.city=="Litchfield")].weekofyear)

precip_amt6_2004=list(data[(data.year==2004) & (data.city=="Tolland")].precip_amt)
humidity6_2004=list(data[(data.year==2004) & (data.city=="Tolland")].humidity)
avg_temp6_2004=list(data[(data.year==2004) & (data.city=="Tolland")].avg_temp)
Total_cases6_2004=list(data[(data.year==2004) & (data.city=="Tolland")].weekofyear)


precip_amt7_2004=list(data[(data.year==2004) & (data.city=="Windham")].precip_amt)
humidity7_2004=list(data[(data.year==2004) & (data.city=="Windham")].humidity)
avg_temp7_2004=list(data[(data.year==2004) & (data.city=="Windham")].avg_temp)
Total_cases7_2004=list(data[(data.year==2004) & (data.city=="Windham")].weekofyear)


precip_amt8_2004=list(data[(data.year==2004) & (data.city=="New_Haven")].precip_amt)
humidity8_2004=list(data[(data.year==2004) & (data.city=="New_Haven")].humidity)
avg_temp8_2004=list(data[(data.year==2004) & (data.city=="New_Haven")].avg_temp)
Total_cases8_2004=list(data[(data.year==2004) & (data.city=="New_Haven")].weekofyear)

y8_2004 = list(data[(data.year==2004) & (data.city=="New_Haven")].weekofyear)


d1 = {'precip_amt' : precip_amt1_2002,
      'humidity':humidity1_2002,
      'avg_temp':avg_temp1_2002,
        'y'   : Total_cases1_2002
       
       }

d2 = {'precip_amt' : precip_amt2_2002,
      'humidity':humidity2_2002,
      'avg_temp':avg_temp2_2002,
        'y'   : Total_cases2_2002
       }

d3 = {'precip_amt' : precip_amt3_2002,
      'humidity':humidity3_2002,
      'avg_temp':avg_temp3_2002,
        'y'   : Total_cases3_2002
       
       }

d4 = {'precip_amt' : precip_amt4_2002,
      'humidity':humidity4_2002,
      'avg_temp':avg_temp4_2002,
        'y'   : Total_cases4_2002
       }

d5 = {'precip_amt' : precip_amt5_2002,
      'humidity':humidity5_2002,
      'avg_temp':avg_temp5_2002,
        'y'   : Total_cases5_2002
       
       }

d6 = {'precip_amt' : precip_amt6_2002,
      'humidity':humidity6_2002,
      'avg_temp':avg_temp6_2002,
        'y'   : Total_cases6_2002
       }

d7 = {'precip_amt' : precip_amt7_2002,
      'humidity':humidity7_2002,
      'avg_temp':avg_temp7_2002,
        'y'   : Total_cases7_2002
       
       }

d8 = {'precip_amt' : precip_amt8_2002,
      'humidity':humidity8_2002,
      'avg_temp':avg_temp8_2002,
        'y'   : Total_cases8_2002
       
       }

####################2003####################################################################

m1 = {'precip_amt' : precip_amt1_2003,
      'humidity':humidity1_2003,
      'avg_temp':avg_temp1_2003,
        'y'   : Total_cases1_2003
       
       }

m2 = {'precip_amt' : precip_amt2_2003,
      'humidity':humidity2_2003,
      'avg_temp':avg_temp2_2003,
        'y'   : Total_cases2_2003
       
       }
m3 = {'precip_amt' : precip_amt3_2003,
      'humidity':humidity3_2003,
      'avg_temp':avg_temp3_2003,
        'y'   : Total_cases3_2003
       
       }

m4 = {'precip_amt' : precip_amt4_2003,
      'humidity':humidity4_2003,
      'avg_temp':avg_temp4_2003,
        'y'   : Total_cases4_2003
       
       }
m5 = {'precip_amt' : precip_amt5_2003,
      'humidity':humidity5_2003,
      'avg_temp':avg_temp5_2003,
        'y'   : Total_cases5_2003
       
       }

m6 = {'precip_amt' : precip_amt6_2003,
      'humidity':humidity6_2003,
      'avg_temp':avg_temp6_2003,
        'y'   : Total_cases6_2003
       
       }
m7 = {'precip_amt' : precip_amt7_2003,
      'humidity':humidity7_2003,
      'avg_temp':avg_temp7_2003,
        'y'   : Total_cases7_2003
       
       }

m8 = {'precip_amt' : precip_amt8_2003,
      'humidity':humidity8_2003,
      'avg_temp':avg_temp8_2003,
        'y'   : Total_cases8_2003
       
       }
############################################2004###################################

s1 = {'precip_amt' : precip_amt1_2004,
      'humidity':humidity1_2004,
      'avg_temp':avg_temp1_2004,
        'y'   : Total_cases1_2004
       
       }

s2 = {'precip_amt' : precip_amt2_2004,
      'humidity':humidity2_2004,
      'avg_temp':avg_temp2_2004,
        'y'   : Total_cases2_2004
       
       }
s3 = {'precip_amt' : precip_amt3_2004,
      'humidity':humidity3_2004,
      'avg_temp':avg_temp3_2004,
        'y'   : Total_cases3_2004
       
       }

s4 = {'precip_amt' : precip_amt4_2004,
      'humidity':humidity4_2004,
      'avg_temp':avg_temp4_2004,
        'y'   : Total_cases4_2004,
       
       }
s5 = {'precip_amt' : precip_amt5_2004,
      'humidity':humidity5_2004,
      'avg_temp':avg_temp5_2004,
        'y'   : Total_cases5_2004
       
       }

s6 = {'precip_amt' : precip_amt6_2004,
      'humidity':humidity6_2004,
      'avg_temp':avg_temp6_2004,
        'y'   : Total_cases6_2004
       
       }
s7 = {'precip_amt' : precip_amt7_2004,
      'humidity':humidity7_2004,
      'avg_temp':avg_temp7_2004,
        'y'   : Total_cases7_2004
       
       }

s8 = {'precip_amt' : precip_amt8_2004,
      'humidity':humidity8_2004,
      'avg_temp':avg_temp8_2004,
        'y'   : Total_cases8_2004
       
       }


source = ColumnDataSource(d1)
source1 = ColumnDataSource(m1)
source2 = ColumnDataSource(s1)

p = figure(plot_width=400, plot_height=450, title="Total Dengue cases recorded in 2002 for the given climate values",
           toolbar_location=None, tools="")
p.circle(x='precip_amt', y='y',color="red",legend="precipitation",source=source,size=7)
p.circle(x='humidity', y='y',color="green",legend="humdity",source=source,size=7)
p.circle(x='avg_temp', y='y',color="blue",legend="average temp",source=source,size=7)

p.yaxis.axis_label = "Week of Year"
p.xaxis.axis_label = "Climate Variables"

p1 = figure(plot_width=400, plot_height=450, title="Total Dengue cases recorded in 2003 for the given climate values",
           toolbar_location=None, tools="")
p1.circle(x='precip_amt', y='y',color="red",legend="precipitation",source=source1,size=7)
p1.circle(x='humidity', y='y',color="green",legend="humdity",source=source1,size=7)
p1.circle(x='avg_temp', y='y',color="blue",legend="average temp",source=source1,size=7)
p1.yaxis.axis_label = "Week of Year"
p1.xaxis.axis_label = "Climate Variables"


p2 = figure(plot_width=400, plot_height=450, title="Total Dengue cases recorded in 2004 for the given climate values",
           toolbar_location=None, tools="")
p2.circle(x='precip_amt', y='y',color="red",legend="precipitation",source=source2,size=7)
p2.circle(x='humidity', y='y',color="green",legend="humdity",source=source2,size=7)
p2.circle(x='avg_temp', y='y',color="blue",legend="average temp",source=source2,size=7)
p2.yaxis.axis_label = "Week of Year"
p2.xaxis.axis_label = "Climate Variables"


select1 = Select(title="City 2002",  options=['New_London', 'Hartford','Middlesex','Fairfield','Litchfield',
                                             'Tolland','Windham','New_Haven'])
select2 = Select(title="City 2003",  options=['New_London', 'Hartford','Middlesex','Fairfield','Litchfield',
                                             'Tolland','Windham','New_Haven'])
select3 = Select(title="City 2004",  options=['New_London', 'Hartford','Middlesex','Fairfield','Litchfield',
                                             'Tolland','Windham','New_Haven'])

def update_plot(attrname, old, new):
    if select1.value == 'New_London':
        newSource = d1  
    if select1.value == 'Hartford':
        newSource = d2  
    if select1.value == 'Middlesex':
        newSource = d3  
    if select1.value == 'Fairfield':
        newSource = d4  
    if select1.value == 'Litchfield':
        newSource = d5  
    if select1.value == 'Tolland':
        newSource = d6  
    if select1.value == 'Windham':
        newSource = d7  
    if select1.value == 'New_Haven':
        newSource = d8        

    source.data =  newSource 

def update_plot1(attrname, old, new):
    if select2.value == 'New_London':
        newSource = m1  
    if select2.value == 'Hartford':
        newSource = m2  
    if select2.value == 'Middlesex':
        newSource = m3  
    if select2.value == 'Fairfield':
        newSource = m4  
    if select2.value == 'Litchfield':
        newSource = m5  
    if select2.value == 'Tolland':
        newSource = m6  
    if select2.value == 'Windham':
        newSource = m7  
    if select2.value == 'New_Haven':
        newSource = m8            

    source1.data =  newSource     

def update_plot2(attrname, old, new):
    if select3.value == 'New_London':
        newSource = s1  
    if select3.value == 'Hartford':
        newSource = s2  
    if select3.value == 'Middlesex':
        newSource = s3  
    if select3.value == 'Fairfield':
        newSource = s4  
    if select3.value == 'Litchfield':
        newSource = s5  
    if select3.value == 'Tolland':
        newSource = s6  
    if select3.value == 'Windham':
        newSource = s7  
    if select3.value == 'New_Haven':
        newSource = s8        

    source2.data =  newSource     
    
    
select1.on_change('value', update_plot)
select2.on_change('value', update_plot1)
select3.on_change('value', update_plot2)


layout1 = column(row(select1, width=400), p)
layout2 = column(row(select2, width=400), p1)
layout3 = column(row(select3, width=400), p2)

mylayout=row(layout1, layout2,layout3)


curdoc().add_root(mylayout) 
# js5, div5 = components(mylayout)
# cdn_js5 =CDN.js_files[0]
# cdn_css5 =CDN.css_files[0]

