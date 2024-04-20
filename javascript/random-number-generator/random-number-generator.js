// Random number generator in JavaScript
// This script generates a random number based on the current time in milliseconds.
// Refactored to output to console.
// Usage: node random-number-generator.js

function randomNumberGenerator() {
  const now = new Date();
  const timeInMs = now.getTime(); // current time in milliseconds
  const randomNumber = Math.floor(timeInMs % 1000); // Take the remainder of the division of the current time in milliseconds by 1000
  return randomNumber;
}

const randomNumber = randomNumberGenerator();
console.log(randomNumber);
