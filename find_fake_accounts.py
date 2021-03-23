from typing import List
from instascrape.scrapers.profile import Profile

# TODO scrape followers for basic data
# TODO scrape followers for posts
# TODO location
# TODO min_number_followers
# TODO min_number_follows
# TODO min_number_media
# TODO min_av_media_likes


def fake_accounts_filter(profile: Profile):
    profile_conditions = (not profile.is_verfied and not profile.is_private
                          and not profile.is_business_account
                          and not profile.followed_by_viewer
                          and profile.posts < 7 and profile.followers <= 10
                          and profile.following >= 100
                          and profile.followers / profile.following < 0.01)
    return profile_conditions


def filter_fake_accounts(users: List[Profile]):
    users = list(filter(fake_accounts_filter, users))
    return users
