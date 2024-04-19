from flask import Flask
from moduleItem import ModuleItem
from db import *
from app import app
import pytest

@pytest.fixture(scope='module')
def create_module_item():
    moduleItem = ModuleItem(ModuleItemID="23", ItemName="Test Item", itemLink="www.test.com", active='True', ModuleID="5")
    return moduleItem

def test_create_module_item(create_module_item):
    with app.app_context():
        assert ModuleItem.get("23") == None
        ModuleItem.create(create_module_item.ModuleItemID, create_module_item.ItemName, create_module_item.itemLink, create_module_item.active, create_module_item.ModuleID)
        assert ModuleItem.get("23") != None

def test_get_module_item(create_module_item):
    with app.app_context():
        assert ModuleItem.get("23") != None
        moduleItem = ModuleItem.get("23")
        assert moduleItem.ModuleItemID == create_module_item.ModuleItemID
        assert moduleItem.ItemName == create_module_item.ItemName
        assert moduleItem.itemLink == create_module_item.itemLink
        assert moduleItem.active == create_module_item.active
        assert moduleItem.ModuleID == create_module_item.ModuleID
        assert ModuleItem.get("24") == None

def test_update_module_item(create_module_item):
    with app.app_context():
        assert ModuleItem.get("23") != None
        ModuleItem.update("23", "New Item", "www.new.com", 'False', "6")
        moduleItem = ModuleItem.get("23")
        assert moduleItem.ModuleItemID == create_module_item.ModuleItemID
        assert moduleItem.ItemName == 'New Item'
        assert moduleItem.itemLink == 'www.new.com'
        assert moduleItem.active == 'False'
        assert moduleItem.ModuleID == "6"

def test_delete_module_item(create_module_item):    
    with app.app_context():
        assert ModuleItem.get(create_module_item.ModuleItemID) != None
        ModuleItem.delete(create_module_item.ModuleItemID)
        assert ModuleItem.get(create_module_item.ModuleItemID) == None
