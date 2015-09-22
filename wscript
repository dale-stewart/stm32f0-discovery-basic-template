def options(opt):
    opt.load('arm-none-eabi-cc', tooldir='.')

def configure(conf):
    conf.load('arm-none-eabi-cc', tooldir='.')

def build(bld):
    bld.recurse('Libraries')

    cflags =  ['-std=c11',
               '-g',
               '-mlittle-endian',
               '-mcpu=cortex-m0',
               '-march=armv6-m',
               '-mthumb',
               '-ffunction-sections',
               '-fdata-sections']

    lflags = ['-Wl,--gc-sections',
              '-Wl,-Map=main.map',
              '-L../Device/ldscripts',
              '-Tstm32f0.ld']

    includes = ['inc',
                'Libraries',
                'Libraries/CMSIS/Device/ST/STM32F0xx/Include',
                'Libraries/CMSIS/Include',
                'Libraries/STM32F0xx_StdPeriph_Driver/inc']

    bld.program(source = bld.path.ant_glob('src/*.c') + bld.path.ant_glob('Device/*.s'),
                includes = includes,
                cflags = cflags,
                linkflags = cflags + lflags,
                target='main.elf',
                use='stm32f0')

from waflib import TaskGen

@TaskGen.extension('.s')
def s_hook(self, node):
    return self.create_compiled_task('c', node)
