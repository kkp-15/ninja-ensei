# 2026-09-19 チャット製 ensei.html を統一仕様に変換（1回限り。記録用に残す）
import re
p='index.html'; s=open(p,encoding='utf-8').read()
BASE='https://ensei.kkpwebninja.com/'
s=s.replace('<link rel="canonical" href="https://kkpwebninja.com/ensei/">','<link rel="canonical" href="'+BASE+'">\n<meta name="theme-color" content="#ff8a3d">\n<!-- WEBNINJA_UNIFIED_FAVICON -->\n<link rel="icon" type="image/png" sizes="32x32" href="/favicon.png">\n<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">\n<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">')
s=s.replace('<meta property="og:url" content="https://kkpwebninja.com/ensei/">','<meta property="og:url" content="'+BASE+'">\n<meta property="og:image" content="'+BASE+'ogp.png?d=20260919">\n<meta name="twitter:image" content="'+BASE+'ogp.png?d=20260919">')
s=s.replace('<meta property="og:site_name" content="kkpwebninja.com">','<meta property="og:site_name" content="遠征費計算ツール｜web忍者の砦">')
s=s.replace('https://kkpwebninja.com/ensei/',BASE)
s=s.replace('"author": {"@type": "Person", "name": "KKP", "url": "https://kkpwebninja.com/"}','"author": {"@type": "Organization", "name": "web忍者の砦", "url": "https://kkpwebninja.com/"}')
s=s.replace('<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;800;900&display=swap" rel="stylesheet">',
'''<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-2LM85GJN0L"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-2LM85GJN0L');
</script>
<!-- AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1298304917726270" crossorigin="anonymous"></script>''')
assert 'Person' not in s and 'kkpwebninja.com/ensei/' not in s and 'fonts.googleapis' not in s
css_new=open('scripts/style_v1.css',encoding='utf-8').read()
s=re.sub(r'<style>.*?</style>','<style>\n'+css_new+'</style>',s,flags=re.S)
s=s.replace('''<div class="hero">
  <h1>🧳 遠征費計算ツール<br><span style="font-size:13px;font-weight:700;opacity:.9">ライブ・野球・サッカー観戦の交通費＋ホテル代はいくら？</span></h1>
  <p>出発地と会場を選ぶだけ。交通費＋ホテル代の目安を3秒で概算</p>
</div>
<div class="pr-notice">本ページにはプロモーション（Agodaのアフィリエイト広告）が含まれます。</div>''',
'''<div class="hero">
  <h1>遠征費計算ツール<span>ライブ・野球・サッカー観戦の交通費＋ホテル代はいくら？</span></h1>
  <p>出発地と会場を選ぶだけ。新幹線・飛行機・夜行バス＋ホテル代の目安を概算します。</p>
</div>
<div class="pr-notice">更新日 2026-09-19 ｜ 本ページには広告（Agoda のアフィリエイト・A8.net）が含まれます。</div>''')
rep={'💰 遠征費を計算する':'遠征費を計算する','🔄 条件を変えて再計算':'条件を変えて再計算','📊 内訳（目安）':'内訳（目安）','🔄 移動手段を比べる（片道・1人）':'移動手段を比べる（片道・1人）','<b>⚠️ 金額はあくまで目安です</b>':'<b>金額はあくまで目安です</b>','💤 カプセル・格安':'カプセル・格安','🏨 ビジネスホテル':'ビジネスホテル','✨ ちょっと贅沢':'ちょっと贅沢','<div class="bd-name">🏨 ホテル代</div>':'<div class="bd-name">ホテル代</div>','<div class="bd-name">🚉 会場までの現地移動</div>':'<div class="bd-name">会場までの現地移動</div>','<div class="bd-name">🚄 交通費（往復）</div>':'<div class="bd-name">交通費（往復）</div>','<span class="pr-badge">PR</span>🏨 <span id="hero-cta-city">':'<span class="pr-badge">PR</span><span id="hero-cta-city">','<span>🏨 <span id="aff-city">東京</span>のホテルをAgodaで探す<small>ラッキー割引・ポイント還元あり</small></span>':'<span><span id="aff-city">東京</span>のホテルをAgodaで探す<small>実際の空室と価格を確認できます</small></span>','<h3>🎤 ライブ・コンサート遠征の費用を知りたい</h3>':'<h3>ライブ・コンサート遠征の費用を知りたい</h3>','<h3>⚾ プロ野球の遠征観戦</h3>':'<h3>プロ野球の遠征観戦</h3>','<h3>⚽ Jリーグ・サッカー観戦の遠征</h3>':'<h3>Jリーグ・サッカー観戦の遠征</h3>','<h3>🎭 舞台・イベント・推し活の遠征</h3>':'<h3>舞台・イベント・推し活の遠征</h3>','<h3>✈️ 旅行・出張の予算感を掴みたい</h3>':'<h3>旅行・出張の予算感を掴みたい</h3>','「🏙 都市のみ」':'「都市のみ」',"{id:'baseball', label:'⚾ 野球'}":"{id:'baseball', label:'野球'}","{id:'live',     label:'🎤 ライブ'}":"{id:'live',     label:'ライブ'}","{id:'soccer',   label:'⚽ サッカー'}":"{id:'soccer',   label:'サッカー'}","{id:'city',     label:'🏙 都市のみ'}":"{id:'city',     label:'都市のみ'}"}
for a,b in rep.items():
    assert a in s, a
    s=s.replace(a,b)
s=s.replace('rel="noopener sponsored"','rel="sponsored nofollow noopener"')
s=s.replace('<p>12球団の本拠地すべてに対応。球場ごとの詳しい早見表・アクセス・宿泊エリアは <a href="./enseihi.html">プロ野球遠征費計算ツール（12球場版）</a> にまとめています。</p>',
'<p>12球団の本拠地すべてに対応しています。優勝争いや CS 進出の状況は <a href="https://npb-magic.kkpwebninja.com/">プロ野球 優勝マジック・順位表</a> で確認できます。</p>')
s=s.replace('    <li><a href="./enseihi.html">プロ野球 遠征費計算ツール（12球場版）</a> — 球場別の早見表とアクセス情報つき</li>\n','')
s=s.replace('<li><a href="https://npb-magic.kkpwebninja.com/">プロ野球マジック点灯計算</a></li>','<li><a href="https://npb-magic.kkpwebninja.com/">プロ野球 優勝マジック・クリンチナンバー＆順位表</a> — 遠征する試合の優勝争いを確認</li>')
assert 'enseihi' not in s
s=s.replace('<button class="share" onclick="share()">𝕏 結果をシェア</button>',
'''<div class="share-row" id="share-row">
    <a id="share-x" href="#" target="_blank" rel="noopener">Xで共有</a>
    <a id="share-line" href="#" target="_blank" rel="noopener">LINEで送る</a>
    <button type="button" onclick="copyResult()">コピー</button>
  </div>
  <img src="https://www13.a8.net/0.gif?a8mat=4BCE3O+3O6AMA+4X1W+BW8O2" width="1" height="1" alt="" style="position:absolute;">''')
s=s.replace('  <div class="notice">\n    <b>金額はあくまで目安です</b>',
'''  <div class="kkp-ad">
    <div class="kkp-ad-label">広告</div>
    <ins class="adsbygoogle" style="display:block"
         data-ad-client="ca-pub-1298304917726270"
         data-ad-slot="2937937957"
         data-ad-format="rectangle"
         data-full-width-responsive="false"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
  </div>

  <div class="notice">
    <b>金額はあくまで目安です</b>''')
assert s.count('class="kkp-ad-label"')==1
old_footer=re.search(r'<div class="footer">.*?</div>\n',s,re.S).group(0)
s=s.replace(old_footer,open('scripts/footer_v1.html',encoding='utf-8').read())
s,n=re.subn(r'(?:// [^\n]*\n){3}const AGODA_CID = "1234567";',
"""// 宿の予約リンク: A8.net のアゴダ商品リンク（掲載サイト web忍者の砦）。飛び先は agoda.com の都市ページ（パラメータ無し）
const A8_AGODA = 'https://px.a8.net/svt/ejp?a8mat=4BCE3O+3O6AMA+4X1W+BW8O2&a8ejpredirect=';
const agodaLinkFor = slug => A8_AGODA + encodeURIComponent('https://www.agoda.com/ja-jp/city/' + slug + '.html');""",s); assert n==1, 'AGODA block'


for k,slug in [('sapporo','sapporo-jp'),('sendai','sendai-jp'),('tokyo','tokyo-jp'),('yokohama','yokohama-jp'),('chiba','chiba-jp'),('saitama','saitama-jp'),('nagoya','nagoya-jp'),('osaka','osaka-jp'),('hiroshima','hiroshima-jp'),('fukuoka','fukuoka-jp')]:
    s,n=re.subn(r"(  %s:\s*\{name:'[^']+',\s*hotel:\{[^}]+\}),\s*agodaCity:\d+\}"%k, r"\1, agoda:'%s'}"%slug, s); assert n==1,k
s,n=re.subn(r'const agodaUrl=`[^`]*`;','const agodaUrl=agodaLinkFor(area.agoda);',s); assert n==1
import sys
for tok in ('AGODA_CID','agodaCity'):
    for m in re.finditer(tok,s): print('残:',tok,repr(s[max(0,m.start()-60):m.start()+40]),file=sys.stderr)
assert 'AGODA_CID' not in s and 'agodaCity' not in s
_share=open('scripts/share_v1.js',encoding='utf-8').read()
s,n=re.subn(r'function share\(\)\{.*?\n\}\n',lambda m:_share,s,flags=re.S); assert n==1
a="  document.getElementById('page-input').classList.add('hidden');\n  document.getElementById('page-result').classList.remove('hidden');"
assert a in s
s=s.replace(a,"  updateShare();\n  gtag('event','ensei_calc',{from:AREAS[fromKey].name,to:st.name,genre:genre,nights:sel.nights,people:sel.people,trans:transUsed,total:total});\n"+a)
a="['aff-link','hero-cta','bd-link'].forEach(id=>document.getElementById(id).href=agodaUrl);"; assert a in s
s=s.replace(a,"['aff-link','hero-cta','bd-link'].forEach(id=>{const el=document.getElementById(id);el.href=agodaUrl;el.onclick=()=>gtag('event','ensei_cta',{choice:'hotel',from:id,city:area.name});});")
open(p,'w',encoding='utf-8').write(s)
print('ok; emoji left:',len(re.findall(r'[\U0001F300-\U0001FAFF\u2600-\u27BF]',s)),'lines:',s.count('\n'))
