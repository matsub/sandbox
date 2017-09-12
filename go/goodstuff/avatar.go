package main

import (
	"image/png"
	"math/rand"
	"os"
	"time"

	"./avatar"
)

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	color := avatar.Mono()

	base := color.Base()
	primary := color.Primary()
	img := avatar.Mozaic(base, primary)

	f, _ := os.Create("generated.png")
	png.Encode(f, img)
	f.Close()
}
