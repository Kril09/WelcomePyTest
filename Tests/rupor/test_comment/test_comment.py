from Libraries.base_page import BasePage
from Libraries.video_page.video_page import VideoPage


class TestVideoPage:

    def test_add_comment_video_non_auth_user(self, driver, url, email, code):
        """Проверка добавления комментария не авторизованным пользователем"""
        video_page = VideoPage(driver, url, email, code)
        video_page.open()
        video_page.find_first_element_videos()
        video_page.click_add_comment()
        video_page.check_pop_up_auth()

    def test_add_comment_video_auth_user(self, driver, url, email, code):
        """Проверка добавления комментария авторизованным пользователем"""
        video_page = VideoPage(driver, url, email, code)
        video_page.open()
        base_page = BasePage(driver, url, email, code)
        base_page.auth(email, code)
        video_page.find_first_element_videos()
        video_page.add_comment()
        video_page.send_comment()
        video_page.check_text_comment()

    def test_edit_comment_video_auth_user(self, driver, url, email, code):
        """Проверка редактирования комментария авторизованным пользователем"""
        video_page = VideoPage(driver, url, email, code)
        video_page.open()
        base_page = BasePage(driver, url, email, code)
        base_page.auth(email, code)
        video_page.find_first_element_videos()
        video_page.click_comment_in_id_video()
        video_page.click_edit_comment_in_id_video()
        video_page.clear_comment_input()
        video_page.fill_comment_input()
        video_page.check_text_edit_comment()

    def test_add_post_comment_video_auth_user(self, driver, url, email, code):
        """Проверка добавления комментария-ответа авторизованным пользователем"""
        video_page = VideoPage(driver, url, email, code)
        video_page.open()
        base_page = BasePage(driver, url, email, code)
        base_page.auth(email, code)
        video_page.find_first_element_videos()
        video_page.add_answer()
        video_page.answer_view()
        video_page.check_text_post_add_comment()

    def test_delete_comment_video_auth_user(self, driver, url, email, code):
        """Удаление всей ветки комментариев авторизованным пользователем"""
        video_page = VideoPage(driver, url, email, code)
        video_page.open()
        base_page = BasePage(driver, url, email, code)
        base_page.auth(email, code)
        video_page.find_first_element_videos()
        video_page.click_comment()
        video_page.delete_comment()
        video_page.check_comment_on_page()
