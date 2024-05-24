from app import db

class Retsept(db.Model):
    __tablename__= 'retseptid'

    pid= db.Column(db.Integer, primary_key= True)
    toit= db.Column(db.Text, nullable= False)
    juhend= db.Column(db.Text)
    aeg= db.Column(db. Text)

    def __repr__(self):
        return f'Toit: {self.toit}. Valmistamine: {self.juhend}' 
