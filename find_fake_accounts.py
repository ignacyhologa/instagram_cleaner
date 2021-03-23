from instascrape.scrapers.profile import Profile

# TODO
# TODO retrieve all followers for account
# TODO scrape followers for basic data
# TODO scrape followers for posts
# TODO location
# TODO min_number_followers
# TODO min_number_follows
# TODO min_number_media
# TODO min_av_media_likes


def fake_accounts_filter(profile: Profile):
    profile_conditions = (profile.is_verfied == False
                          and profile.is_private == False and profile.posts < 7
                          and profile.is_business_account == False
                          and profile.followed_by_viewer == False
                          and profile.followers <= 10
                          and profile.following >= 100
                          and profile.followers / profile.following < 0.01)
    return profile_conditions


def filter_fake_accounts(users):
    users = list(filter(fake_accounts_filter, users))
    return users
