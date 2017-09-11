package main

import (
	"image/color"
	"math/rand"
)

func random(min, max int32) int32 {
	return rand.Int31n(max-min) + min
}

/**
* HSL for cylindrical-coordinate representation
* @field	h	int32	The hue [0 - 359]
* @field	s	float32	The saturation [0.0 - 1.0]
* @field	l	float32	The luminance [0.0 - 1.0]
* @method	RGBA()	(r, g, b, a uint32) interface for color.Color
 */
type HSL struct {
	h    int32
	s, l float32
}

func (col HSL) RGBA() (r, g, b, a uint32) {
	c := (1 - abs(2*col.l-1)) * col.s
	h := float32(col.h) / 60
	x := c * (1 - abs(mod(h, 2)-1))

	r1, g1, b1 := resolveHue(h, c, x)

	m := col.l - c/2
	r = uint32((r1 + m) * 0xffff)
	g = uint32((g1 + m) * 0xffff)
	b = uint32((b1 + m) * 0xffff)
	a = 0xffff
	return
}

func resolveHue(h, c, x float32) (r1, g1, b1 float32) {
	switch {
	case h < 1:
		r1, g1, b1 = c, x, 0
	case h < 2:
		r1, g1, b1 = x, c, 0
	case h < 3:
		r1, g1, b1 = 0, c, x
	case h < 4:
		r1, g1, b1 = 0, x, c
	case h < 5:
		r1, g1, b1 = x, 0, c
	case h < 6:
		r1, g1, b1 = c, 0, x
	default:
		r1, g1, b1 = 0, 0, 0
	}
	return
}

func mod(x float32, b int) float32 {
	n := int(x)
	return x - float32((n/b)*b)
}

func abs(x float32) float32 {
	if x > 0 {
		return x
	} else {
		return -x
	}
}

type MonoColor struct {
	isDark bool
}

func (col MonoColor) base() color.Color {
	var scale uint8
	if col.isDark {
		scale = 0xff
	} else {
		scale = 0x00
	}
	return color.Gray{scale}
}

func (col MonoColor) primary() color.Color {
	var scale uint16
	if col.isDark {
		scale = 0x3fff
	} else {
		scale = 0xc000
	}

	h := random(0, 360)
	s := float32(random(50, 100)) / 100
	l := float32(scale) / 0xffff

	return HSL{h, s, l}
}
