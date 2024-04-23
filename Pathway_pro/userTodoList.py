from db import get_db
import uuid

class UserTodoList:
    def __init__(self, **kwargs):
        self.taskID = kwargs.get('TaskID')
        self.id = kwargs.get('id')
        self.taskName = kwargs.get('TaskName')
        
    @staticmethod
    def create(id, taskName):
        db = get_db()
        cursor = db.cursor()
        taskID = str(uuid.uuid4())
        cursor.execute(
            "INSERT INTO UserTodoList (TaskID, id, TaskName) VALUES (?, ?, ?)",
            (taskID, id, taskName,)
        )
        db.commit()
    
    @staticmethod
    def getById(id):
        db = get_db()
        userTasks = db.execute(
            "SELECT * FROM UserTodoList WHERE id = ?", (id,)
        ).fetchall()
        if userTasks is None:
            return None
        tasks = [UserTodoList(TaskID=task[0], id=task[1], TaskName=task[2]) for task in userTasks]
        return tasks
        