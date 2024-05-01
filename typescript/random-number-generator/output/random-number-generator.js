"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.randomNumberGenerator = void 0;
function randomNumberGenerator() {
    var now = new Date();
    var timeInMs = now.getTime();
    var randomNumber = Math.floor(timeInMs % 1000);
    return randomNumber;
}
exports.randomNumberGenerator = randomNumberGenerator;
var randomOutput = randomNumberGenerator();
console.log(randomOutput);
