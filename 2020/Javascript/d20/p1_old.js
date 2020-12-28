let fs = require('fs');

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

    

    return undefined;
}

function getTopLeft(ps) {
    console.log(`call getTopLeft`);
    // Find potential topLeft piece
    let topLeft = undefined;
    for (let p1 of ps) {
        console.log(` p1: ${p1.id}`);
        let con = false;

        // Check for matches against top
        for (let p2 of ps) {
            console.log(` p2: ${p2.id}`);
            if (p1.id == p2.id) continue;
            let res = match(getTop(p1), getBot, p2);
            if (res != false) {
                console.log(` found match!`);
                con = true;
                break;
            }
        }

        if (con) continue;

        // Check for matches against left
        for (let p2 of ps) {
            if (p1.id == p2.id) continue;
            let res = match(getLeft(p1), getRight, p2);
            if (res != false) {
                con = true;
                break;
            }
        }

        // This is the topLeft piece
        if (!con) {
            return topLeft;
        }
    }
}

// Find match for p1 from any rotation of any piece in ps
// Against edge using given function
function findMatch(p1, getEdge, getEdgeOther, ps) {
    for (let p of ps) {
        if (p1.id == p.id) continue;
        let res = match(getEdge(p1), getEdgeOther, p);
        if (res != false) {
            return res;
        }
    }
    return false;
}

// Rotate and flip p2 in all directions
// searching for a match against edge
// Return rotated p2 or false
function match(edge, getEdge, p2) {
    console.log(`call match`);
    console.log(` edge: ${edge}`);
    console.log(` p2: ${p2.id}`);
    let cp2 = cp(p2);
    let c = 4;
    while (c > 0) {
        let e = getEdge(cp2);
        console.log( `e: ${e}`);
        if (edge == e) {
            return cp2;
        }
        cp2.grid = rotate(cp2.grid);
        c -= 1;
    }
    cp2.grid = flip(cp2.grid);
    c = 4;
    while (c > 0) {
        let e = getEdge(cp2);
        console.log( `e: ${e}`);
        if (edge == e) {
            return cp2;
        }
        cp2.grid = rotate(cp2.grid);
        c -= 1;
    }
    return false;
}

// Copy piece
function cp(p) {
    let cp = {};
    cp.id = p.id;
    cp.grid = p.grid.slice();
    return cp;
}

function rotate(grid) {
    let cgrid = grid.slice();
    const NROWS = cgrid.length;
    const NCOLS = cgrid[0].length;
    let ng = cgrid.slice();
    ng = ng.map(row => row.split(""));
    for (let c = 0; c < NCOLS; c++) {
        for (let r = 0; r < NCOLS; r++) {
            ng[r][c] = cgrid[NROWS - 1 - c][r];
        }
    }
    return ng.map(row => row.join(""));
}

function flip(grid) {
    let crows = grid.slice();
    for (let i = 0; i < crows.length; i++) {
        crows[i] = crows[i].split("").reverse().join("");
    }
    return crows;
}

function getTop(piece) {
    return piece.grid[0];
}

function getRight(piece) {
    const NCOLS = piece.grid[0].length;
    let lst = [];
    for (let r = 0; r < piece.grid.length; r++) {
        lst.push(piece.grid[r][NCOLS - 1]);
    }
    return lst.join("");
}

function getBot(piece) {
    return piece.grid[piece.grid.length - 1];
}

function getLeft(piece) {
    let lst = [];
    for (let r = 0; r < piece.grid.length; r++) {
        lst.push(piece.grid[r][0]);
    }
    return lst.join("");
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
