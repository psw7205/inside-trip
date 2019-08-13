import matplotlib.pyplot as plt
import io
import base64
import folium
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import plotly

def folium_test():
    folium_map = folium.Map(location=[37.549554, 127.074984],
                            zoom_start=17)
    return folium_map._repr_html_()


def test1():
    plt.rcParams["font.family"] = "D2Coding ligature"
    data = pd.read_excel('temp/data/여행지별_국내여행_참가자_수_20190811234215.xlsx')

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
    data = pd.read_excel('temp/data/여행지별_국내여행_참가자_수_20190811234215.xlsx')


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

def test3():
    plt.rcParams["font.family"] = "D2Coding ligature"
    data = pd.read_excel('temp/data/여행지별_국내여행_참가자_수_20190811234215.xlsx')

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
    data = data.iloc[:, 3:]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=location,
                         y=data['15~19세'],
                         name='15~19세',
                         marker_color='rgb(255, 198, 255)'
                         ))
    fig.add_trace(go.Bar(x=location,
                         y=data['20대'],
                         name='20대',
                         marker_color='rgb(239, 144, 255)'
                         ))
    fig.add_trace(go.Bar(x=location,
                         y=data['30대'],
                         name='30대',
                         marker_color='rgb(185, 90, 225)'
                         ))
    fig.add_trace(go.Bar(x=location,
                         y=data['40대'],
                         name='40대',
                         marker_color='rgb(131, 36, 255)'
                         ))
    fig.add_trace(go.Bar(x=location,
                         y=data['50대'],
                         name='50대',
                         marker_color='rgb(77, 0, 237)'
                         ))
    fig.add_trace(go.Bar(x=location,
                         y=data['60대이상'],
                         name='60대',
                         marker_color='rgb(5, 0, 169)'
                         ))
    fig.update_layout(
        title='지역별 방문자 수',
        xaxis_tickfont_size=18,
        yaxis=dict(
            title='방문자수',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )

    import base64

    png = plotly.io.to_image(fig)

    imgdata = base64.b64encode(png).decode()
    return imgdata


