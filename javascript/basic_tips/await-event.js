var btn = document.querySelector("button")

function wrapEventWithAsyncFunction () {
  return new Promise(resolve => {
    btn.onclick = () => resolve("whoaaaaaa!!!!")
  })
}

async function awaitEvent () {
  let msg = await wrapEventWithAsyncFunction()
  console.log("--- emitted ---")
  console.log(msg)
}

awaitEvent()
// when push the button:
//   -> --- emitted ---
//   -> whoaaaaaa!!!!
