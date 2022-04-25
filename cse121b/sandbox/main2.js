// Comparisons

console.log(5 >= 5 && 6 == 6)

// Conditionals

let yourAge = 20
console.log(yourAge >= 18)
if (yourAge >= 18) {
  console.log('You can vote.')
} else {
  console.log('You cannot vote.')
}

let numSales = 1900

if (numSales <= 50) {
  console.log('Way too few sales')
} else if (numSales <= 1000) {
  console.log('Average number of sales')
} else {
  console.log('A good number of sales.')
}

let grade = 'A'
let gpaPoints = 0.0
switch (grade) {
  case 'A':
    gpaPoints = 4.0
    break
  case 'B':
    gpaPoints = 3.0
    break
  case 'C':
    gpaPoints = 2.0
    break
  case 'D':
    gpaPoints = 1.0
    break
  case 'F':
    gpaPoints = 0.0
    break
  default:
    gpaPoints = -1
}

console.log(gpaPoints)

if (yourAge < 5) {
  console.log('Preschool')
} else if (yourAge <= 18) {
  console.log('in secondary school')
} else {
  console.log('Can go to college')
}

function flip () {
  let num = Math.random()
  if (num < 0.5) {
    console.log('Heads')
  } else {
    console.log('Tails')
  }
}

flip()