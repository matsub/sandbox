<template>
  <div></div>
</template>

<script>
// import PIXI from 'pixi.js'
var PIXI = require('pixi.js')

var type = 'WebGL'
if (!PIXI.utils.isWebGLSupported()) {
  type = 'canvas'
}
PIXI.utils.sayHello(type)

var stage = new PIXI.Container()
var renderer = PIXI.autoDetectRenderer(256, 256)
document.body.appendChild(renderer.view)

// Use Pixi's built-in `loader` object to load an image
PIXI.loader
  .add('assets/cool_128.png')
  .load(setup)

// This `setup` function will run when the image has loaded
function setup () {
  // Create the `cat` sprite from the texture
  var cat = new PIXI.Sprite(
    PIXI.loader.resources['assets/cool_128.png'].texture
  )

  // Add the cat to the stage
  stage.addChild(cat)

  // Render the stage   
  renderer.render(stage)
}

export default { }
</script>
