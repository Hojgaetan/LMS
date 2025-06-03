from flask import Blueprint, render_template, jsonify
from services.dashboard_service import DashboardService
from services.borrowing_service import BorrowingService

dashboard_blueprint = Blueprint("dashboard", __name__)

dashboard_service = DashboardService()
borrowing_service = BorrowingService()


@dashboard_blueprint.route("/", methods=["GET"])
def dashboard():
    try:
        stats = dashboard_service.get_dashboard_statistics()
        books_data = dashboard_service.get_books_data()
        members_loans_data = dashboard_service.get_members_loans_data()
        return render_template("index.html", **stats, books=books_data, members_loans=members_loans_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@dashboard_blueprint.route("/books", methods=["GET"])
def books():
    try:
        stats = dashboard_service.get_dashboard_statistics()
        books_data = dashboard_service.get_books_data()
        return render_template("books.html", **stats, books=books_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@dashboard_blueprint.route("/members", methods=["GET"])
def members():
    try:
        stats = dashboard_service.get_dashboard_statistics()
        members_data = dashboard_service.get_members_data()
        members_loans_data = dashboard_service.get_members_loans_data()

        # Debug log
        print("Members data:", members_data)

        return render_template(
            "members.html",
            total_members=stats["total_members"],
            total_active_members=stats["total_active_members"],
            members=members_data,
            members_loans_data=members_loans_data,
        )
    except Exception as e:
        print("Error in members route:", str(e))
        return jsonify({"error": str(e)}), 500


@dashboard_blueprint.route("/loans", methods=["GET"])
def loans():
    try:
        stats = dashboard_service.get_dashboard_statistics()
        members_loans_data = dashboard_service.get_members_loans_data()
        overdue_borrowings = borrowing_service.get_overdue_borrowings()
        return render_template(
            "loans.html",
            total_loans=stats.get("total_books", 0),  # Using total_books as a placeholder
            overdue_loans=len(overdue_borrowings),
            loans_data=members_loans_data,
            overdue_books=overdue_borrowings
        )
    except Exception as e:
        print("Error in loans route:", str(e))
        return jsonify({"error": str(e)}), 500
