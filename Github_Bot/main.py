import requests
import json
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--function", required=True, help="user details or repo details")
ap.add_argument("-l", "--list", required=True, metavar="", nargs='+', default=[], help="handle and repo")
args = vars(ap.parse_args())

class GithubBot():
    def __init__(self):
        print('******************* GITHUB CLI TOOL *********************')
        self.base_url = "https://api.github.com/"
    
    def get_user_details(self, args):
        url = self.base_url + "users/" + args[0]
        res = requests.get(url)
        print('*********** USER:', args[0], '***************')
        if res.status_code == 200:
            data = json.loads(res.text)
            print("NAME: ", data["name"])
            print("BIO: ", data["bio"])
            print("LOCATION: ", data["location"])
            print("FOLLOWERS COUNT: ", data["followers"])
            print("FOLLOWING COUNT: ", data["following"]) 
        else:
            print("Error getting details")

    def get_repo_details(self, args):
        url = self.base_url + "repos/" + args[0] + "/" + args[1]
        res = requests.get(url)
        print('********* USER:', args[0], '| REPO:', args[1], '*********')
        if res.status_code == 200:
            data = json.loads(res.text)
            print("URL: ", data["svn_url"])
            print("STARS: ", data["stargazers_count"])
            print("FORKS: ", data["forks"])
            print("LANGUAGE: ", data["language"])
        else:
            print("Error getting details")

if __name__ == "__main__":
    obj = GithubBot()
    function_map = {
        'user': obj.get_user_details,
        'repo': obj.get_repo_details,
    }
    function_map[args['function']](args['list'])
    