#coding=utf-8
from appium import webdriver
import unittest
import time
import random

class Xuexi(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '8.0'
        self.desired_caps['deviceName'] = 'HUAWEI Mate 9'
        self.desired_caps['appPackage'] = 'cn.xuexi.android'
        self.desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'
        self.desired_caps['noReset'] = True
        self.desired_caps['unicodeKeyboard'] = True
        self.desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.comments = ["祝愿伟大祖国永远繁荣昌盛",
                         "依法治国，建设繁荣富强中国",
                         "祖国是我们心中的灯塔，照亮我们前进的步伐",
                         "神州大地繁花似锦，祖国长空乐曲如潮",
                         "承载了中华儿女无数的光荣与梦想；向着明天，让我们用双手创造更多的辉煌",
                         "中国，正以龙的姿态腾飞，愿您越飞越高，与日月同辉，像恒星一样永存，像星星一样闪亮"]


    def test_getRestScore(self):
        time.sleep(5)
        self.driver.find_element_by_id("home_bottom_tab_button_mine").click()
        time.sleep(2)
        items = self.driver.find_elements_by_xpath("//android.view.View")
        time.sleep(1)
        items[6].click()
        time.sleep(2)
        tasks = self.driver.find_elements_by_xpath("//android.widget.ListView/android.view.View")
        print(len(tasks))



    def tearDown(self):
        self.driver.quit()

    # def test_news(self):
    #     cnt = 0
    #     time.sleep(5)
    #     self.scoreElement = self.driver.find_element_by_id("news_xuexi_score")
    #     self.score = int(self.scoreElement.text)
    #     news_score = 0
    #     self.driver.find_element_by_id("home_bottom_tab_button_work").click()
    #     time.sleep(1)
    #     self.driver.find_elements_by_xpath("//android.widget.ImageView")[2].click()
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '订阅')]").click()
    #     time.sleep(1)
    #     size = self.driver.get_window_size()
    #     x = size['width']
    #     y = size['height']
    #     self.driver.swipe(x * 0.5, y * 0.34, x * 0.5, y * 0.25, 200)
    #     done = False
    #     while(news_score < 6):
    #         newsList = self.driver.find_elements_by_xpath("//android.widget.ListView/android.widget.FrameLayout")
    #         for new in newsList:
    #             new.click()
    #             cnt += 1
    #             time.sleep(10)
    #             self.driver.press_keycode(4) #press back button
    #             time.sleep(2)
    #             news_score += int(self.scoreElement.text) - self.score
    #             self.score = int(self.scoreElement.text)
    #             if(cnt > 50):
    #                 done = True
    #                 break
    #             if(news_score >= 6):
    #                 done = True
    #                 break
    #         if(done == True):
    #             break
    #         time.sleep(1)
    #         self.driver.swipe(x*0.5, y*0.5, x*0.5, y*0.25, 200)
    #         time.sleep(2)
    #
    #     print("阅读文章及待机已获得%d分"%(news_score))
    #
    # def test_video(self):
    #     cnt = 0
    #     new_score = 0
    #     time.sleep(5)
    #
    #     self.driver.find_element_by_id("home_bottom_tab_button_contact").click()
    #     time.sleep(1)
    #
    #     self.scoreElement = self.driver.find_element_by_id("video_xuexi_score")
    #     time.sleep(1)
    #     self.score = int(self.scoreElement.text)
    #
    #     size = self.driver.get_window_size()
    #     x = size['width']
    #     y = size['height']
    #
    #     while (new_score < 6):
    #         vedioList = self.driver.find_elements_by_xpath("//android.widget.ListView/android.widget.FrameLayout")
    #         for vedio in vedioList:
    #             # print(vedio.rect)
    #             xf = vedio.rect.get('x')
    #             yf = vedio.rect.get('y')
    #             height = vedio.rect.get('height')
    #             # print(x, height, y)
    #             self.driver.tap([(xf + 1, yf + height - 1)], 100)
    #             time.sleep(10)
    #             self.driver.press_keycode(4)
    #             time.sleep(2)
    #             new_score += int(self.scoreElement.text) - self.score
    #             self.score = int(self.scoreElement.text)
    #             # print(new_score, self.score)
    #             if (new_score >= 6):
    #                 break
    #         self.driver.swipe(x * 0.5, y * 0.5, x * 0.5, y * 0.25, 200)
    #         time.sleep(1)
    #
    #     print("今日观看视频已经获得%d分"%new_score)
    #
    # def test_comment(self):
    #     cnt = 0
    #     time.sleep(5)
    #     self.scoreElement = self.driver.find_element_by_id("news_xuexi_score")
    #     self.score = int(self.scoreElement.text)
    #
    #     self.driver.find_element_by_id("home_bottom_tab_button_work").click()
    #     time.sleep(2)
    #     self.driver.find_elements_by_xpath("//android.view.ViewGroup/android.widget.LinearLayout")[2].click()
    #     time.sleep(2)
    #     size = self.driver.get_window_size()
    #     x = size['width']
    #     y = size['height']
    #
    #     while(cnt < 5):
    #         self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.FrameLayout").click()
    #         time.sleep(1)
    #         self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '欢迎发表你的观点')]").click()
    #         time.sleep(1)
    #         self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text, '好观点将会被优先展示')]").send_keys(self.comments[random.randrange(0, len(self.comments))])
    #         time.sleep(1)
    #         self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '发布')]").click()
    #         time.sleep(1)
    #         self.driver.press_keycode(4)
    #         time.sleep(1)
    #         cnt += 1
    #     print("今日已完成%d条评论"%(cnt))
    #
    # def test_LeijiNews(self):
    #     added_score = 0
    #     limitedScoreDaily = 8
    #     time.sleep(5)
    #     self.scoreElement = self.driver.find_element_by_id("news_xuexi_score")
    #     time.sleep(1)
    #     self.score = int(self.scoreElement.text)
    #
    #     self.driver.find_element_by_id("home_bottom_tab_button_work").click()
    #     time.sleep(2)
    #     self.driver.find_elements_by_xpath("//android.view.ViewGroup/android.widget.LinearLayout")[0].click()
    #     time.sleep(2)
    #     size = self.driver.get_window_size()
    #     x = size['width']
    #     y = size['height']
    #     while(added_score < limitedScoreDaily):
    #         self.driver.find_elements_by_xpath("//android.widget.ListView/android.widget.FrameLayout")[1].click()
    #         j = y
    #         for i in range(0, 25):
    #             time.sleep(10)
    #             self.driver.swipe(x * 0.5, y * 0.5, x * 0.5, y * 0.25, 200)
    #
    #         self.driver.press_keycode(4)
    #         time.sleep(2)
    #         added_score += int(self.scoreElement.text) - self.score
    #         self.score = int(self.scoreElement.text)
    #
    #     print("今日已经获得累计阅读文章%d分"%added_score)
    #
    # def test_LeijiVideo(self):
    #     added_score = 0
    #     limitedScoreDaily = 10;
    #     time.sleep(5)
    #
    #     self.driver.find_element_by_id("home_bottom_tab_button_contact").click()
    #     time.sleep(2)
    #
    #     self.scoreElement = self.driver.find_element_by_id("video_xuexi_score")
    #     time.sleep(2)
    #     self.score = int(self.scoreElement.text)
    #
    #     size = self.driver.get_window_size()
    #     x = size['width']
    #     y = size['height']
    #     while(added_score < limitedScoreDaily):
    #         video = self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.FrameLayout")
    #         xf = video.rect.get('x')
    #         yf = video.rect.get('y')
    #         height = video.rect.get('height')
    #         self.driver.tap([(xf + 1, yf + height - 1)], 100)
    #         t0 = time.clock()
    #         while(True):
    #             try:
    #                 self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '重新播放')]").click()
    #             except:
    #                 t1 = time.clock()
    #                 if(t1 - t0 > 310):
    #                     break
    #         self.driver.press_keycode(4)
    #         time.sleep(2)
    #
    #         added_score += int(self.scoreElement.text) - self.score
    #         self.score = int(self.scoreElement.text)
    #     print("今日累计观看视频已获得%d分"%added_score)
    #
    # def test_share(self):
    #     cnt = 0
    #     time.sleep(5)
    #
    #     self.driver.find_element_by_id("home_bottom_tab_button_work").click()
    #     time.sleep(2)
    #     self.driver.find_elements_by_xpath("//android.view.ViewGroup/android.widget.LinearLayout")[2].click()
    #     time.sleep(2)
    #
    #
    #     self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.FrameLayout").click()
    #     time.sleep(1)
    #     while(cnt < 6):
    #         buttons = self.driver.find_elements_by_xpath("//android.widget.LinearLayout/android.widget.ImageView")
    #         time.sleep(1)
    #         buttons[1].click()
    #         time.sleep(1)
    #         shares = self.driver.find_elements_by_xpath("//android.widget.GridView/android.widget.RelativeLayout")
    #         time.sleep(1)
    #         shares[3].click()
    #         time.sleep(1)
    #         self.driver.press_keycode(4)
    #         time.sleep(1)
    #         cnt += 1
    #     print("今日已经分享%d次"%cnt)

    # def test_collect(self):
    #     added_score = 0
    #     time.sleep(5)
    #     self.scoreElement = self.driver.find_element_by_id("news_xuexi_score")
    #     time.sleep(1)
    #     self.score = int(self.scoreElement.text)
    #
    #     self.driver.find_element_by_id("home_bottom_tab_button_work").click()
    #     time.sleep(2)
    #     self.driver.find_elements_by_xpath("//android.view.ViewGroup/android.widget.LinearLayout")[2].click()
    #     time.sleep(2)
    #
    #
    #     size = self.driver.get_window_size()
    #     x = size['width']
    #     y = size['height']
    #
    #     while(added_score < 1):
    #         news = self.driver.find_elements_by_xpath("//android.widget.ListView/android.widget.FrameLayout")
    #         time.sleep(1)
    #         for new in news:
    #             new.click()
    #             time.sleep(1)
    #             try:
    #                 self.driver.find_elements_by_xpath("//android.widget.LinearLayout/android.widget.ImageView")[2].click()
    #                 time.sleep(1)
    #                 self.driver.press_keycode(4)
    #             except:
    #                 self.driver.press_keycode(4)
    #
    #             time.sleep(1)
    #             added_score = int(self.scoreElement.text) - self.score
    #             self.score = int(self.scoreElement.text)
    #             if(added_score >= 1):
    #                 break
    #         self.driver.swipe(x * 0.5, y * 0.5, x * 0.5, y * 0.25, 200)
    #         time.sleep(1)
    #     print("今日通过收藏已获得%d分"%added_score)

if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    # suite.addTest(Xuexi("test_news"))
    # suite.addTest(Xuexi("test_video"))
    # suite.addTest(Xuexi("test_comment"))
    # suite.addTest(Xuexi("test_LeijiNews"))
    # suite.addTest(Xuexi("test_LeijiVideo"))
    # suite.addTest(Xuexi("test_share"))
    # suite.addTest(Xuexi("test_collect"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)