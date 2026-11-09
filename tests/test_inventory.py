import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestInventory:
    def test_add_backpack_to_cart(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()

        actual_count = inventory_page.get_cart_badge_count()
        assert actual_count == "1", f"Diharapkan '1', tapi dapat '{actual_count}'"

    def test_logout_flow(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.logout()

        actual_url = login_page.get_current_url()
        assert actual_url == "https://www.saucedemo.com/", f"URL salah: {actual_url}"
        assert login_page.find_element(login_page.LOGIN_BUTTON).is_displayed() is True