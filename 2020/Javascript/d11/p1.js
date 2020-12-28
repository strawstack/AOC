let fs = require('fs');

function sol(data) {
    grid = data.map(x => x.split(""));

    let adj = [
        {r: -1, c: 0}, {r: -1, c: 1}, {r: 0, c: 1}, {r: 1, c: 1},
        {r: 1, c: 0}, {r: 1, c: -1}, {r: 0, c: -1}, {r: -1, c: -1}
    ];

    let nx_grid = [];
    for (let row of grid) {
        nx_grid.push(row.slice());
    }

    let change = true;
    while (change) {
        change = false;
        grid.forEach((row, r) => {
            row.forEach((item, c) => {
                let count = getCount(grid, adj, {r: r, c: c});

                if (item == "L" && count == 0) {
                    nx_grid[r][c] = "#";
                    change = true;

                } else if (item == "#" && count >= 4) {
                    nx_grid[r][c] = "L";
                    change = true;

                }

            });
        });

        nx_grid.forEach((row, i) => {
            grid[i] = row.slice();
        });

    }

    let total = 0;
    grid.forEach((row, r) => {
        row.forEach((item, c) => {
            if (item == "#") {
                total += 1;
            }
        });
    });

    return total;
}

function getCount(grid, adj, coord) {
    const ROW = grid.length;
    const COL = grid[0].length;
    let count = 0;
    for (let offset of adj) {
        let nc = {
            r: coord.r + offset.r,
            c: coord.c + offset.c
        };
        if (nc.r >= 0 && nc.r < ROW && nc.c >= 0 && nc.c < COL) {
            let value = grid[nc.r][nc.c];
            if (value == "#") {
                count += 1;
            }
        }
    }
    return count;
}

//
// main
//

async function main() {
    let data;
    try {
        data = await readFile('./input.txt');
    } catch(err) { throw err; }

    data = data.trim().split("\n");
    let ans = sol(data);

    if(ans !== undefined) {
        console.log(ans);
    }
}

main().catch(err => console.log(err));

//
// Helper Functions
//

// read file
function readFile(path) {
    return new Promise((res, rej) => {
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) rej(err);
            res(data);
        });
    });
}
