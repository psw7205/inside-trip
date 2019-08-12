"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from inside_trip import app
import inside_trip.plot_test as p
from jinja2 import Markup

year = datetime.now().year


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    folium_html_tag = Markup(p.folium_test())
    return render_template(
        'index.html',
        title='INSIDE TRIP',
        year=year,
        img=p.test1(),
        img2=p.test2(),
        map=folium_html_tag
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


@app.route('/home/weather')
def weather():
    return render_template(
        'detail.html',
        img=p.test1(),
        title='날씨별 추천 정보',
        year=year
    )


@app.route('/home/age')
def age():
    return render_template(
        'detail.html',
        title='나이별 추천 정보',
        year=year
    )


@app.route('/home/cost')
def cost():
    return render_template(
        'detail.html',
        title='가성비 추천 정보',
        year=year
    )
