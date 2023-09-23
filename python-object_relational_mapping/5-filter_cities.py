import MySQLdb
def list_cities_by_state_abbr(username, password, database, state_abbr):
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
                   WHERE states.abbreviation = %s
                   ORDER BY cities.id ASC"""
        cursor.execute(query, (state_abbr,))
        results = cursor.fetchall()
        for row in