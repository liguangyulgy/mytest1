__author__ = 'LiGuangyu'

from sqlalchemy import Table,Column,Integer,String,MetaData,create_engine


db = create_engine('sqlite:///tutorial.db',echo=True)



metadata = MetaData(db)

users = Table('users',metadata,
              Column('user_id',Integer,primary_key=True),
              Column('name',String(40)),
              Column('age',Integer),
              Column('password', String))

users.create(checkfirst=True)


# a = users.insert(**{'name':'john','age':10,'password':'****'})
a = users.insert(name='john',age=10,password='****')
a.execute()

s= users.select(users.c.name =='john')
rs = s.execute()
for r in rs:
    print(r)


