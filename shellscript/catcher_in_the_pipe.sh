#!/bin/sh
piped=false

function fa {
    echo $piped
    if $piped; then
        IFS=$'\n'
        echo "piped"
    fi
    opts=()
    for l in $(cat -)
    do
        opts+=("$l")
    done

    echo ${opts[1]}
}

if [ -p /dev/stdin ]; then
    piped=true
    cat -
else
    echo $@
fi | fa
