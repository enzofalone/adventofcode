fs = require("fs");

let directory = {};
let currentDirectory = '/';

fs.readFile("input.txt", "utf8", (err, data) => {
  if (err) throw err;
  const lines = data.split("\n");
  lines.forEach((line) => {
    lineArr = line.split(" ");
    if (lineArr[0] == '$') {
        // instructions
        const instruction = lineArr[1];

        if(instruction == 'cd') {
            const pathTo = lineArr[2];
            if(pathTo === '/'){ 
                currentDirectory = directory;
            } else {
                if(directory[pathTo] ) {
                    currentDirectory = 
                }
                
            }
        }
    }
  });
});
