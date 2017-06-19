# -*- coding: cp1251 -*-

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Iam
#
# Created:     16.05.2014
# Copyright:   (c) Iam 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from cx_Freeze import setup, Executable

executables = [
    Executable("life.py",
               appendScriptToExe=True,
               appendScriptToLibrary=False,
               )
]

buildOptions = dict(create_shared_zip=False)

setup(name="TEST",
      version="1.1",
      description="ежедневник",
      options=dict(build_exe=buildOptions),
      executables=executables,
      )