from db import get_db
import uuid

class UserTodoList:
    """
    Represents a user's todo list.

    Attributes:
        taskID (str): The ID of the task.
        id (str): The ID of the user.
        taskName (str): The name of the task.
    """

    def __init__(self, **kwargs):
        self.taskID = kwargs.get('TaskID')
        self.id = kwargs.get('id')
        self.taskName = kwargs.get('TaskName')
        
    @staticmethod
    def create(id, taskName):
        """
        Creates a new task in the user's todo list.

        Args:
            id (str): The ID of the user.
            taskName (str): The name of the task.
        """
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
        """
        Retrieves all tasks for a given user ID.

        Args:
            id (str): The ID of the user.

        Returns:
            list: A list of UserTodoList objects representing the tasks.
        """
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
        """
        Retrieves a task by its ID and user ID.

        Args:
            id (str): The ID of the user.
            TaskID (str): The ID of the task.

        Returns:
            UserTodoList: The UserTodoList object representing the task.
        """
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
        """
        Deletes a task from the user's todo list.

        Args:
            TaskID (str): The ID of the task.
            id (str): The ID of the user.
        """
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "DELETE FROM UserTodoList WHERE TaskID = ? AND id = ?", (TaskID, id,)
        )
        db.commit()

    @staticmethod
    def update(id, taskID, taskName):
        """
        Updates the name of a task in the user's todo list.

        Args:
            id (str): The ID of the user.
            taskID (str): The ID of the task.
            taskName (str): The new name of the task.
        """
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE UserTodoList SET TaskName = ? WHERE id = ? AND TaskID = ?", (taskName, id, taskID,)
        )
        db.commit()
        