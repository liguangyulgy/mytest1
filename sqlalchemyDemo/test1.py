__author__ = 'LiGuangyu'

from sqlalchemy import Table,Column,Integer,String,MetaData,create_engine
from sqlalchemy.sql import select

db = create_engine('sqlite:///tutorial.db',echo=True)

metadata = MetaData(db)

users = Table('users',metadata,
              Column('user_id',Integer,primary_key=True),
              Column('name',String(40)),
              Column('age',Integer),
              Column('password', String))

addresses = Table('address', metadata,
                  Column('email_id', Integer, primary_key=True),
                  Column('user_id', Integer),
                  Column('addr', String))

#users.create(checkfirst=True)
metadata.create_all(checkfirst=True)


def test1():
    v = {'name':'adf','age':10,'password':'****'}
    sql = "insert into users(name,age) values('a',1),('b',2)"
    a = users.insert().values(name='john',age=10,password='****')
    #a.execute()
    #users.insert().values(**v).execute()
    with db.connect() as conn:
        rev = conn.execute(users.insert(), [v,v,v,v,v])
        print(str(rev))
        # print(rev.inserted_primary_key)
        r = conn.execute(sql)
        print(r)
    s= users.select(users.c.age <=10)
    ss = select([users.c.name,users.c.age]).where(users.c.user_id==34)
    rs = ss.execute()
    a = addresses.insert().values(user_id=1,addr='aldfj@jlafd.cc')
    a.execute()
    for r in rs:
        print(r)


def initTableDatas():
    users.delete().execute()
    addresses.delete().execute()
    with db.connect() as conn:
        conn.execute(users.insert(), [
            {'user_id':1,'name':'xiaohong','age':10},
            {'user_id':2,'name':'hanmei','age':20}
        ])
        conn.execute(addresses.insert(),[
            {'email_id':1,'user_id':1,'addr':'123@qq.com'},
            {'email_id':2,'user_id':2,'addr':'asdf@sin.com'},
            {'email_id':3,'user_id':1,'addr':'123@sin.com'}
        ])



def test2():
    from sqlalchemy.engine import RowProxy
    s = select([users,addresses]).where(users.c.user_id == addresses.c.user_id)
    print(str(s))
    v = s.execute()
    for row in v :
        print(row)
        print(row[users.c.user_id])
    for row in addresses.select().execute():
        print(row)

def testOperators():
    v = (users.c.name.like('%js') & (users.c.user_id==addresses.c.user_id)) | (users.c.age < 10)
    print (v)

def textSql():
    from sqlalchemy.sql import text,bindparam
    s = text('select users.user_id,users.age,address.addr from users, address where users.user_id = address.user_id and users.age < :age and users.name like :name')
    s.bindparams(bindparam('age',Integer),bindparam('name',String))
    s = s.columns(users.c.user_id,users.c.age,addresses.c.addr)
    with db.connect() as conn:
        for x in conn.execute(s, age = '100', name='%'):
            print(x)
            print(dict(x))

def timestampTest():
    from sqlalchemy import func
    users.insert().values(name=func.current_timestamp()).execute()
    s = select(
        [users.c.user_id,
         func.row_number().over(order_by=users.c.age)]
    )
    print(s)
    with db.connect() as conn:
        for x in conn.execute(s):
            print(x)
    for x in users.select().execute():
        print(x)

def ormTest():
    with db.connect() as conn:
        rev = conn.query(users).filter(users.c.age < 100).first()
        print(rev)


if __name__ == '__main__':
    initTableDatas()
    ormTest()
    #timestampTest()
    #textSql()
    pass
