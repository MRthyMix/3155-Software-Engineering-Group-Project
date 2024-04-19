from db import get_db
from moduleItems import ModuleItems

class Modules():
    """
    Represents a module in the system.

    Attributes:
        ModuleID (str): The ID of the module.
        ModuleName (str): The name of the module.
        active (str): Indicates whether the module is active or not.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Modules object.

        Args:
            **kwargs: Keyword arguments representing the module's attributes.
        """
        self.ModuleID = kwargs.get('ModuleID')
        self.ModuleName = kwargs.get('ModuleName')
        self.active = kwargs.get('active')

    @staticmethod
    def get(module_id):
        """
        Retrieves a module from the database by its ID.

        Args:
            module_id (str): The ID of the module to retrieve.

        Returns:
            Modules: The Modules object representing the retrieved module, or None if the module does not exist.
        """
        db = get_db()
        module = db.execute(
            "SELECT * FROM Modules WHERE ModuleID = ?", (module_id,)
        ).fetchone()
        if not module:
            return None

        module = Modules(
            ModuleID=module[0], ModuleName=module[1], active=module[2]
        )
        return module
    
    @staticmethod
    def getAll():
        """
        Retrieves all active modules from the database.

        Returns:
            List[Modules]: A list of Modules objects representing the retrieved modules, or None if no modules exist.
        """
        db = get_db()
        modules = db.execute(
            "SELECT * FROM Modules WHERE active = 'True'"
        ).fetchall()
        if not modules:
            return None

        return modules

    @staticmethod
    def create(ModuleID, ModuleName, active):
        """
        Creates a new module in the database.

        Args:
            ModuleID (str): The ID of the module.
            ModuleName (str): The name of the module.
            active (str): Indicates whether the module is active or not.
        """
        db = get_db()
        db.execute(
            "INSERT INTO Modules (ModuleID, ModuleName, active) "
            "VALUES (?, ?, ?)",
            (ModuleID, ModuleName, active),
        )
        db.commit()
        
    @staticmethod
    def update(ModuleName, active, ModuleID):
        """
        Updates the attributes of a module in the database.

        Args:
            ModuleID (str): The ID of the module.
            ModuleName (str): The name of the module.
            active (str): Indicates whether the module is active or not.
        """
        db = get_db()
        db.execute(
            "UPDATE Modules SET ModuleName = ?, active = ? WHERE ModuleID = ?",
            (ModuleName, active, ModuleID)
        )
        db.commit()

    @staticmethod
    def delete(ModuleID):
        """
        Deletes a module from the database.

        Args:
            ModuleID (str): The ID of the module to delete.
        """
        db = get_db()
        db.execute(
            "DELETE FROM Modules WHERE ModuleID = ?",
            (ModuleID,)
        )
        db.commit()