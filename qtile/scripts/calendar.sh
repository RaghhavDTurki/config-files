#! /usr/bin/bash

emacsclient -c -a 'emacs' --eval '(doom/window-maximize-buffer(dt/year-calendar))'
