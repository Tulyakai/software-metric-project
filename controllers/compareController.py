from flask import jsonify, request, send_file
from matplotlib import pyplot as plt
from utils.github import Github
from utils.loc import Loc

class CompareController:
    @staticmethod
    def compareRepo():
        # try:
        urls = request.get_json()['urls']
        if not urls:
            return jsonify({'message': 'The urls cannot be null'}), 400
        eurl = Github.extract_url(urls)
        for u in eurl:
            issues = Github.get_issues(u[0], u[1])
            pull = Github.get_pulls(u[0], u[1])
            print(u)
            print('issue:', len(issues) - len(pull), 'pull', len(pull))
            loc = Loc.get_loc(u[0], u[1])
            print(loc)

        plt.xlabel('repo', fontweight='bold', fontsize=15)
        plt.legend()
        plt.ylabel('issues', fontweight='bold', fontsize=15)
        plt.title('Issues vs Pulls', fontweight='bold', fontsize=20)
        plt.savefig('resources/issues.png')
        return send_file('resources/issues.png', mimetype='image/png')
        # except:
        #     return jsonify({'message': 'The request body required urls'}), 400
