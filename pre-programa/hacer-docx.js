const d = require('docx');
const {Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
       BorderStyle, AlignmentType, HeadingLevel, PageBreak, HeightRule, VerticalAlign} = d;

const COBALTO='2743D0', TINTA='101010', GRIS='55554F', AMBAR='A35C0A', CAB='EDEDE8', LINEA='C9C9C2';
const ANCHO=10106, F='Arial';
const b=(c=LINEA)=>({style:BorderStyle.SINGLE,size:6,color:c});
const bordes=(c=LINEA)=>({top:b(c),bottom:b(c),left:b(c),right:b(c)});

const p=(txt,o={})=>new Paragraph({spacing:{after:o.after??120,before:o.before??0},
  alignment:o.align, children:[new TextRun({text:txt,font:F,size:o.size??21,bold:o.bold,
  italics:o.it,color:o.color??TINTA})]});

const rico=(partes,o={})=>new Paragraph({spacing:{after:o.after??120,before:o.before??0},
  children:partes.map(x=>new TextRun({text:x[0],font:F,size:o.size??21,bold:x[1],
  italics:x[2],color:o.color??TINTA}))});

const h1=t=>new Paragraph({spacing:{after:60},heading:HeadingLevel.HEADING_1,
  children:[new TextRun({text:t,font:F,size:40,bold:true,color:TINTA})]});
const h2=(n,t)=>new Paragraph({spacing:{before:280,after:100},heading:HeadingLevel.HEADING_2,
  children:[new TextRun({text:n+'  ',font:F,size:26,bold:true,color:COBALTO}),
            new TextRun({text:t,font:F,size:26,bold:true,color:TINTA})]});
const h3=t=>new Paragraph({spacing:{before:200,after:60},heading:HeadingLevel.HEADING_3,
  children:[new TextRun({text:t,font:F,size:22,bold:true,color:TINTA})]});

// tabla con cabecera + n filas vacías
function tabla(cols, anchos, n, alto){
  const cabecera=new TableRow({tableHeader:true, children:cols.map((c,i)=>new TableCell({
    width:{size:anchos[i],type:WidthType.DXA}, borders:bordes(),
    shading:{type:ShadingType.CLEAR,fill:CAB,color:'auto'},
    margins:{top:60,bottom:60,left:90,right:90},
    children:[new Paragraph({spacing:{after:0},children:[new TextRun({text:c.toUpperCase(),
      font:F,size:15,bold:true,color:GRIS})]})]}))});
  const filas=[...Array(n)].map(()=>new TableRow({height:{value:alto,rule:HeightRule.ATLEAST},
    children:anchos.map(w=>new TableCell({width:{size:w,type:WidthType.DXA},borders:bordes(),
      margins:{top:60,bottom:60,left:90,right:90},children:[p('',{after:0})]}))}));
  return new Table({width:{size:ANCHO,type:WidthType.DXA},columnWidths:anchos,
    rows:[cabecera,...filas]});
}

// tabla de campos: etiqueta | hueco
function campos(pares){
  const A=[5400,4706];
  return new Table({width:{size:ANCHO,type:WidthType.DXA},columnWidths:A,
    rows:pares.map(([et,nota])=>new TableRow({height:{value:620,rule:HeightRule.ATLEAST},
      children:[
        new TableCell({width:{size:A[0],type:WidthType.DXA},borders:bordes(),
          margins:{top:70,bottom:70,left:110,right:90},verticalAlign:VerticalAlign.CENTER,
          children:[rico([[et,true]],{after:nota?40:0,size:20}),
            ...(nota?[p(nota,{it:true,size:17,color:GRIS,after:0})]:[])]}),
        new TableCell({width:{size:A[1],type:WidthType.DXA},borders:bordes(),
          margins:{top:70,bottom:70,left:110,right:90},children:[p('',{after:0})]})]}))});
}

// bloque destacado (fondo de color, texto blanco o con marco)
function bloque(hijos,{fondo,marco}={}){
  return new Table({width:{size:ANCHO,type:WidthType.DXA},columnWidths:[ANCHO],
    rows:[new TableRow({children:[new TableCell({
      width:{size:ANCHO,type:WidthType.DXA},
      shading:fondo?{type:ShadingType.CLEAR,fill:fondo,color:'auto'}:undefined,
      borders:marco?bordes(marco):bordes(fondo||'FFFFFF'),
      margins:{top:200,bottom:200,left:220,right:220},
      children:hijos})]})]});
}

const linea=()=>new Paragraph({spacing:{before:220,after:0},
  border:{bottom:{style:BorderStyle.SINGLE,size:6,color:TINTA}},children:[new TextRun({text:' ',font:F,size:21})]});

const casilla=t=>rico([['☐   ',false],[t,false]],{after:140,size:21});
const casillaB=(neg,resto)=>new Paragraph({spacing:{after:140},children:[
  new TextRun({text:'☐   ',font:F,size:21}),
  new TextRun({text:neg+' ',font:F,size:21,bold:true}),
  new TextRun({text:resto,font:F,size:21})]});

const doc=new Document({
  styles:{default:{document:{run:{font:F,size:21,color:TINTA}}}},
  sections:[{
    properties:{page:{margin:{top:850,right:900,bottom:800,left:900}}},
    children:[
      h1('Antes del día 1'),
      p('Tu carpeta de materia prima. 45-60 minutos con un bolígrafo o el teclado, más un cuaderno abierto hasta que empieces.',{it:true,color:GRIS,after:240}),

      bloque([
        p('Aquí se recoge. No se decide.',{bold:true,size:28,color:'FFFFFF',after:120}),
        rico([['Cuando empieces vas a elegir un micro-nicho, construir una oferta y ponerle precio. Esas tres decisiones tienen un método, y están dentro del programa por una razón: cada una depende de la anterior, y si las tomas en desorden se caen todas. ',false],
              ['Hoy traes los ingredientes; el día 1 se cocina.',true],
              [' Si te adelantas a cocinar, lo más probable es que tengas que tirarlo.',false]],{color:'FFFFFF',size:19,after:0})
      ],{fondo:COBALTO}),

      p('',{after:200}),
      p('Lo que sí puedes hacer hoy es tener los datos encima de la mesa. Nadie decide bien sin materia prima, y la tuya está repartida entre tu memoria, tu agenda y tu lista de contactos. Sacarla lleva una hora, y es una hora que no vas a tener que gastar después.'),

      h2('1','La entrevista'),
      p('Contéstala del tirón, sin pulir. Nadie va a leer esto: cuanto más crudo, más útil.'),

      h3('A. Tu vida laboral, en hechos'),
      p('Una fila por cada empleo, negocio propio, prácticas, voluntariado, negocio familiar o responsabilidad seria. Incluye lo que te parezca irrelevante: el bar de tus padres, el verano en el almacén, los tres meses en el call center.'),
      rico([['No escribas el puesto. Escribe lo que pasaba.',true],[' «Administración» no dice nada; «recibía facturas por correo, las cotejaba con los albaranes y perseguía a los que no pagaban» lo dice todo.',false]],{after:160}),
      tabla(['Dónde y cuándo','Qué hacías de verdad, día a día','Qué se rompía o se atascaba ahí'],[2450,4200,3456],6,850),

      new Paragraph({children:[new PageBreak()]}),

      h3('B. Los mundos que conoces por dentro'),
      p('Sectores donde has trabajado, donde trabaja tu familia, donde eres cliente habitual o donde sabes cómo funcionan las cosas por dentro. Un gimnasio, una peluquería, un taller, un despacho, una clínica, una obra.'),
      rico([['Lo que interesa no es el sector: es el detalle que solo sabe alguien de dentro.',true]],{after:160}),
      tabla(['El mundo','Cómo lo conozco','Un detalle que la gente de fuera no sabe'],[2700,2900,4506],4,850),

      h3('C. Tu gente'),
      p('Personas que conoces —aunque sea de lejos— que tienen un negocio, dirigen uno o deciden en uno.'),
      rico([['Esto no es una lista para escribirles. No les escribas.',true],[' Todavía no tienes nada que ofrecerles, y un contacto quemado no vuelve.',false]],{after:160}),
      tabla(['Persona','Su negocio','¿Cómo de cerca? (mucha / media / poca)'],[3500,4100,2506],7,620),

      new Paragraph({children:[new PageBreak()]}),

      h3('D. Tu realidad, sin maquillar'),
      campos([
        ['Horas reales que puedes dedicar a la semana','Las que ya tienes libres, no las que te gustaría tener.'],
        ['En qué días y franjas caen',null],
        ['Presupuesto con el que cuentas para arrancar, sin que te duela',null],
        ['¿Hay alguien alrededor que pueda echarte una mano?','Socio, pareja, amigo del sector, familiar con negocio.']
      ]),
      p('',{after:160}),
      rico([['¿Qué sabes hacer con un ordenador?',true],['   (marca lo que sea verdad)',false]],{after:140}),
      casilla('Me apaño con lo normal'),
      casilla('He tocado alguna herramienta de automatización'),
      casilla('He programado algo alguna vez'),
      casilla('Programo'),

      h3('E. Lo que no estás dispuesto a hacer'),
      p('Lo que sabes que no quieres, aunque funcione: horarios, tipo de cliente, tipo de trabajo, viajar, estar disponible los fines de semana.'),
      linea(), linea(), linea(),

      h2('3','Preparativos de veinte minutos'),
      p('Nada de configurar: solo dejar la puerta abierta.'),
      casillaB('El ordenador.','Comprueba que enciende, que tienes espacio libre y que la conexión aguanta una videollamada de una hora.'),
      casillaB('Un sitio para tus documentos.','Una carpeta en el ordenador o en la nube, con tu nombre y la fecha.'),
      casillaB('Una hora fija en el calendario.','Bloquea desde hoy tus sesiones de las próximas dos semanas, con aviso. Que exista el hueco antes de necesitarlo.'),
      casillaB('Guarda esta carpeta a mano.','El día 1 la vas a abrir.'),
      rico([['Lo que NO hay que instalar ni contratar todavía: ',true],['ninguna herramienta, ningún dominio, ninguna suscripción. Todo eso se monta dentro del programa, en su momento y con criterio. Comprar antes de saber qué necesitas es la forma más rápida de gastar dinero en algo que luego no usas.',false]],{it:true,size:18,color:GRIS,before:120}),

      new Paragraph({children:[new PageBreak()]}),

      h2('2','El diario de fricciones'),
      rico([['A partir de hoy, lleva esta hoja o el móvil a mano y ',false],['apunta cada vez que veas o escuches a alguien quejarse de cómo funciona su negocio',true],['. En la peluquería, en el grupo de WhatsApp del barrio, en la comida del domingo, en una reseña de Google que leas por casualidad.',false]]),
      p('No busques nada concreto. Solo apunta. Con cinco te sobra para empezar; si juntas diez, llegas con ventaja.',{after:160}),
      tabla(['Día','Dónde lo oí o lo vi','La queja, con sus palabras','Qué negocio era'],[1100,2500,4300,2206],10,780),

      new Paragraph({children:[new PageBreak()]}),

      bloque([
        p('4 · Lo que no debes hacer estos días',{bold:true,size:26,color:AMBAR,after:100}),
        p('Esto vale tanto como todo lo anterior.',{size:19,after:200}),
        p('No elijas a quién le vas a vender.',{bold:true,after:40}),
        p('Vas a tener la tentación de decidir «me voy a dedicar a los dentistas». Espera: hay un método para elegirlo y usa datos que aún no has recogido.',{size:19,after:180}),
        p('No diseñes tu oferta ni le pongas precio.',{bold:true,after:40}),
        p('Es la parte que más apetece y la que más caro sale hacer a ojo.',{size:19,after:180}),
        p('No escribas a ningún negocio.',{bold:true,after:40}),
        p('Ni un mensaje, ni un email, ni un «oye, estoy montando una cosa». Cada contacto que gastas ahora es uno que no tendrás cuando tengas algo real que enseñar.',{size:19,after:180}),
        p('No te pongas a estudiar por tu cuenta.',{bold:true,after:40}),
        p('Ni cursos, ni vídeos, ni newsletters de negocio. Vas a llegar con la cabeza llena de ideas de doce sitios distintos que se contradicen entre sí, y el primer trabajo del programa será vaciártela. Empieza con la cabeza limpia: es una ventaja, no una carencia.',{size:19,after:0})
      ],{marco:AMBAR}),

      h2('5','Qué pasa con todo esto el día 1'),
      p('Nada de lo que has escrito se queda en un cajón.',{after:160}),
      new Table({width:{size:ANCHO,type:WidthType.DXA},columnWidths:[4500,5606],
        rows:[
          new TableRow({tableHeader:true,children:['Lo que traes','Dónde se usa'].map((c,i)=>
            new TableCell({width:{size:[4500,5606][i],type:WidthType.DXA},borders:bordes(),
              shading:{type:ShadingType.CLEAR,fill:CAB,color:'auto'},margins:{top:60,bottom:60,left:90,right:90},
              children:[new Paragraph({spacing:{after:0},children:[new TextRun({text:c.toUpperCase(),font:F,size:15,bold:true,color:GRIS})]})]}))}),
          ...[['Tu vida laboral en hechos (A) y los mundos que conoces (B)','En el módulo de nicho y oferta, cuando conviertas tu experiencia en una ventaja comercial concreta'],
              ['Tu realidad y lo que no estás dispuesto a hacer (D, E)','En la primera semana, cuando fijes los criterios con los que vas a diseñar el negocio'],
              ['Tu gente (C)','Más adelante, cuando ya tengas algo que enseñar y toque llenar la agenda'],
              ['El diario de fricciones','En cuanto empieces a mirar negocios: es tu primer material real, y no lo ha escrito nadie por ti']
             ].map(([a,bb])=>new TableRow({children:[a,bb].map((t,i)=>
               new TableCell({width:{size:[4500,5606][i],type:WidthType.DXA},borders:bordes(),
                 margins:{top:90,bottom:90,left:90,right:90},
                 children:[p(t,{after:0,size:19})]}))}))]}),

      new Paragraph({spacing:{before:320,after:140},
        border:{top:{style:BorderStyle.SINGLE,size:12,color:TINTA}},children:[new TextRun({text:' ',font:F,size:12})]}),
      p('Guarda esta carpeta rellenada donde no se pierda. El día que empieces, ábrela antes de la primera lección.'),
      rico([['Si solo haces una cosa de todo esto, que sea el ',false],['diario de fricciones',true],['. Es la única que no se puede recuperar después: son conversaciones que pasan delante de ti estos días y que, si no las apuntas, se van.',false]],{after:0})
    ]}]});

Packer.toBuffer(doc).then(buf=>{require('fs').writeFileSync('Antes-del-dia-1.docx',buf);
  console.log('escrito Antes-del-dia-1.docx', buf.length, 'bytes');});
