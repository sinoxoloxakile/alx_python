import MySQLdb
def list_all_cities(username, password, database):
    try:
        connection = MySQLdb.connect(host='localhost',
                                     user=username,
                                     passwd=password,
                                     db=database,
                                     port=3306)
        cursor = connection.cursor()
        query = """SELECT cities.id, cities.name, states.name 
                   FROM cities 
                   JOIN states ON cities.state_id = states.id 
                   ORDER BY cities.id ASC"""
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row[0], row[1], row[2])
        cursor.close()
    except MySQLdb.Error as e:
        print("Error: {}".format(e))