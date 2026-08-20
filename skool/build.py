import json, html

data = json.load(open('contenido-skool.json', encoding='utf-8'))

# Estado real de cada adjunto (lo escribe componer.py al repartir los archivos).
try:
    estado = json.load(open('estado-adjuntos.json', encoding='utf-8'))
except FileNotFoundError:
    estado = {}
for m in data:
    for i, l in enumerate(m['lecciones'], 1):
        for a in l['adjuntos']:
            e = estado.get(f'{m["codigo"]}|{i}|{a["nombre"]}')
            if not e:
                continue
            if e['est'] == 'listo':
                a['estado'], a['ruta'] = 'listo', f'adjuntos-skool/{e["carp"]}/{e["arch"]}'
            elif e['est'].startswith('FALTA'):
                a['estado'] = 'falta'
            elif e['est'].startswith('ya subido'):
                a['estado'], a['ruta'] = 'repetido', e['est']
            else:
                a['estado'] = 'enlace'

payload = json.dumps(data, ensure_ascii=False)

CSS = """
:root{
  --app:#0b0b0d; --panel:#161619; --panel2:#1d1d21; --line:#2a2a30;
  --ink:#ececed; --ink2:#9b9ba3; --ink3:#6e6e77;
  --blue:#3d7bfd; --green:#28c76f; --amber:#e0a33e;
  --cover1:#1c2145; --cover2:#0a0a12;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
body{background:var(--app);color:var(--ink);
  font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}
button{font:inherit;color:inherit;background:none;border:none;cursor:pointer}
a{color:var(--blue);text-decoration:none}

.topbar{position:sticky;top:0;z-index:20;background:rgba(11,11,13,.92);backdrop-filter:blur(8px);
  border-bottom:1px solid var(--line);display:flex;align-items:center;gap:14px;padding:11px 20px}
.brand{display:flex;align-items:center;gap:9px;font-weight:700;letter-spacing:.14em;font-size:11px;text-transform:uppercase}
.brand i{width:22px;height:22px;border-radius:6px;background:var(--blue);display:inline-block}
.tag{font-size:11px;color:var(--ink3);border:1px solid var(--line);border-radius:99px;padding:3px 9px}
.topbar .spacer{flex:1}
.crumb{font-size:13px;color:var(--ink2)}
.crumb b{color:var(--ink)}

.wrap{max-width:1180px;margin:0 auto;padding:26px 20px 60px}
.hint{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--blue);
  border-radius:10px;padding:13px 16px;color:var(--ink2);font-size:13.5px;margin-bottom:24px}
.hint b{color:var(--ink)}
.hint2{margin-top:10px;padding-top:9px;border-top:1px solid var(--line);font-size:12.5px;color:var(--ink2);display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.hint2 code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:11.5px;color:var(--ink)}

.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(288px,1fr));gap:20px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;
  text-align:left;transition:transform .12s ease,border-color .12s ease;display:flex;flex-direction:column}
.card:hover{transform:translateY(-2px);border-color:#3a3a44}
.cover{aspect-ratio:16/8.4;background:linear-gradient(150deg,var(--cover1),var(--cover2));
  padding:16px 20px;display:flex;flex-direction:column;justify-content:space-between}
.cover .eyebrow{font-size:9.5px;letter-spacing:.2em;color:#c9cbe0;text-transform:uppercase;font-weight:700}
.cover .word{font-size:38px;font-weight:800;letter-spacing:-.02em;line-height:1}
.cover .word span{color:var(--blue)}
.cbody{padding:14px 16px 16px;display:flex;flex-direction:column;gap:8px;flex:1}
.ctitle{font-size:14.5px;font-weight:650;display:flex;align-items:center;gap:8px}
.dot{width:13px;height:13px;border-radius:50%;border:2px solid var(--ink3);flex:none}
.cdesc{font-size:12.8px;color:var(--ink2);flex:1}
.cmeta{display:flex;gap:10px;font-size:11.5px;color:var(--ink3);padding-top:2px}
.bar{height:6px;border-radius:99px;background:#26262c;overflow:hidden}
.bar i{display:block;height:100%;width:0;background:var(--green)}

.course{display:grid;grid-template-columns:296px 1fr;gap:22px;align-items:start}
.side{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:14px;position:sticky;top:76px}
.side h3{font-size:14px;font-weight:650;margin-bottom:3px}
.side .sub{font-size:11.5px;color:var(--ink3);margin-bottom:12px}
.lesson{width:100%;display:flex;align-items:center;gap:10px;padding:9px 10px;border-radius:9px;
  font-size:13.4px;color:var(--ink2);text-align:left;line-height:1.35}
.lesson:hover{background:#212127;color:var(--ink)}
.lesson.on{background:#23232a;color:var(--ink);box-shadow:inset 3px 0 0 var(--amber)}
.lesson .em{flex:none;font-size:14px}
.lesson .tx{flex:1}
.lesson .ck{width:15px;height:15px;border-radius:50%;border:2px solid #3a3a44;flex:none}

.main{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:24px 26px 30px;min-width:0}
.main h1{font-size:22px;font-weight:700;letter-spacing:-.01em;display:flex;align-items:center;gap:10px}
.lmeta{color:var(--ink3);font-size:12.5px;margin:6px 0 18px}
.video{aspect-ratio:16/9;border-radius:11px;border:1px dashed #3a3a44;background:
  radial-gradient(120% 120% at 50% 0%,#1a1a20,#111116);display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:8px;color:var(--ink3);font-size:13px;margin-bottom:20px}
.video .play{width:54px;height:54px;border-radius:50%;border:1px solid #3a3a44;display:grid;place-items:center;font-size:17px;color:var(--ink2)}

.desc{font-size:14.4px;color:#dcdce0}
.desc p{margin:0 0 11px}
.desc strong{color:var(--ink);font-weight:650}
.desc ul{margin:0 0 13px;padding-left:19px}
.desc li{margin-bottom:5px}
.desc em{color:var(--ink2);font-style:normal}

.block{margin-top:22px;border-top:1px solid var(--line);padding-top:18px}
.block h4{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink3);margin-bottom:11px}
.att{display:flex;align-items:center;gap:11px;background:var(--panel2);border:1px solid var(--line);
  border-radius:10px;padding:11px 13px;margin-bottom:8px}
.att .ic{width:34px;height:34px;border-radius:8px;display:grid;place-items:center;font-size:10px;
  font-weight:800;letter-spacing:.03em;flex:none}
.ic.pdf{background:#3a1f22;color:#f08a8a}.ic.csv{background:#1f3226;color:#79d99e}
.ic.enlace{background:#1f2a3d;color:#8ab4f8}.ic.formulario{background:#332a17;color:#e3bd6a}
.att .txt{min-width:0}
.att .nm{font-size:13.4px;font-weight:600}
.att .nt{font-size:12px;color:var(--ink3)}
.att .ruta{font-size:11.5px;color:var(--ink3);font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.sello{display:inline-block;vertical-align:1px;font-size:10px;font-weight:700;letter-spacing:.06em;
  text-transform:uppercase;border-radius:99px;padding:2px 8px;white-space:nowrap}
.sello.ok{background:#12301f;color:#6fd79b;border:1px solid #1e5237}
.sello.no{background:#33240f;color:#e0a33e;border:1px solid #5a3f16}
.sello.rep{background:#1c1c22;color:var(--ink2);border:1px solid var(--line);text-transform:none;letter-spacing:0;font-weight:600}
.sello.link{background:#141f33;color:#8ab4f8;border:1px solid #23375c}
.none{font-size:13px;color:var(--ink3);font-style:italic}

.rec{background:#181410;border:1px solid #3a2f1c;border-radius:10px;padding:12px 14px;font-size:13px;color:#d9c79b}
.rec b{color:#e0a33e}

.acts{display:flex;gap:9px;flex-wrap:wrap;margin-top:20px}
.btn{border:1px solid var(--line);background:var(--panel2);border-radius:9px;padding:8px 14px;font-size:13px;font-weight:600}
.btn:hover{border-color:#45454f}
.btn.pri{background:var(--blue);border-color:var(--blue);color:#fff}
.btn.pri:hover{filter:brightness(1.08)}
.btn.wide{display:block;width:100%;margin-top:14px;text-align:center}
.sidenote{font-size:11px;line-height:1.45;color:var(--ink3);margin-top:8px}
.nav{display:flex;justify-content:space-between;gap:10px;margin-top:26px;border-top:1px solid var(--line);padding-top:16px}

.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(20px);opacity:0;
  background:var(--green);color:#06210f;font-weight:700;font-size:13.5px;padding:10px 18px;border-radius:99px;
  transition:.22s ease;pointer-events:none;z-index:50}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}

@media (max-width:900px){
  .course{grid-template-columns:1fr}
  .side{position:static}
  .main{padding:20px}
  .cover .word{font-size:32px}
}
"""

JS = r"""
const DATA = __PAYLOAD__;
const ICON = {PDF:'pdf', CSV:'csv', 'Enlace':'enlace', 'Formulario':'formulario'};
let cur = null, curL = 0;

function md(t){
  const lines = t.split('\n'); let out=''; let ul=false;
  for (let ln of lines){
    ln = ln.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
           .replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>')
           .replace(/\*(.+?)\*/g,'<em>$1</em>');
    if (ln.trim().startsWith('- ')){
      if(!ul){out+='<ul>';ul=true;}
      out += '<li>'+ln.trim().slice(2)+'</li>';
    } else {
      if(ul){out+='</ul>';ul=false;}
      if(ln.trim()) out += '<p>'+ln+'</p>';
    }
  }
  if(ul) out+='</ul>';
  return out;
}

function home(){
  cur = null;
  document.getElementById('crumb').innerHTML = '<b>Classroom</b>';
  const cards = DATA.map((m,i)=>`
    <button class="card" onclick="openCourse(${i})">
      <div class="cover">
        <div class="eyebrow">AILINK ÉLITE.</div>
        <div class="word">${m.palabraTarjeta}<span>.</span></div>
      </div>
      <div class="cbody">
        <div class="ctitle"><span class="dot"></span>${m.nombreCurso}</div>
        <div class="cdesc">${m.descripcionCurso}</div>
        <div class="cmeta"><span>${m.semanas}</span><span>·</span><span>${m.lecciones.length} lecciones</span></div>
        <div class="bar"><i></i></div>
      </div>
    </button>`).join('');
  document.getElementById('app').innerHTML = `
    <div class="hint"><b>Maqueta de tu aula.</b> Así queda el programa montado en Skool: 7 cursos, 54 lecciones, cada una con su vídeo, su descripción y sus adjuntos. Entra en un curso y usa <b>Copiar descripción</b> para pegarla en el Skool real.
      <div class="hint2">Cada adjunto lleva su sello: <span class="sello ok">listo para subir</span> ya está en <code>adjuntos-skool/</code> con la ruta debajo · <span class="sello no">pendiente de diseño</span> aún no existe · <span class="sello rep">ya subido en LX</span> no se vuelve a subir.</div>
    </div>
    <div class="grid">${cards}</div>`;
  window.scrollTo(0,0);
}

function openCourse(i, l){
  cur = i; curL = l || 0;
  const m = DATA[i];
  document.getElementById('crumb').innerHTML = `<a href="#" onclick="home();return false">Classroom</a> &nbsp;›&nbsp; <b>${m.palabraTarjeta}</b>`;
  document.getElementById('app').innerHTML = `<div class="course">
      <aside class="side">
        <h3>${m.palabraTarjeta}</h3>
        <div class="sub">${m.semanas} · ${m.lecciones.length} lecciones</div>
        <div id="list"></div>
        <button class="btn wide" onclick="copiarCurso()">Copiar el curso entero</button>
        <div class="sidenote">Título, descripción y adjuntos de las ${m.lecciones.length} lecciones, en un solo bloque de texto.</div>
      </aside>
      <section class="main" id="main"></section>
    </div>`;
  paint();
  window.scrollTo(0,0);
}

function paint(){
  const m = DATA[cur], L = m.lecciones[curL];
  document.getElementById('list').innerHTML = m.lecciones.map((x,j)=>`
    <button class="lesson ${j===curL?'on':''}" onclick="pick(${j})">
      <span class="em">${x.emoji}</span><span class="tx">${x.titulo}</span><span class="ck"></span>
    </button>`).join('');

  const att = L.adjuntos.length
    ? L.adjuntos.map(a=>{
        const sello = a.estado==='listo' ? '<span class="sello ok">listo para subir</span>'
          : a.estado==='falta' ? '<span class="sello no">pendiente de diseño</span>'
          : a.estado==='repetido' ? `<span class="sello rep">${a.ruta}</span>`
          : a.estado==='enlace' ? '<span class="sello link">va como enlace</span>' : '';
        const ruta = a.estado==='listo' ? `<br><span class="ruta">${a.ruta}</span>` : '';
        return `<div class="att">
        <span class="ic ${ICON[a.tipo]||'pdf'}">${a.tipo==='Formulario'?'FORM':a.tipo==='Enlace'?'LINK':a.tipo}</span>
        <span class="txt"><span class="nm">${a.nombre}</span> ${sello}<br><span class="nt">${a.nota}</span>${ruta}</span></div>`;
      }).join('')
    : '<div class="none">Esta lección no lleva adjuntos.</div>';

  const rec = L.pantallaReal
    ? `<div class="block"><h4>Nota de grabación · solo la ves tú</h4>
        <div class="rec"><b>Comparte pantalla:</b> ${L.pantallaReal}</div></div>` : '';

  document.getElementById('main').innerHTML = `
    <h1><span>${L.emoji}</span> ${L.titulo}</h1>
    <div class="lmeta">${m.codigo} · ${L.id} · vídeo de ${L.duracion}</div>
    <div class="video"><div class="play">▶</div><div>Vídeo por grabar — ${L.duracion}</div></div>
    <div class="desc">${md(L.descripcion)}</div>
    <div class="block"><h4>Adjuntos de la lección</h4>${att}</div>
    ${rec}
    <div class="acts">
      <button class="btn pri" onclick="copiar('desc')">Copiar descripción</button>
      <button class="btn" onclick="copiar('titulo')">Copiar título</button>
      <button class="btn" onclick="copiar('adjuntos')">Copiar lista de adjuntos</button>
    </div>
    <div class="nav">
      <button class="btn" onclick="pick(${curL-1})" ${curL===0?'disabled style=opacity:.35':''}>← Anterior</button>
      <button class="btn" onclick="pick(${curL+1})" ${curL===m.lecciones.length-1?'disabled style=opacity:.35':''}>Siguiente →</button>
    </div>`;
}

function pick(j){
  const m = DATA[cur];
  if (j<0 || j>=m.lecciones.length) return;
  curL = j; paint();
  document.getElementById('main').scrollIntoView({behavior:'smooth', block:'start'});
}

function aviso(txt){
  const el = document.getElementById('toast');
  el.textContent = txt;
  el.classList.add('on'); setTimeout(()=>el.classList.remove('on'), 1800);
}

function alPortapapeles(t, ok){
  const viejo = () => {
    const ta = document.createElement('textarea');
    ta.value = t; ta.setAttribute('readonly','');
    ta.style.cssText = 'position:fixed;top:-9999px';
    document.body.appendChild(ta); ta.select();
    let bien = false;
    try { bien = document.execCommand('copy'); } catch(e) { bien = false; }
    document.body.removeChild(ta);
    aviso(bien ? ok : 'No se ha podido copiar. Selecciona el texto a mano.');
  };
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(t).then(()=>aviso(ok)).catch(viejo);
  } else { viejo(); }
}

function copiar(qué){
  const L = DATA[cur].lecciones[curL];
  let t = L.descripcion, ok = 'Descripción copiada';
  if (qué==='titulo'){ t = L.emoji + ' ' + L.titulo; ok = 'Título copiado'; }
  if (qué==='adjuntos'){ t = L.adjuntos.map(a=>`${a.nombre} — ${a.nota}`).join('\n') || 'Sin adjuntos'; ok = 'Adjuntos copiados'; }
  alPortapapeles(t, ok);
}

function copiarCurso(){
  const m = DATA[cur];
  const bloques = m.lecciones.map((L,i)=>{
    const ad = L.adjuntos.length
      ? L.adjuntos.map(a=>`- ${a.nombre} — ${a.nota}`).join('\n')
      : '- (sin adjuntos)';
    return [
      `━━━ LECCIÓN ${i+1} de ${m.lecciones.length} ━━━`,
      `TÍTULO: ${L.emoji} ${L.titulo}`,
      `VÍDEO: ${L.duracion}`,
      ``,
      `DESCRIPCIÓN:`,
      L.descripcion,
      ``,
      `ADJUNTOS A SUBIR:`,
      ad,
      L.pantallaReal ? `\nNOTA DE GRABACIÓN (no publicar): ${L.pantallaReal}` : ''
    ].join('\n');
  }).join('\n\n');
  alPortapapeles(`CURSO: ${m.nombreCurso}\nPORTADA: ${m.palabraTarjeta}\n${m.semanas} · ${m.lecciones.length} lecciones\n\n${bloques}`,
    `Curso entero copiado (${m.lecciones.length} lecciones)`);
}

home();
"""

CUERPO = f"""<title>Aula AILINK Élite</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;650;700;800&display=swap">
<style>{CSS}</style>
<header class="topbar">
  <div class="brand"><i></i> AILINK Élite</div>
  <span class="tag">maqueta</span>
  <div class="spacer"></div>
  <div class="crumb" id="crumb"></div>
</header>
<main class="wrap" id="app"></main>
<div class="toast" id="toast"></div>
<script>{JS.replace('__PAYLOAD__', payload)}</script>"""

HTML = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
{CUERPO}
</body>
</html>"""

open('aula-ailink.html','w',encoding='utf-8').write(HTML)
open('aula-ailink-web.html','w',encoding='utf-8').write(CUERPO)
print('OK', len(HTML), 'bytes ·', len(CUERPO), 'bytes (web)')
