#Data
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

button_add_to_basket_locator = '//button[@class= "btn btn-lg btn-primary btn-add-to-basket"]'
language_locator = '//select[@name= "language"]'


def test_watch_button_add_to_basket(browser):
    #Data
    exp_btn_text_dict = {
        "en-gb": "Add to basket",
        "ru": "Добавить в корзину",
        "es": "Añadir al carrito",
        "fr": "Ajouter au panier"
    }
    expected_lang_code = browser.user_language
    expected_btn_text = exp_btn_text_dict[expected_lang_code]

    #Arrange
    browser.get(link)

    #Act
    button_add_to_basket_find = browser.find_element_by_xpath(button_add_to_basket_locator)
    button_add_to_basket = button_add_to_basket_find.text

    #Assert
    assert expected_btn_text in button_add_to_basket, \
        f"button text is different"
