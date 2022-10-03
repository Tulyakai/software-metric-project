import requests
class Github:

    @staticmethod
    def extract_url(urls):
        temp = []
        for url in urls:
            if 'github.com' in url:
                eurl = url.split('/')
                owner = eurl[-2]
                repo = eurl[-1]
                temp.append((owner, repo))
        return temp

    @staticmethod
    def get_detail(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_issues(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/issues'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_pulls(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/pulls'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_commits(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/commits'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_contributors(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/contributors'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_stargazers(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/stargazers'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_watchers(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/subscribers'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_forks(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/forks'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_releases(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/releases'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_branches(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/branches'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_tags(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/tags'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_languages(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/languages'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_readme(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/readme'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_license(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/license'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_events(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/events'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_collaborators(owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}/collaborators'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_all(owner, repo):
        return {
            'issues': Github.get_issues(owner, repo),
            'pulls': Github.get_pulls(owner, repo),
            'commits': Github.get_commits(owner, repo),
            'contributors': Github.get_contributors(owner, repo),
            'stargazers': Github.get_stargazers(owner, repo),
            'watchers': Github.get_watchers(owner, repo),
            'forks': Github.get_forks(owner, repo),
            'releases': Github.get_releases(owner, repo),
            'branches': Github.get_branches(owner, repo),
            'tags': Github.get_tags(owner, repo),
            'languages': Github.get_languages(owner, repo),
            'readme': Github.get_readme(owner, repo),
            'license': Github.get_license(owner, repo),
            'events': Github.get_events(owner, repo),
            'collaborators': Github.get_collaborators(owner, repo)
        }