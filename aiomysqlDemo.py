import asyncio
import sqlalchemy as sa



from aiomysql.sa import create_engine





metadata = sa.MetaData()



tbl = sa.Table('tbl', metadata,

               sa.Column('id', sa.Integer, primary_key=True),

               sa.Column('val', sa.String(255)))





async def create_table(engine):

    async with engine.acquire() as conn:

        await conn.execute('DROP TABLE IF EXISTS tbl')

        await conn.execute('''CREATE TABLE tbl (

                              id serial PRIMARY KEY,

                              val varchar(255))''')





async def go(loop):

    engine = await create_engine(autocommit=True,user='gyli', db='liguangyumysql',

                                 host='liguangyumysql.cf8iw2auduon.ap-southeast-1.rds.amazonaws.com', password='gyligyli', loop=loop)

    await create_table(engine)

    async with engine.acquire() as conn:

        await conn.execute(tbl.insert().values(val='abc'))

        await conn.execute(tbl.insert().values(val='xyz'))



        async for row in conn.execute(tbl.select()):

            print(row.id, row.val)



    engine.close()

    await engine.wait_closed()





loop = asyncio.get_event_loop()

loop.run_until_complete(go(loop))