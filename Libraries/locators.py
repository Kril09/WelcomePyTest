from selenium.webdriver.common.by import By

class MainPageLocators:

    MENY_BUTTON_CATEGORY = (By.XPATH, "//span[text()='Категории']") # раздел Категории
    MENY_BUTTON_SUBSCRIPTION = (By.XPATH, "//span[text()='Подписки']") # раздел Подписки
    MENY_BUTTON_CHANNEL = (By.XPATH, "//span[text()='Каналы']") # раздел Каналы

    SELECTION_VIDEO = (By.CSS_SELECTOR, "[data-testid *= 'h-video-card-header_']") # выбор видео на главной
    SELECTION_COMMENT = (By.CSS_SELECTOR, "[data-testid *= 'dropdown-button']") # выбор комментария
    BUTTON_EDIT = (By.XPATH, "//span[text()='редактировать']") # кнопка редактирования
    SELECTION_AREA_COMMENT = (By.XPATH, "//div[@class = ' grid grid-flow-col justify-start items-center gap-x-4 pb-4']")# выбор области комментария
    ADD_COMMENT = (By.XPATH, "//textarea[@placeholder='Ваш комментарий...']") # добавить комментарий
    EDIT_COMMENT = (By.CSS_SELECTOR, "[data-testid *= '-reply-input_']")  # кнопка редактирования комментария
    SAVE_EDIT_COMMENT = (By.CSS_SELECTOR, "[data-testid *= '-reply-button_']")  # сохранить отредактированный комментарий
    SAVE_EDIT_POST_COMMENT = (By.XPATH, "//span[text()='Ответить']")  # сохранить отредактированный комментарий
    SEND_COMMENT = (By.XPATH, "//span[text()='Отправить коментарий']")  # отправить комментарий
    SAVE_COMMENT = (By.CSS_SELECTOR, "[data-testid *= 'video-comments-comment-']") # кнопка Сохранить
    POP_UP_AUTH = (By.XPATH, "//div[text()='Войдите в свой аккаунт, чтобы оставить комментарий']") # всплывашка
    ADD_ANSWER = (By.XPATH, "//button[text()='Ответить']") # кнопка Ответить
    ANSWER_VIEW = (By.CSS_SELECTOR, "[data-testid *= '-hide-show-childes_']") # раскрывашка показать ответ
    DELETE_COMMENT = (By.CSS_SELECTOR, "[data-testid *= '-dropdown-option-delete_']") # доп.меню кнопка удалить
    DELETE = (By.XPATH, "//span[text()='Удалить']") # подтверждение удаления

    BOX_CATEGORY = (By.XPATH, "//div[text()='Категории']") # название раздела Категории
    BOX_SUBSCRIPTION = (By.XPATH, "//div[text()='Подписки']") # название раздела Подписки
    BOX_CHANNEL = (By.XPATH, "//div[text()='Каналы']") # название раздела Каналы

    BUTTON_AUTH = (By.XPATH, "//span[text()='Войти']")
    INPUT_EMAIL = (By.XPATH, "//input[@name = 'login']")
    NEXT = (By.XPATH, "//span[text() = 'Далее']")
    INPUT_CODE0 = (By.XPATH, "//input[@data-testid='otp-input-0']")
    INPUT_CODE1 = (By.XPATH, "//input[@data-testid='otp-input-1']")
    INPUT_CODE2 = (By.XPATH, "//input[@data-testid='otp-input-2']")
    INPUT_CODE3 = (By.XPATH, "//input[@data-testid='otp-input-3']")