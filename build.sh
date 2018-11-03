#!/usr/bin/env bash

./index.sh
for dir in $(ls | grep -E "[0-9]{4}"); do
  cd $dir
  ./index.sh
done
