target remote localhost:3333
monitor reset init
monitor flash erase_sector 0 0 last
file build/main.elf
load
monitor reset halt
break main
monitor arm semihosting enable
