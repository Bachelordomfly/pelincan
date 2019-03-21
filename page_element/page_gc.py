# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import select
from config.base_page import BasePage

class GCPage(BasePage):
    # 定位器
    customerCode_loc = (By.ID, '9fafde9d-71db-41c4-93eb-d3614cb65867')  # 客户代码
    customerName_loc = (By.ID, '16841e30-4a54-4dc7-ad38-42f53b69b278')  # 客户名称
    # customerTip_loc = (By.XPATH, 'html/body/div[3]/ul/li[1]')
    product_loc = (By.ID, '6d400144-0624-4436-a83f-c15a82a6c673')   # 产品选择框
    cargoType_loc = (By.ID, '817d6d5a-cde6-4f2e-ae1e-4ffcf7abe951')  # 货物类型选择框
    waybillNo_loc = (By.ID, 'a226cab3-112c-4eeb-9656-e7715af5c652')  # 单号输入框
    pieces_loc = (By.ID, '91757076-bc27-49b8-949c-8b0fe7035fd6')    # 件数输入框
    remark_loc = (By.ID, 'af6f108b-64ca-4e33-ba67-16d5f3a4f29f')    # 备注输入框
    allweight_loc = (By.ID, '63a1cd31-0d8d-40e0-ae51-70d676ffbf09')  # 总重显示
    picker_loc = (By.ID, '94903af0-84c0-49e2-89c8-ffec217559ab')    # 取件人输入框
    preweight_loc = (By.ID, '99af2c0c-5ec0-4579-ad7a-5cfa125d19d2')  # 预录重量显示
    save_loc = (By.ID, '2f81b74f-a1ee-42d1-8f64-2b3cf6e97a5b')  # 保存按钮
    table_loc = (By.ID, '390dd8f4-8405-4f64-a260-230a0e54b619-non-body')    # 列表
    menu1_loc = (By.PARTIAL_LINK_TEXT, '业务操作')
    menu2_loc = (By.LINK_TEXT, '收货')
    subwaybill_loc = (By.NAME, '955bcb97-c9e7-4a6b-8a20-96cc135a3dd8')  # 子单号
    subweight_loc = (By.NAME, 'a77a91a3-714a-4bc9-baf9-11b1c7ca049bValue')  # 子单重量

    def gc_enter(self):
        self.enter(self.menu1_loc, self.menu2_loc)

    #   输入客户代码回车
    def cus_code_enter(self, cus_code):
        BasePage.text_enter(self, self.customerCode_loc, cus_code)

    #   输入客户名称回车
    def cus_name_enter(self, cus_name):
        BasePage.text_enter(self, self.customerName_loc, cus_name)

    #   选择产品
    def product_select(self, index):
        BasePage.index_select(self, self.product_loc, index)

    #   选择货物类型
    def cargotype_select(self, index):
        BasePage.index_select(self, self.cargoType_loc, index)

    #   输入单号回车
    def waybill_enter(self, waybill):
        BasePage.text_enter(self, self.waybillNo_loc, waybill)

    def waybill_send(self, waybill):
        BasePage.text_sender(self, self.waybillNo_loc, waybill)

    #   输入件数回车
    def pieces_enter(self, pieces):
        BasePage.text_enter(self, self.pieces_loc, pieces)

    #   输入备注
    def remark_write(self, remark):
        BasePage.text_enter(self, self.remark_loc, remark)

    #   输入子单号
    def subwaybill_enter(self, sub_waybill):
        BasePage.text_enter(self, self.subwaybill_loc, sub_waybill)

    #   输入子单重量
    def subweight_enter(self, weight):
        BasePage.text_enter(self, self.subweight_loc, weight)

    #   点击保存
    def save_click(self):
        BasePage.button_click(self, self.save_loc)

    #   判断单号输入框是否为空
    def waybill_is_null(self):
        return BasePage.is_null(self, self.waybillNo_loc)

    #   判断客户名称是否为空
    def name_is_null(self):
        return BasePage.is_null(self, self.customerName_loc)

    #   产品是否为空
    def product_is_null(self):
         return BasePage.is_null(self, self.product_loc)

    #   货物类型是否为空
    def cargo_is_null(self):
         return BasePage.is_null(self, self.cargoType_loc)

    #   件数是否为空
    def pieces_is_null(self):
        return BasePage.is_null(self, self.pieces_loc)

    #   总重是否为空
    def allweight_is_null(self):
        return BasePage.is_null(self, self.allweight_loc)

    #   获取列表行数
    def get_table_row(self, driver):
        try:
            # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
            table_tr_list = driver.find_element(*self.table_loc).find_elements(By.TAG_NAME, "tr")
            time.sleep(3)
            t = 0
            for tr in table_tr_list:
                t += 1
        except Exception as e:
            print(e)
            t = 0
        return t

    #   输入所有子单信息
    def get_table_content(self, driver, value_num):
        arr = []
        arr1 = []
        try:
            # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
            table_tr_list = driver.find_element(*self.table_loc).find_elements(By.TAG_NAME, "tr")
            time.sleep(5)
            for tr in table_tr_list:
                # result = unicode(tr.text, 'GBK').encode('UTF-8')
                arr1 = (tr.text).split(" ")  # 以空格拆分成若干个(个数与列的个数相同)一维列表
                arr.append(arr1)  # 将表格数据组成二维的列表

        except Exception as e:
            print(e)

        # 循环遍历table数据，确定查询数据的位置
        for i in range(len(arr)):
            tip_num = value_num[i]
            for j in range(len(arr[i])):
                print(arr[i][j])
                input_xpath = (By.XPATH, '//*[@id="390dd8f4-8405-4f64-a260-230a0e54b619-non-body"]/tbody/tr[j]/td[i+1]/input')
                BasePage.text_sender(self, input_xpath, tip_num[j])

        time.sleep(5)

