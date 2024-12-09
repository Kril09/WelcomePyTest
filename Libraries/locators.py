from selenium.webdriver.common.by import By


class MainPageLocators:

    # выбор видео
    FEED_VIDEO = (By.CSS_SELECTOR, "[data-testid *= 'h-video-card-header_']")  # выбор видео на главной
    # действие с комментарием
    SELECTION_COMMENT = (By.CSS_SELECTOR, "[data-testid *= 'dropdown-button']")  # выбор комментария
    BUTTON_EDIT = (By.XPATH, "//span[text()='редактировать']")  # кнопка редактирования
    SELECTION_AREA_COMMENT = \
        (By.XPATH, "//div[@class = ' grid grid-flow-col justify-start items-center gap-x-4 pb-4']")  # выбор области
    ADD_COMMENT = (By.XPATH, "//textarea[@placeholder='Ваш комментарий...']")  # добавить комментарий
    EDIT_COMMENT = (By.CSS_SELECTOR, "[data-testid *= '-reply-input_']")  # кнопка редактирования комментария
    SAVE_EDIT_COMMENT = \
        (By.CSS_SELECTOR, "[data-testid *= '-reply-button_']")  # сохранить отредактированный комментарий
    SAVE_EDIT_POST_COMMENT = (By.XPATH, "//span[text()='Ответить']")  # сохранить отредактированный комментарий
    SEND_COMMENT = (By.XPATH, "//span[text()='Отправить коментарий']")  # отправить комментарий
    SAVE_COMMENT = (By.CSS_SELECTOR, "[data-testid *= 'video-comments-comment-']")  # кнопка Сохранить
    ADD_ANSWER = (By.XPATH, "//button[text()='Ответить']")  # кнопка Ответить
    ANSWER_VIEW = (By.CSS_SELECTOR, "[data-testid *= '-hide-show-childes_']")  # раскрывашка показать ответ
    DELETE_COMMENT = (By.CSS_SELECTOR, "[data-testid *= '-dropdown-option-delete_']")  # доп.меню кнопка удалить
    DELETE = (By.XPATH, "//span[text()='Удалить']")  # подтверждение удаления
    # Авторизация
    BUTTON_AUTH = (By.XPATH, "//span[text()='Войти']")  # кнопка Войти
    INPUT_EMAIL = (By.XPATH, "//input[@name = 'login']")  # ввод почты
    NEXT_BUTTON = (By.XPATH, "//span[text() = 'Далее']")  # кнопка Далее
    INPUT_CODE0 = (By.XPATH, "//input[@data-testid='otp-input-0']")  # ввод кода
    # Тексты комментариев
    TEXT_COMMENT_ONE = '123'  # текст первого комментария
    TEXT_COMMENT_EDIT = 'Трулала'  # текст для редактирования комментария
    TEXT_COMMENT_ANSWER = '123-123-465-789'  # текст комментария ответа
    # Проверки
    CHECK_TEXT_EDIT_COMMENT = (By.XPATH, "//span[text()='{}']".format(TEXT_COMMENT_EDIT))
    POP_UP_AUTH = (By.XPATH, "//div[text()='Войдите в свой аккаунт, чтобы оставить комментарий']")  # всплывашка
    VISIBLE_TEXT_COMMENT = (By.XPATH, "//span[text()='{}']".format(TEXT_COMMENT_ONE))
