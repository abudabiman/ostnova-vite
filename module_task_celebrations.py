# -*- coding: cp1251 -*-

#-------------------------------------------------------------------------------
# Name:        Celebration's Alert
# Purpose:     Celebrations module that will prevent about celebs and holidays from celebrations.txt list
# Author:      Tony Ashman
# Created:     20151221
# Desccription:Первого числа каждого месяца выводятся уведомления обо всех
#              предстоящих событиях в данном месяце.
#              За 3 дня выводится уведомление о предстоящим событии, если необходимо,
#              то возникает предложение посетить что-то и что-то сделать, если
#              это указано в списке celebrations.txt
#              В день праздника уведомить о событии и вызвать связаное действие.
#-------------------------------------------------------------------------------

import os, datetime

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

def today_notice(listing, date):
    result = []
    for line in listing:
        if line[0][:1] != '\t':
            templine = line[1].split(' ')
            if len(templine[0]) == 1:
                day = '0' + templine[0]
            else:
                day = templine[0]
            month = russian_number_month(templine[1])
            try:
                if (month+day) == str(date)[4:]:
                    result.append("Сегодня " + line[2] + " праздник " + line[0] + " и нужно делать: " + line[3][:-1])
            except TypeError:
                print('Проблема скорее всего в файле дат праздников, месяц написан неправильно')
    return result

def three_days_notice(listing, date):
    result = []
    dt = str(date)[4:]
    delta1 = datetime.timedelta(days=1) # кол-во дней, за которое предупреждать о дне рождении
    delta2 = datetime.timedelta(days=2) # кол-во дней, за которое предупреждать о дне рождении
    delta3 = datetime.timedelta(days=3) # кол-во дней, за которое предупреждать о дне рождении
    for line in listing:
        if line[0][:1] != '\t':
            templine = line[1].split(' ')
            if len(templine[0]) == 1:
                day = '0' + templine[0]
            else:
                day = templine[0]
            month = russian_number_month(templine[1])
            dt1 = datetime.datetime.strptime(month+day, "%m%d") - delta1
            dt2 = datetime.datetime.strptime(month+day, "%m%d") - delta2
            dt3 = datetime.datetime.strptime(month+day, "%m%d") - delta3
            if dt1.strftime("%m%d") == dt:
                result.append("Завтра " + line[2] + " праздник " + line[0] + " и нужно делать: " + line[3][:-1])
            elif dt2.strftime("%m%d") == dt:
                result.append("Послезавтра " + line[2] + " праздник " + line[0] + " и нужно делать: " + line[3][:-1])
            elif dt3.strftime("%m%d") == dt:
                result.append("Через 2 дня " + line[2] + " праздник " + line[0] + " и нужно делать: " + line[3][:-1])
    return result

def monthly_notice(listing, date):
    result = []
    for line in listing:
        if line[0][:1] != '\t':
            templine = line[1].split(' ')
            if len(templine[0]) == 1:
                day = '0' + templine[0]
            else:
                day = templine[0]
            month = russian_number_month(templine[1])
            if month == str(date)[4:6]:
                if len(result) == 0:
                    result.append('В этом месяце следующие праздники: ')
                    result[0] += (line[0] + ' (' + day + '); ')
                else:
                    result[0] += (line[0] + ' (' + day + '); ')
    if str(date)[6:] == '01':
        return result
    else:
        result = []
        return result

def starter(date):
    list_of_result = []
    result = []
    fp = os.getcwd() + '\\Personal\\celebrations.txt'
    f = open(fp,'r')
    for line in f:
        linelist = line.split(' - ')
        list_of_result.append(linelist)
    f.close()
    result += today_notice(list_of_result, date)
    result += three_days_notice(list_of_result, date)
    result += monthly_notice(list_of_result, date)
    return result