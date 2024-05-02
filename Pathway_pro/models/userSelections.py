from db import get_db

class UserSelections:
    """
    Represents a user's selections.

    This class provides methods to create, delete, and retrieve user selections from the database.
    """

    @staticmethod
    def create(id, ModuleItemID):
        """
        Creates a new user selection in the database.

        Args:
            id (int): The user's ID.
            ModuleItemID (int): The ID of the selected module item.
        """
        db = get_db()
        db.execute(
            "INSERT INTO UserSelections (id, ModuleItemID) VALUES (?, ?)",
            (id, ModuleItemID,)
        )
        db.commit()

    @staticmethod
    def delete(id):
        """
        Deletes a user selection from the database.

        Args:
            id (int): The ID of the user selection to delete.
        """
        db = get_db()
        db.execute("DELETE FROM UserSelections WHERE id = ?", (id,))
        db.commit()
    
    @staticmethod
    def getAll(id):
        """
        Retrieves all user selections for a given user ID.

        Args:
            id (int): The user's ID.

        Returns:
            list: A list of module item IDs representing the user's selections.
        """
        db = get_db()
        return db.execute(
            "SELECT ModuleItemID FROM UserSelections WHERE id = ?", (id,)
        ).fetchall()
    