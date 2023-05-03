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







def main():
    model = mlem.api.load('model_.mlem')
    path = './dataframe.xlsx'
    df = pd.read_csv(path,encoding='latin-1')


    crime_rate = st.number_input('Inserisci il crimine', 0.0, None, 1.00)
    zn = st.number_input('zn',0.0, None, 1.00)
    ind = st.number_input('Inserisci industria', 0.0, None, 1.00)
    chas = st.number_input('Comprehensive Housing Affordability Strategy', 0, None, 1.00)
    nox = st.number_input('Polveri sottili', 0.0, None, 1.00)
    rm = st.number_input('rm', 0.0, None, 1.00)
    age = st.number_input('Età casa', 0.0, None, 1.00)
    dis = st.number_input('Distanza dal centro', 0.0, None, 1.00)
    rad = st.number_input('rad', 0.0, None, 1.00)
    tax = st.number_input('valore catastale', 0.0, None, 1.00)
    ptratio = st.number_input('ptRatio', 0.0, None, 1.00)
    b = st.number_input('b', 0.0, None, 1.00)
    Istat = st.number_input('Indice Istat', 0.0, None, 1.00)


    model.predict([[np.float32(crime_rate),np.float32(zn),np.float32(ind),np.float32(chas),np.float32(nox),np.float32(rm),np.float32(age),np.float32(dis),np.float32(rad),np.float32(tax),np.float32(ptratio),np.float32(b),np.float32(Istat)]])[0]

if __name__=="__main__":
    main()