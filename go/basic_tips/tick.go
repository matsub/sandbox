package main

import (
	"fmt"
	"time"
)

func main() {
	expiredAtStr := time.Date(2018, 6, 4, 17, 30, 0, 0, time.Local).Unix()
	fmt.Println(expiredAtStr)

	expiredAt := time.Unix(expiredAtStr, 0)
	remain := expiredAt.Sub(time.Now())
	fmt.Println(remain > 0)

	fmt.Println(time.Now().Add(time.Hour * 24))
}
