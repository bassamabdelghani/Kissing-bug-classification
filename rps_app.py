# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 20:26:12 2020

@author: Bassam
"""


import tensorflow as tf
import streamlit as st
import cv2
from PIL import Image, ImageOps
import numpy as np

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Kissing bug classification 🐛")
st.write("This is a simple image classification web app to predict if a bug is kissing bug on non kissing bug")

st.sidebar.subheader("Choose user type : ")
user_classifier=st.sidebar.selectbox("user type",("Normal User","Researcher" ))

model_kissing = tf.keras.models.load_model('kissing non kissing  - New model - 6 layers.h5')
model_kissing = tf.keras.models.load_model('kissing non kissing  - New model - 6 layers.h5')
model_mexico = tf.keras.models.load_model('Mexico 12 spices - New model - 6 layers.h5')
model_brazil = tf.keras.models.load_model('Brazil_Dataset-39 - New model - 6 layers.h5')

def import_and_predict(image_data, model):
    
        size = (150,150)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_resize = (cv2.resize(img, dsize=(224, 224),    interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img_resize[np.newaxis,...]
    
        prediction = model.predict(img_reshape)
        
        return prediction

FILE_TYPES = ["png", "jpg", "jpeg","bmp"]


if user_classifier =='Normal User':
    st.subheader("Kissing or non kissing bug classification")
    file_kissing_normal = st.file_uploader("Please upload an image file", type=FILE_TYPES,key='file_kissing_normal')
    if file_kissing_normal is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file_kissing_normal)
        st.image(image, use_column_width=True)
        prediction = import_and_predict(image, model_kissing)
        
        if np.argmax(prediction) == 0:
            st.write("It is a Kissing bug!")
            st.write("Please do not ever touch it with your bare hands")
            st.write("please write down the date, time of day you found it, where it was caught (indoors or outdoors)")
            st.write("you can submit it to: https://www.dshs.texas.gov/idcu/health/zoonosis/Triatominae/")
            
        else:
            st.write("It is a Non Kissing bug!")
        
       
    
    
if user_classifier =='Researcher':    
    st.subheader("Kissing or non kissing bug classification")
    file_kissing = st.file_uploader("Please upload an image file", type=FILE_TYPES,key='file_kissing')
    if file_kissing is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file_kissing)
        st.image(image, use_column_width=True)
        prediction = import_and_predict(image, model_kissing)
        
        if np.argmax(prediction) == 0:
            st.write("It is a Kissing bug!")
        else:
            st.write("It is a Non Kissing bug!")
        
        st.text("Probability (0: Kissing bugs, 1: Non Kissing bugs")
        st.write(prediction)
    
    st.subheader("Mexico species classification")
    file_mexico = st.file_uploader("Please upload an image file", type=FILE_TYPES,key='file_mexico')
    if file_mexico is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file_mexico)
        st.image(image, use_column_width=True)
        prediction = import_and_predict(image, model_mexico)
        
        if np.argmax(prediction) == 0:
            st.write("It is a Panstrongylus rufotuberculatus!")
        elif np.argmax(prediction) == 1:
            st.write("It is a Triatoma barberi!")
        elif np.argmax(prediction) == 2:
            st.write("It is a Triatoma dimidiata H1!")
        elif np.argmax(prediction) == 3:
            st.write("It is a Triatoma dimidiata H2!")
        elif np.argmax(prediction) == 4:
            st.write("It is a Triatoma dimidiata H3!")
        elif np.argmax(prediction) == 5:
            st.write("It is a Triatoma gerstaeckeri!")
        elif np.argmax(prediction) == 6:
            st.write("It is a Triatoma longipennis!")
        elif np.argmax(prediction) == 7:
            st.write("It is a Triatoma mazzotti!")
        elif np.argmax(prediction) == 8:
            st.write("It is a Triatoma mexicana!")
        elif np.argmax(prediction) == 9:
            st.write("It is a Triatoma nitida!")
        elif np.argmax(prediction) == 10:
            st.write("It is a Triatoma pallidipennis!")
        else:
            st.write("It is a Triatoma phyllosoma!")
        
        st.text("Probability (0: Panstrongylus rufotuberculatus, 1: Triatoma barberi, 2: Triatoma dimidiata H1, 3: Triatoma dimidiata H2, 4: Triatoma dimidiata H3, 5: Triatoma gerstaeckeri, 6: Triatoma longipennis, 7: Triatoma mazzotti, 8: Triatoma mexicana, 9: Triatoma nitida, 10: Triatoma pallidipennis, 11: Triatoma phyllosoma")
        st.write(prediction)
    
    st.subheader("Brazil species classification")
    file_brazil = st.file_uploader("Please upload an image file", type=FILE_TYPES,key='file_brazil')
    if file_brazil is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file_brazil)
        st.image(image, use_column_width=True)
        prediction = import_and_predict(image, model_brazil)
        
        if np.argmax(prediction) == 0:
            st.write("It is a Cavernicola lenti!")
        elif np.argmax(prediction) == 1:
            st.write("It is a Panstrongylus diasi!")
        elif np.argmax(prediction) == 2:
            st.write("It is a Panstrongylus geniculatus!")
        elif np.argmax(prediction) == 3:
            st.write("It is a Panstrongylus lignarius!")
        elif np.argmax(prediction) == 4:
            st.write("It is a Panstrongylus lutzi!")
        elif np.argmax(prediction) == 5:
            st.write("It is a Panstrongylus megistus!")
        elif np.argmax(prediction) == 6:
            st.write("It is a Psammolestes tertius!")
        elif np.argmax(prediction) == 7:
            st.write("It is a Rhodnius brethesi!")
        elif np.argmax(prediction) == 8:
            st.write("It is a Rhodnius domesticus!")
        elif np.argmax(prediction) == 9:
            st.write("It is a Rhodnius milesi!")
        elif np.argmax(prediction) == 10:
            st.write("It is a Rhodnius montenegrensis!")
        elif np.argmax(prediction) == 11:
            st.write("It is a Rhodnius nasutus!")
        elif np.argmax(prediction) == 12:
            st.write("It is a Rhodnius neglectus!")
        elif np.argmax(prediction) == 13:
            st.write("It is a Rhodnius pictipes!")
        elif np.argmax(prediction) == 14:
            st.write("It is a Triatoma arthurneivai!")
        elif np.argmax(prediction) == 15:
            st.write("It is a Triatoma baratai!")
        elif np.argmax(prediction) == 16:
            st.write("It is a Triatoma brasiliensis!")
        elif np.argmax(prediction) == 17:
            st.write("It is a Triatoma carcavalloi!")
        elif np.argmax(prediction) == 18:
            st.write("It is a Triatoma circunmaculata!")
        elif np.argmax(prediction) == 19:
            st.write("It is a Triatoma costalimai!")
        elif np.argmax(prediction) == 20:
            st.write("It is a Triatoma delpontei!")
        elif np.argmax(prediction) == 21:
            st.write("It is a Triatoma dimidiata H21!")
        elif np.argmax(prediction) == 22:
            st.write("It is a Triatoma guazu!")
        elif np.argmax(prediction) == 23:
            st.write("It is a Triatoma infestans!")
        elif np.argmax(prediction) == 24:
            st.write("It is a Triatoma juazeirensis!")
        elif np.argmax(prediction) == 25:
            st.write("It is a Triatoma lenti!")
        elif np.argmax(prediction) == 26:
            st.write("It is a Triatoma maculata!")
        elif np.argmax(prediction) == 27:
            st.write("It is a Triatoma matogrossensis!")
        elif np.argmax(prediction) == 28:
            st.write("It is a Triatoma melanica!")
        elif np.argmax(prediction) == 29:
            st.write("It is a Triatoma pintodiasi!")
        elif np.argmax(prediction) == 30:
            st.write("It is a Triatoma platensis!")
        elif np.argmax(prediction) == 31:
            st.write("It is a Triatoma pseudomaculata!")
        elif np.argmax(prediction) == 32:
            st.write("It is a Triatoma rubrovaria!")
        elif np.argmax(prediction) == 33:
            st.write("It is a Triatoma sherlocki!")
        elif np.argmax(prediction) == 34:
            st.write("It is a Triatoma sordida!")
        elif np.argmax(prediction) == 35:
            st.write("It is a Triatoma tibiamaculata!")
        elif np.argmax(prediction) == 36:
            st.write("It is a Triatoma vandae!")
        elif np.argmax(prediction) == 37:
            st.write("It is a Triatoma vitticeps!")
        else:
            st.write("It is a Triatoma williami!")
        
        st.text("Probability (0: Cavernicola lenti, 1: Panstrongylus diasi, 2: Panstrongylus geniculatus, 3: Panstrongylus lignarius,4: Panstrongylus lutzi, 5: Panstrongylus megistus, 6: Psammolestes tertius, 7: Rhodnius brethesi, 8: Rhodnius domesticus, 9: Rhodnius milesi, 10: Rhodnius montenegrensis, 11: Rhodnius nasutus, 12: Rhodnius neglectus, 13: Rhodnius pictipes,                    14: Triatoma arthurneivai, 15: Triatoma baratai, 16: Triatoma brasiliensis, 17: Triatoma carcavalloi, 18: Triatoma circunmaculata, 19: Triatoma costalimai, 20: Triatoma delpontei, 21: Triatoma dimidiata H21, 22: Triatoma guazu,23: Triatoma infestans, 24: Triatoma juazeirensis, 25: Triatoma lenti,26: Triatoma maculata, 27: Triatoma matogrossensis, 28: Triatoma melanica, 29: Triatoma pintodiasi, 30: Triatoma platensis,31: Triatoma pseudomaculata, 32: Triatoma rubrovaria, 33: Triatoma sherlocki, 34: Triatoma sordida, 35: Triatoma tibiamaculata, 36: Triatoma vandae, 37: Triatoma vitticeps, 38: Triatoma williami")
        
    
        st.write(prediction)



    

    


    

