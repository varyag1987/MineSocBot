import config
from Bot import vk, snebes, manager
from Bot.user import User


manager = manager.Manager(100)
manager.createUser( vk.VkUser(config.VK) )
#manager.start()
#vkuser1 = User(vk.VkUser(config.VK))
#vkuser1.auth()
#user1.doLike('photo', 486783111, 456239019)
#vkuser1.addFriend(486783111)
#print(vkuser1.handler.vk_session.http.cookies)
#snebesuser1 = User(snebes.SnebesUser(vkuser1.handler.vk_session.http.cookies))
#snebesuser1.auth()