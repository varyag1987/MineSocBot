class Task:

	def __init__(self, handler):		
		self.handler = handler

	def getTaskList(self):
		self.handler.getTaskList()

	def getTask(self):
		pass