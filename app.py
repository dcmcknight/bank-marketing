import streamlit as st
from multiapp import MultiApp
from apps import  EDA, model # import your app modules here
import numpy as np
import pandas as pd
import joblib
import pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


app = MultiApp()


# Add all your application here
app.add_app("EDA", EDA.app)
app.add_app("Model", model.app)
# The main app
app.run()


