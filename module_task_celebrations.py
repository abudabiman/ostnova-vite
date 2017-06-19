# -*- coding: cp1251 -*-

#-------------------------------------------------------------------------------
# Name:        Celebration's Alert
# Purpose:     Celebrations module that will prevent about celebs and holidays from celebrations.txt list
# Author:      Tony Ashman
# Created:     20151221
# Desccription:������� ����� ������� ������ ��������� ����������� ��� ����
#              ����������� �������� � ������ ������.
#              �� 3 ��� ��������� ����������� � ����������� �������, ���� ����������,
#              �� ��������� ����������� �������� ���-�� � ���-�� �������, ����
#              ��� ������� � ������ celebrations.txt
#              � ���� ��������� ��������� � ������� � ������� �������� ��������.
#-------------------------------------------------------------------------------

import os, datetime

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
                    result.append("������� " + line[2] + " �������� " + line[0] + " � ����� ������: " + line[3][:-1])
            except TypeError:
                print('�������� ������ ����� � ����� ��� ����������, ����� ������� �����������')
    return result

def three_days_notice(listing, date):
    result = []
    dt = str(date)[4:]
    delta1 = datetime.timedelta(days=1) # ���-�� ����, �� ������� ������������� � ��� ��������
    delta2 = datetime.timedelta(days=2) # ���-�� ����, �� ������� ������������� � ��� ��������
    delta3 = datetime.timedelta(days=3) # ���-�� ����, �� ������� ������������� � ��� ��������
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
                result.append("������ " + line[2] + " �������� " + line[0] + " � ����� ������: " + line[3][:-1])
            elif dt2.strftime("%m%d") == dt:
                result.append("����������� " + line[2] + " �������� " + line[0] + " � ����� ������: " + line[3][:-1])
            elif dt3.strftime("%m%d") == dt:
                result.append("����� 2 ��� " + line[2] + " �������� " + line[0] + " � ����� ������: " + line[3][:-1])
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
                    result.append('� ���� ������ ��������� ���������: ')
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