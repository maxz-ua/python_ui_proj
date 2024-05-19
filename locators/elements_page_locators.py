from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RB = By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]'
    IMPRESSIVE_RB = By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]'
    NO_RB = By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]'
    OUTPUT_RESULT = By.CSS_SELECTOR, 'p span[class="text-success"]'


class ButtonsPageLocators:
    DOUBLE = By.CSS_SELECTOR, "button[id='doubleClickBtn']"
    RIGHT = By.CSS_SELECTOR, "button[id='rightClickBtn']"
    CLICK = By.XPATH, "//div[3]/button"

    # results
    SUCCESS_DOUBLE = By.CSS_SELECTOR, "p[id='doubleClickMessage']"
    SUCCESS_RIGHT = By.CSS_SELECTOR, "p[id='rightClickMessage']"
    SUCCESS_CLICK = By.CSS_SELECTOR, "p[id='dynamicClickMessage']"


class UploadAndDownloadPageLocators:
    UPLOAD = By.CSS_SELECTOR, 'input[id="uploadFile"]'
    UPLOADED = By.CSS_SELECTOR, 'p[id="uploadedFilePath"]'
    DOWNLOAD = By.CSS_SELECTOR, 'a[id="downloadButton"]'
