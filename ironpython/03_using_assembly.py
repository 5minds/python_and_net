#!ipy
# -*- coding: utf-8 -*-

from os import path

import clr

base_path = path.abspath(path.dirname(__file__))
assembly_name = path.join(base_path, '03_using_assembly', 'PythonAndNet.Sample','bin', 'Debug', 'PythonAndNet.Sample.dll')

clr.AddReferenceToFileAndPath(assembly_name)

from PythonAndNet.Sample import SampleDotnetType

a_sample_dotnet_type = SampleDotnetType()

a_sample_dotnet_type.PrintHello()
