// Declaration syntax for functions, can be hoisted.
show()

function show () {
  console.log('bla bla bla')
}

function square (number) {
  return number * number
}

let answer = square(3)

document.querySelector('#result').textContent = answer

// Expression syntax for function, cannot be hoisted.

let add = function (num1, num2) {
  return num1 + num2
}

document.querySelector('#result').textContent = add(2, 3)

// Arrow -- efficient syntax, but no hoisting.

let sum = (no1, no2) => no1 + no2

document.querySelector('#result').textContent = sum(3, 5)

// example 1
const steps = ['one', 'two', 'three']
// callback declaration
function makeList (item) {
  const listElement = document.getElementById('myList')
  listElement.innerHTML += `<li>${item}</li>`
}
steps.forEach(makeList)

// Events - DOM Driven
const buttonElement = document.getElementById("submitButton");

function copyInput(event) {
  console.log(event)
  const inputElement = document.getElementById("inputBox")
  const outputElement = document.getElementById("output")
  outputElement.textContent = inputElement.value
}
buttonElement.addEventListener('click', copyInput)