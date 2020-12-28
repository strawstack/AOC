let fs = require('fs');

function sol(data) {
    const OPEN = "(";
    const CLOSE = ")";

    let res = [];
    for (let row of data) {
        row = row.split("").filter(x => x != " ");
        row = row.map(x => {
            if (x != "+" && x != "*" && x != "(" && x != ")") {
                return parseInt(x);
            }
            return x;
        });

        // resolve expression to value
        let resolve = (stack) => {
            //console.log(" ***");
            //console.log(" resolve");
            //console.log(` stack: ${show(stack)}`);
            let ans = [];
            while (stack.length > 0) {
                let nx = stack.pop();
                if (nx == "+") {
                    let a2 = stack.pop();
                    let a1 = ans.pop();
                    ans.push(a1 + a2);

                } else if (nx == "*") {
                    ans.push(nx);

                } else { // nx == number
                    ans.push(nx);
                }
            }

            while (ans.length > 0) {
                stack.push(ans.pop());
            }

            while (stack.length > 0) {
                let nx = stack.pop();
                if (nx == "*") {
                    let a2 = stack.pop();
                    let a1 = ans.pop();
                    ans.push(a1 * a2);

                } else { // nx == number
                    ans.push(nx);
                }
            }
            return ans[0];
        };

        // Read stack
        let f = (stack) => {
            let ans = [];
            while (stack.length > 0) {
                //console.log("---");
                //console.log(`stack: ${show(stack)}`);
                //console.log(`ans: ${ans.join("")}`);

                let nx = stack.pop();
                //console.log(`nx: ${nx}`);

                if (nx == CLOSE) {

                    // Back track and solve
                    // the previous expression
                    let temp = [];
                    while (true) {
                        let nx2 = ans.pop();
                        if (nx2 == OPEN) break;
                        temp.push(nx2);
                    }
                    let r = resolve(temp);
                    ans.push(r);

                } else { // nx == number | + | * | OPEN
                    ans.push(nx);
                }
            }
            return ans[0];
        };

        // Read data into stack
        let stack = [CLOSE];
        while (row.length > 0) {
            stack.push(row.pop());
        }
        stack.push(OPEN);

        // Eval stack
        // and cache answer for row
        let r = f(stack);
        res.push(r);
    }

    return res.reduce((a, c) => a + c);
}

function show(stack) {
    s = stack.slice();
    let lst = [];
    while (s.length > 0) {
        lst.push(s.pop());
    }
    return lst.join("");
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
