"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from inside_trip import app
import inside_trip.db as d

year = datetime.now().year
database = d.MyDB()

satis_img1 = database.family_income()
satis_img2 = database.family_population()
satis_img3 = database.family_total()

age_img1=database.popular_rank()
age_img2=database.popular_age()
age_img3=database.reason()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""

    return render_template(
        'index.html',
        title='INSIDE TRIP',
        year=year,
        img=database.popular_rank(),
        img2=database.popular_age()
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=year
    )


@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='About',
        year=year
    )


@app.route('/home/age')
def age():
    return render_template(
        'age.html',
        title='연령대 별 여행지 선호도 조사',
        img1=age_img1,
        img2=age_img2,
        img3=age_img3,
        year=year
    )


@app.route('/home/family')
def family():
    return render_template(
        'family.html',
        title='여행 만족도 분석',
        year=year,
        img1=satis_img1,
        img2=satis_img2,
        img3=satis_img3
    )

@app.route('/home/alone')
def alone():
    return render_template(
        'alone.html',
        title='여행 만족도 분석',
        year=year,
        img1=alone_img1,
        img2=alone_img2,
        img3=alone_img3,
        img4=alone_img4
    )


alone_img1 = database.alone_male()
alone_img2 = database.alone_age()
alone_img3 = database.alone_job()
alone_img4 = database.alone_income()
