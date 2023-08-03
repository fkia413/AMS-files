"use strict";
// Iteration exercise

// for(let i = 0; i <= 10; i++) {
//     console.log(i);
// }

// Q1

for(let a = 100; a <= 200; a++) {
    console.log(a);
}

let a = 100;
while (a <= 200) {
    a++;
    console.log(a)
}



// Q2


for (let a = 100; a<=200; a++) {
    if (a%2==0) { // need to remember to add parenthesis for calculations
        console.log("-")
    }
    if a%2!==0 { // extra calculation not needed, adds overhead 
        console.log("*")
    }
}

for (let a = 100; a<=200; a++) {
    if (a % 2 == 0) {
        console.log("-");
    }
    else{
        console.log("*");
    }
}

// while loop (mine followed by solution), need to marinate this

let a = 100;
while (a<=200) {
    a++;
}

let a = 100;
while (a <= 200) {
  if (a % 2 == 0) {
    console.log("-");
  } else {
    console.log("*");
  }
  a++;
}

// I need to practice the logic behind question 3
// Q3: Create a method that can print out the numbers 1-10 10 times each.

// Solution: 

for (let i = 0; i < 10; i++) {
    for (let j = 1; j <= 10; j++) {
      console.log(j);
    }
 }  

 console.log(first)
// clg for console log 

// alert(message) where 'message' is any content you'd like displayed 

