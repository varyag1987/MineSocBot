import Bot

class User:

	#parser = Parser()

	def __init__(self, handler):
		self.is_auth = 0
		self.handler = handler


	def auth(self):
		if not self.is_auth:
			self.handler.auth()

	def doLike(self,type_obj, owner_id, item_id):
		self.handler.doLike(type_obj, owner_id, item_id)

	def addFriend(self):
		pass

	def doRepost(self):
		pass

	def joinGroup(self):
		pass