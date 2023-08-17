import streamlit as st
import pandas as pd
from ydatapreprofiling import Profiler

def main():
    st.title("EDA App using ydata profiling")

    # Upload file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        st.write("Uploaded file:")
        st.write(uploaded_file.name)
        
        # Load data and generate profile
        df = pd.read_csv(uploaded_file)
        profiler = Profiler()
        profile = profiler.profile(df)
        
        # Display profile summary
        st.write("### Profile Summary")
        st.write(profile)
        
        # You can add more customizations, visualizations, and exploration widgets here

if __name__ == "__main__":
    main()
