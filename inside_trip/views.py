"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from inside_trip import app
import inside_trip.plot as p

year = datetime.now().year

p.make_sin_cos()


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='INSIDE TRIP',
        year=year,
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
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=year
    )


@app.route('/home/<category>')
def category(category):
    if category == 'weather':
        return render_template(
            'weather.html',
            title='날씨별 추천 정보',
            year=year
        )
    elif category == 'age':
        return render_template(
            'age.html',
            title='나이별 추천 정보',
            year=year
        )
    elif category == 'cost':
        return render_template(
            'cost.html',
            title='가성비 추천 정보',
            year=year
        )
