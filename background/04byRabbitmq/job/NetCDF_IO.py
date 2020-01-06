# -*- coding: cp936 -*-
import sys, shutil, os, string, time, datetime
import numpy as np
import netCDF4 as nc
import pandas as pd
import numpy.ma as ma
import xarray as xar

from django.db import models
from mongoengine import *


class MassModel(EmbeddedDocument):
    '''
       �������model
    '''
    # ���͵�����
    oil = FloatField(default=None)
    # ����������
    evaporated = FloatField(default=None)
    # ��ɢ������
    dispersed = FloatField(default=None)


class CurrentModel(EmbeddedDocument):
    '''
        ����
    '''
    x = FloatField()
    y = FloatField()


class WindModel(EmbeddedDocument):
    '''
        ��
    '''
    x = FloatField()
    y = FloatField()


class OilModel(EmbeddedDocument):
    '''
        ����ص�model
    '''
    # �͵��ܶ�
    density = FloatField()
    # ��Ĥ�ĺ��
    film_thickness = FloatField()


class OilSpillingModel(Document):
    '''
        ���ͻ���model
    '''
    code = StringField()
    status = IntField()
    time = DateTimeField()
    point = PointField()
    current = EmbeddedDocumentField(CurrentModel)
    wind = EmbeddedDocumentField(WindModel)
    # ����
    wt = FloatField()
    mass = EmbeddedDocumentField(MassModel)
    # ˮ����
    water_fraction = FloatField()

    oil = EmbeddedDocumentField(OilModel)


def getMassOilLst(ncFileName, nTime, lstVariables, nan):
    try:
        ds = nc.Dataset(ncFileName)
        ds_xr = xar.open_dataset(ncFileName)
        xr_variables = ds_xr.isel(time=nTime)[lstVariables[0]]
        for i in range(len(lstVariables)):
            # mass_oil = ds_xr.isel(time=1)['mass_oil']
            # print(mass_oil.where(mass_oil != 9.969210e+36).to_dataframe().dropna(how='any'))
            if (i > 0):
                xr_var = ds_xr.isel(time=nTime)[lstVariables[i]]
                # print(xr_var)
                xr_variables = xar.merge([xr_variables, xr_var])
        df_variables = xr_variables.where(xr_variables != 9.969210e+36).to_dataframe().dropna(how='any')
        return df_variables
    except Exception as ex:
        print(ex)
        return None
    # finally:
    # return None


def main():
    while (1):
        ncFileName = r'D:\02proj\new_SearchRescueSys\SearchRescueSys\background\01byJupyter\data\sanjioil.nc'
        nTime = 30
        lstVariables = ['mass_oil', 'x_sea_water_velocity', 'y_sea_water_velocity', 'x_wind', 'y_wind']
        # lstVariables = ['x_wind', 'y_wind']
        nan = 9.969210e+36
        df_variables = getMassOilLst(ncFileName, nTime, lstVariables, nan)
        print(df_variables)
        # ds = nc.Dataset(file_path)
        # ds_xr = xar.open_dataset(file_path)
        # print(ds_xr.dims)
        # print(ds_xr)
        # print(ds_xr.coords)

        # ��ȡ����ָ��ά�ȵĵ�DataArray
        # ��ȡһ�� wind
        # mass_oil = ds_xr.isel(time=1)['mass_oil']
        # print(mass_oil.where(mass_oil != 9.969210e+36).to_dataframe().dropna(how='any'))

        # x_wind = ds_xr.isel(time=1)['x_wind']
        # print(x_wind.to_dataframe())
        # print(x_wind.where(x_wind != 9.969210e+36).to_dataframe().dropna(how='any'))
        time.sleep(300)


if __name__ == '__main__':
    main()
