notice("yay")

function notice (id, message) {
  if (message === undefined) {
    message = id
  }
  const p = document.createElement("p")
  p.id = id
  p.innerText = message
  document.body.appendChild(p)
}
