class Icon {
  constructor (canvas) {
    this.ctx = canvas.getContext('2d')
  }
}

class Speaker extends Icon {
  draw () {
    this.ctx.clearRect(0, 0, 20, 20)

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


class Echo extends Icon {
  draw (strength) {
    this.ctx.clearRect(0, 0, 20, 20)

    // first echo
    this.ctx.lineWidth = 3
    this.ctx.beginPath();
    if (strength > 0) {
      this.ctx.arc(0, 10, 2, Math.PI*0.5, Math.PI*-0.5, true)
    }
    if (strength > 0.5) {
      this.ctx.moveTo(-20, 20)
      this.ctx.arc(0, 10, 8, Math.PI*0.5, Math.PI*-0.5, true)
    }
    this.ctx.stroke()
  }
}


var speaker = new Speaker(document.getElementById('speaker'))
var echo = new Echo(document.getElementById('echo'))
speaker.draw()
echo.draw(1)
