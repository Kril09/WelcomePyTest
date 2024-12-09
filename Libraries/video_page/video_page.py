from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Libraries.base_page import BasePage
from Libraries.locators import MainPageLocators


class VideoPage(BasePage, MainPageLocators):
    locators = MainPageLocators()

    # клик по первому видео на главной странице
    def find_first_element_videos(self):
        elements = self.element_is_visible_all(self.FEED_VIDEO)
        elements[0].click()

    # клик по комментарию под видео
    def click_comment_in_id_video(self):
        """Клик в область комментария для фокуса и появления кебаб меню"""
        self.element_is_visible(self.SELECTION_AREA_COMMENT).click()
        """Клик на кебаб меню"""
        self.element_is_visible(self.SELECTION_COMMENT).click()

    # фокус на области комментария для появления кебаб меню
    def click_edit_comment_in_id_video(self):
        self.element_is_visible(self.BUTTON_EDIT).click()

    # Очистка поля инпута комментария
    def clear_comment_input(self):
        element = self.element_is_clickable(self.EDIT_COMMENT)
        element.click()  # фокус на элементе
        element.send_keys(Keys.CONTROL + 'a')   # Выделить текст
        element.send_keys(Keys.DELETE)  # Нажатие клавиши DELETE

    # ввод нового комментария
    def fill_comment_input(self):
        (self.element_is_visible(self.EDIT_COMMENT)
         .send_keys(self.TEXT_COMMENT_EDIT))
        self.element_is_clickable(self.SAVE_EDIT_COMMENT).click()

    # клик добавления комментария
    def click_add_comment(self):
        self.element_is_visible(self.ADD_COMMENT).click()

    # отправка комментария
    def send_comment(self):
        self.element_is_clickable(self.SEND_COMMENT).click()

    # Добавление комментария
    def add_comment(self):
        (self.element_is_visible(self.ADD_COMMENT)
         .send_keys(self.TEXT_COMMENT_ONE))

    # добавление комментария ответа
    def add_answer(self):
        self.element_is_visible(self.ADD_ANSWER).click()
        (self.element_is_visible(self.EDIT_COMMENT, 10)
         .send_keys(self.TEXT_COMMENT_ANSWER))
        self.element_is_visible(self.SAVE_EDIT_POST_COMMENT).click()

    # раскрытие формы ответа
    def answer_view(self):
        self.element_is_clickable(self.ANSWER_VIEW).click()

    # удаление комментария
    def delete_comment(self):
        self.element_is_visible(self.DELETE_COMMENT).click()
        self.element_is_visible(self.DELETE).click()

    # клик по доп меню комментария под видео
    def click_comment(self):
        self.element_is_visible(self.SELECTION_AREA_COMMENT).click()
        self.element_is_visible(self.SELECTION_COMMENT).click()

    # проверка отображения всплывающего окна
    def check_pop_up_auth(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.POP_UP_AUTH)
        )
        return element.is_displayed()

    # проверка отображения текста комментария
    def check_text_comment(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                MainPageLocators.VISIBLE_TEXT_COMMENT
            )
        )
        return element.is_displayed()

    # проверка отображения редактированного комментария
    def check_text_edit_comment(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                MainPageLocators.CHECK_TEXT_EDIT_COMMENT
            )
        )
        return element.is_displayed()

    # проверка отображения добавленного ответа на комментарий
    def check_text_post_add_comment(self):
        element = (
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[text()='{}']".format(
                        MainPageLocators.TEXT_COMMENT_ANSWER)))
            )
        )
        return element.is_displayed()

    # проверка отсутствия комментария на странице
    def check_comment_on_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[text()='{}']"
                     .format(MainPageLocators.TEXT_COMMENT_EDIT)))
            )
        except TimeoutException:
            assert False, 'Комментарий не удален'
