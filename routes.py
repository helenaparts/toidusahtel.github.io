from flask import render_template, request

from models import Person

def register_routes(app, db)