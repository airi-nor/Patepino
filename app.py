import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title('わんちゃん')

# st.write('Interactive Widgets')


# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラムです')


# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)


# 'あなたの趣味:', text, 'です'
# 'コンディション:', condition

if st.checkbox('ぱっちゃん'):
    img = Image.open('patchan.jpeg')
    st.balloons()
    st.image(img)

if st.checkbox('ぴーちゃん'):
    img = Image.open('pichan.jpeg')
    st.balloons()
    st.image(img)

