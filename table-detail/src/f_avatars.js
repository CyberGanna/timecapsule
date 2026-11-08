/* ---------- avatars ---------- */
const HAIR = {
  short:c=>`<path d="M20 26C19 12 45 12 44 26C40 19 24 19 20 26Z" fill="${c}"/>`,
  long:c=>`<path d="M19 30C16 9 48 9 45 30L45 44L40 44L40 27C36 20 28 20 24 27L24 44L19 44Z" fill="${c}"/>`,
  bun:c=>`<path d="M20 26C19 12 45 12 44 26C40 19 24 19 20 26Z" fill="${c}"/><circle cx="32" cy="9" r="6" fill="${c}"/>`,
  bald:c=>`<path d="M21 22C23 15 41 15 43 22C39 19 25 19 21 22Z" fill="${c}"/>`,
  beard:c=>`<path d="M20 26C19 12 45 12 44 26C40 19 24 19 20 26Z" fill="${c}"/><path d="M22 28C22 40 42 40 42 28C40 34 24 34 22 28Z" fill="${c}"/>`
};
const P = {
  Lena:   ["#E6E0FF","#17C3C8","#F3D2B8","#D9B26A","long"],
  David:  ["#D9F8FA","#7C5CFF","#D9A47C","#4A3426","short"],
  Marco:  ["#E6E0FF","#17C3C8","#C68E6B","#1B1B1B","short"],
  Ana:    ["#D9F8FA","#7C5CFF","#E8B994","#2B1B14","long"],
  Sofia:  ["#D9F8FA","#090B16","#F1C9A5","#8A4B2A","bun"],
  Jonas:  ["#E6E0FF","#7C5CFF","#F3D2B8","#C9A15A","short"],
  Gregory:["#FFE9C7","#2E3566","#E8B994","#6B4A33","beard"],
  Mia:    ["#FFE0EC","#F4A6D7","#F1C9A5","#1B1B1B","long"],
  Omar:   ["#E6E0FF","#17C3C8","#A86F4C","#1B1B1B","beard"],
  Yuki:   ["#D9F8FA","#C9A7FF","#F3D2B8","#121212","bun"],
  Tom:    ["#FFE9C7","#7C5CFF","#F1C9A5","#B0B6C9","bald"],
  Priya:  ["#FFE0EC","#17C3C8","#B9805A","#1B1B1B","long"],
  Elif:   ["#E6E0FF","#FF9E8A","#E8B994","#3A2A20","long"],
  Kofi:   ["#D9F8FA","#E9F27A","#7A4E33","#121212","short"],
  You:    ["#E6E0FF","#7C5CFF","#E8B994","#3A2A20","short"]
};
function av(name){
  const [bg,shirt,skin,hair,st]=P[name]||P.You;
  return `<svg viewBox="0 0 64 64" role="img" aria-label="${name}"><rect width="64" height="64" fill="${bg}"/><path d="M8 66C8 47 20 43 32 43C44 43 56 47 56 66Z" fill="${shirt}"/><rect x="27" y="34" width="10" height="11" fill="${skin}"/><circle cx="32" cy="26" r="12" fill="${skin}"/>${HAIR[st](hair)}<circle cx="28" cy="27" r="1.5" fill="#090B16"/><circle cx="36" cy="27" r="1.5" fill="#090B16"/><path d="M28.5 31.5Q32 34.5 35.5 31.5" stroke="#090B16" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg>`;
}

