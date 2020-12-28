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

    //console.log(lookup[19]);
    //console.log(lookup[91]);
    //console.log(lookup[55]);
    //console.log(lookup[0]);
    //console.log(lookup[11]);

    // Each element is a list of letters and numbers
    let q = [{
        ltrs: [],
        nums: lookup[0][0]
    }];

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

    let count = 0;
    words.forEach(word => {
        if (word in pm) {
            count += 1;
        }
    });

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
