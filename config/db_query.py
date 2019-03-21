from pymongo import MongoClient
import math

class check_common:

    def __init__(self):
        self.client = MongoClient('192.168.1.79', 27017, connect=False)  # 防止出现no servers found yet错误
        # self.client = MongoClient('47.75.132.197', 27017, connect=False)  # 防止出现no servers found yet错误
        db = self.client.LdxSmart
        self.packageItem = db.packageItem
        self.productInfo = db.productInfo
        self.productCustomer = db.productCustomer
        self.freightInfo = db.freightInfo
        self.accountInfo = db.accountInfo
        self.charging = db.charging
        self.chargeConfig = db.chargeConfig

    def get_packageItem(self, waybill):

        try:
            waybill_id = self.packageItem.find_one({'waybill_no': waybill})['_id']
        except Exception as e:
            print(e)
            waybill_id = None
        try:
            customer_id = self.packageItem.find_one({'waybill_no': waybill})['customer_id']
        except Exception as e:
            print(e)
            customer_id = None
        try:
            product_id = self.packageItem.find_one({'waybill_no': waybill})['product_id']
        except Exception as e:
            print(e)
            product_id = None
        try:
            delivery_volume = self.packageItem.find_one({'waybill_no': waybill})['delivery_volume']
        except Exception as e:
            print(e)
            delivery_volume = None

        value = {'waybill_id': waybill_id, 'customer_id': customer_id, 'product_id': product_id, 'delivery_volume':
            delivery_volume}
        return value

    def get_accountInfo(self, waybill_id):
        try:
            weight = self.accountInfo.find_one({'waybill_id': waybill_id})['weight']
        except Exception as e:
            print(e)
            weight = None
        try:
            account_id = self.accountInfo.find_one({'waybill_id': waybill_id})['_id']
        except Exception as e:
            print(e)
            account_id = None
        try:
            freight = self.charging.find_one({'account_id': account_id, 'item': '运费'})['fee']
        except Exception as e:
            print(e)
            freight = None

        value = {'weight': weight, 'account_id': account_id, 'freight': freight}
        return value


