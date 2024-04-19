from db import get_db

class ModuleItem:

    def __init__(self, **kwargs):
        self.ModuleItemID = kwargs.get('ModuleItemID')
        self.ItemName = kwargs.get('ItemName')
        self.itemLink = kwargs.get('itemLink')
        self.active = kwargs.get('active')    
        self.ModuleID = kwargs.get('ModuleID')
    
    # @staticmethod
    # def create(ModuleItemID, ItemName, active, ModuleID):
    #     """
    #     Creates a new module in the database.

    #     Args:
    #         ModuleID (str): The ID of the module.
    #         ModuleName (str): The name of the module.
    #         active (str): Indicates whether the module is active or not.
    #     """
    #     db = get_db()
    #     db.execute(
    #         "INSERT INTO ModuleItems (ModuleItemID, ItemName, active, ModuleID) "
    #         "VALUES (?, ?, ?, ?)",
    #         (ModuleItemID, ItemName, active, ModuleID),
    #     )
    #     db.commit()
    
    
    @staticmethod
    def getByModuleID(module_id): 
        db = get_db()
        modulesItems = db.execute(
            "SELECT * FROM ModuleItems WHERE ModuleID = ?", (module_id,)
        ).fetchall()
        if not modulesItems:
            return None
        modulesItems = [ModuleItem(ModuleItemID=moduleItem[0], ItemName=moduleItem[1], itemLink=moduleItem[2], active=moduleItem[3], ModuleID=moduleItem[4]) for moduleItem in modulesItems]
        return modulesItems
           