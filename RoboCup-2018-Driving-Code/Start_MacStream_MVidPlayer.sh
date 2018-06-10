#!/bin/bash

netcat -l -p 5000 | mplayer -fps 120 -cache 8192 -cache-min 64 -
