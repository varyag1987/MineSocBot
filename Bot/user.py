class User:

	def __init__(self, handler):
		self.is_auth = 0
		self.handler = handler


	def auth(self):
		if not self.is_auth:
			self.handler.auth()

	def doLike(self,type_obj, owner_id, item_id):
		self.handler.doLike(type_obj, owner_id, item_id)

	def addFriend(self, user_id):
		self.handler.addFriend(user_id)

	def doRepost(self, repost):
		self.handler.doRepost(repost)

	def joinGroup(self, group_id):
		self.handler.joinGroup(group_id)