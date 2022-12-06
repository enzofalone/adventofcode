fs = require("fs");

let crates = [
  ["F", "H", "B", "V", "R", "Q", "D", "P"],
  ["L", "D", "Z", "Q", "W", "V"],
  ["H", "L", "Z", "Q", "G", "R", "P", "C"],
  ["R", "D", "H", "F", "J", "V", "B"],
  ["Z", "W", "L", "C"],
  ["J", "R", "P", "N", "T", "G", "V", "M"],
  ["J", "R", "L", "V", "M", "B", "S"],
  ["D", "P", "J"],
  ["D", "C", "N", "W", "V"],
];

let foundBlank = false;


fs.readFile("input.txt", "utf8", (err, data) => {
  if (err) throw err;
  const lines = data.split("\n");
  lines.forEach((line) => {
    line.replace(/\r?\n|\r/g, '');

    const instructions = line.split(' ');
    const n = instructions[1];
    const from = instructions[3] - 1;
    const to = instructions[5] - 1;

    if(foundBlank) {
        for (let i = 0; i < n; i++) {
            const crate = crates[from].pop();

            crates[to].push(crate);
        }
    }

    if(line.length === 1) {
        foundBlank = true;
    }
  });
});

let result = '';

for (let i = 0; i < crates.length; i++) {
    result += crates[i][crates[i].length-1]
    
}
console.log(result);