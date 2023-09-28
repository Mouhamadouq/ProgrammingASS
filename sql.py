import sqlite3
import sqlalchemy as sa
import pandas as pd
conn = sa.create_engine('sqlite:///books.db')
df =pd.read_sql('SELECT title from book',conn)
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE IF NOT EXISTS book (title text, author text, year real)''') 
curs.execute('INSERT INTO book VALUES("The Weirdstone of Brisingamen", "Alan Garner", 1960)') 
curs.execute('INSERT INTO book VALUES("Perdido Street", "China Mieville", 2000)') 
curs.execute('INSERT INTO book VALUES("Thud!", "Terry Pratchett", 2005)') 
curs.execute('INSERT INTO book VALUES("The spellman Files", "Lisa Lutz", 2007)') 
curs.execute('INSERT INTO book VALUES("Small Gods", "Terry Pratchett", 1992)')
conn.commit()
for row in curs.execute('''SELECT * FROM book'''):
    print(row)

print(df)