import requests
class Loc:
    @staticmethod
    def get_loc(owner, repo):
        url = f'https://api.codetabs.com/v1/loc?github={owner}/{repo}'
        response = requests.get(url)
        return response.json()

