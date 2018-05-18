import config
from Bot import vk
from Bot.user import User

user1 = User(vk.VkUser(config.VK))
user1.auth()
user1.doLike('photo', 486783111, 456239019)