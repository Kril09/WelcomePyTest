from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Libraries.base_page import BasePage
from Libraries.locators import MainPageLocators


class VideoPage(BasePage, MainPageLocators):
    locators = MainPageLocators()

    def find_first_element_videos(self):  # клик по первому видео на главной странице
        elements = self.element_is_visible_all(self.FEED_VIDEO)
        elements[0].click()

    def click_comment_in_id_video(self):  # клик по комментарию под видео
        """Клик в область комментария для фокуса и появления кебаб меню"""
        self.element_is_visible(self.SELECTION_AREA_COMMENT).click()
        """Клик на кебаб меню"""
        self.element_is_visible(self.SELECTION_COMMENT).click()

    def click_edit_comment_in_id_video(self):  # фокус на области комментария для появления кебаб меню
        self.element_is_visible(self.BUTTON_EDIT).click()

    def clear_comment_input(self):  # Очистка поля инпута комментария
        element = self.element_is_clickable(self.EDIT_COMMENT)
        element.click()  # фокус на элементе
        element.send_keys(Keys.CONTROL + 'a')   # Выделить текст
        element.send_keys(Keys.DELETE)  # Нажатие клавиши DELETE

    def fill_comment_input(self):  # ввод нового комментария
        self.element_is_visible(self.EDIT_COMMENT).send_keys(self.TEXT_COMMENT_EDIT)
        self.element_is_clickable(self.SAVE_EDIT_COMMENT).click()

    def click_add_comment(self):  # клик добавления комментария
        self.element_is_visible(self.ADD_COMMENT).click()

    def send_comment(self):  # отправка комментария
        self.element_is_clickable(self.SEND_COMMENT).click()

    def add_comment(self):  # Добавление комментария
        self.element_is_visible(self.ADD_COMMENT).send_keys(self.TEXT_COMMENT_ONE)

    def add_answer(self):  # добавление комментария ответа
        self.element_is_visible(self.ADD_ANSWER).click()
        self.element_is_visible(self.EDIT_COMMENT, 10).send_keys(self.TEXT_COMMENT_ANSWER)
        self.element_is_visible(self.SAVE_EDIT_POST_COMMENT).click()

    def answer_view(self):  # раскрытие формы ответа
        self.element_is_clickable(self.ANSWER_VIEW).click()

    def delete_comment(self):  # удаление комментария
        self.element_is_visible(self.DELETE_COMMENT).click()
        self.element_is_visible(self.DELETE).click()

    def click_comment(self):  # клик по доп меню комментария под видео
        self.element_is_visible(self.SELECTION_AREA_COMMENT).click()
        self.element_is_visible(self.SELECTION_COMMENT).click()

    def check_pop_up_auth(self):  # проверка отображения всплывающего окна
        element = (WebDriverWait(self.driver, 10)
                   .until(EC.presence_of_element_located(MainPageLocators.POP_UP_AUTH)))
        element.is_displayed()

    def check_text_comment(self):  # проверка отображения текста комментария
        element = (WebDriverWait(self.driver, 10)
                   .until(EC.presence_of_element_located(MainPageLocators.VISIBLE_TEXT_COMMENT)))
        element.is_displayed()

    def check_text_edit_comment(self):  # проверка отображения редактированного комментария
        element = (WebDriverWait(self.driver, 10)
                   .until(EC.presence_of_element_located(MainPageLocators.CHECK_TEXT_EDIT_COMMENT)))
        element.is_displayed()

    def check_text_post_add_comment(self):  # проверка отображения добавленного ответа на комментарий
        element = (WebDriverWait(self.driver, 10)
                   .until(EC.presence_of_element_located((By.XPATH, "//span[text()='{}']".format(MainPageLocators.TEXT_COMMENT_ANSWER)))))
        element.is_displayed()

    def check_comment_on_page(self):  # проверка отсутствия комментария на странице
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='{}']".format(MainPageLocators.TEXT_COMMENT_EDIT)))
            )
        except TimeoutException:
            assert False, 'Комментарий не удален'
