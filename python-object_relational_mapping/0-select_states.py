import MySQLdb
def list_states(username, password, database):
    try:
        connection = MySQLdb.connect(host='localhost',
                                     user=username,
                                     passwd=password,
                                     db=database,
                                     port=3306)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        results = cursor.fetchall()
        for row in results:
            print(row[0], row[1])
        cursor.close()
        connection.close()
    except MySQLdb.Error as e:
        print("Error: {}".format(e))
if __name__ == "__main__":
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database = input("Enter database name: ")
    list_states(username, password, database)