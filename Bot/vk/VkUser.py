import vk_api

import Bot

class VkUser:
	"""
	Адаптер для вк апи
	"""
	#parser = Parser()

	def __init__(self, config):
		self.is_auth = 0
		self.vk_session = vk_api.VkApi(**config)


	def auth(self):
		self.vk_session.auth()		
		self.vk = self.vk_session.get_api()
		print(self.vk_session.token)
#https://vk.com/wall349079176_73
	def doLike(self, type_obj, owner_id, item_id):
		d = {'type':type_obj, 'owner_id':owner_id, 'item_id':item_id}
		self.vk.likes.add(**d)

	def addFriend(self):
		pass

	def doRepost(self):
		pass

	def joinGroup(self):
		pass