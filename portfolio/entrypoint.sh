#!/bin/sh

cd $1

cp -r ./data /cv/_data
cp -r ./img /cv/assets/img
cp -r ./posts /cv/_posts

cd /cv
/usr/gem/bin/jekyll build