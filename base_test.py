from pages.product_page import ProductPage


def setup_page(browser, clazz, link):
    page = clazz(browser, link)
    page.open()
    return page


def setup_product_page(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    return setup_page(browser, ProductPage, link)
