const express = require('express');

const sendBot = require('./sendBot');

const paths = require('../configuration/paths.json');
const fields = require('../configuration/fields.json');

(async () => {
    await require('dotenv').config();

    const app = await express();

    await load(app, paths.createbot, async (request, response) => {
        /**
         * @type {express.Request}
         */
        let req = request;
        /**
         * @type {express.Response}
         */
        let res = response;

        const host = req?.headers[fields.host];
        if(!host) return;

        const port = parseInt(req?.headers[fields.port]);
        if(!port) return;

        let username = req?.headers[fields.username];
        if(!username) return;
        username = (username+='%randomnumber%')
            // .replace('%random%', await getUsername())
            .replace('%randomnumber%', Math.floor(Math.random()*10000))
            ;

        let fakehost = req?.headers[fields.fakehost];
        if(!fakehost) fakehost = host;

        let version = req?.headers[fields.version];
        if(!version) version = '1.8.9';

        await sendBot(host, port, username, fakehost, version);
    });

    const port = process.env.port;
    await app.listen(port, () => {
        console.log(`Listening on port ${port}.`);
    });
})();

/**
 * @param {express.Express} app 
 * @param {String} str 
 * @param {Promise<any>} execute 
 */
async function load(app, str, execute) {
    const infos = str.split(' ');
    const method = infos[0];
    const path = infos[1];

    await app[method.toLowerCase()](path, async (req, res) => {
        console.log(req?.headers?.authorization);
        if(req?.headers?.authorization && req.headers.authorization === `Bearer ${process.env.token}`) await execute(req, res);
        await res.status(404).send();
    });
}