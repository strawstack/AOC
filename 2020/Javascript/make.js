let fs = require('fs');
let axios = require('axios');
let secret = require("./secret");
const { exec } = require("child_process");

const YEAR = 2020;
const SESSION = secret.session;

async function main() {
    let day = process.argv[2];
    await run(`mkdir d${day}`);
    await run(`cp ./lib/p1.js ./d${day}`);
    let data = await getInput(day);
    fs.writeFile(`./d${day}/input.txt`, data, (err) => {
        if (err) throw err;
    });
}

function run(cmd) {
    return new Promise((res, rej) => exec(cmd, (error, stdout, stderr) => {
        if (error) rej(error);
        res(stdout);
    }));
}
async function getInput(day) {
    let url = `https://adventofcode.com/${YEAR}/day/${day}/input`;
    let res = await req(url);
    return res.data;
}
function req(url) {
    return new Promise((res, rej) => axios.get(url, {
        headers:{
            Cookie: `session=${SESSION};`
        }
    })
    .then(function (response) {
        res(response);
    })
    .catch(function (error) {
        rej(error);
    }));
}

main();
