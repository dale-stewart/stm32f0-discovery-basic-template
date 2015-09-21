#!/usr/bin/env python
# encoding: utf-8

"""
Detect the ARM-none-EABI C++ compiler
"""

import os, sys
from waflib.Tools import ccroot, ar, gxx
from waflib.Configure import conf

@conf
def find_arm_none_eabi_gxx(conf):
    cc = conf.find_program(['arm-none-eabi-g++'])
    conf.get_cc_version(cc, gcc=True)
    conf.env.CXX_NAME = 'arm-none-eabi-g++'
    conf.env.CXX = cc

def configure(conf):
    conf.find_arm_none_eabi_gxx()
    conf.load('arm-none-eabi-ar', tooldir=os.path.dirname(os.path.realpath(__file__)))
    conf.gcc_common_flags()
    conf.gcc_modifier_platform()
    conf.cxx_load_tools()
    conf.cxx_add_flags()
    conf.link_add_flags()
