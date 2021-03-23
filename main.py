import argparse

from find_fake_accounts import filter_fake_accounts
from instagram_driver import InstagramDriver

if __name__ == "__main__":
    desc = "Creates the InstagramDriver, analyzes and deletes fake followers."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("--username",
                        type=str,
                        help="instagram username/email/login",
                        required=True)
    parser.add_argument("--password",
                        type=str,
                        help="instagram password",
                        required=True)
    args = parser.parse_args()

    ins_driver = InstagramDriver(username=args.username,
                                 password=args.password)
    followers = ins_driver.get_all_followers()
    # TODO map usernames to instascrape.scrapers.profile.Profile objects
    fake_users = filter_fake_accounts(followers.keys())
    # TODO invoke unfollow fake accounts
    print(followers)
    print(fake_users)
    ins_driver.close()
