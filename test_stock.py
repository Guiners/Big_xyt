import pytest
from stock import Stock

def test_update_info():
    test_stock = Stock()
    test_stock.update_info("buy", "add")
    assert test_stock.id == 1
    assert test_stock.order == "buy"
    assert test_stock.type == "add"

def test_print_info():
    test_stock = Stock()
    test_stock.update_info("buy", "add")
    test_stock.price = 200
    test_stock.quantity = 150
    test_stock.print_info()
    assert test_stock.info[0][0] == "001"
    assert test_stock.info[0][1] == "buy"
    assert test_stock.info[0][2] == "add"
    assert test_stock.info[0][3] == 200
    assert test_stock.info[0][4] == 150
