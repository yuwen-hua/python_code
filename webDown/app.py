# coding:utf-8
import datetime

from flask import Flask
from sea_manage import create_app
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from apscheduler.triggers.cron import CronTrigger

from sea_manage.passport.views_gfs import DownLoad
from sea_manage.passport.views_copernicus import Copernicus
# from sea_manage.passport.chromedriver import Chrome
from sea_manage.passport.views_weather import Weather
from sea_manage.passport.views_trend import Trend
from sea_manage.passport.views_tide import Tide

# gunicorn 部署
app = create_app('product')  # 生产环境


# app = create_app('dev') # 开发环境

# app = Flask(__name__)

def label1():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_25_ASC_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label1', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label2():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_25_DES_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label2', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label3():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_50_ASC_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label3', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label4():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_50_DES_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label4', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label5():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_25_ASC_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label5', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label6():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_25_DES_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label6', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label7():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_50_ASC_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label7', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label8():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_50_DES_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label8', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label9():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_50_DES_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label9', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label10():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_12_ASC_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label10', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label11():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_12_DES_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label11', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label12():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_25_ASC_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label12', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label13():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_25_DES_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label13', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label14():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_12_ASC_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label14', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label15():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_12_DES_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label15', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label16():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_25_ASC_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label16', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label17():
    label = [{
        "label": "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002",
        "children": [
            {
                "label": "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_25_DES_V2"
            },
        ]
    }]
    Copernicus(label)
    print('label17', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label18():
    label = [{
        "label": "SEALEVEL_GLO_PHY_L4_NRT_OBSERVATIONS_008_046",
        "children": [
            {
                "label": "dataset-duacs-nrt-global-merged-allsat-phy-l4"
            }
        ]
    }]
    Copernicus(label)
    print('label18', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label19():
    label = [{
        "label": "WAVE_GLO_WAV_L4_SWH_NRT_OBSERVATIONS_014_003",
        "children": [
            {
                "label": "dataset-wav-l4-swh-nrt-global"
            }
        ]
    }]
    Copernicus(label)
    print('label19', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label20():
    label = [{
        "label": "MULTIOBS_GLO_PHY_NRT_015_003",
        "children": [
            {
                "label": "dataset-uv-nrt-daily"
            }
        ]
    }]
    Copernicus(label)
    print('label20', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label21():
    label = [{
        "label": "MULTIOBS_GLO_PHY_NRT_015_003",
        "children": [
            {
                "label": "dataset-uv-nrt-hourly"
            },
        ]
    }]
    Copernicus(label)
    print('label21', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label22():
    label = [{
        "label": "GLOBAL_ANALYSIS_FORECAST_PHY_001_024",
        "children": [
            {
                "label": "cmems_mod_glo_phy_anfc_merged-uv_PT1H-i"
            },
        ]
    }]
    Copernicus(label)
    print('label22', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label23():
    label = [{
        "label": "GLOBAL_ANALYSIS_FORECAST_PHY_001_024",
        "children": [
            {
                "label": "global-analysis-forecast-phy-001-024"
            }
        ]
    }]
    Copernicus(label)
    print('label23', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label24():
    label = [{
        "label": "GLOBAL_ANALYSIS_FORECAST_PHY_001_024",
        "children": [
            {
                "label": "global-analysis-forecast-phy-001-024-3dinst-so"
            }
        ]
    }]
    Copernicus(label)
    print('label24', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label25():
    label = [{
        "label": "GLOBAL_ANALYSIS_FORECAST_PHY_001_024",
        "children": [
            {
                "label": "global-analysis-forecast-phy-001-024-3dinst-thetao"
            }
        ]
    }]
    Copernicus(label)
    print('label25', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label26():
    label = [{
        "label": "GLOBAL_ANALYSIS_FORECAST_PHY_001_024",
        "children": [
            {
                "label": "global-analysis-forecast-phy-001-024-3dinst-uovo"
            }
        ]
    }]
    Copernicus(label)
    print('label26', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label27():
    label = [{
        "label": "GLOBAL_ANALYSIS_FORECAST_PHY_001_024",
        "children": [
            {
                "label": "global-analysis-forecast-phy-001-024-hourly-t-u-v-ssh"
            }
        ]
    }]
    Copernicus(label)
    print('label27', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label28():
    label = [{
        "label": "GLOBAL_ANALYSIS_FORECAST_PHY_001_024",
        "children": [
            {
                "label": "global-analysis-forecast-phy-001-024-monthly"
            }
        ]
    }]
    Copernicus(label)
    print('label28', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label29():
    label = [{
        "label": "GLOBAL_ANALYSIS_FORECAST_WAV_001_027",
        "children": [
            {
                "label": "global-analysis-forecast-wav-001-027"
            },
        ]
    }]
    Copernicus(label)
    print('label29', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label30():
    label = [{
        "label": "SST_GLO_SST_L3S_NRT_OBSERVATIONS_010_010",
        "children": [
            {
                "label": "IFREMER-GLOB-SST-L3-NRT-OBS_FULL_TIME_SERIE"
            }
        ]
    }]
    Copernicus(label)
    print('label30', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label31():
    label = [{
        "label": "MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013",
        "children": [
            {
                "label": "dataset-sss-ssd-nrt-monthly"
            }
        ]
    }]
    Copernicus(label)
    print('label31', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label32():
    label = [{
        "label": "MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013",
        "children": [
            {
                "label": "dataset-sss-ssd-nrt-weekly"
            },
        ]
    }]
    Copernicus(label)
    print('label32', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label33():
    label = [{
        "label": "OCEANCOLOUR_GLO_BGC_L3_NRT_009_101",
        "children": [
            {
                "label": "cmems_obs-oc_glo_bgc-plankton_nrt_l3-multi-4km_P1D"
            },
        ]
    }]
    Copernicus(label)
    print('label33', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label34():
    label = [{
        "label": "OCEANCOLOUR_GLO_BGC_L3_NRT_009_101",
        "children": [
            {
                "label": "cmems_obs-oc_glo_bgc-plankton_nrt_l3-olci-300m_P1D"
            },
        ]
    }]
    Copernicus(label)
    print('label34', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label35():
    label = [{
        "label": "OCEANCOLOUR_GLO_BGC_L3_NRT_009_101",
        "children": [
            {
                "label": "cmems_obs-oc_glo_bgc-plankton_nrt_l3-olci-4km_P1D"
            },
        ]
    }]
    Copernicus(label)
    print('label35', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label36():
    label = [{
        "label": "OCEANCOLOUR_GLO_BGC_L3_NRT_009_101",
        "children": [
            {
                "label": "cmems_obs-oc_glo_bgc-reflectance_nrt_l3-multi-4km_P1D"
            },
        ]
    }]
    Copernicus(label)
    print('label36', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label37():
    label = [{
        "label": "OCEANCOLOUR_GLO_BGC_L3_NRT_009_101",
        "children": [
            {
                "label": "cmems_obs-oc_glo_bgc-reflectance_nrt_l3-olci-4km_P1D"
            },
        ]
    }]
    Copernicus(label)
    print('label37', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label38():
    label = [{
        "label": "OCEANCOLOUR_GLO_BGC_L3_NRT_009_101",
        "children": [
            {
                "label": "cmems_obs-oc_glo_bgc-transp_nrt_l3-multi-4km_P1D"
            },
        ]
    }]
    Copernicus(label)
    print('label38', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label39():
    label = [{
        "label": "OCEANCOLOUR_GLO_BGC_L3_NRT_009_101",
        "children": [
            {
                "label": "cmems_obs-oc_glo_bgc-transp_nrt_l3-multi-4km_P1D"
            },
        ]
    }]
    Copernicus(label)
    print('label39', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def label40():
    label = [{
        "label": "OCEANCOLOUR_GLO_BGC_L3_NRT_009_101",
        "children": [
            {
                "label": "cmems_obs-oc_glo_bgc-transp_nrt_l3-olci-4km_P1D"
            },
        ]
    }]
    Copernicus(label)
    print('label40', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def label41():
    label = [{
        "label": "OCEANCOLOUR_GLO_BGC_L3_NRT_009_101",
        "children": [
            {
                "label": "cmems_obs-oc_glo_bgc-optics_nrt_l3-multi-4km_P1D"
            }
        ]
    }]
    Copernicus(label)
    print('label41', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def con():
    Trend()
    Tide()
    print('潮汐潮流:', datetime.datetime.now())


def weather():
    Weather()


if __name__ == '__main__':
    sched = BackgroundScheduler()
    # sched.add_job(down, 'cron', id='3_second_job', day_of_week='*', hour=2,minute=22)
    # sched.add_job(down, 'cron',args=[index+1], id='3_second_job', day_of_week='*', hour=2,minute=22)
    # sched.add_job(con, 'cron',args=['时间'], id='1_second_job', day_of_week='*', hour=1,minute=22)

    trggier1 = CronTrigger(day_of_week='*', hour=1, minute=1)
    sched.add_job(label1, id='label1', trigger=trggier1, misfire_grace_time=500)

    trggier2 = CronTrigger(day_of_week='*', hour=1, minute=11)
    sched.add_job(label2, id='label2', trigger=trggier2, misfire_grace_time=500)

    trggier3 = CronTrigger(day_of_week='*', hour=1, minute=22)
    sched.add_job(label3, id='label3', trigger=trggier3, misfire_grace_time=500)

    trggier4 = CronTrigger(day_of_week='*', hour=1, minute=33)
    sched.add_job(label4, id='label4', trigger=trggier4, misfire_grace_time=500)

    trggier5 = CronTrigger(day_of_week='*', hour=1, minute=44)
    sched.add_job(label5, id='label5', trigger=trggier5, misfire_grace_time=500)

    trggier6 = CronTrigger(day_of_week='*', hour=1, minute=55)
    sched.add_job(label6, id='label6', trigger=trggier6, misfire_grace_time=500)

    trggier7 = CronTrigger(day_of_week='*', hour=2, minute=5)
    sched.add_job(label7, id='label7', trigger=trggier7, misfire_grace_time=500)

    trggier8 = CronTrigger(day_of_week='*', hour=2, minute=15)
    sched.add_job(label8, id='label8', trigger=trggier8, misfire_grace_time=500)

    trggier9 = CronTrigger(day_of_week='*', hour=2, minute=25)
    sched.add_job(label9, id='label9', trigger=trggier9, misfire_grace_time=500)

    trggier10 = CronTrigger(day_of_week='*', hour=2, minute=35)
    sched.add_job(label10, id='label10', trigger=trggier10, misfire_grace_time=500)

    trggier11 = CronTrigger(day_of_week='*', hour=2, minute=45)
    sched.add_job(label11, id='label11', trigger=trggier11, misfire_grace_time=500)

    trggier12 = CronTrigger(day_of_week='*', hour=2, minute=55)
    sched.add_job(label12, id='label12', trigger=trggier12, misfire_grace_time=500)

    trggier13 = CronTrigger(day_of_week='*', hour=3, minute=5)
    sched.add_job(label13, id='label13', trigger=trggier13, misfire_grace_time=500)

    trggier14 = CronTrigger(day_of_week='*', hour=3, minute=15)
    sched.add_job(label14, id='label14', trigger=trggier14, misfire_grace_time=500)

    trggier15 = CronTrigger(day_of_week='*', hour=3, minute=25)
    sched.add_job(label15, id='label15', trigger=trggier15, misfire_grace_time=500)

    trggier16 = CronTrigger(day_of_week='*', hour=3, minute=35)
    sched.add_job(label16, id='label16', trigger=trggier16, misfire_grace_time=500)

    trggier17 = CronTrigger(day_of_week='*', hour=3, minute=45)
    sched.add_job(label17, id='label17', trigger=trggier17, misfire_grace_time=500)

    trggier18 = CronTrigger(day_of_week='*', hour=3, minute=55)
    sched.add_job(label18, id='label18', trigger=trggier18, misfire_grace_time=500)

    trggier19 = CronTrigger(day_of_week='*', hour=4, minute=5)
    sched.add_job(label19, id='label19', trigger=trggier19, misfire_grace_time=500)

    trggier20 = CronTrigger(day_of_week='*', hour=4, minute=15)
    sched.add_job(label20, id='label20', trigger=trggier20, misfire_grace_time=500)

    trggier21 = CronTrigger(day_of_week='*', hour=4, minute=25)
    sched.add_job(label21, id='label21', trigger=trggier21, misfire_grace_time=500)

    trggier22 = CronTrigger(day_of_week='*', hour=4, minute=35)
    sched.add_job(label22, id='label22', trigger=trggier22, misfire_grace_time=1800)

    trggier23 = CronTrigger(day_of_week='*', hour=5, minute=6)
    sched.add_job(label23, id='label23', trigger=trggier23, misfire_grace_time=1800)

    trggier24 = CronTrigger(day_of_week='*', hour=5, minute=37)
    sched.add_job(label24, id='label24', trigger=trggier24, misfire_grace_time=1800)

    trggier25 = CronTrigger(day_of_week='*', hour=6, minute=8)
    sched.add_job(label25, id='label25', trigger=trggier25, misfire_grace_time=1800)

    trggier26 = CronTrigger(day_of_week='*', hour=6, minute=39)
    sched.add_job(label26, id='label26', trigger=trggier26, misfire_grace_time=1800)

    trggier27 = CronTrigger(day_of_week='*', hour=7, minute=10)
    sched.add_job(label27, id='label27', trigger=trggier27, misfire_grace_time=1800)

    trggier28 = CronTrigger(day_of_week='*', hour=7, minute=41)
    sched.add_job(label28, id='label28', trigger=trggier28, misfire_grace_time=1800)

    trggier29 = CronTrigger(day_of_week='*', hour=8, minute=12)
    sched.add_job(label29, id='label29', trigger=trggier29, misfire_grace_time=1800)

    trggier30 = CronTrigger(day_of_week='*', hour=8, minute=43)
    sched.add_job(label30, id='label30', trigger=trggier30, misfire_grace_time=1800)

    trggier31 = CronTrigger(day_of_week='*', hour=9, minute=14)
    sched.add_job(label31, id='label31', trigger=trggier31, misfire_grace_time=1800)

    trggier32 = CronTrigger(day_of_week='*', hour=9, minute=45)
    sched.add_job(label32, id='label32', trigger=trggier32, misfire_grace_time=1800)

    trggier33 = CronTrigger(day_of_week='*', hour=10, minute=16)
    sched.add_job(label33, id='label33', trigger=trggier33, misfire_grace_time=1800)

    trggier34 = CronTrigger(day_of_week='*', hour=10, minute=47)
    sched.add_job(label34, id='label34', trigger=trggier34, misfire_grace_time=1800)

    trggier35 = CronTrigger(day_of_week='*', hour=11, minute=18)
    sched.add_job(label35, id='label35', trigger=trggier35, misfire_grace_time=1800)

    trggier36 = CronTrigger(day_of_week='*', hour=11, minute=49)
    sched.add_job(label36, id='label36', trigger=trggier36, misfire_grace_time=1800)

    trggier37 = CronTrigger(day_of_week='*', hour=12, minute=20)
    sched.add_job(label37, id='label37', trigger=trggier37, misfire_grace_time=1800)

    trggier38 = CronTrigger(day_of_week='*', hour=12, minute=51)
    sched.add_job(label38, id='label38', trigger=trggier38, misfire_grace_time=1800)

    trggier39 = CronTrigger(day_of_week='*', hour=13, minute=22)
    sched.add_job(label39, id='label39', trigger=trggier39, misfire_grace_time=1800)

    trggier40 = CronTrigger(day_of_week='*', hour=13, minute=53)
    sched.add_job(label40, id='label40', trigger=trggier40, misfire_grace_time=1800)

    trggier41 = CronTrigger(day_of_week='*', hour=14, minute=24)
    sched.add_job(label41, id='label41', trigger=trggier41, misfire_grace_time=1800)

    weather1 = CronTrigger(day_of_week='*', hour=8, minute=20)
    sched.add_job(weather, id='weather1_second_job', trigger=weather1, misfire_grace_time=60)
    con1 = CronTrigger(day_of_week='*', hour=8, minute=23)
    sched.add_job(con, id='con1_second_job', trigger=con1, misfire_grace_time=600)
    sched.start()

    # app.run(host='0.0.0.0', debug=True, port=5889,use_reloader=True)
    # user_reloader 需要在服务器上运行时关闭， 否则会开启两个进程
    app.run(host='0.0.0.0', debug=False, port=5889, use_reloader=False)
