#!/bin/bash

command -v getarg >/dev/null || . /lib/dracut-lib.sh
. /lib/url-lib.sh
. /lib/anaconda-lib.sh

info "STACKIQ: initiating ludicrous speed"

# [ ! -h /opt ] && ln -s /updates/opt /opt

#
# initqueue/online hook passes interface name as $1
#
netif="$1"

server=""
if [ -f /tmp/net.$netif.dhcpopts ]
then
	. /tmp/net.$netif.dhcpopts
	server="${new_next_server:-$new_dhcp_server_identifier}"
fi

#
# starting ludicrous speed
#

# If we're a frontend, then mount cdrom before starting ludicrous speed
if getargbool 0 frontend; then
	mkdir -p /mnt/cdrom
	mount /dev/cdrom /mnt/cdrom
fi

LUDICROUSPID=`ps auwx | grep hunter2 | grep -v grep | /opt/stack/bin/awk '{print $2}'`
while [ "$LUDICROUSPID" != "" ]; do
	
	for pid in $LUDICROUSPID; do kill $pid; done
	LUDICROUSPID=`ps auwx | grep hunter2 | grep -v grep | /opt/stack/bin/awk '{print $2}'`
done

/opt/stack/bin/python /opt/stack/bin/ludicrous-client.py --environment=initrd



