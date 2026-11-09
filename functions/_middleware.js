// Simple shared password for the whole site (browser asks once per session).
// Change it here, or set SITE_PASSWORD in Cloudflare Pages > Settings > Variables.
const DEFAULT_PASSWORD = "tavola-9154";

// The pages were designed as claude.ai artifacts, which wrap every page in a
// small base stylesheet. The key rule is [hidden] { display:none !important }:
// without it, pop-ups that are closed with the hidden attribute but also have
// their own display rule (for example the report dialog on Chats) show open on
// load. We add the same base styles first in <head>, so each page's own CSS
// still wins everywhere else and the site matches the artifacts.
const BASE_STYLE =
  '<style id="tc-artifact-base">:root{color-scheme:light}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style>';

class PrependBase {
  constructor() { this.done = false; }
  element(el) {
    if (this.done) return;
    this.done = true;
    el.prepend(BASE_STYLE, { html: true });
  }
}

export async function onRequest({ request, env, next }) {
  const password = env.SITE_PASSWORD || DEFAULT_PASSWORD;
  const auth = request.headers.get("Authorization") || "";
  let ok = false;
  if (auth.startsWith("Basic ")) {
    try {
      const [, pass] = atob(auth.slice(6)).split(/:(.*)/s);
      ok = pass === password;
    } catch (e) {}
  }
  if (ok) {
    const res = await next();
    const type = res.headers.get("Content-Type") || "";
    if (!type.includes("text/html")) return res;
    return new HTMLRewriter().on("head", new PrependBase()).transform(res);
  }
  return new Response("Password required", {
    status: 401,
    headers: { "WWW-Authenticate": 'Basic realm="TimeCapsule", charset="UTF-8"' },
  });
}
