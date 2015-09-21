def options(opt):
    opt.recurse('Libraries')
    opt.load('arm-none-eabi-cc', tooldir='.')

def configure(conf):
    conf.recurse('Libraries')
    conf.load('arm-none-eabi-cc', tooldir='.')

    flags =  ['-std=c11',
              '-g',
              '-ffreestanding',
              '-nostdlib',
              '-Werror',
              '-Wall',
              '-mlittle-endian',
              '-mcpu=cortex-m0',
              '-march=armv6-m',
              '-mthumb',
              '-ffunction-sections',
              '-fdata-sections',
              '-includestm32f0xx_conf.h']

    conf.env.append_value('CFLAGS', flags)

def build(bld):
    bld.recurse('Libraries')
    bld.program(source=bld.path.ant_glob('src/*.c'),
                includes=['Libraries',
                          'Libraries/CMSIS/Include',
                          'Libraries/CMSIS/Device/ST/STM32F0xx/Include',
                          'Libraries/STM32F0xx_StdPeriph_Driver/inc'],
                linkflags=['-Wl,--gc-sections',
                           '-Wl,-Map=main.map',
                           '-specs=rdimon.specs',
                           '-LDevice/ldscripts'
                           '-Tstm32f0.ld'],
                lib='gcc c m rdimon',
                target='main.elf',
                use='stm32f0')
