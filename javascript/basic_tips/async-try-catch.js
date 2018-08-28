async function f () {
  throw new Error("yabai");
}

async function g () {
  try {
    await f();
  } catch (err) {
    console.warn(err);
  }
}

async function h () {
  f()
    .then(() => {
      console.log("yoi");
    })
    .catch(err => {
      console.warn(err);
    })
}

h();
