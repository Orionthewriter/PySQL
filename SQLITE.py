import sqlite3

connect =sqlite3.connect('cardssr.db')
#custom

#connect.execute('''CREATE TABLE CARDS
#                (ID INT PRIMARY KEY NOT NULL,
#                TYPE TEXT NOT NULL,
#                CODE TEXT NOT NULL);''')
#This creates the table RUN FIRST

#connect.execute("INSERT INTO CARDS (ID,TYPE,CODE) VALUES (1,'Monster','ABYR-EN025')")
#connect.execute("INSERT INTO CARDS (ID,TYPE,CODE) VALUES (2,'Spell','ABYR-EN061')")
#connect.execute("INSERT INTO CARDS (ID,TYPE,CODE) VALUES (3,'XYZ','DANE-EN039')")
#connect.execute("INSERT INTO CARDS (ID,TYPE,CODE) VALUES (4,'Spell','GFTP-EN117')")
#connect.execute("INSERT INTO CARDS (ID,TYPE,CODE) VALUES (5,'Trap','REDU-EN071')")
# This block was run second! It populated the table created in the first run!


connect.execute("INSERT INTO CARDS (ID,TYPE,CODE) Values(6,'Fusion','SDCB-EN042')")
all_data= connect.execute('''SELECT * FROM CARDS''')
for row in all_data:
    print(row)

connect.commit()
#Like any commit command this makes any changes permanent/saved
connect.close()