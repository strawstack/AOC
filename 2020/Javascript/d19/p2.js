let fs = require('fs');

function sol(data) {
    let rules = data[0].split("\n").map(x => {
        let xs = x.split(": ");
        let n = parseInt(xs);
        let rule = xs[1].split(" | ");
        return {
            number: parseInt(n),
            match: rule.map(y => {
                if (y.indexOf("\"") != -1) {
                    return [y[1]];
                } else {
                    return y.split(" ").map(z => parseInt(z));
                }
            })
        };
    });
    let words = data[1].split("\n");

    // Expand rule 0 to all possible derived words
    let lookup = {};
    rules.forEach(x => {
        lookup[x.number] = x.match;
    });

    // Altered rules
    // 8: 42 | 42 8
    // 11: 42 31 | 42 11 31
    if (false) {
        lookup[8] = [[42], [42, 8]];
        lookup[11] = [[42, 31], [42, 11, 31]];
    }

    //console.log(lookup[19]);
    //console.log(lookup[91]);
    //console.log(lookup[31]);
    //console.log(lookup[0]);
    //console.log(lookup[11]);

    let base42 = getRules(lookup, 42);
    let base31 = getRules(lookup, 31);

    // A match is some number of reps of base42
    // Followed by a rule 11

    let count = 0;
    words.forEach(word => {

        let a = (_word) => {
            let chunk = 8;
            for (let i = 0; i < _word.length; i += chunk) {
                let target = _word.substr(i, chunk);
                if (!(target in base42)) {
                    return false;
                }
            }
            return true;
        };

        let b = (_word) => {
            let chunk = 8;
            let len = _word.length;
            let groups = Math.floor(len / chunk);
            if (groups % 2 != 0) {
                return false;
            }
            let half = groups / 2;
            for (let i = 0; i < half; i++) {
                let target = _word.substr(i * chunk, chunk);
                if (!(target in base42)) {
                    return false;
                }
            }
            for (let i = half; i < groups; i++) {
                let target = _word.substr(i * chunk, chunk);
                if (!(target in base31)) {
                    return false;
                }
            }
            return true;
        };

        let chunk = 8;
        let len = word.length;
        let groups = Math.floor(len / chunk);

        let valid = false;
        for (let i = 1; i < groups; i++) {
            let one = word.substr(0, i * chunk);
            let two = word.substr(i * chunk, word.length);
            if (a(one) && b(two)) {
                valid = true;
                break;
            }
        }

        if (valid) {
            count += 1;
        }
    });

    /*
    console.log("bbabaaba" in base42);
    console.log("aabaabbb" in base42);
    console.log("abbbbbbb" in base42); */

    return count;
}

function getRules(lookup, base) {
    // Each element is a list of letters and numbers
    let q = [];
    for (let rule of lookup[base]) {
        q.push({
            ltrs: [],
            nums: rule
        });
    }

    // Store possible matches
    let possible_matches = [];
    while (q.length > 0) {
        //console.log("---");

        let nx = q.pop();
        let ltrs = nx.ltrs;
        let nums = nx.nums;

        //console.log("nums");
        //console.log(nums);

        if (nums.length == 0) {
            possible_matches.push(ltrs);

        } else {
            // Number of next rule
            let next_num = nums[0];
            //console.log("next_num");
            //console.log(next_num);

            // The next rule to examine
            let next_rule = lookup[next_num];
            //console.log("next_rule");
            //console.log(next_rule);

            // Copy nums list
            let cnums = nums.slice();
            cnums.shift();

            //console.log("cnums");
            //console.log(cnums);

            //console.log("next_rule.length");
            //console.log(next_rule.length);

            // For each branch of the next rule
            // push something to the stack
            for (let i = 0; i < next_rule.length; i++) {

                // Copy nums and ltrs for this branch
                let ccnums = cnums.slice();
                let cltrs = ltrs.slice();

                // One branch of the rule
                let r = next_rule[i];

                //console.log("next_rule[i]");
                //console.log(r);

                // The rule is a letter
                if (r[0] == "a" || r[0] == "b") {
                    cltrs.push(r[0]);
                    q.push({
                        ltrs: cltrs,
                        nums: ccnums
                    });

                // The rule is not just a letter
                } else {
                    let cr = r.slice();
                    cr.push(...ccnums);

                    //console.log("cr");
                    //console.log(cr);

                    q.push({
                        ltrs: cltrs,
                        nums: cr
                    });
                }
            }
        }
    }

    let pm = {};
    possible_matches.forEach(x => {
        pm[x.join("")] = true;
    });

    return pm;
}

//
// main
//

async function main() {
    let data;
    try {
        data = await readFile('./input.txt');
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
