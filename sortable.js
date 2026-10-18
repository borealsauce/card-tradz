/* Shared sortable tables (Grok Bot trackers). Click any header: asc/desc toggle with ▲/▼.
   Works on dynamically rendered tables via event delegation. Totals (tfoot, .total/.ft/.tot rows,
   or first cell TOTAL/ALL-TIME/GRAND) stay pinned at bottom. Group-label rows (fewer cells / colspan)
   keep their members: sorting happens within each group. Uses td[data-v] when present.
   Skip: th with own onclick, th.nosort, or table[data-nosort]. */
(function(){
  if(window.__sortableShared)return;window.__sortableShared=1;
  var st=document.createElement('style');
  st.textContent='table:not([data-nosort]) th:not(.nosort){cursor:pointer;user-select:none}th .srt-ar{font-size:.8em;opacity:.85;margin-left:3px}';
  (document.head||document.documentElement).appendChild(st);
  var MON={jan:1,feb:2,mar:3,apr:4,may:5,jun:6,jul:7,aug:8,sep:9,oct:10,nov:11,dec:12};
  function key(cell){
    if(!cell)return null;
    var raw=cell.dataset&&cell.dataset.v!=null?cell.dataset.v:cell.textContent;
    var s=String(raw).replace(/[▲▼]/g,'').trim();
    if(!s||s==='—'||s==='-'||s==='–'||/^n\/?a$/i.test(s))return null;
    var m;
    if((m=s.match(/^(\d{4})-(\d{2})(?:-(\d{2}))?/)))return {n:Date.UTC(+m[1],+m[2]-1,+(m[3]||1))};
    if((m=s.match(/^(\d{1,2})\/(\d{1,2})\/(\d{2,4})$/))){var y=+m[3];if(y<100)y+=2000;return {n:Date.UTC(y,+m[1]-1,+m[2])};}
    if((m=s.match(/^([A-Za-z]{3})[a-z]*\.? (\d{1,2}),? (\d{4})$/))&&MON[m[1].toLowerCase()])return {n:Date.UTC(+m[3],MON[m[1].toLowerCase()]-1,+m[2])};
    if((m=s.match(/^([A-Za-z]{3})[a-z]* (\d{4})$/))&&MON[m[1].toLowerCase()])return {n:Date.UTC(+m[2],MON[m[1].toLowerCase()]-1,1)};
    if((m=s.match(/^Q([1-4]) (\d{4})$/i)))return {n:Date.UTC(+m[2],(+m[1]-1)*3,1)};
    var t=s.replace(/[$,%x×\s]|USD/gi,'').replace(/^\+/,'').replace(/[−–]/g,'-');
    var neg=/^\(.*\)$/.test(t);if(neg)t=t.slice(1,-1);
    var mult=1;if((m=t.match(/^(-?[\d.]+)([KMB])$/i))){t=m[1];mult={k:1e3,m:1e6,b:1e9}[m[2].toLowerCase()];}
    if(/^-?\d*\.?\d+$/.test(t))return {n:parseFloat(t)*mult*(neg?-1:1)};
    return {s:s.toLowerCase()};
  }
  function pinned(r){
    if(r.parentElement&&r.parentElement.tagName==='TFOOT')return true;
    if(/(^|\s)(total|totals|ft|tot|sum|grand|pinned)(\s|$)/i.test(r.className))return true;
    var c=r.cells[0];return !!c&&/^\s*(TOTAL|TOTALS|ALL-TIME|GRAND TOTAL)\b/i.test(c.textContent);
  }
  document.addEventListener('click',function(e){
    var th=e.target.closest&&e.target.closest('th');if(!th||th.onclick||th.classList.contains('nosort'))return;
    var tb=th.closest('table');if(!tb||tb.hasAttribute('data-nosort'))return;
    var hr=th.parentElement;if(hr.parentElement.tagName==='TFOOT')return;
    var ci=0;for(var k=0;k<hr.cells.length&&hr.cells[k]!==th;k++)ci+=hr.cells[k].colSpan||1;
    var ncol=0;for(k=0;k<hr.cells.length;k++)ncol+=hr.cells[k].colSpan||1;
    var dir=th.dataset.sdir==='asc'?'desc':'asc',m=dir==='asc'?1:-1;
    tb.querySelectorAll('th').forEach(function(x){delete x.dataset.sdir;var a=x.querySelector('.srt-ar');if(a)a.remove();});
    th.dataset.sdir=dir;var ar=document.createElement('span');ar.className='srt-ar';ar.textContent=dir==='asc'?'▲':'▼';th.appendChild(ar);
    var bodies=tb.tBodies.length?[].slice.call(tb.tBodies):[tb];
    bodies.forEach(function(body){
      var all=[].slice.call(body.rows).filter(function(r){return r!==hr&&!(r.cells.length&&r.cells[0].tagName==='TH'&&!r.querySelector('td'));});
      var pins=[],groups=[{head:null,rows:[]}];
      all.forEach(function(r){
        if(pinned(r)){pins.push(r);return;}
        var w=0;for(var j=0;j<r.cells.length;j++)w+=r.cells[j].colSpan||1;
        if(r.cells.length===1&&ncol>1)groups.push({head:r,rows:[]});else groups[groups.length-1].rows.push(r);
      });
      function cellAt(r){var x=0;for(var j=0;j<r.cells.length;j++){if(x===ci)return r.cells[j];x+=r.cells[j].colSpan||1;}return null;}
      groups.forEach(function(g){
        g.rows.sort(function(a,b){var A=key(cellAt(a)),B=key(cellAt(b));
          if(!A&&!B)return 0;if(!A)return 1;if(!B)return -1;
          if(A.n!=null&&B.n!=null)return (A.n-B.n)*m;
          return String(A.s!=null?A.s:A.n).localeCompare(String(B.s!=null?B.s:B.n),undefined,{numeric:true})*m;});
        if(g.head)body.appendChild(g.head);g.rows.forEach(function(r){body.appendChild(r);});
      });
      pins.forEach(function(r){body.appendChild(r);});
    });
  },false);
})();
