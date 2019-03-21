# coding:utf-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config import log
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.common.by import By
from config.globalparameter import img_path


class BasePage(object):

    # def __init__(self, selenium_driver, base_url, page_title):
    #     # type: (object, object, object) -> object
    #     self.driver = selenium_driver
    #     self.url = base_url
    #     self.title = page_title
    #     self.mylog = log.log()
    '''
    由于pelican项目无法直接通过url进入页面，取消url和page_title数据验证
    '''

    def __init__(self, selenium_driver):
        # type: (object, object, object) -> object
        self.driver = selenium_driver
        self.mylog = log.log()

    #   打开页面,并校验链接是否加载正确
    # def _open(self, url, page_title):
    #     try:
    #         self.driver.get(url)
    #         self.driver.maximize_window()
    #         #通过断言输入的title是否在当前title中
    #         assert page_title in self.driver.title, 'title not same'
    #     except:
    #         self.mylog.error(u'未能正确打开页面:'+url)

    #   重写find_element方法，增加定位元素的健壮性
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            print(e)
            self.mylog.error(u'找不到元素:'+str(loc))

    #   打开页面
    def enter(self, menu1_loc, menu2_loc):
        try:
            self.find_element(*menu1_loc).click()
        except Exception as e:
            print(e)
        time.sleep(5)
        try:
            self.find_element(*menu2_loc).click()
        except Exception as e:
            print(e)
        time.sleep(3)
        # try:
        #     assert self.title in self.driver.title, u'title not same'
        # except Exception as e:
        #     print(u'未能正确打开页面:' + self.title)
        #     self.driver.close()

    #   输入text并回车
    def text_enter(self, loc, value):
        try:
            self.find_element(*loc).clear()
            time.sleep(3)
            if self.is_null(loc) is False:
                self.find_element(*loc).clear()
                time.sleep(2)
            self.find_element(*loc).send_keys(value)
            time.sleep(2)
        except AttributeError:
            self.mylog.error(u'输入失败,loc='+str(loc)+u';value='+value)
        try:
            self.find_element(*loc).send_keys(Keys.ENTER)
        except Exception as e:
            print(e)

    #   仅输入text
    def text_sender(self, loc, value, clear=True):
        try:
            if clear:
                self.find_element(*loc).clear()
                time.sleep(3)
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            self.mylog.error(u'输入失败,loc='+str(loc)+u';value='+value)

    #   下拉框根据index选择
    def index_select(self, loc, index):
        try:
            select.Select(self.find_element(*loc)).select_by_index(index)
            time.sleep(2)
        except Exception as e:
            print(e)

        time.sleep(2)

    #   下拉框根据text选择
    def text_select(self, loc, text):
        try:
            select.Select(self.find_element(*loc)).select_by_visible_text(text)
        except Exception as e:
            print(e)
            print(u'找不到元素' + str(loc))
        time.sleep(2)

    #   点击按钮
    def button_click(self, loc):
        try:
            self.find_element(*loc).click()
        except Exception as e:
            print(e)
            print(u'找不到元素' + str(loc))
        time.sleep(5)

    #   判断输入框是否为空
    def is_null(self, loc):
        try:
            value = self.find_element(*loc).get_attribute('value')
        except Exception as e:
            return True
        try:
            if value.strip():
                return False
            else:
                return True
        except Exception as e:
            return True

    #   获取列表行数
    def get_table_row(self, tab_loc):
        try:
            # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
            table_tr_list = self.find_element(*tab_loc).find_elements(By.TAG_NAME, "tr")
            time.sleep(3)
            t = 0
            for tr in table_tr_list:
                t += 1
            return t
        except Exception as e:
            print(e)
        time.sleep(3)

    #   获取元素value
    def get_value(self, loc):
        try:
            value = self.find_element(*loc).get_attribute('value')
            return value
        except Exception as e:
            print(e)
            return None

    #   截图
    def img_screenshot(self, img_name):
        try:
            self.driver.get_screenshot_as_file(img_path+img_name+'.png')
        except:
            self.mylog.error(u'截图失败：'+img_name)
