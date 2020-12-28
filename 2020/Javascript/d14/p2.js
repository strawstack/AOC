let fs = require('fs');

function sol(data) {
    data = data.map(x => {
        if (x.substr(0, 4) == "mask") {
            let msk = x.substr(7, x.length -1);
            if (msk.length != 36) {
                throw "Incorrect size for mask";
            }
            return {
                mask: true,
                val: x.substr(7, x.length -1)
            };
        } else {
            let res = x.match(/mem\[(\d+)\] = (\d+)/);
            let addr = res[1];
            let val = res[2];
            return {
                mask: false,
                addr: parseInt(addr),
                val: parseInt(val)
            };
        }
    });

    let mem = {};
    let mask = undefined;

    for (let cmd of data) {
        if (cmd.mask) {
            mask = cmd.val;
        } else {
            let addrList = getAddrList(mask, cmd.addr);
            for (let addr of addrList) {
                mem[addr] = cmd.val;
            }
        }
    }

    let total = 0;
    for (let k in mem) {
        let val = mem[k];
        total += val;
    }

    // wrong - 3817097789094
    // wrong - 3837642624535
    return total;
}

function getAddrList(mask, addr) {
    let resList = [];
    let baseAddr = applyMask(mask, addr);
    let numX = getNumX(baseAddr);
    let range = Math.pow(2, numX) - 1;
    for (let i = 0; i <= range; i++) {
        let xMask = pad(i.toString(2), numX).split("").reverse();
        let xMaskIndex = 0;
        let nextAddr = baseAddr.split("");
        nextAddr.forEach((c, i) => {
            if (c == "X") {
                nextAddr[i] = xMask[xMaskIndex];
                xMaskIndex += 1;
            }
        });
        resList.push(nextAddr);
    }

    let ansList = resList.map(x => {
        return parseInt(x.join(""), 2);
    });

    return ansList;
}

function getNumX(baseAddr) {
    let total = 0;
    for (let c of baseAddr) {
        if (c == "X") {
            total += 1;
        }
    }
    return total;
}

function applyMask(mask, val) {
    let bStr = val.toString(2);
    let bStrPad = pad(bStr, 36);
    let res = [];
    for (let i = 0; i < bStrPad.length; i++) {
        let mBit = mask[i];
        let vBit = bStrPad[i];
        if (mBit == "X") {
            res.push("X");
        } else if (mBit == "1") {
            res.push("1");
        } else { // mask bit 0
            res.push(vBit);
        }
    }
    return res.join("");
}

// pad zeros on left
function pad(val, len) {
    let sVal = val.toString();
    let zeros = [];
    if (sVal.length < len) {
        for (let i = 0; i < len - sVal.length; i++) {
            zeros.push("0");
        }
    }
    return zeros.join("") + sVal;
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
