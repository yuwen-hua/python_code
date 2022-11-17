import datetime
import os
from time import sleep

from flask import current_app
from selenium import webdriver

data = [
    {
        "GLOBAL_ANALYSIS_FORECAST_PHY_001_024": [
            "cmems_mod_glo_phy_anfc_merged-uv_PT1H-i",
            "global-analysis-forecast-phy-001-024",
            "global-analysis-forecast-phy-001-024-3dinst-so",
            "global-analysis-forecast-phy-001-024-3dinst-thetao",
            "global-analysis-forecast-phy-001-024-3dinst-uovo",
            "global-analysis-forecast-phy-001-024-hourly-t-u-v-ssh",
            "global-analysis-forecast-phy-001-024-monthly",
            "global-analysis-forecast-phy-001-024-statics"
        ]
    },
    {
        "GLOBAL_ANALYSIS_FORECAST_WAV_001_027": [
            "global-analysis-forecast-wav-001-027",
            "global-analysis-forecast-wav-001-027-statics"
        ]
    },
    {
        "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002": [
            "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_25_ASC_V2",
            "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_25_DES_V2",
            "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_50_ASC_V2",
            "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_50_DES_V2",
            "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_25_ASC_V2",
            "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_25_DES_V2",
            "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_50_ASC_V2",
            "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_50_DES_V2",
            "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_12_ASC_V2",
            "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_12_DES_V2",
            "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_25_ASC_V2",
            "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_25_DES_V2",
            "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_12_ASC_V2",
            "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_12_DES_V2",
            "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_25_ASC_V2",
            "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_25_DES_V2",
            "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_12_ASC_V2",
            "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_12_DES_V2",
            "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_25_ASC_V2",
            "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_25_DES_V2",
            "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_25_ASC_V2",
            "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_25_DES_V2",
            "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_50_ASC_V2",
            "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_50_DES_V2"
        ]
    },
    {
        "SEALEVEL_GLO_PHY_L4_NRT_OBSERVATIONS_008_046": [
            "dataset-duacs-nrt-global-merged-allsat-phy-l4"
        ]
    },
    {
        "WAVE_GLO_WAV_L4_SWH_NRT_OBSERVATIONS_014_003": [
            "dataset-wav-l4-swh-nrt-global"
        ]
    },
    {
        "MULTIOBS_GLO_PHY_NRT_015_003": [
            "dataset-uv-nrt-daily",
            "dataset-uv-nrt-hourly",
            "dataset-uv-nrt-monthly"
        ]
    },
    {
        "OCEANCOLOUR_GLO_BGC_L3_NRT_009_101": [
            "cmems_obs-oc_glo_bgc-plankton_nrt_l3-multi-4km_P1D",
            "cmems_obs-oc_glo_bgc-plankton_nrt_l3-olci-300m_P1D",
            "cmems_obs-oc_glo_bgc-plankton_nrt_l3-olci-4km_P1D",
            "cmems_obs-oc_glo_bgc-reflectance_nrt_l3-multi-4km_P1D",
            "cmems_obs-oc_glo_bgc-reflectance_nrt_l3-olci-4km_P1D",
            "cmems_obs-oc_glo_bgc-transp_nrt_l3-multi-4km_P1D",
            "cmems_obs-oc_glo_bgc-transp_nrt_l3-olci-4km_P1D",
            "cmems_obs-oc_glo_bgc-optics_nrt_l3-multi-4km_P1D"
        ]
    },
    {
        "SST_GLO_SST_L3S_NRT_OBSERVATIONS_010_010": [
            "IFREMER-GLOB-SST-L3-NRT-OBS_FULL_TIME_SERIE"
        ]
    },
    {
        "MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013": [
            "dataset-sss-ssd-nrt-monthly",
            "dataset-sss-ssd-nrt-weekly",
            "dataset-sss-ssd-rep-monthly",
            "dataset-sss-ssd-rep-weekly"
        ]
    }
]


# 自动下载  https://resources.marine.copernicus.eu/ 网站八个类型的每天所有数据

# chromedriver = "F:/chromedriver_win32/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# chromeOptions = webdriver.ChromeOptions()
#     # 设定下载文件的保存目录
#     # 如果该目录不存在，将会自动创建
#     prefs = {"download.default_directory": down_path}
#     # 将自定义设置添加到Chrome配置对象实例中
#     chromeOptions.add_experimental_option("prefs", prefs)
#     # 启动带有自定义设置的Chrome浏览器
#     driver = webdriver.Chrome(chromedriver, \
#                               chrome_options=chromeOptions)
#     driver.maximize_window()  # 窗口最大化（无关紧要哈）
class Chrome():
    def __init__(self):
        # driver = webdriver.Chrome()
        # chromedriver 安装位置
        os.environ["webdriver.chrome.driver"] = current_app.config['CHROMEDRIVER']
        chromeOptions = webdriver.ChromeOptions()

        option = webdriver.ChromeOptions()
        # 设置 下载路径
        file_date = datetime.datetime.now().strftime('%Y\\%m\\%d')
        down_path = 'D:\\dataSource\\copernicus' + '\\' + file_date
        prefs = {"download.default_directory": down_path}
        option.add_experimental_option("detach", True)
        chromeOptions.add_experimental_option("prefs", prefs)

        # 将option作为参数添加到Chrome中
        driver = webdriver.Chrome(current_app.config['CHROMEDRIVER'], \
                                  chrome_options=chromeOptions)

        # 登录
        driver.get('https://cmems-cas.cls.fr/cas/login')
        username = driver.find_element_by_id("username")
        password = driver.find_element_by_id("password")
        # It = driver.find_element_by_xpath("//fieldset[@class='input']/input[2]")
        submit = driver.find_element_by_class_name("submit")
        # print(It,submit)
        username.send_keys('xchen7')
        sleep(5)
        password.send_keys('Wdmm9916@')
        sleep(5)
        submit.click()
        sleep(30)
        #  下面是 遍历data中的数据并下载
        for i in data:
            for product in i:
                driver.get('https://resources.marine.copernicus.eu/products')
                sleep(30)
                # 获取数据集
                path = 'https://resources.marine.copernicus.eu/product-detail/' + product + '/DATA-ACCESS'
                for s in range(len(i[product])):
                    driver.get(path)
                    sleep(60)
                    # 跳转下载页面
                    api_xpath = "//tbody/tr[@class='mat-row cdk-row ng-star-inserted'][" + str(
                        s + 1) + "]/td[@class='mat-cell cdk-cell width-cell-dataset cdk-column-datasetSub mat-column-datasetSub ng-star-inserted']/span[@class='ng-star-inserted']/a[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary ng-star-inserted']"
                    api = driver.find_element_by_xpath(api_xpath)
                    api.click()
                    sleep(60)
                    # 点击下载按钮
                    down_button = driver.find_element_by_xpath(
                        "//p[@class='product-download-actions']/button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary']")
                    down_button.click()
                    sleep(60)
                    # 下载
                    down = driver.find_element_by_xpath(
                        "//div[@class='product-download-parameters-selection-data-ready ng-star-inserted']/button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary']")
                    down.click()

        # 下载固定类型，固定dataset
        # driver.get('https://resources.marine.copernicus.eu/products')
        # sleep(2)
        # driver.get('https://resources.marine.copernicus.eu/product-detail/GLOBAL_ANALYSIS_FORECAST_PHY_001_024/DATA-ACCESS')
        # sleep(2)
        # api = driver.find_element_by_xpath("//tbody/tr[@class='mat-row cdk-row ng-star-inserted'][1]/td[@class='mat-cell cdk-cell width-cell-dataset cdk-column-datasetSub mat-column-datasetSub ng-star-inserted']/span[@class='ng-star-inserted']/a[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary ng-star-inserted']")
        # api.click()
        # sleep(30)
        # down_button = driver.find_element_by_xpath("//p[@class='product-download-actions']/button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary']")
        # down_button.click()
        # sleep(30)
        # down = driver.find_element_by_xpath("//div[@class='product-download-parameters-selection-data-ready ng-star-inserted']/button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary']")
        # down.click()
