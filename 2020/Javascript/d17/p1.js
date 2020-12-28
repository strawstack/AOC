let fs = require('fs');

function sol(data) {

    // Tight bounds around active cells
    let size = {
        x: {low: 0, hi: data[0].length - 1}, // positive right
        y: {low: 0, hi: data.length - 1},  // negative up
        z: {low: 0, hi: 0},  // positive out of the screen
    };

    // Track active cells
    let active = {};

    // Read input into active
    let z = 0;
    for (let y = 0; y <= size.y.hi; y++) { // Rows
        for (let x = 0; x <= size.x.hi; x++) { // Cols
            if (data[y][x] == "#") {
                let h = hash({x: x, y: y, z: z});
                active[h] = true;
            }
        }
    }

    // 26 Neighbour cells
    let adj = [];
    for (let i = -1; i <= 1; i++) {
        for (let j = -1; j <= 1; j++) {
            for (let k = -1; k <= 1; k++) {
                if (i == 0 && j == 0 && k == 0) {
                    continue;
                }
                adj.push({x: i, y: j, z: k});
            }
        }
    }

    let cycle = 6;
    while (cycle > 0) {
        let p = 1;
        let zlo = size.z.low - p;
        let zhi = size.z.hi + p;
        let ylo = size.y.low - p;
        let yhi = size.y.hi + p;
        let xlo = size.x.low - p;
        let xhi = size.x.hi + p;

        let next = {};
        for (let z = zlo; z <= zhi; z++) { // close to far
            for (let y = ylo; y <= yhi; y++) { // top to bot
                for (let x = xlo; x <= xhi; x++) { // left to right
                    let pos = {x: x, y: y, z: z};
                    let h = hash(pos);
                    let isActive = h in active;
                    let count = countActive(active, adj, pos, size);
                    if (isActive && (count == 2 || count == 3)) {
                        next[h] = true;

                    } else if(!isActive && count == 3) {
                        next[h] = true;

                    }
                }
            }
        }

        active = next;
        cycle -= 1;
    }

    let total = Object.keys(active).length;
    return total;
}

function hash(pos) {
    return `${pos.x}:${pos.y}:${pos.z}`;
}

// Count active cells adj to pos
function countActive(active, adj, pos, size) {
    let count = 0;
    for (let a of adj) {

        let nx = a.x + pos.x;
        let ny = a.y + pos.y;
        let nz = a.z + pos.z;

        // Possibly update size of 3D space
        size.x.low = Math.min(size.x.low, nx);
        size.x.hi = Math.max(size.x.hi, nx);
        size.y.low = Math.min(size.y.low, ny);
        size.y.hi = Math.max(size.y.hi, ny);
        size.z.low = Math.min(size.z.low, nz);
        size.z.hi = Math.max(size.z.hi, nz);

        let apos = { x: nx, y: ny, z: nz };
        let h = hash(apos);
        if (h in active) {
            count += 1;
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
        //data = await readFile('./test_input.txt');
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
