from db import get_db

class ModuleItem:

    def __init__(self, **kwargs):
        self.ModuleItemID = kwargs.get('ModuleItemID')
        self.ItemName = kwargs.get('ItemName')
        self.itemLink = kwargs.get('itemLink')
        self.active = kwargs.get('active')    
        self.ModuleID = kwargs.get('ModuleID')

    @staticmethod
    def create(ModuleItemID, ItemName, itemLink, active, ModuleID):
        db = get_db()
        db.execute(
            "INSERT INTO ModuleItems (ModuleItemID, ItemName, itemLink, active, ModuleID) VALUES (?, ?, ?, ?, ?)",
            (ModuleItemID, ItemName, itemLink, active, ModuleID)
        )
        db.commit()

    @staticmethod
    def get(ModuleItemID):
        db = get_db()
        moduleItem = db.execute(
            "SELECT * FROM ModuleItems WHERE ModuleItemID = ?", (ModuleItemID,)
        ).fetchone()
        if not moduleItem:
            return None
        return ModuleItem(ModuleItemID=moduleItem[0], ItemName=moduleItem[1], itemLink=moduleItem[2], active=moduleItem[3], ModuleID=moduleItem[4])

    @staticmethod
    def delete(ModuleItemID):
        db = get_db()
        db.execute("DELETE FROM ModuleItems WHERE ModuleItemID = ?", (ModuleItemID,))
        db.commit()

    @staticmethod
    def update(ModuleItemID, ItemName, itemLink, active, ModuleID):
        db = get_db()
        db.execute(
            "UPDATE ModuleItems SET ItemName = ?, itemLink = ?, active = ?, ModuleID = ? WHERE ModuleItemID = ?",
            (ItemName, itemLink, active, ModuleID, ModuleItemID)
        )
        db.commit()
    
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
           