let fs = require('fs');

function sol(data) {

    let d0 = data[0].split("\n");
    let d1 = data[1].split("\n");
    d0.shift();
    d1.shift();
    let p = d0.map(x => parseInt(x));
    let c = d1.map(x => parseInt(x));

    // Play recursive game
    let res = game(p.slice(), c.slice(), 0);
    let winner = (res[0].length == 0) ? res[1] : res[0];

    // Calculate score
    let total = 0;
    let length = winner.length;
    for (let card of winner) {
        total += card * length;
        length -= 1;
    }

    // wrong - 4854
    // wrong - 196
    return total;
}

let prevRounds = [];

// Returns [[], []] representing two decks
function game(p, c, rn) {
    // New game means don't consider
    // rounds from previous games
    prevRounds.push({});

    let round = 1;
    while (p.length > 0 && c.length > 0) {

        // console.log(`\n-- Round ${round} (Game ${rn + 1}) --`);
        // console.log(`P1 Deck: ${p}`);
        // console.log(`P2 Deck: ${c}`);

        // Check instant win condition
        let h = hash(p, c);
        if (h in prevRounds[rn]) {
            //console.log(score(p));
            //throw "Instant win for player one!";
            return [[1], []];
        }
        prevRounds[rn][h] = true;

        // Draw cards
        let pCard = p.shift();
        let cCard = c.shift();

        // console.log(`P1 Play: ${pCard}`);
        // console.log(`P2 Play: ${cCard}`);

        // If players have enough cards
        if (p.length >= pCard && c.length >= cCard) {
            let res = game(p.slice(0, pCard), c.slice(0, cCard), rn + 1);
            if (res[0].length == 0) { // c wins
                c.push(cCard);
                c.push(pCard);
                // console.log(`Player 2 wins round ${round} of game ${rn + 1}!`);
            } else { // p wins
                p.push(pCard);
                p.push(cCard);
                // console.log(`Player 1 wins round ${round} of game ${rn + 1}!`);
            }
        } else {
            // Winner of round is higher card
            if (pCard > cCard) {
                p.push(pCard);
                p.push(cCard);
                // console.log(`Player 1 wins round ${round} of game ${rn + 1}!`);
            } else {
                c.push(cCard);
                c.push(pCard);
                // console.log(`Player 2 wins round ${round} of game ${rn + 1}!`);
            }
        }
    }

    // Return result of game
    return [p, c];
}

function hash(p, c) {
    let ps = p.map(x => x.toString()).join(":");
    let cs = c.map(x => x.toString()).join(":");
    return `${ps}::${cs}`;
}

function score(winner) {
    let total = 0;
    let length = winner.length;
    for (let card of winner) {
        total += card * length;
        length -= 1;
    }
    return total;
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
