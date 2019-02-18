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


    def test_run(self, result=None):
        time.sleep(5)
        self.news()



    def tearDown(self):
        self.driver.quit()

    def test_news(self):
        cnt = 0
        time.sleep(5)
        self.scoreElement = self.driver.find_element_by_id("news_xuexi_score")
        self.score = int(self.scoreElement.text)
        news_score = 0
        self.driver.find_element_by_id("home_bottom_tab_button_work").click()
        time.sleep(1)
        self.driver.find_elements_by_xpath("//android.widget.ImageView")[2].click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '订阅')]").click()
        time.sleep(1)
        size = self.driver.get_window_size()
        x = size['width']
        y = size['height']
        self.driver.swipe(x * 0.5, y * 0.34, x * 0.5, y * 0.25, 200)
        done = False
        while(news_score < 6):
            newsList = self.driver.find_elements_by_xpath("//android.widget.ListView/android.widget.FrameLayout")
            for new in newsList:
                new.click()
                cnt += 1
                time.sleep(10)
                self.driver.press_keycode(4) #press back button
                time.sleep(2)
                news_score += int(self.scoreElement.text) - self.score
                self.score = int(self.scoreElement.text)
                if(cnt > 50):
                    done = True
                    break
                if(news_score >= 6):
                    done = True
                    break
            if(done == True):
                break
            time.sleep(1)
            self.driver.swipe(x*0.5, y*0.5, x*0.5, y*0.25, 200)
            time.sleep(2)

        print("阅读文章及待机已获得%d分"%(news_score))

    def test_comment(self):
        cnt = 0
        time.sleep(5)
        self.scoreElement = self.driver.find_element_by_id("news_xuexi_score")
        self.score = int(self.scoreElement.text)

        self.driver.find_element_by_id("home_bottom_tab_button_work").click()
        time.sleep(2)
        self.driver.find_elements_by_xpath("//android.view.ViewGroup/android.widget.LinearLayout")[2].click()
        time.sleep(2)
        size = self.driver.get_window_size()
        x = size['width']
        y = size['height']

        while(cnt < 5):
            self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.FrameLayout").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '欢迎发表你的观点')]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text, '好观点将会被优先展示')]").send_keys(self.comments[random.randrange(0, len(self.comments))])
            time.sleep(1)
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '发布')]").click()
            time.sleep(1)
            self.driver.press_keycode(4)
            time.sleep(1)
            cnt += 1
        print("今日已完成%d条评论"%(cnt))

    def test_video(self):
        cnt = 0
        new_score = 0
        time.sleep(5)

        self.driver.find_element_by_id("home_bottom_tab_button_contact").click()
        time.sleep(1)

        self.scoreElement = self.driver.find_element_by_id("video_xuexi_score")
        time.sleep(1)
        self.score = int(self.scoreElement.text)

        size = self.driver.get_window_size()
        x = size['width']
        y = size['height']

        while (new_score < 6):
            vedioList = self.driver.find_elements_by_xpath("//android.widget.ListView/android.widget.FrameLayout")
            for vedio in vedioList:
                # print(vedio.rect)
                xf = vedio.rect.get('x')
                yf = vedio.rect.get('y')
                height = vedio.rect.get('height')
                # print(x, height, y)
                self.driver.tap([(xf + 1, yf + height - 1)], 100)
                time.sleep(10)
                self.driver.press_keycode(4)
                time.sleep(2)
                new_score += int(self.scoreElement.text) - self.score
                self.score = int(self.scoreElement.text)
                # print(new_score, self.score)
                if (new_score >= 6):
                    break
            self.driver.swipe(x * 0.5, y * 0.5, x * 0.5, y * 0.25, 200)
            time.sleep(1)

        print("今日观看视频已经获得%d分"%new_score)


    def test_demo(self):
        cnt = 0
        new_score = 0
        time.sleep(5)

        self.driver.find_element_by_id("home_bottom_tab_button_contact").click()
        time.sleep(1)

        self.scoreElement = self.driver.find_element_by_id("video_xuexi_score")
        time.sleep(1)
        self.score = int(self.scoreElement.text)

        size = self.driver.get_window_size()
        x = size['width']
        y = size['height']

        while(new_score < 6):
            vedioList = self.driver.find_elements_by_xpath("//android.widget.ListView/android.widget.FrameLayout")
            for vedio in vedioList:
                tmp = vedio.find_elements_by_xpath("/android.widget.TextView")
                if(len(tmp)):
                    # print(vedio.rect)
                    xf = vedio.rect.get('x')
                    yf = vedio.rect.get('y')
                    height = vedio.rect.get('height')
                    # print(x, height, y)
                    self.driver.tap([(xf + 1, yf + height - 1)], 100)
                    time.sleep(10)
                    self.driver.press_keycode(4)
                    time.sleep(2)
                    # self.scoreElement = self.driver.find_element_by_id("news_xuexi_score")
                    new_score += self.score - int(self.scoreElement.text)
                    self.score = int(self.scoreElement.text)
                    print(new_score, self.score)
                    if (new_score >= 6):
                        break
            self.driver.swipe(x * 0.5, y * 0.5, x * 0.5, y * 0.25, 200)
            time.sleep(1)
        print("今日观看视频已获得%d分")



if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    # suite.addTest(Xuexi("test_news"))
    # suite.addTest(Xuexi("test_comment"))
    # suite.addTest(Xuexi("test_video"))
    suite.addTest(Xuexi("test_video"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)