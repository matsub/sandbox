import 'pixi.js'

var stage = new PIXI.Container(),
    renderer = PIXI.autoDetectRenderer(
        256, 256,
        {antialias: false, transparent: false, resolution: 1}
    );
document.body.appendChild(renderer.view);
renderer.autoResize = true;
renderer.resize(512, 512);

// Use Pixi's built-in `loader` object to load an image
PIXI.loader
    .add("assets/cool_128.png")
    .on("progress", loadProgressHandler)
    .load(setup);

function loadProgressHandler(loader, resource) {

    //Display the file `url` currently being loaded
    console.log("loading: " + resource.url); 

    //Display the precentage of files currently loaded
    console.log("progress: " + loader.progress + "%"); 
}

// This `setup` function will run when the image has loaded
function setup() {
    // Create the `cat` sprite from the texture
    var icon = new PIXI.Sprite(
        PIXI.loader.resources["assets/cool_128.png"].texture
    );

    icon.anchor.set(0.5, 0.5);
    icon.scale.set(1.0, 1.0);
    icon.position.set(256, 256);
    icon.rotation = 0.5;

    //Add the cat to the stage
    stage.addChild(icon);

    //Render the stage
    renderer.render(stage);
    console.log("setup"); 
}
