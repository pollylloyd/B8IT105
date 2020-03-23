# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:35:47 2020

@author: Owner
"""

class Commit:
    
    def __init__(self, details, comments=''):
        self.__id = details[0]
        self.__programmer = details[1]
        self.__date_time = details[2]
        self.__date = details[2].split(' ')[0]
        self.__time = details[2].split(' ')[1]
        self.__day = details[2].split(' ')[3].lstrip('(').rstrip(',')
        self.__full_no_comment_lines = details[3] # no of lines is the 3rd index
        self.__no_comment_lines = details[3].rstrip(' ')[0] # strip "line(s)" from no: comments
        self.__comments = comments

        
    def __str__(self):
        return'"{0}", "{1}", "{2}","{3}","{4}","{5}","{6}"  \n'.format(
                self.__id, 
                self.__programmer,
                self.__date, 
                self.__time,
                self.__day,
                self.__no_comment_lines,
                self.__comments)
             