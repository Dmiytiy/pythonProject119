from sqlalchemy import create_engine, MetaData, Table


engine = create_engine('postgresql://postgres:postgres@localhost/postgres')


table_name = 'questions'


connection = engine.connect()


metadata = MetaData()
table = Table(table_name, metadata, autoload_with=engine)


result = connection.execute(table.select()).fetchall()


for row in result:
    print(row)


connection.close()