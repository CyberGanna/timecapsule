// node render.js  ->  TimeCapsule-Keeping-the-Record.pdf (+ PNG previews in ./shots when PREVIEW=1)
const {chromium} = require('playwright');
const fs = require('fs');
(async () => {
  const dir = __dirname;
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1280, height: 720}});
  await p.goto('file://' + dir + '/slides.html', {waitUntil: 'load'});
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({path: dir + '/TimeCapsule-Keeping-the-Record.pdf', printBackground: true, preferCSSPageSize: true});
  if (process.env.PREVIEW) {
    fs.mkdirSync(process.env.PREVIEW, {recursive: true});
    const n = await p.$$eval('section.s', s => s.length);
    for (let i = 0; i < n; i++) {
      const el = (await p.$$('section.s'))[i];
      await el.screenshot({path: process.env.PREVIEW + '/s' + (i + 1) + '.png'});
    }
  }
  await b.close();
  console.log('done');
})();
