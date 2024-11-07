function double(arr) {
  return arr.map(function(val) {
    return val * 2;
  });
}

Refactor the above code to use two arrow functions. Turn it into a one-liner.

Solulion:
const double = arr => arr.map(val => val *2);


**Refactor the following function to use arrow functions:**
Replace ALL functions with arrow functions:

function squareAndFindEvens(numbers){
  var squares = numbers.map(function(num){
    return num ** 2;
  });
  var evens = squares.filter(function(square){
    return square % 2 === 0;
  });
  return evens;
}

Solution:
const squareAndFindEvens = numbers => {
  var squares = numbers.map(num => num **2);
  var evens = squares.filter(square => square % 2 === 0);
  return evens;
};

Or even shorter!

const squareAndFindEvens = numbers => numbers.map(num => num ** 2).filter(val => val % 2 === 0);
