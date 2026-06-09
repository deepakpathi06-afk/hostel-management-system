from flask import Blueprint
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for

from models import Student
from models import Room
from models import Visitor
from models import Movement
from models import Fee
from models import Announcement

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)

@dashboard_bp.route(
    "/dashboard"
)
def dashboard():

    if "user_id" not in session:

        return redirect(
            url_for(
                "auth.login"
            )
        )

    total_students = Student.query.count()

    total_rooms = Room.query.count()

    occupied_rooms = Room.query.filter(
        Room.occupied > 0
    ).count()

    available_rooms = Room.query.filter(
        Room.occupied < Room.capacity
    ).count()

    total_visitors = Visitor.query.count()

    total_movements = Movement.query.count()

    total_announcements = Announcement.query.count()

    total_fees = Fee.query.count()

    total_collection = 0

    for fee in Fee.query.all():

        total_collection += (
            fee.paid_amount
        )

    class_8 = Student.query.filter_by(
        class_name="8th"
    ).count()

    class_9 = Student.query.filter_by(
        class_name="9th"
    ).count()

    class_10 = Student.query.filter_by(
        class_name="10th"
    ).count()

    class_11 = Student.query.filter_by(
        class_name="11th"
    ).count()

    class_12 = Student.query.filter_by(
        class_name="12th"
    ).count()

    recent_visitors = Visitor.query.order_by(
        Visitor.created_at.desc()
    ).limit(
        5
    ).all()

    recent_movements = Movement.query.order_by(
        Movement.created_at.desc()
    ).limit(
        5
    ).all()

    announcements = Announcement.query.order_by(
        Announcement.created_at.desc()
    ).limit(
        5
    ).all()

    return render_template(
        "dashboard.html",
        total_students=total_students,
        total_rooms=total_rooms,
        occupied_rooms=occupied_rooms,
        available_rooms=available_rooms,
        total_visitors=total_visitors,
        total_movements=total_movements,
        total_announcements=total_announcements,
        total_fees=total_fees,
        total_collection=total_collection,
        class_8=class_8,
        class_9=class_9,
        class_10=class_10,
        class_11=class_11,
        class_12=class_12,
        recent_visitors=recent_visitors,
        recent_movements=recent_movements,
        announcements=announcements
    )