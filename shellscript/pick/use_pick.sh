#!/bin/sh
source pick.sh

menu=(
"First Option"
"Second Option"
"Third Option"
)

case `pick $menu` in
    0|1)
        echo "the first or the second!"
        ;;
    1)
        echo "the second!"
        ;;
    2)
        echo "the third!"
        ;;
esac
