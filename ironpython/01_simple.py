#!ipy
# -*- coding: utf-8 -*-

from System import String
from System.Collections.Generic import Dictionary
from System import Console

a_string = String("hello world")
print a_string

a_dict = Dictionary[String, String]()
a_dict['key1'] = "value1"
a_dict['key2'] = "value2"
print a_dict

Console.WriteLine('Hello IronPython.')

Console.Write("Eingabe: drücken zum Beenden:")
Console.ReadKey()
