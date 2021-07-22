#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# Constantes
cuadriculaVisible = True

# Selección y lectura del archivo .csv

#Izquierda
nombreArchivoI = 'DatosManoIzquierda.csv'
dfI = pd.read_csv(nombreArchivoI)

#Derecha
nombreArchivoD = 'DatosManoDerecha.csv'
dfD = pd.read_csv(nombreArchivoD)

# Crear una columna de tiempo que inicie en cero para usarla como entrada
dfI['time'] = 0.001*(dfI['timestamp2001_ms']-dfI['timestamp2001_ms'][0])
colsI = dfI.columns.tolist()
colsI = colsI[-1:]+colsI[1:-1]
paramsI = dfI[colsI].set_index('time')

dfD['time'] = 0.001*(dfD['timestamp2001_ms']-dfD['timestamp2001_ms'][0])
colsD = dfD.columns.tolist()
colsD = colsD[-1:]+colsD[1:-1]
paramsD = dfD[colsD].set_index('time')

#Extracción de las columnas velocidad angular en x, y y z
dataI = np.array(paramsI)
rotXI = dataI[:,3]
rotYI = dataI[:,4]
rotZI = dataI[:,5]

dataD = np.array(paramsD)
rotXD = dataD[:,3]
rotYD = dataD[:,4]
rotZD = dataD[:,5]

# RMS de los datos

RMSrotXI = math.degrees(np.sqrt(np.mean(rotXI**2)))
RMSrotYI = math.degrees(np.sqrt(np.mean(rotYI**2)))
RMSrotZI = math.degrees(np.sqrt(np.mean(rotZI**2)))
RMSaveI = math.log10((RMSrotXI + RMSrotYI + RMSrotZI)/3)
RMSaveI = str(RMSaveI)

RMSrotXD = math.degrees(np.sqrt(np.mean(rotXD**2)))
RMSrotYD = math.degrees(np.sqrt(np.mean(rotYD**2)))
RMSrotZD = math.degrees(np.sqrt(np.mean(rotZD**2)))
RMSaveD = math.log10((RMSrotXD + RMSrotYD + RMSrotZD)/3)
RMSaveD = str(RMSaveD)

# Creación archivo .txt

intensidad = open("datos.txt","w") #Se crea en la misma carpeta donde se ejecuta el script, si ya existe una con el nombre la reemplaza
intensidad.write(RMSaveI+', ')
intensidad.write(RMSaveD)
intensidad.close()


# In[ ]:




