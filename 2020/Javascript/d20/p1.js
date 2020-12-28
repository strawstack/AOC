let fs = require('fs');

// Size of puzzle piece
const SIZE = 10;

function sol(data) {
    let ps = data.map(chunk => {
        let rows = chunk.split("\n");
        let res = rows[0].match(/^Tile (\d+):$/);
        let number = parseInt(res[1]);
        rows.shift();
        return {
            id: number,
            grid: rows
        };
    });

    console.log(ps);
    console.log(ps.length);

    return undefined;
}

// Get side, top to bot, left to right
// for given grid with flip or rotation
// piece: object with id, and 2D array of chars
// flip: true or false for flip
// rotate: 1 to 3 rotations
// side: 0, 1, 2, 3 for top, right, bot, left
// Uses memoization
let sideLookup = {};
function getSide(piece, flip, rotate, side) {
    let h = hashForGetSide(piece.id, flip, rotate);
    if (h in sideLookup) {
        return sideLookup[h];
    }

    // TODO - compute coord translation
    // given flip and rotate
    // compute coords to read side

}

function getCell(grid, loc, flip, rotate) {
    const MV = SIZE - 1;
    const row = loc.r;
    const col = loc.c;
    let ml = loc;
    if (flip) {
        if (rotate == 1) { // 90 deg clockwise
            ml = {r: col, c: -1 * row + MV};
        } else if (rotate == 2) {
            ml = {r: -1 * row + MV, c: -1 * col + MV};
        } else if (rotate == 3) {
            ml = {r: -1 * col + MV, c: row};
        }
    } else {
        if (rotate == 1) {
            ml = {r: row, c: -1 * col + MV};
        } else if (rotate == 2) {
            ml = {r: -1 * col + MV, c: -1 * row + MV};
        } else if (rotate == 3) {
            ml = {r: -1 * row + MV, c: col};
        }
    }

    return grid[ml.r][ml.c];
}

function hashForGetSide(id, flip, rotate) {
    return `${id}:${flip}:${rotate}`;
}

//
// main
//

async function main() {
    let data;
    try {
        //data = await readFile('./input.txt');
        data = await readFile('./test_input.txt');
    } catch(err) { throw err; }

    data = data.trim().split("\n\n");
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
