import streamlit as st
from mlem.api import load
import mlem 
import json
import pandas as pd
import numpy as np
from PIL import Image
import requests
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
from pag1 import main as  pag1

def main():

    st.title('Pagina Principale')
    link = ['Modello']
    sim_selection = st.selectbox('Seleziona la pagina', link)

    if sim_selection == link[0]:
        pag1()
    else:
        st.markdown("Something went wrong. We are looking into it.")

    st.subheader('EDA')
    path = './dataframe.xlsx'
    df_clean = pd.read_csv(path, encoding='latin-1')
    st.subheader("Countplot of Price")
    figone = plt.figure(figsize=(12,8))
    sns.countplot(x='price',data=df_clean)
    st.pyplot(figone)

    st.subheader('Correlation Matrix')
    fig = plt.figure(figsize=(12,8))
    sns.heatmap(df_clean.corr(), annot=True, fmt='.2f')
    st.pyplot(fig)




















if __name__=="__main__":
    main()