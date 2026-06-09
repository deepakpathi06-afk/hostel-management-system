import os

class Config:

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "hostel_management_system_secret_key"
    )

    BASE_DIR = os.path.abspath(
        os.path.dirname(__file__)
    )

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(
            BASE_DIR,
            "hostel.db"
        )
    )

    if SQLALCHEMY_DATABASE_URI.startswith(
        "postgres://"
    ):
        SQLALCHEMY_DATABASE_URI = (
            SQLALCHEMY_DATABASE_URI.replace(
                "postgres://",
                "postgresql://",
                1
            )
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STUDENTS_PER_PAGE = 20

    ROOMS_PER_PAGE = 20

    VISITORS_PER_PAGE = 20

    MOVEMENTS_PER_PAGE = 20

    FEES_PER_PAGE = 20

    ANNOUNCEMENTS_PER_PAGE = 20