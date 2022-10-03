from flask import Blueprint
from controllers.compareController import CompareController

class CompareBlueprint:
    compare_bp = Blueprint('compare_bp', __name__, url_prefix='/compare')
    compare_bp.route('/', methods=['POST'])(CompareController.compareRepo)
