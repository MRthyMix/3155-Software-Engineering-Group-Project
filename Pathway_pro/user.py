from flask_login import UserMixin

from db import get_db

class User(UserMixin):
    """
    Represents a user in the system.

    Attributes:
        id (str): The user's ID.
        name (str): The user's name.
        email (str): The user's email address.
        profile_pic (str): The URL of the user's profile picture.
        major (str): The user's major.
        year (int): The user's academic year.
        gpa (float): The user's GPA.
        advisor (str): The user's advisor.
        Enrollment_Status (str): The user's enrollment status.
        level (str): The user's level.
        program (str): The user's program.
        college (str): The user's college.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new User object.

        Args:
            **kwargs: Keyword arguments representing the user's attributes.
        """
        self.id = kwargs.get('id_')
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.profile_pic = kwargs.get('profile_pic')
        self.major = kwargs.get('major')
        self.year = kwargs.get('year')
        self.gpa = kwargs.get('gpa')
        self.advisor = kwargs.get('advisor')
        self.Enrollment_Status = kwargs.get('Enrollment_Status')
        self.level = kwargs.get('level')
        self.program = kwargs.get('program')
        self.college = kwargs.get('college')

    @staticmethod
    def get(user_id):
        """
        Retrieves a user from the database by their ID.

        Args:
            user_id (str): The ID of the user to retrieve.

        Returns:
            User: The User object representing the retrieved user, or None if the user does not exist.
        """
        db = get_db()
        user = db.execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()
        if not user:
            return None

        user = User(
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3]
        )
        return user
    
    @staticmethod
    def getAll(user_id):
        """
        Retrieves all user attributes from the database by their ID.

        Args:
            user_id (str): The ID of the user to retrieve.

        Returns:
            User: The User object representing the retrieved user, or None if the user does not exist.
        """
        db = get_db()
        user = db.execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()
        if not user:
            return None

        user = User(
            id_=user[0], 
            name=user[1], 
            email=user[2], 
            profile_pic=user[3], 
            major=user[4], 
            year=user[5], 
            gpa=user[6], 
            advisor=user[7], 
            Enrollment_Status=user[8], 
            level=user[9], 
            program=user[10], 
            college=user[11]
        )
        return user


    @staticmethod
    def create(id_, name, email, profile_pic):
        """
        Creates a new user in the database.

        Args:
            id_ (str): The ID of the user.
            name (str): The name of the user.
            email (str): The email address of the user.
            profile_pic (str): The URL of the user's profile picture.
        """
        db = get_db()
        db.execute(
            "INSERT INTO user (id, name, email, profile_pic) "
            "VALUES (?, ?, ?, ?)",
            (id_, name, email, profile_pic),
        )
        db.commit()
    
    @staticmethod
    def createUsingALlAttributes(id_, name, email, profile_pic, major, year, gpa, advisor, Enrollment_Status, level, program, college):
        """
        Creates a new user in the database with all attributes.

        Args:
            id_ (str): The ID of the user.
            name (str): The name of the user.
            email (str): The email address of the user.
            profile_pic (str): The URL of the user's profile picture.
            major (str): The user's major.
            year (int): The user's academic year.
            gpa (float): The user's GPA.
            advisor (str): The user's advisor.
            Enrollment_Status (str): The user's enrollment status.
            level (str): The user's level.
            program (str): The user's program.
            college (str): The user's college.
        """
        db = get_db()
        db.execute(
            "INSERT INTO user (id, name, email, profile_pic, major, year, gpa, advisor, Enrollment_Status, level, program, college) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (id_, name, email, profile_pic, major, year, gpa, advisor, Enrollment_Status, level, program, college),
        )
        db.commit()

    
    @staticmethod
    def update(id_, major, year, gpa, advisor, Enrollment_Status, level, program, college):
        """
        Updates the attributes of a user in the database.

        Args:
            id_ (str): The ID of the user.
            major (str): The user's major.
            year (int): The user's academic year.
            gpa (float): The user's GPA.
            advisor (str): The user's advisor.
            Enrollment_Status (str): The user's enrollment status.
            level (str): The user's level.
            program (str): The user's program.
            college (str): The user's college.
        """
        db = get_db()
        db.execute(
            "UPDATE user SET major = ?, year = ?, gpa = ?, advisor = ?, Enrollment_Status = ?, level = ?, program = ?, college = ? WHERE id = ?",
            (major, year, gpa, advisor, Enrollment_Status, level, program, college, id_)
        )
        db.commit()

    @staticmethod
    def delete(id_):
        """
        Deletes a user from the database.

        Args:
            id_ (str): The ID of the user to delete.
        """
        db = get_db()
        db.execute(
            "DELETE FROM user WHERE id = ?",
            (id_,)
        )
        db.commit()