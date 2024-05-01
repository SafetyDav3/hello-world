// Randomly generate a number between 0 and 999

export function randomNumberGenerator(): number {
  const now: Date = new Date();
  const timeInMs: number = now.getTime();
  const randomNumber: number = Math.floor(timeInMs % 1000);
  return randomNumber;
}

const randomOutput: number = randomNumberGenerator();
console.log(randomOutput);
