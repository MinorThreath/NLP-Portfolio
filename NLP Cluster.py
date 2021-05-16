# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 10:25:11 2021

@author: andre
"""
import pandas as pd
import texthero as hero 
# from unidecode import unidecode 
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

#Lectura de archivo
Base = pd.read_excel('C:/Users/andre/OneDrive/Documentos/Especialización/SUPERVISADO.xlsx',header=0)

#Limpieza de los datos
Base['req_cl']= hero.clean(Base['req_estudio_req_experiencia'])
Base['req_cl']= [p for p in Base['req_cl'] if p not in stopwords.words("spanish")]
Base['prop_cl']= hero.clean(Base['proposito'])
Base['prop_cl']= [p for p in Base['prop_cl'] if p not in stopwords.words("spanish")]
Base['fx_cl']= hero.clean(Base['funciones'])
Base['fx_cl']= [p for p in Base['fx_cl'] if p not in stopwords.words("spanish")]

#Bags of Words
# create the transform
req = CountVectorizer(stop_words='spanish')
prop = CountVectorizer(stop_words='spanish')
fx= CountVectorizer(stop_words='spanish')
# tokenize and build vocab
req.fit(Base['req_cl'])
prop.fit(Base['prop_cl'])
fx.fit(Base['fx_cl'])
# # summarize
# print(req.vocabulary_)
# # encode document
vreq = req.transform(Base['req_cl'])
vprop= prop.transform(Base['prop_cl'])
vfx= fx.transform(Base['fx_cl'])

# summarize encoded vector
# print(vreq.shape)
# print(type(vreq))
# print(vreq.toarray())

# print(vreq.vocabulary_)



## Intentos previos

# print(Base.loc[Base['OPEC']==785,'proposito'])
# Base.loc[Base['OPEC']==785,'prop_cl']

# def prep (x):
#     #Poner en minusculas
#     x = x.lower()
#     print (x)
#     # Remover simbolos 
#     x = filter(str.isalnum,x)
#     print(x)
#     # Remover tildes
#     x = unidecode(x)
#     print(x)
#     # Remover stopwords
#     x = [p for p in x if p not in stopwords.words("spanish")]
#     print(x)
#     # Remover espacios en blanco
#     x=x.strip()
#     print(x)
#     return(x)

# Base['prop_cl']= prep(Base['proposito'])