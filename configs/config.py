

class Config:
	def __init__(self):
		# Set your configuration items here
		self.driver = 'Chrome'
		self.full_path_to_driver = '' # path to webdrivers .exe
		self.headless = False
		self.base_url = ''
		self.subdomain = ''
		self.http_prefix = 'http://'
		self.port = ''
		# Example: self.options_list = ["headless"]
		self.options_list = []

	def url(self):
		full_url = self.base_url
		if self.subdomain:
			full_url = self.subdomain + '.' + full_url

		if self.port:
			full_url = full_url + ':' + self.port

		full_url = self.http_prefix + full_url

		return full_url
