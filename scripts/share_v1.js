function shareText(){
  if(!last)return '';
  return `${last.from} → ${last.st.name}\n${last.nights?last.nights+'泊':'日帰り'}・${last.people}人で 約${fmt(last.total)}円（交通費＋ホテル代の目安）\n遠征費計算ツール`;
}
function updateShare(){
  const u='https://ensei.kkpwebninja.com/?d=20260919';
  const t=shareText();
  document.getElementById('share-x').href='https://twitter.com/intent/tweet?text='+encodeURIComponent(t)+'&url='+encodeURIComponent(u)+'&via=kkp_webninja&hashtags='+encodeURIComponent('遠征費');
  document.getElementById('share-line').href='https://social-plugins.line.me/lineit/share?url='+encodeURIComponent(u)+'&text='+encodeURIComponent(t);
}
function copyResult(){
  const t=shareText()+'\nhttps://ensei.kkpwebninja.com/';
  navigator.clipboard.writeText(t).then(()=>alert('コピーしました'));
}
