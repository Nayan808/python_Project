import sqlite3
def create_table():
  conn =sqlite3.connect('Products.db');
  cursor=conn.cursor();

  cursor.execute('''
       CREATE TABLE IF NOT EXITS Products(
                 id TEXT PRIMARY KEY,
                 name TEXT,
                 in_stock INTEGER,
                 price INTEGER)
       ''') 
  conn.commit()
  conn.close()

def fetch_products():
  conn=sqlite3.connect('Products.db')
  cursor=conn.cursor()
  cursor.execute('SELECT * FROM Products')
  Products=cursor.fetchall()
  conn.close()
  return Products

def insert_product(id,name,in_stock,price):
  conn=sqlite3.connect('Products.db');
  cursor=conn.cursor()
  cursor.execute('INSERT INTO Products(id,name,in_stock,price) VALUES (?,?,?,?)'(id,name,in_stock,price))
  conn.commit()
  conn.close()

def delete_product(id):
  conn=sqlite3.connect('Product.db')
  cursor=conn.cursor()
  cursor.execute('DELETE FROM Products WHERE id =?',(id,))
  conn.commit()
  conn.close()

def update_product(id):
  conn=sqlite3.connect('Product.db')
  cursor=conn.cursor()
  cursor.execute('UPDATE Products SET name=?,in_stock=?,price=? WHERE id=?',(new_name,new_stock,new_price,id))
  conn.commit()
  conn.close()

def id_exists(id):
  conn=sqlite3.connect('Product.db')
  cursor=conn.cursor()
  cursor.execute('Select Count(*) From Products WHERE id=?',(id,))
  result=cursor.fetchone()
  conn.close()
  return result[0]>0

create_table()