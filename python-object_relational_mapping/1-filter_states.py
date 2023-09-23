import MySQLdb
def list_cities_in_california(username, password, database):
    try:
        connection = MySQLdb.connect(host='localhost',
                                     user=username,
                                     passwd=password,
                                     db=database,
                                     port=3306)
        cursor = connection.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name \
                        FROM cities \
                        JOIN states ON cities.state_id = states.id \
                        WHERE states.name = 'California' \
                        ORDER BY cities.id ASC")
        results = cursor.fetchall()
        for row in results:
            print(row[0], row[1], row[2])
        cursor.close()