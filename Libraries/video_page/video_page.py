from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Libraries.base_page import BasePage
from .constants import TEXT_COMMENT_ONE, TEXT_COMMENT_ANSWER, TEXT_COMMENT_EDIT
from .locators import MainPageLocators


class VideoPage(BasePage, MainPageLocators):

    # клик по первому видео на главной странице
    def find_first_element_videos(self):
        self.elements(self.FEED_VIDEO)[0].click()

    # клик по комментарию под видео
    def click_comment_in_id_video(self):
        """Клик в область комментария для фокуса и появления кебаб меню"""
        self.element(self.SELECTION_AREA_COMMENT).click()
        """Клик на кебаб меню"""
        self.element_is_visible(self.SELECTION_COMMENT)
        self.element(self.SELECTION_COMMENT).click()

    # фокус на области комментария для появления кебаб меню
    def click_edit_comment_in_id_video(self):
        self.element(self.BUTTON_EDIT).click()

    # Очистка поля инпута комментария
    def clear_comment_input(self):
        element = self.element_is_clickable(self.EDIT_COMMENT)
        element.click()  # фокус на элементе
        element.send_keys(Keys.CONTROL + 'a')   # Выделить текст
        element.send_keys(Keys.DELETE)  # Нажатие клавиши DELETE

    # ввод нового комментария
    def fill_comment_input(self):
        (self.element(self.EDIT_COMMENT)
         .send_keys(TEXT_COMMENT_EDIT))
        self.element_is_visible(self.SAVE_EDIT_COMMENT)
        self.element_is_clickable(self.SAVE_EDIT_COMMENT).click()

    # клик добавления комментария
    def click_add_comment(self):
        self.element(self.ADD_COMMENT).click()

    # отправка комментария
    def send_comment(self):
        self.element_is_clickable(self.SEND_COMMENT).click()

    # Добавление комментария
    def add_comment(self):
        (self.element(self.ADD_COMMENT)
         .send_keys(TEXT_COMMENT_ONE))

    # добавление комментария ответа
    def add_answer(self):
        self.element(self.ADD_ANSWER).click()
        (self.element(self.EDIT_COMMENT, 10)
         .send_keys(TEXT_COMMENT_ANSWER))
        self.element(self.SAVE_EDIT_POST_COMMENT).click()

    # раскрытие формы ответа
    def answer_view(self):
        self.element_is_clickable(self.ANSWER_VIEW).click()

    # удаление комментария
    def delete_comment(self):
        self.element(self.DELETE_COMMENT).click()
        self.element(self.DELETE).click()

    # клик по доп меню комментария под видео
    def click_comment(self):
        self.element(self.SELECTION_AREA_COMMENT).click()
        self.element(self.SELECTION_COMMENT).click()

    # проверка отображения всплывающего окна
    def check_pop_up_auth(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.POP_UP_AUTH)
        )
        return element.is_displayed()

    # проверка отображения текста комментария
    def check_text_comment(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.VISIBLE_TEXT_COMMENT
            )
        )
        return element.is_displayed()

    # проверка отображения редактированного комментария
    def check_text_edit_comment(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.CHECK_TEXT_EDIT_COMMENT
            )
        )
        return element.is_displayed()

    # проверка отображения добавленного ответа на комментарий
    def check_text_post_add_comment(self):
        element = (
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    self.CHECK_TEXT_COMMENT_ANSWER
                )
            )
        )
        return element.is_displayed()

    # проверка отсутствия комментария на странице
    def check_comment_on_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    self.CHECK_TEXT_EDIT_COMMENT)
            )
        except TimeoutException:
            assert False, 'Комментарий не удален'

    def auth(self, email, code):  # метод авторизации
        self.element(self.BUTTON_AUTH).click()
        self.element_is_clickable(self.INPUT_EMAIL, 10).send_keys(email)
        self.element(self.NEXT_BUTTON).click()
        self.element(self.INPUT_CODE).send_keys(code)
