from mysql.connector import cursor

from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    query = ("SELECT * FROM gs1.products;")

    cursor.execute(query)
    response = []
    for (products_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'products_id' : products_id,
                'name' : name,
                'uom_id' : uom_id,
                'price_per_unit' : price_per_unit,
                'uom_name' : uom_name
            }
        )
    return response

def insert_new_product(connection, product):
    curser = connection.cursor()
    query = ("INSERT INTO products"
            ("name, uom_id, price_per_unit")
            "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid()

def delete_product(connection, product_id):
    cursor = connection.corsor
    query = ("DELETE FROM products were product_id=" + str (product_id))
    cursor.execute(query)
    connection.commit()

if __name__== '__main__' :
    connection = get_sql_connection()
    print(get_all_products(connection, {
        'product_name': 'cabbage',
        'uom_id': '1',
        'price_per_unit': '10'
    }))
