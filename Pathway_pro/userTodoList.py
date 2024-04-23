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
    
    @staticmethod
    def getByTaskId(id, TaskID):
        db = get_db()
        userTask = db.execute(
            "SELECT * FROM UserTodoList WHERE id = ? AND TaskID = ?", (id, TaskID,)
        ).fetchone()
        if userTask is None:
            return None
        task = UserTodoList(TaskID=userTask[0], id=userTask[1], TaskName=userTask[2])
        return task
    
    @staticmethod
    def delete(TaskID, id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "DELETE FROM UserTodoList WHERE TaskID = ? AND id = ?", (TaskID, id,)
        )
        db.commit()

    @staticmethod
    def update(id, taskID, taskName):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE UserTodoList SET TaskName = ? WHERE id = ? AND TaskID = ?", (taskName, id, taskID,)
        )
        db.commit()
        