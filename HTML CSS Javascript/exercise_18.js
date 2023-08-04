// Objects and arrays exercises

"use strict";

// Q1

let darthVader = new Object();

darthVader["allegiance"] = "empire";
darthVader["weapon"] = "lightsaber";
darthVader["sith"] = "true";

console.log(darthVader)

console.log(`Darth Vader's allegiance is to the ${darthVader.allegiance}`);
console.log(`Darth Vader's weapon of choice is a ${darthVader.weapon}`);
console.log(`Darth Vader is a sith? ${darthVader.sith}`);

// The solution had this structure for "Darth Vader is a Jedi? False"
console.log(`Darth Vader is a Jedi? ${darthVader.sith ? "false" : "true"}`);

// Q2

let myArray = ["hello",'everyone'];

console.log(myArray.length);

myArray.push("howdy");

console.log(myArray.length); // Remember myArray.length 

myArray.shift();

 for(let eachElement of myArray) {
     console.log(eachElement);
 } // I need to remember this structure (for .. of) 