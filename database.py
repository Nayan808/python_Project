import sqlite3
def create_table():
  conn =sqlite3.connect('inventory.db')
  cursor=conn.cursor()

  cursor.execute('''CREATE TABLE inventory(
                 id TEXT PRIMARY KEY,
                 name TEXT,
                 in_stock INTEGER,
                 price INTEGER) ''') 
  conn.commit()
  conn.close()

def fetch_inventory():
  conn=sqlite3.connect('inventory.db')
  cursor=conn.cursor()
  cursor.execute('SELECT * FROM inventory')
  inventory=cursor.fetchall()
  conn.close()
  return inventory

def insert_inventory(id,name,in_stock,price):
  conn=sqlite3.connect('inventory.db')
  cursor=conn.cursor()
  cursor.execute('INSERT INTO inventory(id,name,in_stock,price) VALUES (?,?,?,?)',(id,name,in_stock,price))
  conn.commit()
  conn.close()

def delete_inventory(id):
  conn=sqlite3.connect('inventory.db')
  cursor=conn.cursor()
  cursor.execute('DELETE FROM inventory WHERE id =?',(id,))
  conn.commit()
  conn.close()

def update_inventory(new_name,new_stock,new_price,id):
  conn=sqlite3.connect('inventory.db')
  cursor=conn.cursor()
  cursor.execute('UPDATE inventory SET name=?,in_stock=?,price=? WHERE id=?',(new_name,new_stock,new_price,id))
  conn.commit()
  conn.close()

def id_exists(id):
  conn=sqlite3.connect('inventory.db')
  cursor=conn.cursor()
  cursor.execute('Select Count(*) From inventory WHERE id=?',(id,))
  result=cursor.fetchone()
  conn.close()
  return result[0]>0

create_table()