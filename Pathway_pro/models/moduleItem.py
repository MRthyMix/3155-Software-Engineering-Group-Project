from db import get_db

class ModuleItem:
    """
    Represents a module item.

    Attributes:
        ModuleItemID (int): The ID of the module item.
        ItemName (str): The name of the item.
        itemLink (str): The link to the item.
        active (bool): Indicates whether the item is active or not.
        ModuleID (int): The ID of the module that the item belongs to.
    """

    def __init__(self, **kwargs):
        self.ModuleItemID = kwargs.get('ModuleItemID')
        self.ItemName = kwargs.get('ItemName')
        self.itemLink = kwargs.get('itemLink')
        self.active = kwargs.get('active')    
        self.ModuleID = kwargs.get('ModuleID')

    @staticmethod
    def create(ModuleItemID, ItemName, itemLink, active, ModuleID):
        """
        Creates a new module item and inserts it into the database.

        Args:
            ModuleItemID (int): The ID of the module item.
            ItemName (str): The name of the item.
            itemLink (str): The link to the item.
            active (bool): Indicates whether the item is active or not.
            ModuleID (int): The ID of the module that the item belongs to.
        """
        db = get_db()
        db.execute(
            "INSERT INTO ModuleItems (ModuleItemID, ItemName, itemLink, active, ModuleID) VALUES (?, ?, ?, ?, ?)",
            (ModuleItemID, ItemName, itemLink, active, ModuleID)
        )
        db.commit()

    @staticmethod
    def get(ModuleItemID):
        """
        Retrieves a module item from the database based on its ID.

        Args:
            ModuleItemID (int): The ID of the module item.

        Returns:
            ModuleItem: The module item object if found, None otherwise.
        """
        db = get_db()
        moduleItem = db.execute(
            "SELECT * FROM ModuleItems WHERE ModuleItemID = ?", (ModuleItemID,)
        ).fetchone()
        if not moduleItem:
            return None
        return ModuleItem(ModuleItemID=moduleItem[0], ItemName=moduleItem[1], itemLink=moduleItem[2], active=moduleItem[3], ModuleID=moduleItem[4])

    @staticmethod
    def delete(ModuleItemID):
        """
        Deletes a module item from the database based on its ID.

        Args:
            ModuleItemID (int): The ID of the module item.
        """
        db = get_db()
        db.execute("DELETE FROM ModuleItems WHERE ModuleItemID = ?", (ModuleItemID,))
        db.commit()

    @staticmethod
    def update(ModuleItemID, ItemName, itemLink, active, ModuleID):
        """
        Updates the attributes of a module item in the database.

        Args:
            ModuleItemID (int): The ID of the module item.
            ItemName (str): The name of the item.
            itemLink (str): The link to the item.
            active (bool): Indicates whether the item is active or not.
            ModuleID (int): The ID of the module that the item belongs to.
        """
        db = get_db()
        db.execute(
            "UPDATE ModuleItems SET ItemName = ?, itemLink = ?, active = ?, ModuleID = ? WHERE ModuleItemID = ?",
            (ItemName, itemLink, active, ModuleID, ModuleItemID)
        )
        db.commit()
    
    @staticmethod
    def getByModuleID(module_id): 
        """
        Retrieves all module items associated with a specific module ID.

        Args:
            module_id (int): The ID of the module.

        Returns:
            list: A list of module item objects if found, None otherwise.
        """
        db = get_db()
        modulesItems = db.execute(
            "SELECT * FROM ModuleItems WHERE ModuleID = ?", (module_id,)
        ).fetchall()
        if not modulesItems:
            return None
        modulesItems = [ModuleItem(ModuleItemID=moduleItem[0], ItemName=moduleItem[1], itemLink=moduleItem[2], active=moduleItem[3], ModuleID=moduleItem[4]) for moduleItem in modulesItems]
        return modulesItems
           