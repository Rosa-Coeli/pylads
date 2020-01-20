#!/bin/bash

for i in *.xml; do mv $i ${i%xml}cps ; done
