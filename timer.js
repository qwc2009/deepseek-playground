#!/usr/bin/env node
const seconds = parseInt(process.argv[2]) || 5;
console.log(`Timer: ${seconds}s`);
let remaining = seconds;
const interval = setInterval(() => {
    remaining--;
    process.stdout.write(`\r${remaining}s remaining`);
    if (remaining <= 0) {
        clearInterval(interval);
        console.log("\n\nTime's up!");
    }
}, 1000);
