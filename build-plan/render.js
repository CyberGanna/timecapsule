const {chromium} = require('playwright');
const {execSync} = require('child_process');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  const dir = process.cwd();
  const foot = '<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:7px;letter-spacing:2px;color:#6B6F86;padding:0 22mm;display:flex;justify-content:space-between"><span></span><span class="pageNumber"></span></div>';
  await p.goto('file://' + dir + '/cover.html', {waitUntil: 'load'});
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({path: '/tmp/tc-cover.pdf', format: 'A4', printBackground: true, margin: {top: 0, bottom: 0, left: 0, right: 0}});
  await p.goto('file://' + dir + '/plan.html', {waitUntil: 'load'});
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({path: '/tmp/tc-body.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: require('fs').readFileSync(dir + '/header.html', 'utf8'), footerTemplate: foot});
  await b.close();
  execSync('pdfunite /tmp/tc-cover.pdf /tmp/tc-body.pdf "' + dir + '/TimeCapsule-Build-Plan.pdf"');
  console.log('done');
})();
