import sqlite3
import random
numbers = ['1','2','3','4','5','6','7','8','9','0']
idnumber1 = str(random.choice(numbers))
idnumber2 = str(random.choice(numbers))
idnumber3 = str(random.choice(numbers))
idnumber4 = str(random.choice(numbers))
id = idnumber1 + idnumber2 + idnumber3 + idnumber4
conn = sqlite3.connect('backend/chat/accounts.db')
cursor = conn.cursor()
cursor.execute(f'''INSERT INTO accounts (ID, username, password, role)
VAlUES ('{id}', 'Yutubi06', 'zabest', 'user');
''')
#cursor.execute("DELETE FROM accounts WHERE username='Xn1vity'")
conn.commit()
conn.close()
