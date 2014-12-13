#from app import db
from pymongo import MongoClient



db = MongoClient('localhost',27017).test_database


class User(dict):
    def __init__(self,username,email):
        self['username'] = username
        self['email'] = email

    def __repr__(self):
        return '<User %r>' % self['uesrname']

    def save(self):
        if db.users.find_one({'email':self['email']}):
            return "Error: Email has been used\n"
        db.users.insert(self)
        return

    def update(self):
        db.users.update({'email':self['email']},self)

    @classmethod
    def find(cls,email):
        return db.users.find_one({'email':email})

    @classmethod
    def find_by(clf):
        pass

    @classmethod
    def delete(clf,email):
        return db.users.remove({'email':email})

    @classmethod
    def find_all(clf):
        return list(db.users.find())

def main():
    #user = User('ddest','test3@gmail.com')
    #user.update()
    #err = None
    #if err:
    #    print(err)
    #res=User.find('test@gmail.com')
    #res=User.delete('test@gmail.com')
    #print(res)
    print(User.find_all())
    print('ok')

if __name__ == '__main__':
    main()

'''
class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    description = db.Comlumn(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('Items',lazy='dynamic'))

    def __init__(self,title,description,category,pub_date=None):
        self.title = title
        self.description = description
       if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Item %r>' %self.title

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

'''
