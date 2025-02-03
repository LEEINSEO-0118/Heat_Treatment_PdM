import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')
import time


DATA_URL = ('Data/anomaly_data.csv')
@st.cache_data # for loading Dataframe from csv, etc ...
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    # lowercase = lambda x: str(x).lower()
    # data.rename(lowercase, axis='columns', inplace=True)
    return data

# 초기 데이터 로드 (50개 행)
data = load_data(50)
columns = data.columns[1:].values # time stamp 제외

# 페이지 설정
st.set_page_config(layout="wide")
st.title('Heat Treament Dashboard')
st.write('Welcome to the Heat Treatment Dashboard!')

# 실시간 차트 초기화
sensor_num = len(columns)-2 # outliers_cnt, anomaly 제외
col_num = 4
row_num = (sensor_num // 4) + (1 if sensor_num % col_num > 0 else 0)

# 차트를 업데이트할 공간
st.title('Sensor Data')
chart_placeholders = []

for row in range(row_num):
    cols = st.columns(col_num)  # 3개의 컬럼 생성
    for col_idx in range(col_num):
        sensor_idx = row * col_num + col_idx
        if sensor_idx < sensor_num:
            with cols[col_idx]:
                st.text(columns[sensor_idx])  # 센서 이름 표시
                chart_placeholders.append(cols[col_idx].empty())  # 차트 자리 확보

while True:
    new_data = load_data(1)
    data = pd.concat([data.iloc[1:], new_data], ignore_index=True)  # 오래된 데이터 삭제 후 추가

    for i, chart in enumerate(chart_placeholders):
        chart.line_chart(data[columns[i]])  # 실시간 차트 업데이트

    time.sleep(1)  # 1초마다 갱신