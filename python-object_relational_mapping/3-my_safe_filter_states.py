import MySQLdb
def list_states_starting_with_n(username, password, database, state_name):
    try:
        connection = MySQLdb.connect(host='localhost',
                                     user=username,
                                     passwd=password,
                                     db=database,
                                     port=3306)
        cursor = connection.cursor()
        query = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC"
        cursor.execute(query, (state_name,))
        results = cursor.fetchall()
        for row in results:
            print(row[0], row[1])
        cursor.close()
    except MySQLdb.Error as e:
        print("Error: {}".format(e))