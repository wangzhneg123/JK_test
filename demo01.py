#coding:utf-8
import allure
import pytest
"""
allure 测试报告内容展示

@allure.step()  测试用例步骤的描述
@allure.story() -个测试用例就是一个story
@allure.feature() 可以理解是一个功能点


"""

@allure.feature("功能点")
class Test01():

    @allure.step("这是step1==》测试用例步骤的描述，@allure.step  在测试报告告展示")
    def step1(self):
        print("执行步骤1")

    def step2(self):
        print("执行步骤2")

    def step3(self):
        print("执行步骤3")

    # @pytest.mark.usefixtures("login")
    # @allure.story("我是一个测试用例的 story")
    @allure.story("点击商品，加入购物车")
    def test_01(self,login):
        """
        我是测试用例的详情描述，我可以展示在报告中
        :param login: 前置条件，登录
        :return:
        """
        self.step1()
        self.step2()
        print("用例1")
        assert True

    def test_02(self,login):
        self.step1()
        self.step2()
        self.step3()
        print("用例2")
        assert True

    def test_03(self,login):
        self.step1()
        self.step3()
        print("用例3")
        assert True

