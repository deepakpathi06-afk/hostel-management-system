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

hostel_bp = Blueprint(
    "hostel",
    __name__
)

@hostel_bp.route(
    "/students"
)
def students():

    if "user_id" not in session:

        return redirect(
            url_for(
                "auth.login"
            )
        )

    students = Student.query.order_by(
        Student.id.desc()
    ).all()

    return render_template(
        "students.html",
        students=students
    )

@hostel_bp.route(
    "/students/<int:student_id>"
)
def student_details(student_id):

    if "user_id" not in session:

        return redirect(
            url_for(
                "auth.login"
            )
        )

    student = Student.query.get_or_404(
        student_id
    )

    return render_template(
        "student_details.html",
        student=student
    )

@hostel_bp.route(
    "/rooms"
)
def rooms():

    if "user_id" not in session:

        return redirect(
            url_for(
                "auth.login"
            )
        )

    rooms = Room.query.order_by(
        Room.room_no
    ).all()

    return render_template(
        "rooms.html",
        rooms=rooms
    )

@hostel_bp.route(
    "/rooms/<int:room_id>"
)
def room_details(room_id):

    if "user_id" not in session:

        return redirect(
            url_for(
                "auth.login"
            )
        )

    room = Room.query.get_or_404(
        room_id
    )

    occupants = Student.query.filter_by(
        room_no=room.room_no
    ).all()

    return render_template(
        "rooms_details.html",
        room=room,
        occupants=occupants
    )

@hostel_bp.route(
    "/visitors"
)
def visitors():

    if "user_id" not in session:

        return redirect(
            url_for(
                "auth.login"
            )
        )

    visitors = Visitor.query.order_by(
        Visitor.created_at.desc()
    ).all()

    return render_template(
        "visitors.html",
        visitors=visitors
    )

@hostel_bp.route(
    "/movements"
)
def movements():

    if "user_id" not in session:

        return redirect(
            url_for(
                "auth.login"
            )
        )

    movements = Movement.query.order_by(
        Movement.created_at.desc()
    ).all()

    return render_template(
        "movements.html",
        movements=movements
    )

@hostel_bp.route(
    "/fees"
)
def fees():

    if "user_id" not in session:

        return redirect(
            url_for(
                "auth.login"
            )
        )

    fees = Fee.query.order_by(
        Fee.created_at.desc()
    ).all()

    total_fee_amount = sum(
        fee.total_fee
        for fee in fees
    )

    total_paid_amount = sum(
        fee.paid_amount
        for fee in fees
    )

    total_pending_amount = sum(
        fee.pending_amount
        for fee in fees
    )

    return render_template(
        "fees.html",
        fees=fees,
        total_fee_amount=total_fee_amount,
        total_paid_amount=total_paid_amount,
        total_pending_amount=total_pending_amount
    )

@hostel_bp.route(
    "/announcements"
)
def announcements():

    if "user_id" not in session:

        return redirect(
            url_for(
                "auth.login"
            )
        )

    announcements = Announcement.query.order_by(
        Announcement.created_at.desc()
    ).all()

    return render_template(
        "announcements.html",
        announcements=announcements
    )