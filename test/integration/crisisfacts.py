import re
import unittest
from ir_datasets.datasets.crisisfacts import CrisisFactsStreamDoc, CrisisFactsQuery
from ir_datasets.formats import TrecQrel, GenericQuery
from .base import DatasetIntegrationTest


class TestCranfield(DatasetIntegrationTest):
    def test_docs(self):
        self._test_docs('crisisfacts/001/2017-12-07', count=7288, items={
            0: CrisisFactsStreamDoc('CrisisFACTS-001-News-5-0', 'CrisisFACTS-001', 'Live updates: San Diego County fire is 92 percent contained', {'url': 'http://www.sandiegouniontribune.com/news/public-safety/sd-latest-updates-san-diego-fire-20171207-htmlstory.html', 'title': 'Live updates: San Diego County fire is 92 percent contained', 'text': "The Lilac fire now 92 percent contained, Cal Fire officials said Tuesday morning.\n\nThe county of San Diego has opened a Local Assistance Center to help victims of the fire begin the rebuilding and recovery process. The center is at the Vista branch library on 700 Eucalyptus Avenue and will be open from 9:00 a.m. to 6:00 p.m.\n\nServices offered will include crisis counseling and referral services, short term housing referrals and a mobile medical clinic. Homeowners also will be able to get information on residential rebuilding and consumer fraud.\n\nThe Lilac fire charred about 4,100 acres and destroyed 157 structures and damaged 64 buildings, at last count. All evacuation orders were lifted Sunday.\n\nFire officials say damage assessment teams from Cal Fire and other fire agencies are continuing to inspect fire areas.\n\nSanta Ana winds fail to materialize\n\nSan Diego was lashed by Santa Anas when the Lilac fire broke out midday Thursday. Early Sunday, the winds were largely blowing in the mountains and foothills, with gusts from 35 mph to 70 mph, but high winds failed to materialize in the burn areas, which helped firefighters greatly in their efforts to douse hot spots. The red flag fire weather warning expired Sunday night.\n\nHere are the latest updates:\n\nLilac fire in San Diego County\n\nCurrent estimated fire perimeter:\n\nSize: 4,100 acres\n\nContainment: 92 percent\n\nRoad closures: All roads have been reopened.\n\nSchool closures on Tuesday:\n\n· Bonsall Unified School District\n\nDamage: 151 structures destroyed, 56 damaged, seven people injured. (Officials said the count of structures destroyed went down as they were able to do more accurate assessments.)\n\nEvacuation centers: Palomar College (1140 W. Mission Road in San Marcos). Pets are accepted.\n\nRecovery help: San Diego County opened a local assistance center on Monday at the Vista branch library (700 Eucalyptus Ave.) to help fire survivors navigate the recovery and rebuilding process. Hours of operation will be 9 a.m. to 6 p.m.\n\nAnimal assistance: Residents can bring horses and other livestock to the San Diego County fairgrounds in Del Mar for safety. Horses are being accepted at the fairgrounds’ Stable Gate off Jimmy Durante Boulevard. They also can be taken to the Del Mar Horse Park just east of I-5 at El Camino Real. If you need help evacuating animals, call the county's animal services emergency line at (619) 236-2341.\n\nPower outages: SDG&E said Monday that services were expected to be restored by early evening Tuesday to all customers who had gone without power because of the fire.\n\nHere are the latest stories from The San Diego Union-Tribune:\n\nCheck back for continued updates.\n\nYour local headlines, delivered straight to your device. Subscribe on iTunes.\n\nEmail: abby.hamblin@sduniontribune.com\n\nTwitter: @abbyhamblin", 'authors': [], 'published_date': '2017-12-07 00:00:00', 'top_image': 'https://ca-times.brightspotcdn.com/dims4/default/24e80fa/2147483647/strip/true/crop/480x252+0+54/resize/1200x630!/quality/90/?url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FquHdmFEvrjQ%2Fhqdefault.jpg', 'videos': [], 'keywords': [], 'summary': '', 'unixTimestamp': 1512604800}, 'News', 1512604800),
            9: CrisisFactsStreamDoc('CrisisFACTS-001-News-5-9', 'CrisisFACTS-001', 'The red flag fire weather warning expired Sunday night.', {'url': 'http://www.sandiegouniontribune.com/news/public-safety/sd-latest-updates-san-diego-fire-20171207-htmlstory.html', 'title': 'Live updates: San Diego County fire is 92 percent contained', 'text': "The Lilac fire now 92 percent contained, Cal Fire officials said Tuesday morning.\n\nThe county of San Diego has opened a Local Assistance Center to help victims of the fire begin the rebuilding and recovery process. The center is at the Vista branch library on 700 Eucalyptus Avenue and will be open from 9:00 a.m. to 6:00 p.m.\n\nServices offered will include crisis counseling and referral services, short term housing referrals and a mobile medical clinic. Homeowners also will be able to get information on residential rebuilding and consumer fraud.\n\nThe Lilac fire charred about 4,100 acres and destroyed 157 structures and damaged 64 buildings, at last count. All evacuation orders were lifted Sunday.\n\nFire officials say damage assessment teams from Cal Fire and other fire agencies are continuing to inspect fire areas.\n\nSanta Ana winds fail to materialize\n\nSan Diego was lashed by Santa Anas when the Lilac fire broke out midday Thursday. Early Sunday, the winds were largely blowing in the mountains and foothills, with gusts from 35 mph to 70 mph, but high winds failed to materialize in the burn areas, which helped firefighters greatly in their efforts to douse hot spots. The red flag fire weather warning expired Sunday night.\n\nHere are the latest updates:\n\nLilac fire in San Diego County\n\nCurrent estimated fire perimeter:\n\nSize: 4,100 acres\n\nContainment: 92 percent\n\nRoad closures: All roads have been reopened.\n\nSchool closures on Tuesday:\n\n· Bonsall Unified School District\n\nDamage: 151 structures destroyed, 56 damaged, seven people injured. (Officials said the count of structures destroyed went down as they were able to do more accurate assessments.)\n\nEvacuation centers: Palomar College (1140 W. Mission Road in San Marcos). Pets are accepted.\n\nRecovery help: San Diego County opened a local assistance center on Monday at the Vista branch library (700 Eucalyptus Ave.) to help fire survivors navigate the recovery and rebuilding process. Hours of operation will be 9 a.m. to 6 p.m.\n\nAnimal assistance: Residents can bring horses and other livestock to the San Diego County fairgrounds in Del Mar for safety. Horses are being accepted at the fairgrounds’ Stable Gate off Jimmy Durante Boulevard. They also can be taken to the Del Mar Horse Park just east of I-5 at El Camino Real. If you need help evacuating animals, call the county's animal services emergency line at (619) 236-2341.\n\nPower outages: SDG&E said Monday that services were expected to be restored by early evening Tuesday to all customers who had gone without power because of the fire.\n\nHere are the latest stories from The San Diego Union-Tribune:\n\nCheck back for continued updates.\n\nYour local headlines, delivered straight to your device. Subscribe on iTunes.\n\nEmail: abby.hamblin@sduniontribune.com\n\nTwitter: @abbyhamblin", 'authors': [], 'published_date': '2017-12-07 00:00:00', 'top_image': 'https://ca-times.brightspotcdn.com/dims4/default/24e80fa/2147483647/strip/true/crop/480x252+0+54/resize/1200x630!/quality/90/?url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FquHdmFEvrjQ%2Fhqdefault.jpg', 'videos': [], 'keywords': [], 'summary': '', 'unixTimestamp': 1512604800}, 'News', 1512604800),
            7287: CrisisFactsStreamDoc('CrisisFACTS-001-Twitter-49301-0', 'CrisisFACTS-001', 'today in school. scared out of my mind. #LilacFire https://t.co/OCfjmz2nPN', {'created_at': 'Thu Dec 07 23:59:56 +0000 2017', 'id': 938921048015171584, 'id_str': '938921048015171584', 'text': 'today in school. scared out of my mind. #LilacFire https://t.co/OCfjmz2nPN', 'display_text_range': [0, 50], 'source': '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>', 'truncated': False, 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 889938186419314688, 'id_str': '889938186419314688', 'name': 'diana⁷ ♥', 'screen_name': 'bunbunjeonk', 'location': '🇲🇽🇺🇸, 20 ✩ #8', 'url': None, 'description': 'to #hyunjin♥ + #jungkook♥, thank you for being my paradise ʚ♡ɞ | ♡ june ♡ | SHE/HER ⭐️', 'translator_type': 'none', 'protected': False, 'verified': False, 'followers_count': 442, 'friends_count': 527, 'listed_count': 2, 'favourites_count': 3328, 'statuses_count': 4872, 'created_at': 'Tue Jul 25 19:59:32 +0000 2017', 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': '', 'profile_background_image_url_https': '', 'profile_background_tile': False, 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'profile_image_url': 'http://pbs.twimg.com/profile_images/937741404385697792/hzf7NE2a_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/937741404385697792/hzf7NE2a_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/889938186419314688/1512319102', 'default_profile': True, 'default_profile_image': False, 'following': None, 'follow_request_sent': None, 'notifications': None, 'updated': ['description', 'name', 'location']}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'quote_count': 0, 'reply_count': 0, 'retweet_count': 0, 'favorite_count': 0, 'entities': {'hashtags': [{'text': 'LilacFire', 'indices': [40, 50]}], 'urls': [], 'user_mentions': [], 'symbols': [], 'media': [{'id': 938921042470248449, 'id_str': '938921042470248449', 'indices': [51, 74], 'media_url': 'http://pbs.twimg.com/media/DQe3tqiUIAET59Q.jpg', 'media_url_https': 'https://pbs.twimg.com/media/DQe3tqiUIAET59Q.jpg', 'url': 'https://t.co/OCfjmz2nPN', 'display_url': 'pic.twitter.com/OCfjmz2nPN', 'expanded_url': 'https://twitter.com/bunbunjeonk/status/938921048015171584/photo/1', 'type': 'photo', 'sizes': {'medium': {'w': 900, 'h': 1200, 'resize': 'fit'}, 'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'small': {'w': 510, 'h': 680, 'resize': 'fit'}, 'large': {'w': 1536, 'h': 2048, 'resize': 'fit'}}}]}, 'extended_entities': {'media': [{'id': 938921042470248449, 'id_str': '938921042470248449', 'indices': [51, 74], 'media_url': 'http://pbs.twimg.com/media/DQe3tqiUIAET59Q.jpg', 'media_url_https': 'https://pbs.twimg.com/media/DQe3tqiUIAET59Q.jpg', 'url': 'https://t.co/OCfjmz2nPN', 'display_url': 'pic.twitter.com/OCfjmz2nPN', 'expanded_url': 'https://twitter.com/bunbunjeonk/status/938921048015171584/photo/1', 'type': 'photo', 'sizes': {'medium': {'w': 900, 'h': 1200, 'resize': 'fit'}, 'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'small': {'w': 510, 'h': 680, 'resize': 'fit'}, 'large': {'w': 1536, 'h': 2048, 'resize': 'fit'}}}, {'id': 938921045469249536, 'id_str': '938921045469249536', 'indices': [51, 74], 'media_url': 'http://pbs.twimg.com/media/DQe3t1tVQAA_T4e.jpg', 'media_url_https': 'https://pbs.twimg.com/media/DQe3t1tVQAA_T4e.jpg', 'url': 'https://t.co/OCfjmz2nPN', 'display_url': 'pic.twitter.com/OCfjmz2nPN', 'expanded_url': 'https://twitter.com/bunbunjeonk/status/938921048015171584/photo/1', 'type': 'photo', 'sizes': {'medium': {'w': 900, 'h': 1200, 'resize': 'fit'}, 'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'small': {'w': 510, 'h': 680, 'resize': 'fit'}, 'large': {'w': 1536, 'h': 2048, 'resize': 'fit'}}}]}, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'filter_level': 'low', 'lang': 'en', 'timestamp_ms': '1512691196813', 'matching_rules': [{'tag': 'hashtags', 'id': 8414591381820374875, 'id_str': '8414591381820374875'}]}, 'Twitter', 1512691196),
        })

    def test_queries(self):
        self._test_queries('crisisfacts/001/2017-12-07', count=52, items={
            0: CrisisFactsQuery('CrisisFACTS-General-q001', 'Have airports closed', 'airport closed', 'Report-Factoid', 'CrisisFACTS-001', 'Lilac Wildfire 2017', '2017_12_07_lilac_wildfire.2017', 'The Lilac Fire was a fire that burned in northern San Diego County, California, United States, and the second-costliest one of multiple wildfires that erupted in Southern California in December 2017.', 'TRECIS-CTIT-H-092', 'Wildfire', 'https://en.wikipedia.org/wiki/Lilac_Fire'),
            9: CrisisFactsQuery('CrisisFACTS-General-q010', 'How many people have been killed', 'killed dead', 'Report-Factoid', 'CrisisFACTS-001', 'Lilac Wildfire 2017', '2017_12_07_lilac_wildfire.2017', 'The Lilac Fire was a fire that burned in northern San Diego County, California, United States, and the second-costliest one of multiple wildfires that erupted in Southern California in December 2017.', 'TRECIS-CTIT-H-092', 'Wildfire', 'https://en.wikipedia.org/wiki/Lilac_Fire'),
            51: CrisisFactsQuery('CrisisFACTS-Wildfire-q006', 'What is the fire containment level', 'containment', 'Report-Factoid', 'CrisisFACTS-001', 'Lilac Wildfire 2017', '2017_12_07_lilac_wildfire.2017', 'The Lilac Fire was a fire that burned in northern San Diego County, California, United States, and the second-costliest one of multiple wildfires that erupted in Southern California in December 2017.', 'TRECIS-CTIT-H-092', 'Wildfire', 'https://en.wikipedia.org/wiki/Lilac_Fire'),
        })

if __name__ == '__main__':
    unittest.main()