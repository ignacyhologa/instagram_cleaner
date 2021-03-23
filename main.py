from find_fake_accounts import filter_fake_accounts
from instagram_driver import InstagramDriver

ins_driver = InstagramDriver()
followers = ins_driver.get_all_followers()
fake_users = filter_fake_accounts(followers.keys())
print(followers)
print(fake_users)
ins_driver.close()
