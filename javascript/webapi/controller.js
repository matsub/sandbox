class Icon {
  constructor (canvas) {
    this.ctx = canvas.getContext('2d')
    this.width = canvas.width
    this.height = canvas.height
  }

  draw() {
    this.ctx.clearRect(0, 0, this.width, this.height)
  }
}

class Sound extends Icon {
  draw () {
    super.draw()

    // rect box
    this.ctx.fillRect(0, 5, 5, 10)

    // muff
    this.ctx.beginPath();
    this.ctx.moveTo(0, 10);
    this.ctx.lineTo(10, 0);
    this.ctx.lineTo(10, 20);
    this.ctx.fill();
  }
}


class Speaker extends Sound {
  draw (strength) {
    super.draw()

    this.ctx.lineWidth = 3
    this.ctx.beginPath();
    // first echo
    if (strength > 0) {
      this.ctx.arc(12.5, 10, 2, Math.PI*0.5, Math.PI*-0.5, true)
    }
    // second echo
    if (strength > 0.5) {
      this.ctx.moveTo(12.5, 18)
      this.ctx.arc(12.5, 10, 8, Math.PI*0.5, Math.PI*-0.5, true)
    }
    this.ctx.stroke()
  }
}
