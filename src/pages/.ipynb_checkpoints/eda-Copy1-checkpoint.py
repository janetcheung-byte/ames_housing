# import libraries
pd.set_option('plotting.backend', 'pandas_bokeh')
import streamlit as st
import holoviews as hv
hv.extension('bokeh')
import pandas as pd
import matplotlib.pyplot as plt
import hvplot.pandas 
import datetime

%matplotlib inline


def write():
    """Used to write the page in the dashboard_instagram_post.py file"""
    with st.spinner("Loading data analysis and visualization ..."):

        
        
        
        if st.checkbox('Show dataframe'):
            # create dataframe instance
            read_csv=pd.read_csv("train.csv")
            df=read_csv.copy()
            df
            
        st.markdown(body, unsafe_allow_html=False)

        # Select dataframe column names to produce visual graph 
        if st.sidebar.checkbox('Select your chart'):
            plots = f.dictValues()
            plot = st.selectbox("Select your chart.", list(plots.keys()))
            'You selected: ', plot
            st.write(hv.render(plots[plot].hvplot(kind='bar',x='date',by='post id', stacked=True, rot=90, use_container_width=True, width=2000, height=1000), backend='bokeh'))# Visual graph
            
        # See post id content
        if st.sidebar.checkbox('Show Post ID content'):
            values = idContent.index.to_list()
            options = idContent['Post caption'].tolist()
            dic = dict(zip(options, values))
            a=st.selectbox('Choose a post id', options, format_func=lambda x: dic[x])
            st.write(a)
            
         # Popular posts by post ids
        if st.sidebar.checkbox('Show popular posts by id'):
            plots = f.topPosts()
            plot = st.selectbox("Select your chart.", list(plots.keys()))
            'You selected: ', plot
            st.write(hv.render(plots[plot].hvplot(kind='bar',x='id_date', stacked=True, rot=90, use_container_width=True, width=2000, height=1000), backend='bokeh'))# Visual graph
            

        # Post average calculation visual graph
        if st.sidebar.checkbox('Show Post Average Calculation '):
            st.write(hv.render(f.postAvg().hvplot(kind='line',x='date', rot=90, use_container_width=True, title="Post Average Calculation"), backend='bokeh'))
            st.write("Can the data answer the questions?")
            
            
 
        # Options to show dataframe   
        if st.sidebar.checkbox('Show dataframe'):
            st.dataframe(df.style.highlight_max(axis=0))
            
        
       


           
    