from selenium.webdriver.common.by import By


class MainPageLocators:

    # выбор видео
    FEED_VIDEO = (By.CSS_SELECTOR, "[data-testid *= 'h-video-card-header_']")
    # действие с комментарием
    # выбор комментария
    SELECTION_COMMENT = (By.CSS_SELECTOR, "[data-testid *= 'dropdown-button']")
    # кнопка редактирования
    BUTTON_EDIT = (By.XPATH, "//span[text()='редактировать']")
    # выбор области
    SELECTION_AREA_COMMENT = \
        (By.XPATH,
         "//div[@class = "
         "' grid grid-flow-col justify-start items-center gap-x-4 pb-4']")
    # добавить комментарий
    ADD_COMMENT = (By.XPATH, "//textarea[@placeholder='Ваш комментарий...']")
    # кнопка редактирования комментария
    EDIT_COMMENT = (By.CSS_SELECTOR, "[data-testid *= '-reply-input_']")
    # сохранить отредактированный комментарий
    SAVE_EDIT_COMMENT = \
        (By.CSS_SELECTOR, "[data-testid *= '-reply-button_']")
    # сохранить отредактированный комментарий
    SAVE_EDIT_POST_COMMENT = (By.XPATH, "//span[text()='Ответить']")
    # отправить комментарий
    SEND_COMMENT = (By.XPATH, "//span[text()='Отправить коментарий']")
    # кнопка Сохранить
    SAVE_COMMENT = \
        (By.CSS_SELECTOR, "[data-testid *= 'video-comments-comment-']")
    # кнопка Ответить
    ADD_ANSWER = (By.XPATH, "//button[text()='Ответить']")
    # раскрывашка показать ответ
    ANSWER_VIEW = (By.CSS_SELECTOR, "[data-testid *= '-hide-show-childes_']")
    # доп.меню кнопка удалить
    DELETE_COMMENT = \
        (By.CSS_SELECTOR, "[data-testid *= '-dropdown-option-delete_']")
    DELETE = (By.XPATH, "//span[text()='Удалить']")  # подтверждение удаления
    # Авторизация
    # кнопка Войти
    BUTTON_AUTH = (By.XPATH, "//span[text()='Войти']")
    # ввод почты
    INPUT_EMAIL = (By.XPATH, "//input[@name = 'login']")
    # кнопка Далее
    NEXT_BUTTON = (By.XPATH, "//span[text() = 'Далее']")
    # ввод кода
    INPUT_CODE0 = (By.XPATH, "//input[@data-testid='otp-input-0']")
    # Тексты комментариев
    TEXT_COMMENT_ONE = '123'  # текст первого комментария
    TEXT_COMMENT_EDIT = 'Трулала'  # текст для редактирования комментария
    TEXT_COMMENT_ANSWER = '123-123-465-789'  # текст комментария ответа
    # Проверки
    CHECK_TEXT_EDIT_COMMENT = \
        (By.XPATH, "//span[text()='{}']".format(TEXT_COMMENT_EDIT))
    # всплывашка
    POP_UP_AUTH = (
        By.XPATH, "//div[text()="
                  "'Войдите в свой аккаунт, чтобы оставить комментарий']")
    VISIBLE_TEXT_COMMENT = \
        (By.XPATH, "//span[text()='{}']".format(TEXT_COMMENT_ONE))
