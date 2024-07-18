import streamlit as st
import pickle
import numpy as np
st.title("K-Nearest Neighbor(KNN) model with 97% Accuracy")

st.header("Check weather patient have Cancer Or Not")
model=pickle.load(open(r"C:\Users\dell\OneDrive\Documents\deploy2\knn_model.pkl",'rb'))


clump_thinkness=st.slider('Clump_thickness',min_value=-1,max_value=3)
cell_size=st.slider("Uniformity_Cell_Size",min_value=-6,max_value=3)
cell_shape=st.slider("Uniformity_Cell_Shape",min_value=-7,max_value=3)
marginal_adesian=st.slider("Marginal_Adhesion ",min_value=-6,max_value=3)
Single_Epithelial_Cell_Size=st.slider("Single_Epithelial_Cell_Size",min_value=-1,max_value=4)
bar_neclei=st.slider("Bare_Nuclei",min_value=-6,max_value=2)
bland_chromin=st.slider("Bland_Chromatin",min_value=-9,max_value=3)
normal_nucleiu=st.slider("Normal_Nucleoli",min_value=-6,max_value=3)
mitoses=st.slider("Mitoses",min_value=-3,max_value=6)

query=np.array([clump_thinkness,cell_size,cell_shape,marginal_adesian,Single_Epithelial_Cell_Size,bar_neclei,bland_chromin,normal_nucleiu,mitoses])
if st.button("predict"):
    query=query.reshape(1,9)
    res=model.predict(query)[0]
    if res==2:
        st.header("Patient don't have Cancer")
    else:
        st.header("Patient have Cancer")

    



