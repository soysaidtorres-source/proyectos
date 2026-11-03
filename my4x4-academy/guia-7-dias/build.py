import re,glob,subprocess,sys,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
parts=sorted(glob.glob('parts/*.html'))
body=''.join(open(p).read() for p in parts)
toc_ph='<!--TOC-->'
# insert TOC page after the letter (end of part 00)
first=open(parts[0]).read()
body=body.replace(first, first+toc_ph,1)
secs=re.split(r'(?=<section )',body)
out=[];toc=[];n=0
for s in secs:
    if not s.startswith('<section'):
        out.append(s); continue
    n+=1
    m=re.search(r'data-toc="([^"]+)"',s)
    if m: toc.append((m.group(1),n))
    s=s.replace('<span class="n"></span>',f'<span class="n">{n}</span>')
    out.append(s)
    if toc_ph in s: pass
body=''.join(out)
# TOC page counts as a page: it is inserted after page 2, so shift pages >=3 by 1
def shift(b):
    return re.sub(r'<span class="n">(\d+)</span>',lambda m:f'<span class="n">{int(m.group(1))+1 if int(m.group(1))>=3 else m.group(1)}</span>',b)
body=shift(body)
toc=[(t,p+1 if p>=3 else p) for t,p in toc]
rows=''.join(f'<div class="toc-r{" day" if t.startswith("Día") else ""}"><span>{t}</span><i></i><b>{p}</b></div>' for t,p in toc)
tocpage=f'''<section class="page"><div class="kicker">Tu ruta de 7 días</div><h1 class="pt">Contenido</h1><div class="toc">{rows}</div>
<div class="tip" style="margin-top:18px"><div class="t">TUS BONOS</div><strong>Bono 1:</strong> Calculadora de costos, precio y punto de equilibrio (la usarás el Día 4). <strong>Bono 2:</strong> Masterclass "Emprende en la Era de la IA" de Sam González.</div>
<div class="pf"><span><b>TU NEGOCIO EN 7 DÍAS</b> · Método 4x4</span><span class="n">3</span></div></section>'''
body=body.replace(toc_ph,tocpage)
html=f'<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>Tu Negocio en 7 Días · Método 4x4</title><link rel="stylesheet" href="guia.css"></head><body>{body}</body></html>'
open('guia-completa.html','w').write(html)
out_pdf=sys.argv[1] if len(sys.argv)>1 else 'Tu-Negocio-en-7-Dias-Metodo-4x4.pdf'
ch=glob.glob('/opt/pw-browsers/chromium-*/chrome-linux*/chrome')[0]
subprocess.run([ch,'--headless','--no-sandbox','--disable-gpu','--no-pdf-header-footer','--allow-file-access-from-files','--virtual-time-budget=5000',f'--print-to-pdf={out_pdf}','file://'+os.path.abspath('guia-completa.html')],stderr=subprocess.DEVNULL,check=True)
print('pages html:',n+1,'->',out_pdf)
