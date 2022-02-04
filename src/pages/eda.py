# import libraries
 
import holoviews as hv

import streamlit as st
import hvplot.pandas
import pandas as pd
import datetime
 



def write():
    """Used to write the page in the dashboard_instagram_post.py file"""
    with st.spinner("Loading data analysis and visualization ..."):

        
        st.title("Exploratory Data Analysis of Ames, Iowa Housing data")
        
        st.markdown("---")


        st.markdown('#### Select this if you want to see data set:', unsafe_allow_html=False)
        read_csv=pd.read_csv("train.csv")
        df=read_csv.copy()
        
            
        if st.checkbox('Show dataframe'):
            with st.echo():
                # Extract csv data and store the data into "df" variable.
                read_csv=pd.read_csv("train.csv")
                df=read_csv.copy()
            # create dataframe instance
            st.dataframe(df)
            
        st.markdown('#### 1)Can the data answer the questions?', unsafe_allow_html=False)
        st.markdown('* From my observation at the data, the following information is present to make an estimate for a home\'s sales prices: size, number of bedrooms, number of bathrooms, the year it was built, and ordinal data (Overall quality of the home, 1-10, 10 being "Very Excellent"). As well as nominal data (Neighborhood), and a host of other features. So far, the data passes an initial sniff test.')
        
        st.markdown("---")
        
        
        
        hist_plot=df.hvplot.hist("SalePrice",xformatter='$%.0f', title='Distribution of Home Prices: Ames, Iowa 2006-2011', ylabel='Count', xlabel=' Sales Price (USD)')
  
        st.write("I will use the describe method to generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset's distribution, excluding``NaN`` values.")
        
        with st.echo():
            df.SalePrice.describe()
           
        st.write(df.SalePrice.describe())  

        # Sum of houses with sale price in the $200,000 range
        with st.echo():
            hist_df=hist_plot.dframe()
            hist_df[(hist_df['SalePrice']>=200000) & (hist_df['SalePrice']<=299999)].sum()['SalePrice_count']
           
        st.write(hist_df=hist_plot.dframe())
        st.write(hist_df[(hist_df['SalePrice']>=200000) & (hist_df['SalePrice']<=299999)].sum()['SalePrice_count'])
        
        
        st.markdown("#### A histogram showing the shape of sales price")
        if st.checkbox('Show distribution of home Prices'):
            with st.echo():
                hist_plot=df.hvplot.hist("SalePrice",xformatter='$%.0f', title='Distribution of Home Prices: Ames, Iowa 2006-2011', ylabel='Count', xlabel=' Sales Price (USD)')
            
            st.write(hv.render(hist_plot), backend='bokeh')
        
           
        st.markdown(" * There are total of 230 homes in the $200,000 range, and a long tail to the right showing the most expensive homes. That tail pulls the mean sales price \($181,000\) past the median price \(\$163,000\). A handful of expensive homes makes the mean larger than the median value.", unsafe_allow_html=False)
        
        st.markdown("---")
        
        st.markdown("#### Using box plots to compare sale prices at different quality rankings")
        
        box_plot=df.hvplot.box(y='SalePrice', by='OverallQual', yformatter='$%.0f', ylabel='Sales Price (USD)', 
              xlabel='Overall Quality of Home', title='Comparing Home Prices: Ames, Iowa 2006-2011', ).sort()
        
        if st.checkbox('Show box plot chart: Comparing home Prices'):
            with st.echo():
                box_plot=df.hvplot.box(y='SalePrice', by='OverallQual', yformatter='$%.0f', ylabel='Sales Price (USD)', 
              xlabel='Overall Quality of Home', title='Comparing Home Prices: Ames, Iowa 2006-2011', ).sort()
            
            st.write(hv.render(box_plot), backend='bokeh')
            
        st.markdown("* Here, the relationship between overall quality and home prices feels intuitive. Higher-quality homes typically have a higher sales price. We can spot a $200,000 home with an overall quality score of 10 (the bottom tip of the line), but it seems reasonable to assume it sold for less than other perfect-10 homes due to other factors.", unsafe_allow_html=False)
        st.markdown("---")
        st.markdown("#### A bar chart showing the counts by types of electrical installation")
        # A bar chart showing the counts by types of electrical installation
        bar_count=df.Electrical.value_counts().hvplot.bar(title='Count of Homes by Electrical Types', ylabel='Count', xlabel='Electrical Types')
        
        if st.checkbox('Show bar plot chart: Count of Homes by Electrical Types'):
            with st.echo():
                bar_count=df.Electrical.value_counts().hvplot.bar(title='Count of Homes by Electrical Types', ylabel='Count', xlabel='Electrical Types')
            
            st.write(hv.render(bar_count), backend='bokeh')
            
        st.markdown('* Does the data make intuitive sense?')
        st.markdown('* This bar chart shows almost all homes have the same value for this feature. This information is helpful. Since most homes have the same value for this variable, it likely won\'t contribute to any meaningful differences in the sales price of homes.')
        st.markdown("---")
        
        st.markdown("#### A line chart showing the number of houses sold in different months") 
        
        # Combining column "MoSold" and "YrSold" into a new column "date" , parse values as string and then converting the values into datetime object

        cols=['MoSold', 'YrSold']
        df['date'] = df[cols].apply(lambda x: '-'.join(x.values.astype(str)), axis="columns")
        df['date']=pd.to_datetime(df['date'])
        homes_sold_month=df.groupby('date').size().reset_index(name='number_of_homes_sold')
        line_chart=homes_sold_month.hvplot.line(x='date', y='number_of_homes_sold', title='Number of Homes Sold by Month')
        
        if st.checkbox('Show line chart: Number of Homes Sold by Month'):
            with st.echo():
                cols=['MoSold', 'YrSold']
                df['date'] = df[cols].apply(lambda x: '-'.join(x.values.astype(str)), axis="columns")
                df['date']=pd.to_datetime(df['date'])
                homes_sold_month=df.groupby('date').size().reset_index(name='number_of_homes_sold')
                line_chart=homes_sold_month.hvplot.line(x='date', y='number_of_homes_sold', title='Number of Homes Sold by Month')
            st.write(hv.render(line_chart), backend='bokeh')
            
        st.markdown("* This data visualization display seasonality where home sales spike in summer and retract in the winter")
        st.markdown("---")
        
        # A scatter plot showing square footage and sales price
        st.markdown("#### A scatter plot showing square footage and sales price")
        scatt_plot=df.hvplot.scatter(x='1stFlrSF',y='SalePrice', title='Home Size and Sales Price', xlabel='Sq Ft on First Floor', ylabel='Sales Price (USD)', yformatter='$%.0f')
        
        if st.checkbox('Show scatter plot: square footage and sales price'):
            with st.echo():
                scatt_plot=df.hvplot.scatter(x='1stFlrSF',y='SalePrice', title='Home Size and Sales Price', xlabel='Sq Ft on First Floor', ylabel='Sales Price (USD)', yformatter='$%.0f')
            st.write(hv.render(scatt_plot), backend='bokeh') 
            
        st.markdown('#### 2)Did you discover any relationship?')
        st.markdown("* This scatter plot shows higher overall quality and larger square footage are related to higher sales prices.")
        
        st.markdown("---")
        
        st.markdown("#### What other variables share a relationship with sales price?")
        st.markdown("* If you look at the heatmap plot below, it looks like ' GarageArea', 'GarageCars', and 'GrLivArea' have a strong correlation with sales price")
        
        heatmap = df.corr().hvplot.heatmap(rot=90,  height=600, width=700)
        
        if st.checkbox('Heatmap: Correlation'):
            with st.echo():
                heatmap = df.corr().hvplot.heatmap(rot=90,  height=600, width=700)
            st.write(hv.render(heatmap), backend='bokeh') 
            
        corr=scatt_plot.dframe().corr()
        with st.echo():
                scatt_plot.dframe().corr()
        st.write(corr)
        st.markdown("* Square footage and sales price have a correlation of 0.62, which measures the tightness of the data points around the solid linear trend line.")
        scatt_best_fit_line=scatt_plot.opts(size=10) * hv.Slope.from_scatter(scatt_plot ).opts(color='red')
        if st.checkbox('Show scatter plot with best fit line'):
            with st.echo():
                scatt_best_fit_line=scatt_plot.opts(size=10) * hv.Slope.from_scatter(scatt_plot ).opts(color='red')
            st.write(hv.render(scatt_best_fit_line), backend='bokeh') 
        