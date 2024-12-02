from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Libraries.base_page import BasePage
from Libraries.locators import MainPageLocators


class VideoPage(BasePage, MainPageLocators):
    locators = MainPageLocators()

    def find_first_element_videos(self): # клик по первому видео на главной странице
        elements = self.el_is_visible_all(self.SELECTION_VIDEO)
        elements[0].click()

    def click_comment_in_id_video(self): # клик по комментарию под видео
        self.el_is_visible(self.SELECTION_AREA_COMMENT).click()
        self.el_is_visible(self.SELECTION_COMMENT).click()

    def click_edit_comment_in_id_video(self): # фокус на области комментария для появления кебаб меню
        self.el_is_visible(self.BUTTON_EDIT).click()

    def click_key_delete(self): #
        element = self.el_is_clickable(self.EDIT_COMMENT)
        element.click() # фокус на элементе
        element.send_keys(Keys.CONTROL + 'a')  # Выделить текст
        element.send_keys(Keys.DELETE) # Нажатие клавиши DELETE

    def input_comment(self): # ввод нового комментария
        self.el_is_visible(self.EDIT_COMMENT).send_keys("Трулала")
        self.el_is_clickable(self.SAVE_EDIT_COMMENT).click()

    def click_add_comment(self): # клик добавления комментария
        self.el_is_visible(self.ADD_COMMENT).click()

    def auth(self): # метод авторизации
        self.el_is_visible(self.BUTTON_AUTH).click()
        self.el_is_clickable(self.INPUT_EMAIL, 10).send_keys("test_testuser1@yandex.ru")
        self.el_is_visible(self.NEXT).click()
        self.el_is_visible(self.INPUT_CODE0).send_keys("8")
        self.el_is_visible(self.INPUT_CODE1).send_keys("0")
        self.el_is_visible(self.INPUT_CODE2).send_keys("8")
        self.el_is_visible(self.INPUT_CODE3).send_keys("0")

    def send_comment(self): # отправка комментария
        self.el_is_clickable(self.SEND_COMMENT).click()

    def add_comment(self): # Добавление комментария
        self.el_is_visible(self.ADD_COMMENT).send_keys("123")

    def add_answer(self): # добавление комментария ответа
        element = self.el_is_visible(self.ADD_ANSWER)
        element.click()
        self.el_is_visible(self.EDIT_COMMENT, 10).send_keys("123-123-465-789")
        self.el_is_visible(self.SAVE_EDIT_POST_COMMENT).click()

    def answer_view(self): # раскрытие формы ответа
        self.el_is_clickable(self.ANSWER_VIEW).click()

    def delete_comment(self): # удаление комментария
        self.el_is_visible(self.DELETE_COMMENT).click()
        self.el_is_visible(self.DELETE).click()

    def click_comment(self): # клик по доп меню комментария под видео
        self.el_is_visible(self.SELECTION_AREA_COMMENT).click()
        self.el_is_visible(self.SELECTION_COMMENT).click()

    def check_pop_up_auth(self): # проверка отображения всплывающего окна
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Войдите в свой аккаунт, чтобы оставить комментарий']")))
        element.is_displayed()

    def check_text_comment(self): # проверка отображения текста комментария
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='123']")))
        element.is_displayed()

    def check_text_edit_comment(self): # проверка отображения редактированного комментария
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Трулала']")))
        element.is_displayed()

    def check_text_post_add_comment(self): # проверка отображения добавленного ответа на комментарий
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='123-123-465-789']")))
        element.is_displayed()

    def check_comment_on_page(self): # проверка отсутствия комментария на странице
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Трулала']")))
        assert not element.is_displayed() == False









