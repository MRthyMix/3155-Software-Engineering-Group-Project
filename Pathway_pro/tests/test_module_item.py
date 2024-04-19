from flask import Flask
from moduleItem import ModuleItem
from db import *
from app import app
import pytest

@pytest.fixture(scope='module')
def create_module_item():
    moduleItem = ModuleItem(ModuleItemID="23", ItemName="Test Item", itemLink="www.test.com", active=True, ModuleID="5")
    return moduleItem

def test_create_module_item(create_module_item):
    with app.app_context():
        assert ModuleItem.get("23") == None
        ModuleItem.create(create_module_item.ModuleItemID, create_module_item.ItemName, create_module_item.itemLink, create_module_item.active, create_module_item.ModuleID)
        assert ModuleItem.get("23") != None