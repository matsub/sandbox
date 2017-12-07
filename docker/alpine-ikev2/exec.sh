#!/bin/sh
docker run -itd --privileged \
    -v /lib/modules:/lib/modules:ro \
    -v ./cert:/data/key_files \
    -e HOSTIP="192.168.99.100" \
    -e VPNUSER="jack" -e VPNPASS="jack&opsAdmin" \
    -e CERT_C="JP" -e CERT_O="sandbox" -e CERT_CN="sandbox/alpine-ikev2-vpn" \
    -p 500:500/udp -p 4500:4500/udp \
    matsub/alpine-ikev2-vpn
