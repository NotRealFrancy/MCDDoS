const { createBot } = require('mineflayer');

/**
 * @param {String} host 
 * @param {number} port 
 * @param {String} username 
 * @param {String} fakehost 
 * @param {String} version 
 */
module.exports = async (host, port, username, fakehost, version) => {
    await loadBot(host, port, username, fakehost, version);
}

/**
 * @param {String} host 
 * @param {number} port 
 * @param {String} username 
 * @param {String} fakehost 
 * @param {String} version 
 */
async function loadBot(host, port, username, fakehost, version) {
    const bot = await createBot({
        host,
        port,
        fakeHost: fakehost,
        username,
        viewDistance: 'far',
        version
    });

    bot.once('error', async (err) => {
        console.error(err);
        await bot.end();
        await loadBot(host, port, username, fakehost, version);
    });

    bot.once('end', async (reason) => {
        console.error(reason);
        await bot.end();
        await loadBot(host, port, username, fakehost, version);
    });
}