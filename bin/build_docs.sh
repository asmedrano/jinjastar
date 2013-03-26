#!/bin/bash
# This bash script build docs relative to the location of the installation of this module.

SCRIPTPATH=$(cd "$(dirname "$0")"; pwd) # the bin directory


python $SCRIPTPATH/jstar.py -t "$SCRIPTPATH/../docs/templates" -c "$SCRIPTPATH/../docs/content" -o "$SCRIPTPATH/../docs/build"

