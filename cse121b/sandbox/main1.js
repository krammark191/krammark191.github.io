console.log(typeof 42);
console.log(typeof 'abc');
console.log(typeof true);
console.log(typeof undefined);
console.log(typeof null);
console.log(typeof { a: 1 });
console.log(typeof [1, 2, 3]);
console.log(typeof function hello () {});

let adult = true; // Use let, not var unless global scope needed.
let myName = 'Bob';
let age = 24;

if (adult) {
  myName = 'Bob'
  age = 24
};

console.log(myName);
console.log(age);
console.log(adult);

let variable = '5' + 3; // 53
console.log(variable);

let myVariable = 4;
if (adult) {
    myVarable = 6;
    console.log(myVarable);
};

let names = ["Bob", "Sue", "Jorge", "Svetlana"];
console.log(names[2]);
let aName = names[0];
names[2] = "George";
console.log(names)

names.push("Grace");
console.log(names);
//Displays ['Bob','Sue','George','Svetlana','Grace']

names.pop();
console.log(names);
//Displays ['Bob','Sue','George','Svetlana']

let myString = "This is my String!";
console.log(myString.length); // 18
console.log(myString[2]); // "i"  - remember that indexes start counting with 0!

const hello = "Hello";
const world = "World";
const complexString = hello + " " + world;
const complexString2 = `${hello} ${world}`;
console.log(complexString);
console.log(complexString2);

const myArray = ["one", "two", "three"];
const htmlString = `
<ol>
  <li>${myArray[0]}</li>
  <li>${myArray[1]}</li>
  <li>${myArray[2]}</li>
</ol>`;

document.querySelector('div').innerHTML = htmlString;

const PI = 3.14;
let radius = 3;
let area = 0;
area = radius * radius * PI;
console.log(area);
radius = 4;
area = radius * radius * PI;
console.log(area);
