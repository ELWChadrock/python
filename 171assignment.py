import os
open (fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg'))

import sqlite3

conn = sqlite3.conenct('fake.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_coolstuff ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_dude TEXT, \
        col_bro TEXT, \
        col_guy TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('fake.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_coolstuff(col_dude, col_bro, col_guy) VALUES (?,?,?)", \
                ('I', 'Dont', 'know'))
    cur.execute("INSERT INTO tbl_coolstuff(col_dude, col_bro, col_guy) VALUES (?,?,?)", \
                ('You', 'Pretty', 'Neat'))
    cur.execute("INSERT INTO tbl_coolstuff(col_dude, col_bro, col_guy) VALUES (?,?,?)", \
                ('Oh', 'Hi', 'Mark'))
    conn.commit()
conn.close()


conn = sqlite3.connect('fake.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_dude,col_bro,col_guy, FROM tbl_coolstuff WHERE col_dude = 'Oh'")
    varPerson = our.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}\nOther: {}".format(item[0],item[1],item[2])
    print(msg)
