# -*- coding: cp1251 -*-

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     24.12.2015
# Copyright:   (c) Admin 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import datetime

def russian_name_day(day):
	if day==1: return '�����������'
	elif day==2: return '�������'
	elif day==3: return '�����'
	elif day==4: return '�������'
	elif day==5: return '�������'
	elif day==6: return '�������'
	elif day==7: return '�����������'

def russian_name_month(month):
	if month==1: return '������'
	elif month==2: return '�������'
	elif month==3: return '����'
	elif month==4: return '������'
	elif month==5: return '���'
	elif month==6: return '����'
	elif month==7: return '����'
	elif month==8: return '������'
	elif month==9: return '��������'
	elif month==10: return '�������'
	elif month==11: return '������'
	elif month==12: return '�������'

def russian_number_month(month):
	if month=='������': return '01'
	elif month=='�������': return '02'
	elif month=='����': return '03'
	elif month=='������': return '04'
	elif month=='���': return '05'
	elif month=='����': return '06'
	elif month=='����': return '07'
	elif month=='������': return '08'
	elif month=='��������': return '09'
	elif month=='�������': return '10'
	elif month=='������': return '11'
	elif month=='�������': return '12'


def convert_to_russian_datename(date):
    temp = datetime.datetime.strptime(str(date), "%Y%m%d")
    day = temp.isoweekday()
    month = temp.month
    dayname = russian_name_day(day)
    monthname = russian_name_month(month)
    resultstroke = dayname + ' - ' + str(date)[:4] + ' ' + monthname + ' ' + str(date)[6:]
    return resultstroke
