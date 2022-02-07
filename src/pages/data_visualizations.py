
import streamlit as st
 
import holoviews as hv
import hvplot.pandas
import pandas as pd
import panel as pn
from panel.interact import interact
import plotly.express as px
pn.extension("plotly")

#BASE=os.path.dirname(os.path.abspath("__file__"))
csv_path=path="train.csv"

read_csv=pd.read_csv(csv_path)
df=read_csv.copy()

hist_plot=df.hvplot.hist("SalePrice",xformatter='$%.0f', title='Distribution of Home Prices: Ames, Iowa 2006-2011', ylabel='Count', xlabel=' Sales Price (USD)')

box_plot=df.hvplot.box(y='SalePrice', by='OverallQual', yformatter='$%.0f', ylabel='Sales Price (USD)', 
            xlabel='Overall Quality of Home', title='Comparing Home Prices: Ames, Iowa 2006-2011', ).sort()

bar_count=df.Electrical.value_counts().hvplot.bar(title='Count of Homes by Electrical Types', ylabel='Count', xlabel='Electrical Types', rot=90)

cols=['MoSold', 'YrSold']
df['date'] = df[cols].apply(lambda x: '-'.join(x.values.astype(str)), axis="columns")
df['date']=pd.to_datetime(df['date'])
homes_sold_month=df.groupby('date').size().reset_index(name='number_of_homes_sold')
line_chart=homes_sold_month.hvplot.line(x='date', y='number_of_homes_sold', title='Number of Homes Sold by Month')

heatmap = df.corr().hvplot.heatmap(rot=90,  height=600, width=700)

scatt_plot=df.hvplot.scatter(x='1stFlrSF',y='SalePrice', title='Home Size and Sales Price', xlabel='Sq Ft on First Floor', ylabel='Sales Price (USD)', yformatter='$%.0f')
scatt_best_fit_line=scatt_plot.opts(size=10) * hv.Slope.from_scatter(scatt_plot ).opts(color='red')

row1 = pn.Row(pn.Card(hist_plot), pn.Card(box_plot))
row2= pn.Row( pn.Card(bar_count) , pn.Card(line_chart))
row3 = pn.Row(pn.Card(  heatmap),  pn.Card(scatt_best_fit_line))

# Create panels to structure the layout of the dashboard
column1 = pn.Column(
    "## row1 + row2", 
    row1,
    row2,
    row3
)

# Create tabs
dashboard = pn.Tabs(
    ("Test tab", column1)
)

#dashboard.servable()

#dashboard.show()

def write():

    st.write(hv.render(dashboard.show()))
    #st.write(hv.render(dashboard.show()), backend='bokeh')
    
