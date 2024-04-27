from db import get_db
import uuid

class Projects:
    def __init__(self, **kwargs):
        self.project_id = kwargs.get('project_id')
        self.id = kwargs.get('id')
        self.projectName = kwargs.get('projectName')
        self.projectDescription = kwargs.get('projectDescription')
        #self.completed = kwargs.get('completed')
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
        db = get_db()
        db.execute("DELETE FROM UserProjects WHERE ProjectID = ? AND id = ?", (project_id, id,))
        db.commit()
    
    @staticmethod
    def getByProjectID(project_id, id):
        db = get_db()
        project = db.execute(
            "SELECT * FROM UserProjects WHERE ProjectID = ? AND id = ?", (project_id, id,)
            ).fetchone()
        if project is None:
            return None
        return Projects(project_id=project[0], 
                        id=project[1], 
                        projectName=project[2], 
                        projectDescription=project[3], 
                        startDate=project[4], 
                        endDate=project[5], 
                        techStack=project[6])
    
    @staticmethod
    def update(id, project_id, projectName, projectDescription, startDate, endDate, techStack):
        db = get_db()
        db.execute(
            "UPDATE UserProjects SET ProjectName = ?, ProjectDescription = ?, start_date = ?, end_date = ?, techStack = ? WHERE ProjectID = ? AND id = ?",
            (projectName, projectDescription, startDate, endDate, techStack, project_id, id)
        )
        db.commit()