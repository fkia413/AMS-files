// Function expressions

"use strict";

// Q1

function subCalc(num1, num2) {
    return num1 - num2;
}

console.log(subCalc(10,1000));

// Q2

const welcome = function(name,age,gender){ // They used const instead of let so they don't overwrite it accidentally in the future
    return console.log(`My name is ${name}, i am ${age} years old and of gender ${gender}`);
    }

// Q3

powerUp = (n1,n2) => Math.pow(n1,n2);

console.log(powerUp(2,5)); // Understood but want to do more practice on arrow function syntax