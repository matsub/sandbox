package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestAdd(t *testing.T) {
	assert.Equal(t, 12, Add(8, 4), "8 + 4 = 12")
	assert.NotEqual(t, 32, Add(15, 16), "15 + 16 not 32")
}

func TestSubtract(t *testing.T) {
	assert.Equal(t, 4, Subtract(8, 4), "8 - 4 = 4")
}

func TestMultiple(t *testing.T) {
	assert.Equal(t, 32, Multiple(8, 4), "8 x 4 = 32")
}

func TestDivide(t *testing.T) {
	assert.Equal(t, 2, Divide(8, 4), "8 / 4 = 2")
	assert.Equal(t, 2, Divide(7, 3), "7 / 3 = 2")
}
