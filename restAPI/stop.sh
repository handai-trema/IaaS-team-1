#!/bin/sh

sudo rm -r /home/ensyuu2/docker/*
docker stop $(docker ps -q)
docker rm $(docker ps -aq)
