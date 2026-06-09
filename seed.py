from app import app
from extensions import db
from models import (
    User,
    Student,
    Room,
    Visitor,
    Movement,
    Fee,
    Announcement
)

from werkzeug.security import generate_password_hash
import random

with app.app_context():

    db.drop_all()
    db.create_all()

    print("Creating Admin User...")

    admin = User(
        first_name="Admin",
        last_name="User",
        username="admin",
        email="admin@gmail.com",
        password=generate_password_hash("admin123")
    )

    db.session.add(admin)

    print("Creating Rooms...")

    room_numbers = []

    for i in range(1, 101):

        room_no = str(100 + i)

        room = Room(
            room_no=room_no,
            floor=random.choice([
                "Ground Floor",
                "First Floor",
                "Second Floor"
            ]),
            room_type=random.choice([
                "Standard",
                "Premium",
                "Deluxe"
            ]),
            capacity=10,
            occupied=0
        )

        room_numbers.append(room_no)

        db.session.add(room)

    db.session.commit()

    print("Rooms Created")

    print("Creating 1000 Students...")

    classes = [
        "8th",
        "9th",
        "10th",
        "11th",
        "12th"
    ]

    blood_groups = [
        "A+",
        "A-",
        "B+",
        "B-",
        "AB+",
        "AB-",
        "O+",
        "O-"
    ]

    students_created = 0

    for i in range(1, 1001):

        room_no = random.choice(room_numbers)

        total_fee = random.choice([
            45000,
            50000,
            55000,
            60000
        ])

        paid_fee = random.randint(
            10000,
            total_fee
        )

        pending_fee = total_fee - paid_fee

        student = Student(
            admission_no=f"ADM{i:05}",
            name=f"Student {i}",
            class_name=random.choice(classes),
            gender=random.choice([
                "Male",
                "Female"
            ]),
            date_of_birth=f"200{random.randint(5,9)}-{random.randint(1,12):02}-{random.randint(1,28):02}",
            blood_group=random.choice(blood_groups),
            phone=f"9{random.randint(100000000,999999999)}",
            email=f"student{i}@gmail.com",
            address=f"Address {i}",
            father_name=f"Father {i}",
            mother_name=f"Mother {i}",
            guardian_phone=f"9{random.randint(100000000,999999999)}",
            emergency_contact=f"9{random.randint(100000000,999999999)}",
            joining_date=f"2025-{random.randint(1,12):02}-{random.randint(1,28):02}",
            room_no=room_no,
            floor=random.choice([
                "Ground Floor",
                "First Floor",
                "Second Floor"
            ]),
            bed_no=f"B{random.randint(1,4)}",
            total_fee=total_fee,
            paid_fee=paid_fee,
            pending_fee=pending_fee,
            status=random.choice([
                "Active",
                "Active",
                "Active",
                "Inactive"
            ])
        )

        db.session.add(student)

        students_created += 1

        if students_created % 500 == 0:

            db.session.commit()

            print(f"{students_created} Students Created")

    db.session.commit()

    print("Students Created")

    print("Updating Room Occupancy...")

    rooms = Room.query.all()

    for room in rooms:

     room.occupied = 10

    db.session.commit()

    print("Room Occupancy Updated")

    db.session.commit()

    print("Creating Fee Records...")

    students = Student.query.all()

    fee_count = 0

    for student in students:

        fee = Fee(
            student_name=student.name,
            class_name=student.class_name,
            total_fee=student.total_fee,
            paid_amount=student.paid_fee,
            pending_amount=student.pending_fee,
            due_date=f"2026-{random.randint(1,12):02}-{random.randint(1,28):02}",
            status=random.choice([
                "Paid",
                "Pending",
                "Pending",
                "Overdue"
            ])
        )

        db.session.add(fee)

        fee_count += 1

        if fee_count % 500 == 0:

            db.session.commit()

            print(f"{fee_count} Fees Created")

    db.session.commit()

    print("Fee Records Created")

    print("Creating Visitors...")

    for i in range(1, 201):

        visitor = Visitor(
            name=f"Visitor {i}",
            student_name=f"Student {random.randint(1,10000)}",
            relationship=random.choice([
                "Father",
                "Mother",
                "Brother",
                "Sister",
                "Guardian",
                "Uncle"
            ]),
            phone=f"9{random.randint(100000000,999999999)}",
            visit_date=f"2026-{random.randint(1,12):02}-{random.randint(1,28):02}",
            status=random.choice([
                "Approved",
                "Pending",
                "Rejected"
            ])
        )

        db.session.add(visitor)

    db.session.commit()

    print("Visitors Created")

    print("Creating Movements...")

    for i in range(1, 201):

        movement = Movement(
            student_name=f"Student {random.randint(1,10000)}",
            class_name=random.choice(classes),
            room_no=random.choice(room_numbers),
            movement_type=random.choice([
                "Out Pass",
                "Leave",
                "Gate Pass"
            ]),
            date=f"2026-{random.randint(1,12):02}-{random.randint(1,28):02}",
            time=f"{random.randint(1,12)}:{random.randint(0,59):02} {'AM' if random.randint(0,1)==0 else 'PM'}",
            reason=random.choice([
                "Medical Visit",
                "Family Function",
                "Personal Work",
                "Shopping",
                "Emergency"
            ]),
            status=random.choice([
                "Approved",
                "Pending",
                "Rejected"
            ])
        )

        db.session.add(movement)

    db.session.commit()

    print("Movements Created")

    print("Creating Announcements...")

    for i in range(1, 21):

        announcement = Announcement(
            title=f"Announcement {i}",
            message=f"This is hostel announcement number {i}. Please follow hostel regulations and instructions.",
            priority=random.choice([
                "High",
                "Medium",
                "Low"
            ])
        )

        db.session.add(announcement)

    db.session.commit()

    print("Announcements Created")

    print("Database Seeded Successfully")