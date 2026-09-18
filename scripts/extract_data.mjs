// index.html の JS から AREAS / STADIUMS / FARE / AREA_KEY / KANTO_LOCAL を取り出して評価する（ビルドとテストで共用）
import fs from 'node:fs';
export function loadData(path = new URL('../index.html', import.meta.url)) {
  const html = fs.readFileSync(path, 'utf8');
  const js = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]).find(x => x.includes('const FARE'));
  const pick = name => { const m = js.match(new RegExp(`const ${name}\\s*=\\s*([\\s\\S]*?);\\n`)); if (!m) throw new Error('no ' + name); return m[1]; };
  const src = `const AREAS=${pick('AREAS')};const STADIUMS=${pick('STADIUMS')};const AREA_KEY=${pick('AREA_KEY')};const FARE=${pick('FARE')};const KANTO_LOCAL=${pick('KANTO_LOCAL')};return {AREAS,STADIUMS,AREA_KEY,FARE,KANTO_LOCAL};`;
  return new Function(src)();
}
export function fareBetween(d, a, b) {
  const A = d.AREA_KEY(a), B = d.AREA_KEY(b);
  if (A === B) return { same: true, local: (A === 'tokyo' && a !== b) ? d.KANTO_LOCAL : 0 };
  const f = d.FARE[`${A}-${B}`] || d.FARE[`${B}-${A}`];
  if (!f) return null;
  const mid = (lo, hi) => Math.round((lo + hi) / 2 / 100) * 100;
  return { same: false,
    shinkansen: f.s ? { price: f.s[0], min: f.s[1] } : null,
    plane: f.p ? { price: mid(f.p[0], f.p[1]), lo: f.p[0], hi: f.p[1], min: f.p[2] } : null,
    bus: f.b ? { price: mid(f.b[0], f.b[1]), lo: f.b[0], hi: f.b[1], min: f.b[2] } : null };
}
// 早見表のセル: 往復交通費（新幹線があれば新幹線、無ければ飛行機の中間値）＋ビジホ1泊
export function hayamiCell(d, from, to) {
  const f = fareBetween(d, from, to);
  if (!f || f.same) return null;
  const t = f.shinkansen ? { price: f.shinkansen.price, plane: false } : f.plane ? { price: f.plane.price, plane: true } : null;
  if (!t) return null;
  return { total: t.price * 2 + d.AREAS[to].hotel.biz, plane: t.plane };
}
