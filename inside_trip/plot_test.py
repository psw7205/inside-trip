import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import folium
import pandas as pd
import seaborn as sns


def folium_test():
    folium_map = folium.Map(location=[37.549554, 127.074984],
                            zoom_start=17)
    return folium_map._repr_html_()


def test1():
    plt.rcParams["font.family"] = "D2Coding ligature"
    data = pd.read_excel('data/여행지별_국내여행_참가자_수_20190811234215.xlsx')
    data = data.iloc[:, 1:]
    location = ['기준', '서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
                '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
    data.columns = location
    data = data.iloc[1:10, :]
    age = list(data['기준'])
    data.index = age
    data = data.drop('기준', axis=1)
    data.iloc[0, :]

    data = data.T
    data = data.sort_values('소계', ascending=False)

    img = io.BytesIO()
    plt.figure(figsize=(10, 6))
    plt.title('인기많은 관광지순위')
    sns.barplot(x=data.index, y='소계', data=data)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return plot_url


def test2():
    plt.rcParams["font.family"] = "D2Coding ligature"
    data = pd.read_excel('data/여행지별_국내여행_참가자_수_20190811234215.xlsx')
    data = data.iloc[:, 1:]
    location = ['기준', '서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종',
                '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
    data.columns = location
    data = data.iloc[1:10, :]
    age = list(data['기준'])
    data.index = age
    data = data.drop('기준', axis=1)
    data.iloc[0, :]

    data = data.T
    data = data.sort_values('소계', ascending=False)

    img = io.BytesIO()
    plt.figure(figsize=(10, 6))
    plt.title('20대')
    sns.violinplot(x='소계', y=data.index, data=data, dodge=False)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return plot_url
