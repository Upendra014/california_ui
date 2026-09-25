#step1-->import libraries
import numpy as np
import joblib
import streamlit as st

#Step2-->Load the model
obj = joblib.load('california.joblib')
model = obj['model']
cols = obj['columns']

#Step3-->Setting up the UI

st.title('california app')
Input =[]
for i in cols:
  v = st.number_input(f'Enter {i} value')
  Input.append(v)
if st.button('click'):
  In = np.array([Input])
  out = model.predict(In)
  st.success(f"The median House value is:{out}")