from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from extensions import db
from models import User

auth_bp = Blueprint(
    "auth",
    __name__
)

@auth_bp.route("/")
def home():

    if "user_id" in session:

        return redirect(
            url_for(
                "dashboard.dashboard"
            )
        )

    return redirect(
        url_for(
            "auth.login"
        )
    )

@auth_bp.route(
    "/login",
    methods=[
        "GET",
        "POST"
    ]
)
def login():

    if request.method == "POST":

        username = request.form.get(
            "username"
        )

        password = request.form.get(
            "password"
        )

        user = User.query.filter_by(
            username=username
        ).first()

        if user and check_password_hash(
            user.password,
            password
        ):

            session["user_id"] = user.id

            session["username"] = (
                user.username
            )

            flash(
                "Login successful",
                "success"
            )

            return redirect(
                url_for(
                    "dashboard.dashboard"
                )
            )

        flash(
            "Invalid username or password",
            "danger"
        )

    return render_template(
        "login.html"
    )

@auth_bp.route(
    "/register",
    methods=[
        "GET",
        "POST"
    ]
)
def register():

    if request.method == "POST":

        first_name = request.form.get(
            "first_name"
        )

        last_name = request.form.get(
            "last_name"
        )

        username = request.form.get(
            "username"
        )

        email = request.form.get(
            "email"
        )

        password = request.form.get(
            "password"
        )

        confirm_password = request.form.get(
            "confirm_password"
        )

        if password != confirm_password:

            flash(
                "Passwords do not match",
                "danger"
            )

            return redirect(
                url_for(
                    "auth.register"
                )
            )

        existing_user = User.query.filter(
            (
                User.username
                == username
            )
            |
            (
                User.email
                == email
            )
        ).first()

        if existing_user:

            flash(
                "Username or Email already exists",
                "danger"
            )

            return redirect(
                url_for(
                    "auth.register"
                )
            )

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=generate_password_hash(
                password
            )
        )

        db.session.add(
            user
        )

        db.session.commit()

        flash(
            "Registration successful. Please login.",
            "success"
        )

        return redirect(
            url_for(
                "auth.login"
            )
        )

    return render_template(
        "register.html"
    )

@auth_bp.route(
    "/logout"
)
def logout():

    session.clear()

    flash(
        "Logged out successfully",
        "success"
    )

    return redirect(
        url_for(
            "auth.login"
        )
    )