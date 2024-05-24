from flask import render_template, request, redirect, url_for

from models import Retsept

def register_routes(app, db):

    @app.route('/')
    def index():
        retseptid= Retsept.query.all()
        return render_template('index.html', retseptid=retseptid)
    
    @app.route('/add', methods=['POST'])
    def add_retsept():
        toit = request.form['toit']
        juhend = request.form['juhend']
        aeg = request.form['aeg']
        
        new_retsept = Retsept(toit=toit, juhend=juhend, aeg=aeg)
        db.session.add(new_retsept)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    @app.route('/delete/<int:retsept_id>', methods=['POST'])
    def delete_retsept(retsept_id):
        retsept = Retsept.query.get_or_404(retsept_id)
        db.session.delete(retsept)
        db.session.commit()
        return redirect(url_for('index'))