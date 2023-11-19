from python_postgresql.database_handler import DatabaseHandler
from python_postgresql.config_handler import ConfigHandler
import os
if __name__ == "__main__":
	file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database_configs/database_config.yml")
	conf_handler = ConfigHandler(file_path=file_path)  # Specify the path to your YAML file
	conf_handler.load_config()

	db_conf = conf_handler.get_config()["config"]
	db_utils = DatabaseHandler(database=db_conf["database"], user=db_conf["user"], password="123")
	
	db_utils.connect()

	# Execute SELECT query
	select_query = "SELECT * FROM your_table;"
	result = db_utils.execute_query(select_query)
	if result:
		print("Query Result:")
		for row in result:
			print(row)

	# Execute INSERT query
	insert_query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s);"
	insert_params = ("value1", "value2")
	db_utils.execute_update(insert_query, insert_params)

	# Close the database connection
	db_utils.close_connection()