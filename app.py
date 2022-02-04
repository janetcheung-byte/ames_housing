"""Main module for the streamlit app"""
import streamlit as st
import awesome_streamlit as ast
import src.pages.eda

import src.pages.home

ast.core.services.other.set_logging_format()

PAGES = {
    "Exploratory Data Analysis": src.pages.eda

}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)
    st.sidebar.title("Please review Jupyter Notebook code in Github:")
    st.sidebar.info(
        "[Jupyter Notebook](https://github.com/janetcheung-byte/ames_housing/blob/main/Ames_Housing_EDA.ipynb) "
    )
    st.sidebar.title("About")
    st.sidebar.info(
        """
        Data analysis by Janet Cheung
        
        Dataset was extracted from https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data?select=train.csv
        
"""
    )

 

if __name__ == "__main__":
    main()
 
    