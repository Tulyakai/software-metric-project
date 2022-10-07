from flask import jsonify, request, send_file
from matplotlib import pyplot as plt
from utils.github import Github
from utils.loc import Loc
import numpy as np

class CompareController:
    @staticmethod
    def compareRepo():
        # try:
        urls = request.get_json()['urls']
        if not urls:
            return jsonify({'message': 'The urls cannot be null'}), 400
        eurl = Github.extract_url(urls)
        info = {'issues': [], 'repos':[], 'sizes': [], 'stars': [], 'watches': [], 'wikies': [],
                'forks': [], 'networks': [], 'subscribers': [], 'locs': []}

        for u in eurl:
            detail = Github.get_detail(u[0], u[1])
            info['issues'].append(detail['open_issues_count'])
            info['repos'].append(detail['name'])
            info['sizes'].append(detail['size'])
            info['stars'].append(detail['stargazers_count'])
            info['watches'].append(detail['watchers_count'])
            info['wikies'].append(1 if detail['has_wiki'] else 0)
            info['forks'].append(detail['forks_count'])
            info['networks'].append(detail['network_count'])
            info['subscribers'].append(detail['subscribers_count'])
            info['locs'].append(Loc.get_loc(u[0], u[1])[-1]['linesOfCode'])

        fig, ax = plt.subplots(2, figsize=(10, 10))
        x = np.arange(2)
        width = 0.15

        # NOTE: bar chart plotting
        ax[0].bar(x - 3 * width / 2, info['issues'], width, label='Issues', color='#0343df')
        ax[0].bar(x + width / 2, info['wikies'], width, label='Wikies', color='#653700')
        ax[0].legend()
        ax[0].set_xticks(x, info['repos'])
        ax[0].set_title('Issues and Wikies')
        # ax1.title('Repository Comparison', fontweight='bold', fontsize=16)
        # ax1.ylabel('score', fontweight='bold', fontsize=12)

        # NOTE: pie chart plotting
        ax[1].pie(info['locs'], labels=info['repos'], autopct='%1.1f%%')
        ax[1].set_title('Lines of Code')

        plt.savefig('resources/issues.png')
        return send_file('resources/issues.png', mimetype='image/png')
        # except:
        #     return jsonify({'message': 'The request body required urls'}), 400
