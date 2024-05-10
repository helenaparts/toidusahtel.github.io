from app import db

class Toit(db.Model):
    __tablename__= 'Retseptid'

    pid= db.Column(db.Integer, primary_key= True)
    toidunimi= db.Column(db.Text, nullable= False)
    kirjeldus= db.Coulmn(db.Text)
    aeg= db.Column(db. Integer)

    def __repr__(self):
        return f'Retsept {self.toidumini}, valmista nii: {self.kirjeldus}'