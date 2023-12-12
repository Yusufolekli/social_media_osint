import requests
from bs4 import BeautifulSoup

def get_social_media_profiles(username):
    urls=  {
        'Instagram' : f'https://www.instagram.com/{username}',
        'Github' : f'https://www.instagram.com/{username}',
        'LinkedIn' : f'https://www.linkedin.com/in/{username}',
        'X' : f'https://www.twitter.com/{username}',
        'Facebook' : f'https://www.instagram.com/{username}',
        'Reddit' : f'https://www.reddit.com/{username}',
        'Pinterest' : f'https://www.pinterest.com/{username}', 
    }
    
    profiles = {}
    for name, url in urls.items():
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.contents,'html.parser')
            if soup.title.text.strip() == 'Page Not Found . Github' :
                continue
            profiles[name] = url
        except:
                continue
        return profiles

username = input("Enter the UserName: ")
profiles = get_social_media_profiles(username)
print(profiles)
                                     
    