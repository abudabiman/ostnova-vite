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
	if day==1: return 'ПОНЕДЕЛЬНИК'
	elif day==2: return 'ВТОРНИК'
	elif day==3: return 'СРЕДА'
	elif day==4: return 'ЧЕТВЕРГ'
	elif day==5: return 'ПЯТНИЦА'
	elif day==6: return 'СУББОТА'
	elif day==7: return 'ВОСКРЕСЕНЬЕ'

def russian_name_month(month):
	if month==1: return 'январь'
	elif month==2: return 'февраль'
	elif month==3: return 'март'
	elif month==4: return 'апрель'
	elif month==5: return 'май'
	elif month==6: return 'июнь'
	elif month==7: return 'июль'
	elif month==8: return 'август'
	elif month==9: return 'сентябрь'
	elif month==10: return 'октябрь'
	elif month==11: return 'ноябрь'
	elif month==12: return 'декабрь'

def russian_number_month(month):
	if month=='январь': return '01'
	elif month=='февраль': return '02'
	elif month=='март': return '03'
	elif month=='апрель': return '04'
	elif month=='май': return '05'
	elif month=='июнь': return '06'
	elif month=='июль': return '07'
	elif month=='август': return '08'
	elif month=='сентябрь': return '09'
	elif month=='октябрь': return '10'
	elif month=='ноябрь': return '11'
	elif month=='декабрь': return '12'


def convert_to_russian_datename(date):
    temp = datetime.datetime.strptime(str(date), "%Y%m%d")
    day = temp.isoweekday()
    month = temp.month
    dayname = russian_name_day(day)
    monthname = russian_name_month(month)
    resultstroke = dayname + ' - ' + str(date)[:4] + ' ' + monthname + ' ' + str(date)[6:]
    return resultstroke
