// 早見表（主要7都市・1泊2日・1人）を運賃データから生成して index.html の <tbody> を書き換える
import fs from 'node:fs';
import { loadData, hayamiCell } from './extract_data.mjs';
const p = new URL('../index.html', import.meta.url);
const d = loadData(p);
const cities = ['tokyo','nagoya','osaka','hiroshima','fukuoka','sendai','sapporo'];
const fmt = n => n.toLocaleString('ja-JP');
const rows = cities.map(to => {
  const cells = cities.map(from => {
    if (from === to) return '<td style="color:#9CA3AF">—</td>';
    const c = hayamiCell(d, from, to);
    if (!c) return '<td style="color:#9CA3AF">—</td>';
    return `<td>${fmt(c.total)}円<small>${c.plane ? '✈' : ''}</small></td>`;
  }).join('');
  return `<tr><th>${d.AREAS[to].name}へ<br><small>ビジホ約${fmt(d.AREAS[to].hotel.biz)}円</small></th>${cells}</tr>`;
}).join('\n');
let html = fs.readFileSync(p, 'utf8');
const before = html;
html = html.replace(/(<table class="seo-tbl">[\s\S]*?<tbody>\n)[\s\S]*?(\n<\/tbody>)/, `$1${rows}$2`);
if (html === before) throw new Error('tbody not replaced');
fs.writeFileSync(p, html);
console.log('hayami rebuilt:', rows.split('\n').length, 'rows');
