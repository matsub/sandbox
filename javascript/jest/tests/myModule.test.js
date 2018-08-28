const mod = require('../src/myModule');


describe('f', () => {
  test('f() returns 2', () => {
    expect(mod.f()).toBe(2);
  });
});


describe('g', () => {
  test('g() returns double of f()', () => {
    const spy = jest
      .spyOn(mod, 'f');
    const value = mod.g();

    expect(spy).toHaveBeenCalled();
    expect(value).toBe(12);

    spy.mockRestore();
  });
});
