import os
import sqlite3

fileList = ['information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']

conn = sqlite3.connect('fake.db')


for v in fileList:
    if v.endswith(".txt"):
        print(v)

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filetest ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT, \
        col_ID INT \
        )")
    cur.execute("INSERT INTO tbl_filetest(col_file, col_ID) VALUES (?,?)", \
                (v,))
    
    conn.commit()
conn.close()




    
##    cur.execute("INSERT INTO tbl_coolstuff(col_dude, col_bro, col_guy) VALUES (?,?,?)", \
##                ('I', 'Dont', 'know'))
##    cur.execute("INSERT INTO tbl_coolstuff(col_dude, col_bro, col_guy) VALUES (?,?,?)", \
##                ('You', 'Pretty', 'Neat'))
##    cur.execute("INSERT INTO tbl_coolstuff(col_dude, col_bro, col_guy) VALUES (?,?,?)", \
##                ('Oh', 'Hi', 'Mark'))
##    conn.commit()
##conn.close()
##
##
##conn = sqlite3.connect('fake.db')
##
##with conn:
##    cur = conn.cursor()
##    cur.execute("SELECT col_dude,col_bro,col_guy, FROM tbl_coolstuff WHERE col_dude = 'Oh'")
##    varPerson = our.fetchall()
##    for item in varPerson:
##        msg = "First Name: {}\nLast Name: {}\nOther: {}".format(item[0],item[1],item[2])
##    print(msg)
##
##
