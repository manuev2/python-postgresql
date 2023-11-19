import psycopg2

class DatabaseHandler:
	def __init__(self, database, user, password, host="localhost", port="5432"):
		self.database = database
		self.user = user
		self.password = password
		self.host = host
		self.port = port
		self.connection = None

	def connect(self):
		"""Connect to the PostgreSQL database."""
		try:
			self.connection = psycopg2.connect(
				database=self.database,
				user=self.user,
				password=self.password,
				host=self.host,
				port=self.port
			)
			print("Connected to the database.")
		except Exception as e:
			print(f"Error: Unable to connect to the database. {e}")

	def execute_query(self, query, params=None):
		"""Execute a SQL query and retrieve results (SELECT queries).


		Args:
			query (_type_): _description_
			params (_type_, optional): _description_. Defaults to None.

		Returns:
			_type_: _description_
		"""
		try:
			cursor = self.connection.cursor()
			cursor.execute(query, params)
			result = cursor.fetchall()
			cursor.close()
			return result
		except Exception as e:
			print(f"Error executing query: {e}")
			return None

	def execute_update(self, query, params=None):
		"""Execute a SQL query that updates the database (INSERT, UPDATE, DELETE)."""
		try:
			cursor = self.connection.cursor()
			cursor.execute(query, params)
			self.connection.commit()  # Commit to save changes to the database
			cursor.close()
		except Exception as e:
			print(f"Error executing update: {e}")
			self.connection.rollback()  # Rollback in case of error

	def close_connection(self):
		"""Close the database connection."""
		if self.connection is not None:
			self.connection.close()
			print("Database connection closed.")