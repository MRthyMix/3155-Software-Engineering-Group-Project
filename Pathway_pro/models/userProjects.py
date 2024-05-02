from db import get_db
import uuid

class Projects:
    """
    Represents a user project.

    Attributes:
        project_id (str): The unique identifier for the project.
        id (str): The user ID associated with the project.
        projectName (str): The name of the project.
        projectDescription (str): The description of the project.
        startDate (str): The start date of the project.
        endDate (str): The end date of the project.
        techStack (str): The technology stack used in the project.
    """

    def __init__(self, **kwargs):
        self.project_id = kwargs.get('project_id')
        self.id = kwargs.get('id')
        self.projectName = kwargs.get('projectName')
        self.projectDescription = kwargs.get('projectDescription')
        self.startDate = kwargs.get('startDate')
        self.endDate = kwargs.get('endDate')
        self.techStack = kwargs.get('techStack')

    @staticmethod
    def create(id, projectName, projectDescription, startDate, endDate, techStack):
        project_id = str(uuid.uuid4())
        db = get_db()
        db.execute(
            "INSERT INTO UserProjects (ProjectID, id, ProjectName, ProjectDescription, start_date, end_date, techStack) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (project_id, id, projectName, projectDescription, startDate, endDate, techStack,)
        )
        db.commit()

    @staticmethod
    def getById(id):
        """
        Retrieve a list of projects from the database based on the given user id.

        Args:
            id (str): The user id of the project to retrieve.

        Returns:
            list: A list of Projects objects matching the given user id.

        """
        db = get_db()
        projects = db.execute(
            "SELECT * FROM UserProjects WHERE id = ?", (id,)
        ).fetchall() 
        if projects is None:
            return None
        
        return [Projects(project_id=project[0], 
                         id=project[1], 
                         projectName=project[2], 
                         projectDescription=project[3], 
                         startDate=project[4], 
                         endDate=project[5], 
                         techStack=project[6]) for project in projects]
    
    @staticmethod
    def delete(project_id, id):
        """
        Deletes a user project from the database.

        Args:
            project_id (int): The ID of the project.
            id (int): The ID of the user project.

        Returns:
            None
        """
        db = get_db()
        db.execute("DELETE FROM UserProjects WHERE ProjectID = ? AND id = ?", (project_id, id,))
        db.commit()
    
    @staticmethod
    def getByProjectID(project_id, id):
        """
        Retrieves a project from the UserProjects table based on the given project_id and id.

        Args:
            project_id (int): The ID of the project.
            id (int): The ID of the user.

        Returns:
            Projects: The project object with the specified project_id and id, or None if not found.
        """
        db = get_db()
        project = db.execute(
            "SELECT * FROM UserProjects WHERE ProjectID = ? AND id = ?", (project_id, id,)
        ).fetchone()
        if project is None:
            return None
        
        return Projects(
            project_id=project[0],
            id=project[1],
            projectName=project[2],
            projectDescription=project[3],
            startDate=project[4],
            endDate=project[5],
            techStack=project[6]
        )
    
    @staticmethod
    def update(id, project_id, projectName, projectDescription, startDate, endDate, techStack):
        """
        Update the details of a user project in the database.

        Parameters:
        - id (int): The user ID.
        - project_id (int): The project ID.
        - projectName (str): The updated project name.
        - projectDescription (str): The updated project description.
        - startDate (str): The updated start date of the project.
        - endDate (str): The updated end date of the project.
        - techStack (str): The updated technology stack of the project.

        Returns:
        None
        """
        db = get_db()
        db.execute(
            "UPDATE UserProjects SET ProjectName = ?, ProjectDescription = ?, start_date = ?, end_date = ?, techStack = ? WHERE ProjectID = ? AND id = ?",
            (projectName, projectDescription, startDate, endDate, techStack, project_id, id)
        )
        db.commit()
