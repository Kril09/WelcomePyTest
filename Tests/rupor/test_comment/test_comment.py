from Libraries.video_page.video_page import VideoPage
from Tests.rupor.conftest import driver
from Tests.rupor.conftest import url


class TestVideoPage:

    """Проверка добавления комментария не авторизованным пользователем"""
    def test_add_comment_video_non_auth_user(self, driver, url):
        video_page = VideoPage(driver, url)
        video_page.open()
        video_page.find_first_element_videos()
        video_page.click_add_comment()
        video_page.check_pop_up_auth()

    """Проверка добавления комментария авторизованным пользователем"""
    def test_add_comment_video_auth_user(self, driver, url):
        video_page = VideoPage(driver, url)
        video_page.open()
        video_page.auth()
        video_page.find_first_element_videos()
        video_page.add_comment()
        video_page.send_comment()
        video_page.check_text_comment()

    """Проверка редактирования комментария авторизованным пользователем"""
    def test_edit_comment_video_auth_user(self, driver, url):
        video_page = VideoPage(driver, url)
        video_page.open()
        video_page.auth()
        video_page.find_first_element_videos()
        video_page.click_comment_in_id_video()
        video_page.click_edit_comment_in_id_video()
        video_page.click_key_delete()
        video_page.input_comment()
        video_page.check_text_edit_comment()

    """Проверка добавления комментария ответа авторизованным пользователем"""
    def test_add_post_comment_video_auth_user(self, driver, url):
        video_page = VideoPage(driver, url)
        video_page.open()
        video_page.auth()
        video_page.find_first_element_videos()
        video_page.add_answer()
        video_page.answer_view()
        video_page.check_text_post_add_comment()

    """Удаление всей ветки комментариев авторизованным пользователем"""
    def test_delete_comment_video_auth_user(self, driver, url):
        video_page = VideoPage(driver, url)
        video_page.open()
        video_page.auth()
        video_page.find_first_element_videos()
        video_page.click_comment()
        video_page.delete_comment()
        video_page.check_comment_on_page()











