function f() {
  return 2;
}

function g() {
  return f() * 2;
}

module.exports = {
  f,
  g,
};
