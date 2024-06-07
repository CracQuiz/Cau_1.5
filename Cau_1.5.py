import streamlit as st
import numpy as np
import pandas as pd

st.title('My first deployed DL model')
st.header('Header đây chứ đâu')
st.write('Đây là text')
st.markdown('**Markdown dây anh em ơi**')
st.text('Còn dưới đây là latex')
st.latex(r'''a + b = 3''')
st.write(12345)
code = '''def(hello):
            print("Hello world!")'''
st.code(code, language='python', line_numbers=True)
st.text('Hiển thị luôn cả chart')
data = np.random.randn(20, 3)
df = pd.DataFrame(data, columns=['a', 'b', 'c'])
st.line_chart(df)