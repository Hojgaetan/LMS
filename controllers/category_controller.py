from flask import Blueprint, jsonify
from services import CategoryService

category_blueprint = Blueprint("categories", __name__)


@category_blueprint.route("/total-category", methods=["GET"])
def total_categories():
    try:
        total_category = CategoryService.count_categories()
        return jsonify({"total_category": total_category})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
