import pandas as pd
import streamlit as st


path = ''
tips = pd.read_csv(path)
tips = pd.DataFrame(tips)
new = tips[['total_bill','tip']]
new_data = tips.groupby('day')[['tip', 'total_bill']].sum()


st.title('Чаевые по доходу ресторана CHIPO')
page_name = ['Связь чаевых и выручки за все время', 'Связь чаевых и выручки по дням недели']
page = st.radio('Сhart', page_name)
st.write('**VARIABLE CHARTS**')

if page == 'Связь чаевых и выручки за все время':
    st.subheader('*Связь чаевых и выручки за все время*')
    st.write('NICE **ЧАЕВЫЕ**')
    st.area_chart(data = new, width = 0, height= 0)
else:
    st.subheader('*Сумма чаевых и выручки по дням недели*')
    st.write('NICE **ВЫРУЧКА**')
    st.bar_chart(data = new_data, width = 0, height= 0)
    

