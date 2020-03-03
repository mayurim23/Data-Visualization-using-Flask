import pandas as pd
import random
data= pd.read_csv("DV_Data.csv")
data['week_start_date'] =  pd.to_datetime(data['week_start_date']) 
data['week_start_date']=data.week_start_date.map(lambda x: x.strftime('%Y-%m-%d'))

from bokeh.models import ColumnDataSource,HoverTool
from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.models.widgets import Select,Panel,Tabs
from bokeh.io import curdoc
from bokeh.layouts import column, row,widgetbox
from bokeh.layouts import layout
from bokeh.io import curdoc
import pandas as pd
from bokeh.models.widgets import Paragraph

from bokeh.embed import components
from bokeh.resources import CDN
    
weekofyear1_2002=list(data[(data.year==2002) & (data.city=="New_London")].week_start_date)
totalcases1_2002=list(data[(data.year==2002) & (data.city=="New_London")].total_cases)


weekofyear2_2002=list(data[(data.year==2002) & (data.city=="Hartford")].week_start_date)
totalcases2_2002=list(data[(data.year==2002) & (data.city=="Hartford")].total_cases)


weekofyear3_2002=list(data[(data.year==2002) & (data.city=="Middlesex")].week_start_date)
totalcases3_2002=list(data[(data.year==2002) & (data.city=="Middlesex")].total_cases)

weekofyear4_2002=list(data[(data.year==2002) & (data.city=="Fairfield")].week_start_date)
totalcases4_2002=list(data[(data.year==2002) & (data.city=="Fairfield")].total_cases)

weekofyear5_2002=list(data[(data.year==2002) & (data.city=="Litchfield")].week_start_date)
totalcases5_2002=list(data[(data.year==2002) & (data.city=="Litchfield")].total_cases)

weekofyear6_2002=list(data[(data.year==2002) & (data.city=="Tolland")].week_start_date)
totalcases6_2002=list(data[(data.year==2002) & (data.city=="Tolland")].total_cases)


weekofyear7_2002=list(data[(data.year==2002) & (data.city=="Windham")].week_start_date)
totalcases7_2002=list(data[(data.year==2002) & (data.city=="Windham")].total_cases)


weekofyear8_2002=list(data[(data.year==2002) & (data.city=="New_Haven")].week_start_date)
totalcases8_2002=list(data[(data.year==2002) & (data.city=="New_Haven")].total_cases)



#################2003#########################################################################
weekofyear1_2003=list(data[(data.year==2003) & (data.city=="New_London")].week_start_date)
totalcases1_2003=list(data[(data.year==2003) & (data.city=="New_London")].total_cases)


weekofyear2_2003=list(data[(data.year==2003) & (data.city=="Hartford")].week_start_date)
totalcases2_2003=list(data[(data.year==2003) & (data.city=="Hartford")].total_cases)


weekofyear3_2003=list(data[(data.year==2003) & (data.city=="Middlesex")].week_start_date)
totalcases3_2003=list(data[(data.year==2003) & (data.city=="Middlesex")].total_cases)

weekofyear4_2003=list(data[(data.year==2003) & (data.city=="Fairfield")].week_start_date)
totalcases4_2003=list(data[(data.year==2003) & (data.city=="Fairfield")].total_cases)

weekofyear5_2003=list(data[(data.year==2003) & (data.city=="Litchfield")].week_start_date)
totalcases5_2003=list(data[(data.year==2003) & (data.city=="Litchfield")].total_cases)

weekofyear6_2003=list(data[(data.year==2003) & (data.city=="Tolland")].week_start_date)
totalcases6_2003=list(data[(data.year==2003) & (data.city=="Tolland")].total_cases)


weekofyear7_2003=list(data[(data.year==2003) & (data.city=="Windham")].week_start_date)
totalcases7_2003=list(data[(data.year==2003) & (data.city=="Windham")].total_cases)


weekofyear8_2003=list(data[(data.year==2003) & (data.city=="New_Haven")].week_start_date)
totalcases8_2003=list(data[(data.year==2003) & (data.city=="New_Haven")].total_cases)

###########################20004#########################################################################

weekofyear1_2004=list(data[(data.year==2004) & (data.city=="New_London")].week_start_date)
totalcases1_2004=list(data[(data.year==2004) & (data.city=="New_London")].total_cases)

weekofyear2_2004=list(data[(data.year==2004) & (data.city=="Hartford")].week_start_date)
totalcases2_2004=list(data[(data.year==2004) & (data.city=="Hartford")].total_cases)

weekofyear3_2004=list(data[(data.year==2004) & (data.city=="Middlesex")].week_start_date)
totalcases3_2004=list(data[(data.year==2004) & (data.city=="Middlesex")].total_cases)

weekofyear4_2004=list(data[(data.year==2004) & (data.city=="Fairfield")].week_start_date)
totalcases4_2004=list(data[(data.year==2004) & (data.city=="Fairfield")].total_cases)

weekofyear5_2004=list(data[(data.year==2004) & (data.city=="Litchfield")].week_start_date)
totalcases5_2004=list(data[(data.year==2004) & (data.city=="Litchfield")].total_cases)

weekofyear6_2004=list(data[(data.year==2004) & (data.city=="Tolland")].week_start_date)
totalcases6_2004=list(data[(data.year==2004) & (data.city=="Tolland")].total_cases)

weekofyear7_2004=list(data[(data.year==2004) & (data.city=="Windham")].week_start_date)
totalcases7_2004=list(data[(data.year==2004) & (data.city=="Windham")].total_cases)

weekofyear8_2004=list(data[(data.year==2004) & (data.city=="New_Haven")].week_start_date)
totalcases8_2004=list(data[(data.year==2004) & (data.city=="New_Haven")].total_cases)

d1 = {'weekofyear' : weekofyear1_2002,
      'totalcases':totalcases1_2002
       }

d2 = {'weekofyear' : weekofyear2_2002,
      'totalcases':totalcases2_2002
       }

d3 = {'weekofyear' : weekofyear3_2002,
      'totalcases':totalcases3_2002
       }

d4 = {'weekofyear' : weekofyear4_2002,
      'totalcases':totalcases4_2002
       }
d5 = {'weekofyear' : weekofyear5_2002,
      'totalcases':totalcases5_2002
       }

d6 = {'weekofyear' : weekofyear6_2002,
      'totalcases':totalcases6_2002
       }

d7 = {'weekofyear' : weekofyear7_2002,
      'totalcases':totalcases7_2002
       }

d8 = {'weekofyear' : weekofyear8_2002,
      'totalcases':totalcases8_2002
       }


####################2003####################################################################

m1 = {'weekofyear' : weekofyear1_2003,
      'totalcases':totalcases1_2003
       }

m2 = {'weekofyear' : weekofyear2_2003,
      'totalcases':totalcases2_2003
       }

m3 = {'weekofyear' : weekofyear3_2003,
      'totalcases':totalcases3_2003
       }

m4 = {'weekofyear' : weekofyear4_2003,
      'totalcases':totalcases4_2003
       }
m5 = {'weekofyear' : weekofyear5_2003,
      'totalcases':totalcases5_2003
       }

m6 = {'weekofyear' : weekofyear6_2003,
      'totalcases':totalcases6_2003
       }

m7 = {'weekofyear' : weekofyear7_2003,
      'totalcases':totalcases7_2003
       }

m8 = {'weekofyear' : weekofyear8_2003,
      'totalcases':totalcases8_2003
       }
############################################2004###################################

s1 = {'weekofyear' : weekofyear1_2004,
      'totalcases':totalcases1_2004
       }

s2 = {'weekofyear' : weekofyear2_2004,
      'totalcases':totalcases2_2004
       }

s3 = {'weekofyear' : weekofyear3_2004,
      'totalcases':totalcases3_2004
       }

s4 = {'weekofyear' : weekofyear4_2004,
      'totalcases':totalcases4_2004
       }
s5 = {'weekofyear' : weekofyear5_2004,
      'totalcases':totalcases5_2004
       }

s6 = {'weekofyear' : weekofyear6_2004,
      'totalcases':totalcases6_2004
       }

s7 = {'weekofyear' : weekofyear7_2004,
      'totalcases':totalcases7_2004
       }

s8 = {'weekofyear' : weekofyear8_2004,
      'totalcases':totalcases8_2004
       }

source = ColumnDataSource(d1)
source1 = ColumnDataSource(m1)
source2 = ColumnDataSource(s1)

p = figure(x_axis_type='datetime',plot_width=400, plot_height=450, title="Total Dengue cases recorded in 2002 for 52 weeks",toolbar_location=None, tools="")
p.vbar(x='weekofyear', top='totalcases',width=0.1,source=source)
#p.x_range = Range1d( start=pd.to_datetime('2008-03-01'), end= pd.to_datetime('2009-01-01') )


p1 = figure(x_axis_type='datetime',plot_width=400, plot_height=450, title="Total Dengue cases recorded in 2003 for 52 weeks",
           toolbar_location=None, tools="")
p1.vbar(x='weekofyear', top='totalcases',width=0.1,source=source1)
#p1.x_range = Range1d( start=pd.to_datetime('2008-03-01'), end= pd.to_datetime('2009-01-01') )

p2 = figure(x_axis_type='datetime',plot_width=400, plot_height=450, title="Total Dengue cases recorded in 2004 for 52 weeks",
           toolbar_location=None, tools="")
p2.vbar(x='weekofyear', top='totalcases',width=0.1,source=source2)
#p2.x_range = Range1d( start=pd.to_datetime('2008-03-01'), end= pd.to_datetime('2009-01-01') )

select1 = Select(title="2002",  options=['New_London', 'Hartford','Middlesex','Fairfield','Litchfield',
                                             'Tolland','Windham','New_Haven'])
select2 = Select(title="2003",  options=['New_London', 'Hartford','Middlesex','Fairfield','Litchfield',
                                             'Tolland','Windham','New_Haven'])
select3 = Select(title="2004",  options=['New_London', 'Hartford','Middlesex','Fairfield','Litchfield',
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

