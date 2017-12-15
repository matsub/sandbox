#!/bin/sh
function fa {
	IFS=$(printf "\n")
	for obj in $(cat -)
	do
		echo $obj
	done
}

if [ -p /dev/stdin ]; then
    cat -
else
    echo $@
fi | fa
