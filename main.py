import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github Username: ')
url = 'https://github.com/' + github_user + '?tab=repositories'

r = requests.get(url)
soup = bs(r.content, 'html.parser')

user_repos = soup.find('div', {'id' : 'user-repositories-list'})
repositories = user_repos.find_all('li', {'itemprop': 'owns'})

print('Repositories created by ', github_user + ":")
for index, repo in enumerate(repositories, start=1): 
    repo_name = repo.find('a', {'itemprop': 'name codeRepository'}).text.strip()
    description = repo.find('p', {'itemprop': 'description'})
    if description:
        repo_desc = description.text.strip()
    else:
        repo_desc = "No description provided for this repository!"
    print(f"{index}. Repository Name: {repo_name}:")
    print(f"     Description: {repo_desc}")
