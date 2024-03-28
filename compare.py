import xml.etree.ElementTree as ET
import sys
import pymssql

def execute_sybase_query(connection, query):
    """
    Execute a Sybase SQL query.
    """
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def compare_results(result1, result2):
    """
    Compare two query results.
    """
    return result1 == result2

def search_xml_for_keyword(xml_file, keyword):
    """
    Search an XML file for a specific keyword.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    found = False
    for elem in root.iter():
        if keyword in elem.text:
            found = True
            break
    return found

# Sybase database connection settings
server = "your_server"
user = "your_username"
password = "your_password"
database = "your_database"

# SQL queries to execute
sql_query1 = "SELECT * FROM table1 WHERE column = 'value'"
sql_query2 = "SELECT * FROM table2 WHERE column = 'value'"

# XML file path
xml_file = "your_xml_file.xml"

# Keyword to search for in the XML file
keyword = "your_keyword"

try:
    # Connect to the Sybase database
    connection = pymssql.connect(server, user, password, database)

    # Execute the SQL queries
    result1 = execute_sybase_query(connection, sql_query1)
    result2 = execute_sybase_query(connection, sql_query2)

    # Close the database connection
    connection.close()

    # Compare SQL query results
    if compare_results(result1, result2):
        print("SQL query results are identical.")
    else:
        print("SQL query results are different.")

    # Search for keyword in the XML file
    if search_xml_for_keyword(xml_file, keyword):
        print(f"Keyword '{keyword}' found in the XML file.")
    else:
        print(f"Keyword '{keyword}' not found in the XML file.")

except pymssql.Error as e:
    print("Error:", e)
    sys.exit(1)
