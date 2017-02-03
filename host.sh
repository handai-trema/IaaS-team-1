#!/bin/bash

CMDNAME=`basename $0`
if [ $# -ne 2 ]; then
  echo "Usage: $CMDNAME [interface] [port number]" 1>&2
  exit 1
fi

sudo service network-manager stop

if [ "$2" -lt 10 ] ; then
	sudo ifconfig $1 192.168.1.10$2 netmask 255.255.255.0
elif [ "$2" -lt 49 ] ; then
	sudo ifconfig $1 192.168.1.1$2 netmask 255.255.255.0
else
	echo "port number must be less than 49"
	exit 1
fi	
	
sudo route add -net 192.168.1.0 gw 192.168.1.254 metric 0 netmask 255.255.255.0 $1
