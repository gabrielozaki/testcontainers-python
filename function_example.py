import psycopg2


def working_function(connection_cursor):
    connection_cursor.execute("INSERT INTO example_table values (1, 'example')")
    connection_cursor.execute("INSERT INTO example_table2 values (1, 1, 'example2')")


def broken_function(connection_cursor):
    connection_cursor.execute("INSERT INTO example_table values (2, 'example')")
    # Violates the FK
    connection_cursor.execute("INSERT INTO example_table2 values (2, 3, 'example2')")
