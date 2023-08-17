import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def main():
    st.title("EDA App using pandas_profiling")

    # Upload file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        st.write("Uploaded file:")
        st.write(uploaded_file.name)

        # Load data
        df = pd.read_csv(uploaded_file)

        # Generate EDA report
        profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

        # Display the EDA report
        st.header("Exploratory Data Analysis")
        st_profile_report(profile)

if __name__ == "__main__":
    main()
