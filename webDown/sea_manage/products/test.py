import xml.etree.ElementTree as ET


arr = [1,2,3,4]
for i in arr[1:]:
    print(i)


#   global-analysis-forecast-phy-001-024
# path = ['D:/xml/PHY.xml','D:/xml/WAV.xml']
# for url in path:
#     tree = ET.parse(url)
#     root = tree.getroot()
#     print(root.tag,root.attrib)
#     variables = []
#     for i in root:
#         # print(i.get('standardName'),i.attrib)
#         if i.tag == 'timeCoverage':
#             start = i.attrib['start']
#             end = i.attrib['end']
#         if i.tag == 'availableDepths':
#             depth = i.text.split(';')
#         if i.tag == 'variables':
#             for j in i:
#                 variables.append(j.attrib)
#     obj = {
#         "depth": depth,
#         "list": variables,
#         "start": start,
#         "end": end
#     }
#     print(obj)


# data = [
#         {
#             "GLOBAL_ANALYSIS_FORECAST_PHY_001_024": [
#                 "cmems_mod_glo_phy_anfc_merged-uv_PT1H-i",
#                 "global-analysis-forecast-phy-001-024",
#                 "global-analysis-forecast-phy-001-024-3dinst-so",
#                 "global-analysis-forecast-phy-001-024-3dinst-thetao",
#                 "global-analysis-forecast-phy-001-024-3dinst-uovo",
#                 "global-analysis-forecast-phy-001-024-hourly-t-u-v-ssh",
#                 "global-analysis-forecast-phy-001-024-monthly",
#                 "global-analysis-forecast-phy-001-024-statics"
#             ]
#         },
#         {
#             "GLOBAL_ANALYSIS_FORECAST_WAV_001_027": [
#                 "global-analysis-forecast-wav-001-027",
#                 "global-analysis-forecast-wav-001-027-statics"
#             ]
#         },
#         {
#             "WIND_GLO_WIND_L3_NRT_OBSERVATIONS_012_002": [
#                 "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_25_ASC_V2",
#                 "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_25_DES_V2",
#                 "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_50_ASC_V2",
#                 "KNMI-GLO-WIND_L3-OBS_HY-2C_HSCAT_50_DES_V2",
#                 "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_25_ASC_V2",
#                 "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_25_DES_V2",
#                 "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_50_ASC_V2",
#                 "KNMI-GLO-WIND_L3-OBS_HY-2B_HSCAT_50_DES_V2",
#                 "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_12_ASC_V2",
#                 "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_12_DES_V2",
#                 "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_25_ASC_V2",
#                 "KNMI-GLO-WIND_L3-OBS_METOP-A_ASCAT_25_DES_V2",
#                 "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_12_ASC_V2",
#                 "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_12_DES_V2",
#                 "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_25_ASC_V2",
#                 "KNMI-GLO-WIND_L3-OBS_METOP-B_ASCAT_25_DES_V2",
#                 "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_12_ASC_V2",
#                 "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_12_DES_V2",
#                 "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_25_ASC_V2",
#                 "KNMI-GLO-WIND_L3-OBS_METOP-C_ASCAT_25_DES_V2",
#                 "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_25_ASC_V2",
#                 "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_25_DES_V2",
#                 "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_50_ASC_V2",
#                 "KNMI-GLO-WIND_L3-OBS_SCATSAT-1_OSCAT_50_DES_V2"
#             ]
#         },
#         {
#             "SEALEVEL_GLO_PHY_L4_NRT_OBSERVATIONS_008_046": [
#                 "dataset-duacs-nrt-global-merged-allsat-phy-l4"
#             ]
#         },
#         {
#             "WAVE_GLO_WAV_L4_SWH_NRT_OBSERVATIONS_014_003": [
#                 "dataset-wav-l4-swh-nrt-global"
#             ]
#         },
#         {
#             "MULTIOBS_GLO_PHY_NRT_015_003": [
#                 "dataset-uv-nrt-daily",
#                 "dataset-uv-nrt-hourly",
#                 "dataset-uv-nrt-monthly"
#             ]
#         },
#         {
#             "OCEANCOLOUR_GLO_BGC_L3_NRT_009_101": [
#                 "cmems_obs-oc_glo_bgc-plankton_nrt_l3-multi-4km_P1D",
#                 "cmems_obs-oc_glo_bgc-plankton_nrt_l3-olci-300m_P1D",
#                 "cmems_obs-oc_glo_bgc-plankton_nrt_l3-olci-4km_P1D",
#                 "cmems_obs-oc_glo_bgc-reflectance_nrt_l3-multi-4km_P1D",
#                 "cmems_obs-oc_glo_bgc-reflectance_nrt_l3-olci-4km_P1D",
#                 "cmems_obs-oc_glo_bgc-transp_nrt_l3-multi-4km_P1D",
#                 "cmems_obs-oc_glo_bgc-transp_nrt_l3-olci-4km_P1D",
#                 "cmems_obs-oc_glo_bgc-optics_nrt_l3-multi-4km_P1D"
#             ]
#         },
#         {
#             "SST_GLO_SST_L3S_NRT_OBSERVATIONS_010_010": [
#                 "IFREMER-GLOB-SST-L3-NRT-OBS_FULL_TIME_SERIE"
#             ]
#         },
#         {
#             "MULTIOBS_GLO_PHY_S_SURFACE_MYNRT_015_013": [
#                 "dataset-sss-ssd-nrt-monthly",
#                 "dataset-sss-ssd-nrt-weekly",
#                 "dataset-sss-ssd-rep-monthly",
#                 "dataset-sss-ssd-rep-weekly"
#             ]
#         }
#     ]
# url = 'https://resources.marine.copernicus.eu/product-detail/'
# # for i in data:
#     # print('product')
#     # for product in i:
#     #     path = url + product + '/DATA-ACCESS'
#     #     for s in range(len(i[product])):
#     #         print(path, s+1)
#     #         api_xpath = "//tbody/tr[@class='mat-row cdk-row ng-star-inserted'][" + str(s + 1) + "]/td[@class='mat-cell cdk-cell width-cell-dataset cdk-column-datasetSub mat-column-datasetSub ng-star-inserted']/span[@class='ng-star-inserted']/a[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary ng-star-inserted']"
#
#
# arr = ["-180, -90, -90, 0","-90, -90, 0, 0","0, -90, 90, 0","90, -90, 1800, 0"]
# for i in arr:
#     print(i)