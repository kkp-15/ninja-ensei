import assert from 'node:assert/strict';
import { loadData, fareBetween, hayamiCell } from '../scripts/extract_data.mjs';
const d = loadData();
// 出典: スマートEX発売額（のぞみ・通常期・指定席・2025-04-01時点）
assert.equal(d.FARE['tokyo-osaka'].s[0], 14520);
assert.equal(d.FARE['tokyo-nagoya'].s[0], 11100);
assert.equal(d.FARE['hiroshima-fukuoka'].s[0], 9430);
// 東京→大阪 新幹線 片道
assert.equal(fareBetween(d,'tokyo','osaka').shinkansen.price, 14520);
// 早見表: 東京発→大阪へ 1泊 = 14,520×2 + ビジホ12,000 = 41,040
assert.equal(hayamiCell(d,'tokyo','osaka').total, 41040);
// 東京→札幌は新幹線なし→飛行機中間値 (8000+22000)/2=15,000 → 30,000+9,500=39,500 ✈
assert.deepEqual(hayamiCell(d,'tokyo','sapporo'), { total: 39500, plane: true });
// 関東内は同一エリア扱い（在来線 800）
assert.deepEqual(fareBetween(d,'tokyo','saitama'), { same: true, local: 800 });
// 全FAREの手段が最低1つある・分の値がある
for (const [k,v] of Object.entries(d.FARE)) { assert.ok(v.s||v.p||v.b, k); for (const m of ['s','p','b']) if (v[m]) assert.ok(v[m].every(n=>Number.isInteger(n)&&n>0), k+m); }
// 全会場のエリアが存在する
for (const st of d.STADIUMS) assert.ok(d.AREAS[st.area], st.name);
// 早見表の静的HTMLがデータと一致する
import fs from 'node:fs';
const html = fs.readFileSync(new URL('../index.html', import.meta.url), 'utf8');
const tbody = html.match(/<table class="seo-tbl">[\s\S]*?<tbody>([\s\S]*?)<\/tbody>/)[1];
const cells = [...tbody.matchAll(/<td>([\d,]+)円/g)].map(m => Number(m[1].replace(/,/g,'')));
const cities = ['tokyo','nagoya','osaka','hiroshima','fukuoka','sendai','sapporo'];
const expect = [];
for (const to of cities) for (const from of cities) { if (from===to) continue; const c = hayamiCell(d,from,to); if (c) expect.push(c.total); }
assert.deepEqual(cells, expect, '早見表がデータと一致しない: scripts/build_hayami.mjs を実行する');
console.log('calc.test ok');
