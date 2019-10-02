class Step:
	def __init__(self, action, element, data=''):
		self.action = action
		self.element = element
		self.data = data
	def explain(self):
    		if('a' in self.element.element.tag_name or 'e' in self.element.element.tag_name or 'i' in self.element.element.tag_name or 'o' in self.element.element.tag_name or 'u' in self.element.element.tag_name)
			print("This step {0} {1} into an {2} element of {3} {4}".format(self.action, self.data,self.element.element.tag_name, self.element.by, self.element.value))
		else:
			print("This step {0} {1} into a {2} element of {3} {4}".format(self.action, self.data,self.element.element.tag_name, self.element.by, self.element.value))
