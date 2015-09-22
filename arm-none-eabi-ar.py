#! /usr/bin/env python
# encoding: utf-8

from waflib.Configure import conf
@conf
def configure(conf):
    conf.find_program('arm-none-eabi-ar', var='AR')
    conf.env.ARFLAGS='-r'
