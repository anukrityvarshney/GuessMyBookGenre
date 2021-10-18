import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow
import plotly.offline as pyoff
import plotly.graph_objs as go
pyoff.init_notebook_mode()

bookdata_path = 'book_data.csv'
testdata_path = 'book_data18.csv'
book = pd.read_csv(bookdata_path)
test = pd.read_csv(testdata_path)
book.columns

from langdetect import detect
def remove_invalid_lang(df):
    invalid_desc_idxs=[]
    for i in df.index:
        try:
            a=detect(df.at[i,'book_desc'])
        except:
            invalid_desc_idxs.append(i)
    
    df=df.drop(index=invalid_desc_idxs)
    return df
book = remove_invalid_lang(book)
test = remove_invalid_lang(test)

book[‘lang’]=book[‘book_desc’].map(lambda desc: detect(desc))
test['lang']=test['book_desc'].map(lambda desc: detect(desc))

lang_lookup = pd.read_html('https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes')[1]
langpd = lang_lookup[['ISO language name','639-1']]
langpd.columns = ['language','iso']
def desc_lang(x):
    if x in list(langpd['iso']):
        return langpd[langpd['iso'] == x]['language'].values[0]
    else:
        return 'nil'
book['language'] = book['lang'].apply(desc_lang)
test['language'] = test['lang'].apply(desc_lang)

book[‘lang’]=book[‘book_desc’].map(lambda desc: detect(desc))
test['lang']=test['book_desc'].map(lambda desc: detect(desc))
