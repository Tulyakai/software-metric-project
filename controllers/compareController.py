from flask import jsonify
import requests

class CompareController:
    @staticmethod
    def compareRepo(owner, repo):
        return 0