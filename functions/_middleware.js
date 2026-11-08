// Simple shared password for the whole site (browser asks once per session).
// Change it here, or set SITE_PASSWORD in Cloudflare Pages > Settings > Variables.
const DEFAULT_PASSWORD = "tavola-9154";

export async function onRequest({ request, env, next }) {
  const password = env.SITE_PASSWORD || DEFAULT_PASSWORD;
  const auth = request.headers.get("Authorization") || "";
  if (auth.startsWith("Basic ")) {
    try {
      const [, pass] = atob(auth.slice(6)).split(/:(.*)/s);
      if (pass === password) return next();
    } catch (e) {}
  }
  return new Response("Password required", {
    status: 401,
    headers: { "WWW-Authenticate": 'Basic realm="TimeCapsule", charset="UTF-8"' },
  });
}
