from flask import Flask
from modules import Modules
from db import *
from app import app
import pytest

@pytest.fixture(scope='module')
def create_module():
    module = Modules(ModuleID= '6', ModuleName='Module 6', active='True')
    return module

def test_create_module(create_module):
    with app.app_context():
        assert Modules.get(create_module.ModuleID) is None
        Modules.create(create_module.ModuleID, create_module.ModuleName, create_module.active)
        module_in_database = Modules.get(create_module.ModuleID)
        assert module_in_database.ModuleID == create_module.ModuleID
        assert module_in_database.ModuleName == create_module.ModuleName
        assert module_in_database.active == create_module.active
        assert Modules.get(create_module.ModuleID) is not None
        # Modules.delete(create_module.ModuleID)


def test_get_module(create_module):
    with app.app_context():
        assert Modules.get(create_module.ModuleID) is not None
        module_in_database = Modules.get(create_module.ModuleID)
        assert (module_in_database.ModuleID == "6") and (module_in_database.ModuleID == create_module.ModuleID)
        assert (module_in_database.ModuleName == "Module 6") and (module_in_database.ModuleName == create_module.ModuleName)
        assert (module_in_database.active == 'True') and (module_in_database.active == create_module.active)
        Modules.delete(create_module.ModuleID)
        assert Modules.get(create_module.ModuleID) is None


def test_get_all_modules():
    with app.app_context():
        assert Modules.getAll() is not None
        modules_in_database = Modules.getAll()
        assert len(modules_in_database) == 5
        for i in range(len(modules_in_database)):
            assert modules_in_database[i][0] == str(i + 1)

def test_update_module(create_module):
    with app.app_context():
        Modules.create(create_module.ModuleID, create_module.ModuleName, create_module.active)
        assert Modules.get(create_module.ModuleID) is not None
        Modules.update("More Information", 'False', create_module.ModuleID)
        module_in_database = Modules.get(create_module.ModuleID)
        assert (module_in_database.active == 'False') and (module_in_database.ModuleName == "More Information")
    


def test_delete_module(create_module):
    with app.app_context():
        assert Modules.get(create_module.ModuleID) is not None
        Modules.delete(create_module.ModuleID)
        assert Modules.get(create_module.ModuleID) is None
