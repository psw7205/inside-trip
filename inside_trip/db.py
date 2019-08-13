# 데이타베이스 관리 파일
import pymysql
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
import seaborn as sns
import sqlalchemy


class MyDB:
    def __init__(self):
        self._db_connection = pymysql.connect(host='127.0.0.1',
                                              user='test',
                                              password='0000',
                                              db='inside_trip',
                                              charset='utf8')

        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        return self._db_cur.execute(query, params)

    def __del__(self):
        self._db_connection.close()

    def load_data(self, table_name):
        query = f' select * from {table_name}'
        self._db_cur.execute(query)
        temp = self._db_cur.fetchall()
        return temp

    def age_plot_config(self):
        plt.rcParams["font.family"] = "D2Coding ligature"
        data = self.load_data('age')
        data = pd.DataFrame(list(data))
        data = data.set_index(0)

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

        for col in data.columns:
            data[col] = pd.to_numeric(data[col])
        data = data.sort_values('소계', ascending=False)

        plt.figure(figsize=(10, 6))
        return data

    def test1(self):
        data = self.age_plot_config()

        plt.title('인기많은 관광지순위')
        sns.barplot(x=data.index, y='소계', data=data)

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        return plot_url

    def test2(self):
        data = self.age_plot_config()

        plt.title('20대')
        sns.violinplot(x='소계', y=data.index, data=data, dodge=False)

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        return plot_url

    def test3(self):
        pass
