import os
import time
import json

from selenium import webdriver

# config = open('./config.txt','r')
f=open('./config.txt', encoding='utf-8')
txt=''
for line in f:
    txt = txt + line.strip()
print(txt,type(txt))
print(json.loads(txt),type(json.loads(txt)))
config = json.loads(txt)
chromedriver = config['chromedriver']
# chromedriver = "F:/chromedriver_win32/chromedriver"  # 驱动程序所在的位置
os.environ["webdriver.chrome.driver"] = chromedriver
chromeOptions = webdriver.ChromeOptions()
# 设定下载文件的保存目录
# 如果该目录不存在，将会自动创建
# data = input("please enter the data: ")
down_path = ''
prefs = {"download.default_directory": down_path}
# 将自定义设置添加到Chrome配置对象实例中
chromeOptions.add_experimental_option("prefs", prefs)
# 启动带有自定义设置的Chrome浏览器
driver = webdriver.Chrome(chromedriver, \
                          options=chromeOptions)
driver.maximize_window()  # 窗口最大化（无关紧要哈）


# 登录
driver.get(config['website'])
username = driver.find_element_by_name("username")
username.send_keys(config['username'])
password = driver.find_element_by_name("password")
password.send_keys(config['password'])
time.sleep(1)
submit = driver.find_element_by_xpath("//div[@class='el-form-item__content']/button[@class='el-button el-button--primary']")
submit.click()

time.sleep(3)


# 查询数据
dataset_name = driver.find_element_by_xpath("//div[@class='el-row dataSearchRowStyle'][1]/div[@class='el-col el-col-16']/div[@class='el-input el-input--mini']/div[@class='el-input__wrapper']/input")
dataset_name.send_keys(config['form'])
search = driver.find_element_by_xpath("//div[@class='dataSearchRowStyle']/button[@class='el-button el-button--mini'][1]")
search.click()
time.sleep(1)

table = driver.find_element_by_xpath("/html[@class=' ']/body/div[@id='app']/div[@class='el-carousel el-carousel--horizontal']/div[@class='el-carousel__container']/div[@class='el-carousel__item is-active is-animating']/section[@class='el-container']/aside[@id='el-aside-table']/div[@class='el-table--fit el-table--enable-row-hover el-table--enable-row-transition el-table el-table--layout-fixed is-scrolling-none']/div[@class='el-table__inner-wrapper']/div[@class='el-table__body-wrapper']/div[@class='el-scrollbar']/div[@class='el-scrollbar__wrap el-scrollbar__wrap--hidden-default']/div[@class='el-scrollbar__view']/table[@class='el-table__body']/tbody/tr[@class='el-table__row'][1]/td[@class='el-table_3_column_11 is-center el-table__cell']/div[@class='cell el-tooltip']")
table.click()

time.sleep(3)
table_detail = driver.find_element_by_xpath("/html[@class=' ']/body/div[@id='app']/div[@class='el-carousel el-carousel--horizontal']/div[@class='el-carousel__container']/div[@class='el-carousel__item is-active is-animating']/section[@class='el-container']/aside[@class='el-aside metadata']/div[@class='el-table--fit el-table--border el-table--enable-row-hover el-table--enable-row-transition el-table el-table--layout-fixed is-scrolling-none']/div[@class='el-table__inner-wrapper']/div[@class='el-table__body-wrapper']/div[@class='el-scrollbar']/div[@class='el-scrollbar__wrap el-scrollbar__wrap--hidden-default']/div[@class='el-scrollbar__view']/table[@class='el-table__body']/tbody/tr[@class='el-table__row'][1]/td[@class='el-table_4_column_13 is-center el-table__cell']/div[@class='cell el-tooltip']")
table_detail = driver.find_element_by_xpath("/html[@class=' ']/body/div[@id='app']/div[@class='el-carousel el-carousel--horizontal']/div[@class='el-carousel__container']/div[@class='el-carousel__item is-active is-animating']/section[@class='el-container']/aside[@class='el-aside metadata']/div[@class='el-table--fit el-table--border el-table--enable-row-hover el-table--enable-row-transition el-table el-table--layout-fixed is-scrolling-none']/div[@class='el-table__inner-wrapper']/div[@class='el-table__body-wrapper']/div[@class='el-scrollbar']/div[@class='el-scrollbar__wrap el-scrollbar__wrap--hidden-default']/div[@class='el-scrollbar__view']/table[@class='el-table__body']/tbody/tr[@class='el-table__row'][1]")
table_detail.click()

profile = driver.find_element_by_xpath("/html[@class=' ']/body/div[@id='app']/div[@class='el-carousel el-carousel--horizontal']/div[@class='el-carousel__container']/div[@class='el-carousel__item is-active is-animating']/section[@class='el-container']/main[@class='el-main']/div[@class='deepAndSea'][1]/button[@class='el-button el-button--small btn'][2]")
profile.click()

canvas = driver.find_element_by_id("wind")
# top= "var q=document.documentElement.scrollTop=0"
# driver.execute_script(top)
actions = webdriver.ActionChains(driver)
actions.click_and_hold(canvas)
time.sleep(3)
print('yidong')
# actions.move_by_offset(-400,-300)
for i in range(1,60):
    actions.move_by_offset(-10, -8)
time.sleep(5)
actions.click().release().perform()

time.sleep(5)
lon = driver.find_element_by_xpath("//div[@id=' btnTemporalAnalysisId']")
lon.click()
time.sleep(5)
lat = driver.find_element_by_xpath("//div[@id='btnLonLatDepthId']")
lat.click()
time.sleep(5)


# 滚轮
# test = driver.find_element_by_id("testone")
# display_block = "document.getElementById(\"testone\").style.display='block';"
# # 调用js脚本
# driver.execute_script(display_block)
# test.click()
# display_none = "document.getElementById(\"testone\").style.display='none';"
# driver.execute_script(display_none)

