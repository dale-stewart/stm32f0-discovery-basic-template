#!/usr/bin/env python
# encoding: utf-8

"""
Detect the ARM-none-EABI C compiler
"""

import os, sys
from waflib.Tools import ccroot, ar, gcc
from waflib.Configure import conf

@conf
def find_arm_none_eabi_gcc(conf):
    cc = conf.find_program(['arm-none-eabi-gcc'])
    conf.get_cc_version(cc, gcc=True)
    conf.env.CC_NAME = 'arm-none-eabi-gcc'
    conf.env.CC = cc

def configure(conf):
    conf.find_arm_none_eabi_gcc()
    conf.load('arm-none-eabi-ar', tooldir=os.path.dirname(os.path.realpath(__file__)))
    conf.gcc_common_flags()
    conf.gcc_modifier_platform()
    conf.cc_load_tools()
    conf.cc_add_flags()
    conf.link_add_flags()
