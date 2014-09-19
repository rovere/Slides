#!/usr/bin/env python

import os, datetime, time, hashlib, signal, sys

CODE={
    'ENDC':0,  # RESET COLOR
    'BOLD':1,
    'UNDERLINE':4,
    'BLINK':5,
    'INVERT':7,
    'CONCEALD':8,
    'STRIKE':9,
    'GREY30':90,
    'GREY40':2,
    'GREY65':37,
    'GREY70':97,
    'GREY20_BG':40,
    'GREY33_BG':100,
    'GREY80_BG':47,
    'GREY93_BG':107,
    'DARK_RED':31,
    'RED':91,
    'RED_BG':41,
    'LIGHT_RED_BG':101,
    'DARK_YELLOW':33,
    'YELLOW':93,
    'YELLOW_BG':43,
    'LIGHT_YELLOW_BG':103,
    'DARK_BLUE':34,
    'BLUE':94,
    'BLUE_BG':44,
    'LIGHT_BLUE_BG':104,
    'DARK_MAGENTA':35,
    'PURPLE':95,
    'MAGENTA_BG':45,
    'LIGHT_PURPLE_BG':105,
    'DARK_CYAN':36,
    'AUQA':96,
    'CYAN_BG':46,
    'LIGHT_AUQA_BG':106,
    'DARK_GREEN':32,
    'GREEN':92,
    'GREEN_BG':42,
    'LIGHT_GREEN_BG':102,
    'BLACK':30,
}

def termcode(num):
    return '\033[%sm'%num

def colorstr(astr,color):
    return termcode(CODE[color])+astr+termcode(CODE['ENDC'])

def gracefulExit(signal, frame):
    print colorstr('Quitting', "RED")
    sys.exit(0)

def instrumentGracefulExit():
    signal.signal(signal.SIGINT, gracefulExit)

if __name__=='__main__':
    instrumentGracefulExit()
    file_to_monitor = 'index.Rmd'
    print ">>> Start monitoring %s file. Press Ctrl-C to Stop." % file_to_monitor
    before = os.stat("index.Rmd").st_mtime
    before_hash = hashlib.md5(open(file_to_monitor, 'rb').read()).digest()
    while 1:
      time.sleep (1)
      after = os.stat("index.Rmd").st_mtime
      if after > before:
          after_t = datetime.datetime.fromtimestamp(after) 
          print ">>> Change detected at %d:%d:%d" % (after_t.hour, 
                                                     after_t.minute, 
                                                     after_t.second)
          after_hash = hashlib.md5(open(file_to_monitor, 'rb').read()).digest()
          if before_hash == after_hash:
              print colorstr('indentical', 'DARK_GREEN')
          else:
              before_hash = after_hash
              print colorstr('Updating', 'DARK_YELLOW')
              os.system("./generate.r &> /dev/null")
          before = after
