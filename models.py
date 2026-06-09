from datetime import datetime
from extensions import db

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    first_name = db.Column(
        db.String(100),
        nullable=False
    )

    last_name = db.Column(
        db.String(100),
        nullable=False
    )

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    admission_no = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    class_name = db.Column(
        db.String(20),
        nullable=False
    )

    gender = db.Column(
        db.String(20),
        nullable=False
    )

    date_of_birth = db.Column(
        db.String(50)
    )

    blood_group = db.Column(
        db.String(20)
    )

    phone = db.Column(
        db.String(20)
    )

    email = db.Column(
        db.String(150)
    )

    address = db.Column(
        db.Text
    )

    father_name = db.Column(
        db.String(150)
    )

    mother_name = db.Column(
        db.String(150)
    )

    guardian_phone = db.Column(
        db.String(20)
    )

    emergency_contact = db.Column(
        db.String(20)
    )

    joining_date = db.Column(
        db.String(50)
    )

    room_no = db.Column(
        db.String(20)
    )

    floor = db.Column(
        db.String(50)
    )

    bed_no = db.Column(
        db.String(20)
    )

    total_fee = db.Column(
        db.Float,
        default=0
    )

    paid_fee = db.Column(
        db.Float,
        default=0
    )

    pending_fee = db.Column(
        db.Float,
        default=0
    )

    status = db.Column(
        db.String(20),
        default="Active"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

class Room(db.Model):

    __tablename__ = "rooms"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    room_no = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    floor = db.Column(
        db.String(50),
        nullable=False
    )

    room_type = db.Column(
        db.String(50),
        nullable=False
    )

    capacity = db.Column(
        db.Integer,
        default=4
    )

    occupied = db.Column(
        db.Integer,
        default=0
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

class Visitor(db.Model):

    __tablename__ = "visitors"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    student_name = db.Column(
        db.String(150),
        nullable=False
    )

    relationship = db.Column(
        db.String(100)
    )

    phone = db.Column(
        db.String(20)
    )

    visit_date = db.Column(
        db.String(50)
    )

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

class Movement(db.Model):

    __tablename__ = "movements"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    student_name = db.Column(
        db.String(150),
        nullable=False
    )

    class_name = db.Column(
        db.String(20)
    )

    room_no = db.Column(
        db.String(20)
    )

    movement_type = db.Column(
        db.String(50)
    )

    date = db.Column(
        db.String(50)
    )

    time = db.Column(
        db.String(50)
    )

    reason = db.Column(
        db.Text
    )

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

class Fee(db.Model):

    __tablename__ = "fees"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    student_name = db.Column(
        db.String(150),
        nullable=False
    )

    class_name = db.Column(
        db.String(20)
    )

    total_fee = db.Column(
        db.Float,
        default=0
    )

    paid_amount = db.Column(
        db.Float,
        default=0
    )

    pending_amount = db.Column(
        db.Float,
        default=0
    )

    due_date = db.Column(
        db.String(50)
    )

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

class Announcement(db.Model):

    __tablename__ = "announcements"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(255),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    priority = db.Column(
        db.String(20),
        default="Low"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )