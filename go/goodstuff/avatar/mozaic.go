package avatar

import (
	"image"
	"image/color"
	"math/rand"
)

func randBool() bool {
	return rand.Uint32()&1 == 1
}

func pointToRect(dot image.Point, scale int) image.Rectangle {
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

func Mozaic(base, primary color.Color) *image.RGBA {
	img := image.NewRGBA(image.Rect(0, 0, 64, 64))

	fillRect(img, image.Rect(0, 0, 64, 64), base)
	for y := 0; y < 8; y++ {
		for x := 0; x < 8; x++ {
			if randBool() && randBool() {
				rect := pointToRect(image.Pt(x, y), 8)
				fillRect(img, rect, primary)
			}
		}
	}

	return img
}
