const sum = require('../src/sum');


describe('sugoi yo', () => {
  let sumSpy;

  test('adds 1 + 2 to equal 3', () => {
    expect(sum.sum(1, 2)).toBe(3);
  });

  test('sugoi 2, 3 to equal 10', () => {
    sumSpy = jest
      .spyOn(sum, 'sum')
      .mockReturnValue(6)

    expect(sum.sugoi(2, 3)).toBe(12);
  });
});
