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

        plt.figure(figsize=(12, 10))
        return data

    def draw_plot(self):
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        return plot_url

    def popular_rank(self):
        data = self.age_plot_config()

        sns.barplot(x=data.index, y='소계', data=data)

        return self.draw_plot()

    def popular_age(self):
        data = self.age_plot_config()

        data = data.iloc[:, 3:]
        plt.figure(figsize=(16, 9))
        data.plot(kind='barh', stacked='True')
        return self.draw_plot()

    def reason(self):
        plt.rcParams["font.family"] = "Malgun Gothic"
        plt.rcParams['axes.unicode_minus'] = False

        engine = sqlalchemy.create_engine(
            "mysql+pymysql://test:0000@localhost:3306/inside_trip", encoding='utf8')

        conn = engine.connect()

        data_p = pd.read_sql_table('reason', conn)
        del data_p['index']

        data_p.columns = list(data_p.loc[0])
        data_p.index = list(data_p['통계분류(2)'])

        data_p = data_p.iloc[4:10, 2:]
        data_p2 = data_p.T

        for col in data_p2.columns:
            data_p2[col] = pd.to_numeric(data_p2[col])

        plt.figure(figsize=(16, 10))
        plt.plot(data_p2, marker='o')
        plt.xticks(rotation=60)

        return self.draw_plot()

    def load_family_data(self):
        plt.rcParams["font.family"] = "Malgun Gothic"
        plt.rcParams['axes.unicode_minus'] = False

        engine = sqlalchemy.create_engine(
            "mysql+pymysql://test:0000@localhost:3306/inside_trip", encoding='utf8')

        conn = engine.connect()

        return pd.read_sql_table('family_satis', conn)

    def family_income(self):
        familydata = self.load_family_data()

        f, ax = plt.subplots(2, 3, figsize=(16, 9))
        ax[0][0].plot(familydata['지역'], familydata['100만~200만원 미만'])
        ax[0][0].set_title('소득:100만~200만원')
        ax[0][0].set_ylabel("")

        ax[0][1].plot(familydata['지역'], familydata['200만~300만원 미만'])
        ax[0][1].set_title('소득:200만~300만원')
        ax[0][1].set_ylabel("")

        ax[0][2].plot(familydata['지역'], familydata['300만~400만원 미만'])
        ax[0][2].set_title('소득:300만~400만원')
        ax[0][2].set_ylabel("")

        ax[1][0].plot(familydata['지역'], familydata['400만~500만원 미만'])
        ax[1][0].set_title('소득:400만~500만원')
        ax[1][0].set_ylabel("")

        ax[1][1].plot(familydata['지역'], familydata['500만~600만원 미만'])
        ax[1][1].set_title('소득:500만~600만원')
        ax[1][1].set_ylabel("")

        ax[1][2].plot(familydata['지역'], familydata['600만원 이상'])
        ax[1][2].set_title('소득:600만원~')
        ax[1][2].set_ylabel("")

        return self.draw_plot()

    def family_population(self):
        familydata = self.load_family_data()

        plt.subplots(2, 2, figsize=(16, 15))

        plt.subplot(2, 2, 1)
        ax1 = sns.barplot(familydata['지역'], familydata['2인가구'])
        ax1.set(ylim=(3.5, 4.5))
        plt.title('2인가구의 지역별 국내여행 만족도')

        plt.subplot(2, 2, 2)
        ax2 = sns.barplot(familydata['지역'], familydata['3인가구'])
        ax2.set(ylim=(3.5, 4.5))
        plt.title('3인가구의 지역별 국내여행 만족도')

        plt.subplot(2, 2, 3)
        ax3 = sns.barplot(familydata['지역'], familydata['4인가구'])
        ax3.set(ylim=(3.5, 4.5))
        plt.title('4인가구의 지역별 국내여행 만족도')

        plt.subplot(2, 2, 4)
        ax4 = sns.barplot(familydata['지역'], familydata['5인가구 이상'])
        ax4.set(ylim=(3.5, 4.5))
        plt.title('5인가구 이상의 국내여행 만족도')

        return self.draw_plot()

    def family_total(self):
        familydata = self.load_family_data()
        plt.subplots()
        family_citysize = familydata[['지역', '대도시', '중소도시', '읍/면']]
        family_citysize['종합만족도'] = family_citysize['대도시'] + family_citysize['중소도시'] + family_citysize['읍/면']

        ax = sns.barplot(family_citysize['지역'], family_citysize['종합만족도'])
        ax.set(ylim=(11.5, 13))

        return self.draw_plot()

    def load_alone_data(self):
        plt.rcParams["font.family"] = "Malgun Gothic"
        plt.rcParams['axes.unicode_minus'] = False

        engine = sqlalchemy.create_engine(
            "mysql+pymysql://test:0000@localhost:3306/inside_trip", encoding='utf8')
        conn = engine.connect()

        return pd.read_sql_table('alone_satis', conn)

    def alone_male(self):
        alonedata = self.load_alone_data()
        alone_sex = alonedata[['지역', '남자', '여자']]
        alone_sex['여자'] = (alone_sex['여자'] - 3.5)
        alone_sex['남자'] = (alone_sex['남자'] - 3.5)

        alone_sex['여자'] = alone_sex['여자'] * -1
        alone_sex = alone_sex.melt('지역', var_name='gender', value_name='vals')

        # draw plot
        plt.figure(figsize=(13, 10), dpi=80)
        group_col = 'gender'
        order_of_bars = alone_sex.지역.unique()[::-1]
        float(len(alone_sex[group_col].unique()) - 1)
        colors = [plt.cm.Spectral(i / float(len(alone_sex[group_col].unique()) - 1)) for i in
                  range(len(alone_sex[group_col].unique()))]

        for c, group in zip(colors, alone_sex[group_col].unique()):
            sns.barplot(x='vals', y='지역', data=alone_sex.loc[alone_sex[group_col] == group, :], order=order_of_bars,
                        color=c, label=group)

        # decorations
        plt.xlabel('만족도')
        plt.title('남/여 지역별 만족도 차이')
        plt.legend()
        return self.draw_plot()

    def alone_age(self):
        alonedata = self.load_alone_data()
        alone_age = alonedata[['지역', '15~19세', '20대', '30대', '40대', '50대', '60대이상']]
        alone_age = alone_age.melt('지역', var_name='age', value_name='val')
        g = sns.FacetGrid(data=alone_age, hue='age', size=12)
        g.map(plt.plot, '지역', 'val').add_legend()
        return self.draw_plot()

    def alone_job(self):
        alonedata = self.load_alone_data()

        plt.subplots(5, figsize=(16, 15))

        plt.subplot(3, 2, 1)
        ax1 = sns.barplot(alonedata['지역'], alonedata['전문관리'])
        ax1.set(ylim=(2.9, 4.5))
        plt.title('직종:전문관리 국내개인여행 지역별만족도')

        plt.subplot(3, 2, 2)
        ax2 = sns.barplot(alonedata['지역'], alonedata['사무'])
        ax2.set(ylim=(2.9, 4.5))
        plt.title('직종:사무 국내개인여행 지역별만족도')

        plt.subplot(3, 2, 3)
        ax3 = sns.barplot(alonedata['지역'], alonedata['서비스판매'])
        ax3.set(ylim=(2.9, 4.5))
        plt.title('직종:서비스판매 국내개인여행 지역별만족도')

        plt.subplot(3, 2, 4)
        ax4 = sns.barplot(alonedata['지역'], alonedata['농어업'])
        ax4.set(ylim=(2.9, 4.5))
        plt.title('직종:농어업 국내개인여행 지역별만족도')

        plt.subplot(3, 2, 5)
        ax5 = sns.barplot(alonedata['지역'], alonedata['기능노무'])
        ax5.set(ylim=(2.9, 4.5))
        plt.title('직종:기능노무 국내개인여행 지역별만족도')
        return self.draw_plot()

    def alone_income(self):
        alonedata = self.load_alone_data()
        alone_income = alonedata[
            ['지역', '50만~100만원 미만', '100만~200만원 미만', '200만~300만원 미만', '300만~400만원 미만', '400만~500만원 미만', '500만~600만원 미만',
             '600만원 이상']]
        alone_income = alone_income.melt('지역', var_name='income', value_name='val')
        g = sns.FacetGrid(data=alone_income, hue='income', size=12)
        g.map(plt.plot, '지역', 'val').add_legend()
        return self.draw_plot()
