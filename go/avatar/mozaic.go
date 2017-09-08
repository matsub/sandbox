package main

import (
	"image"
	"image/color"
	"image/png"
	"math/rand"
	"os"
	"time"
)

func RandColor(rnd *rand.Rand) color.Color {
	// fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck
	r := uint8(rnd.Uint32() & 0xff)
	g := uint8(rnd.Uint32() & 0xff)
	b := uint8(rnd.Uint32() & 0xff)

	return color.RGBA{r, g, b, 255}
}

func RandGray(rnd *rand.Rand) color.Color {
	scale := uint8(rnd.Uint32() & 0xff)
	return color.Gray{scale}
}

func PixRect(dot image.Point, scale int) image.Rectangle {
	min := dot.Mul(scale)
	max := dot.Add(image.Pt(1, 1)).Mul(scale)
	return image.Rectangle{min, max}
}

func fillRect(img *image.RGBA, rect image.Rectangle, col color.Color) {
	for h := rect.Min.Y; h < rect.Max.Y; h++ {
		for v := rect.Min.X; v < rect.Max.X; v++ {
			img.Set(v, h, col)
		}
	}
}

func Avatar(rnd *rand.Rand) *image.RGBA {
	base := RandColor(rnd)
	img := image.NewRGBA(image.Rect(0, 0, 64, 64))

	fillRect(img, image.Rect(0, 0, 64, 64), RandGray(rnd))
	for y := 0; y < 8; y++ {
		for x := 0; x < 8; x++ {
			if flg := rnd.Uint32() & 1; flg != 0 {
				fillRect(img, PixRect(image.Pt(x, y), 8), base)
			}
		}
	}

	return img
}

func main() {
	src := rand.NewSource(time.Now().UTC().UnixNano())
	rnd := rand.New(src)
	img := Avatar(rnd)

	f, _ := os.Create("generated.png")
	png.Encode(f, img)
	f.Close()
}
