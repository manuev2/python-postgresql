import yaml

class ConfigHandler:
	def __init__(self, file_path):
		self.file_path = file_path
		self.config_dict = None

	def load_config(self):
		"""Load YAML configuration from the specified file."""
		try:
			with open(self.file_path, "r") as config_file:
				self.config_dict = yaml.safe_load(config_file)
			print("Configuration loaded successfully.")
		except Exception as e:
			print(f"Error loading configuration: {e}")

	def get_config(self):
		"""Get the loaded configuration as a dictionary."""
		return self.config_dict