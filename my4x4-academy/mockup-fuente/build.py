import os
D = os.path.dirname(os.path.abspath(__file__))

boxes = [
    ("01", ["CICLO", "COMERCIAL"]),
    ("02", ["COMPRAS", "INTELIGENTES"]),
    ("03", ["PROPUESTA", "DE VALOR"]),
    ("04", ["VENTAS QUE", "CIERRAN"]),
    ("05", ["CRÉDITO", "SIN RIESGO"]),
]

def box_svg(num, lines, gift=False):
    # front 118x178, side depth 28, top height 18
    W, H, DX, DY = 118, 178, 28, 18
    w, h = W + DX + 4, H + DY + 4
    if gift:
        front = "url(#gGoldF)"; side = "url(#gGoldS)"; top = "url(#gGoldT)"
    else:
        front = "url(#gNavyF)"; side = "url(#gNavyS)"; top = "url(#gNavyT)"
    o = DY
    s = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">'
    s += DEFS
    # top face
    s += f'<polygon points="0,{o} {DX},0 {W+DX},0 {W},{o}" fill="{top}"/>'
    # side face
    s += f'<polygon points="{W},{o} {W+DX},0 {W+DX},{H} {W},{H+o}" fill="{side}"/>'
    # front face
    s += f'<rect x="0" y="{o}" width="{W}" height="{H}" fill="{front}"/>'
    if gift:
        # ribbon vertical + horizontal
        s += f'<rect x="{W/2-9}" y="{o}" width="18" height="{H}" fill="#0B1660"/>'
        s += f'<polygon points="{W/2-9+DX*0.5},{o*0.5} {W/2+9+DX*0.5},{o*0.5} {W/2+9},{o} {W/2-9},{o}" fill="#0B1660"/>'
        s += f'<rect x="0" y="{o+52}" width="{W}" height="16" fill="#0B1660"/>'
        s += f'<polygon points="{W},{o+52} {W+DX},{52} {W+DX},{68} {W},{o+68}" fill="#08104a"/>'
        # bow
        s += f'<ellipse cx="{W/2-14+DX*0.5}" cy="{o*0.5-6}" rx="18" ry="9" fill="#0B1660" transform="rotate(-20 {W/2-14+DX*0.5} {o*0.5-6})"/>'
        s += f'<ellipse cx="{W/2+14+DX*0.5}" cy="{o*0.5-6}" rx="18" ry="9" fill="#0B1660" transform="rotate(20 {W/2+14+DX*0.5} {o*0.5-6})"/>'
        s += f'<circle cx="{W/2+DX*0.5}" cy="{o*0.5-4}" r="6" fill="#00B3AD"/>'
        # tag
        s += f'<rect x="8" y="{o+84}" width="{W-16}" height="88" rx="8" fill="#ffffff"/>'
        s += f'<text x="{W/2}" y="{o+101}" text-anchor="middle" font-family="Montserrat" font-weight="900" font-size="11" fill="#E0A100" letter-spacing="1.5">BONO</text>'
        for i, t in enumerate(["MASTERCLASS", "EMPRENDE EN", "LA ERA DE LA IA"]):
            s += f'<text x="{W/2}" y="{o+119+i*16}" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="{11.5 if i==0 else 10.6}" fill="#0B1660">{t}</text>'
    else:
        # turquoise band and logo stripe
        s += f'<rect x="0" y="{o}" width="{W}" height="8" fill="#00B3AD"/>'
        s += f'<text x="12" y="{o+30}" font-family="Montserrat" font-weight="800" font-size="10" fill="#7fe3de" letter-spacing="1.2">MÉTODO 4x4</text>'
        s += f'<circle cx="{W/2}" cy="{o+70}" r="23" fill="none" stroke="#00B3AD" stroke-width="3"/>'
        s += f'<text x="{W/2}" y="{o+79}" text-anchor="middle" font-family="Anton" font-size="24" fill="#ffffff">{num}</text>'
        for i, t in enumerate(lines):
            s += f'<text x="{W/2}" y="{o+125+i*18}" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="13" fill="#ffffff">{t}</text>'
        s += f'<rect x="12" y="{o+H-22}" width="{W-24}" height="3" rx="1.5" fill="#00B3AD" opacity="0.7"/>'
        s += f'<text x="{W/2}" y="{o+H-8}" text-anchor="middle" font-family="Montserrat" font-weight="700" font-size="7.5" fill="#9fb0e8" letter-spacing="1">LECCIÓN EN VIDEO</text>'
    s += '</svg>'
    return s

DEFS = '''<defs>
<linearGradient id="gNavyF" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a2a8a"/><stop offset="1" stop-color="#0B1660"/></linearGradient>
<linearGradient id="gNavyS" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#070f45"/><stop offset="1" stop-color="#050a33"/></linearGradient>
<linearGradient id="gNavyT" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2d3fa8"/><stop offset="1" stop-color="#22339a"/></linearGradient>
<linearGradient id="gGoldF" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE08A"/><stop offset="0.5" stop-color="#F2B92E"/><stop offset="1" stop-color="#C98B12"/></linearGradient>
<linearGradient id="gGoldS" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#B07A0E"/><stop offset="1" stop-color="#8f620a"/></linearGradient>
<linearGradient id="gGoldT" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFE9A8"/><stop offset="1" stop-color="#F6CC5A"/></linearGradient>
</defs>'''

box_html = ""
xs = [40, 208, 376, 544, 712, 880]
for i, (n, l) in enumerate(boxes):
    box_html += f'<div class="box" style="left:{xs[i]}px">{box_svg(n, l)}</div>'
box_html += f'<div class="box gift" style="left:{xs[5]}px">{box_svg("", [], gift=True)}</div>'

ICON_PLAY = '<svg width="34" height="34" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#00B3AD"/><polygon points="10,7.5 17,12 10,16.5" fill="#fff"/></svg>'
ICON_INF = '<svg width="34" height="34" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#00B3AD"/><path d="M6.2 12c0-1.6 1.2-2.8 2.7-2.8 2.3 0 3.8 5.6 6.2 5.6 1.5 0 2.7-1.2 2.7-2.8s-1.2-2.8-2.7-2.8c-2.4 0-3.9 5.6-6.2 5.6-1.5 0-2.7-1.2-2.7-2.8z" fill="none" stroke="#fff" stroke-width="1.8"/></svg>'
ICON_WEB = '<svg width="34" height="34" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#00B3AD"/><rect x="8" y="5.5" width="8" height="13" rx="1.6" fill="none" stroke="#fff" stroke-width="1.8"/><circle cx="12" cy="16" r="0.9" fill="#fff"/></svg>'

lessons = ["Ciclo comercial", "Compras inteligentes", "Propuesta de valor", "Ventas que cierran", "Crédito sin riesgo"]
lesson_html = "".join(f'<div class="ls"><span class="pl">▶</span>{t}</div>' for t in lessons)

html = f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="fonts/local.css">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1080px;overflow:hidden;background:#050a33}}
.c{{position:relative;width:1080px;height:1080px;overflow:hidden;font-family:Montserrat,sans-serif;
 background:radial-gradient(ellipse 620px 420px at 460px 420px, rgba(0,179,173,.32), rgba(0,179,173,0) 70%),
 radial-gradient(ellipse 900px 700px at 540px 380px, #15238a 0%, #0B1660 45%, #050a33 100%);}}
.rays{{position:absolute;inset:0;background:repeating-conic-gradient(from 0deg at 460px 400px, rgba(255,255,255,.035) 0 6deg, rgba(255,255,255,0) 6deg 18deg);}}
.desk{{position:absolute;left:0;right:0;top:590px;bottom:0;
 background:linear-gradient(180deg,#5a3a24 0%,#3d2615 35%,#24160c 100%);
 box-shadow:inset 0 3px 0 rgba(255,220,180,.25);}}
.desk:after{{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(0,0,0,.06) 0 2px,transparent 2px 46px),
 radial-gradient(ellipse 600px 160px at 460px 0, rgba(255,210,150,.22), transparent 70%);}}
.pill{{position:absolute;top:30px;left:50%;transform:translateX(-50%);background:#fff;color:#0B1660;font-weight:800;font-size:19px;
 letter-spacing:1.5px;padding:9px 26px;border-radius:40px;white-space:nowrap;box-shadow:0 4px 14px rgba(0,0,0,.3)}}
.title{{position:absolute;top:78px;left:0;right:0;text-align:center;font-family:Anton;font-size:66px;color:#fff;letter-spacing:1px;line-height:1;
 text-shadow:0 2px 0 #08104a,0 4px 0 #08104a,0 6px 0 #08104a,0 7px 0 #00B3AD,0 12px 22px rgba(0,0,0,.55)}}
.sub{{position:absolute;top:158px;left:0;right:0;text-align:center;font-weight:800;font-size:24px;color:#00B3AD;letter-spacing:2px}}
/* laptop */
.lap{{position:absolute;left:118px;top:212px;width:640px;}}
.scr{{position:relative;width:600px;height:372px;margin:0 auto;background:#0d0d12;border-radius:18px 18px 6px 6px;padding:14px;
 box-shadow:0 0 0 2px #2a2a33, 0 30px 60px rgba(0,0,0,.55)}}
.cov{{position:relative;width:100%;height:100%;border-radius:6px;overflow:hidden;background:linear-gradient(120deg,#0B1660 0%,#0f1f7a 55%,#0068A0 100%)}}
.cov img{{position:absolute;right:-40px;top:-6px;height:380px;}}
.cov .fade{{position:absolute;inset:0;background:linear-gradient(90deg,#0B1660 0%,#0B1660 38%,rgba(11,22,96,.0) 66%)}}
.cov .brand{{position:absolute;left:24px;top:20px;font-weight:800;font-size:12px;color:#7fe3de;letter-spacing:2px}}
.cov .m1{{position:absolute;left:22px;top:44px;font-family:Anton;font-size:58px;color:#fff;line-height:1}}
.cov .m2{{position:absolute;left:20px;top:100px;font-family:Anton;font-size:108px;color:#00B3AD;line-height:1;text-shadow:0 4px 0 #08104a}}
.cov .m3{{position:absolute;left:24px;top:222px;font-weight:900;font-size:19px;color:#fff;letter-spacing:1.2px;line-height:1.25}}
.cov .m4{{position:absolute;left:24px;top:276px;font-weight:600;font-size:13px;color:#cfd7ff}}
.cov .bar{{position:absolute;left:0;right:0;bottom:0;height:30px;background:rgba(0,0,0,.55);display:flex;align-items:center;padding:0 12px;gap:10px}}
.cov .bar .p{{width:0;height:0;border-left:11px solid #fff;border-top:7px solid transparent;border-bottom:7px solid transparent}}
.cov .bar .t{{flex:1;height:4px;background:rgba(255,255,255,.3);border-radius:2px;position:relative}}
.cov .bar .t:after{{content:"";position:absolute;left:0;top:0;bottom:0;width:34%;background:#00B3AD;border-radius:2px}}
.cov .bar .s{{color:#fff;font-size:10px;font-weight:600}}
.base{{position:relative;width:680px;height:20px;margin:0 0 0 -20px;background:linear-gradient(180deg,#d9dce3,#9aa0ab);
 clip-path:polygon(4% 0,96% 0,100% 100%,0 100%);border-radius:0 0 10px 10px}}
.base:after{{content:"";position:absolute;left:50%;top:0;width:110px;height:7px;transform:translateX(-50%);background:#8b909a;border-radius:0 0 8px 8px}}
.lapshadow{{position:absolute;left:90px;top:592px;width:720px;height:28px;background:radial-gradient(ellipse at center,rgba(0,0,0,.6),transparent 70%)}}
/* phone */
.ph{{position:absolute;left:800px;top:300px;width:186px;height:360px;background:#0d0d12;border-radius:30px;padding:9px;
 transform:rotate(5deg);box-shadow:0 0 0 2px #2a2a33,0 26px 50px rgba(0,0,0,.6)}}
.ph .in{{width:100%;height:100%;border-radius:22px;overflow:hidden;background:#0B1660;position:relative}}
.ph .hd{{height:120px;position:relative;overflow:hidden;background:linear-gradient(120deg,#0B1660,#0068A0)}}
.ph .hd img{{position:absolute;right:-20px;top:0;height:150px}}
.ph .hd .fd{{position:absolute;inset:0;background:linear-gradient(90deg,#0B1660 25%,rgba(11,22,96,0) 75%)}}
.ph .hd .t1{{position:absolute;left:10px;top:30px;font-family:Anton;font-size:24px;color:#fff;line-height:1}}
.ph .hd .t2{{position:absolute;left:10px;top:56px;font-family:Anton;font-size:38px;color:#00B3AD;line-height:1}}
.ph .ls{{font-size:10.5px;font-weight:700;color:#fff;padding:7px 10px;border-bottom:1px solid rgba(255,255,255,.08);display:flex;gap:7px;align-items:center}}
.ph .ls .pl{{color:#00B3AD;font-size:9px}}
.ph .cap{{font-size:9px;font-weight:800;color:#7fe3de;letter-spacing:1.4px;padding:9px 10px 3px}}
/* sticker */
.stk{{position:absolute;left:868px;top:150px;width:176px;height:176px;border-radius:50%;
 background:radial-gradient(circle at 35% 30%,#FFE58A,#FFC83D 55%,#E9A800);transform:rotate(10deg);
 box-shadow:0 0 0 6px #fff,0 14px 30px rgba(0,0,0,.45);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#0B1660;text-align:center}}
.stk .a{{font-weight:900;font-size:15px;letter-spacing:1px}}
.stk .b{{font-family:Anton;font-size:56px;line-height:1}}
.stk .d{{font-weight:900;font-size:17px;letter-spacing:2px}}
/* boxes */
.box{{position:absolute;top:612px;transform:scale(1.1);transform-origin:top left;filter:drop-shadow(0 18px 14px rgba(0,0,0,.55))}}
.tag{{position:absolute;top:862px;left:0;right:0;text-align:center;color:#fff;font-weight:800;font-size:23px;letter-spacing:.3px;text-shadow:0 3px 10px rgba(0,0,0,.6)}}
.tag b{{color:#FFC83D}}
/* bottom bar */
.bb{{position:absolute;left:40px;right:40px;bottom:30px;height:96px;border-radius:20px;background:rgba(5,10,51,.88);
 border:2px solid rgba(0,179,173,.55);display:flex;align-items:center;justify-content:space-around;padding:0 18px}}
.it{{display:flex;align-items:center;gap:12px;color:#fff;font-weight:800;font-size:18px;letter-spacing:.5px;line-height:1.15}}
.sep{{width:2px;height:46px;background:rgba(255,255,255,.18)}}
</style></head><body><div class="c">
<div class="rays"></div>
<div class="desk"></div>
<div class="pill">CURSO ONLINE · MY 4X4 ACADEMY</div>
<div class="title">TODO LO QUE INCLUYE TU CURSO</div>
<div class="sub">MÉTODO 4x4: COMPRA, VENDE Y COBRA</div>
<div class="lapshadow"></div>
<div class="lap"><div class="scr"><div class="cov">
 <img src="sam.jpg"><div class="fade"></div>
 <div class="brand">MY 4X4 ACADEMY</div>
 <div class="m1">MÉTODO</div><div class="m2">4x4</div>
 <div class="m3">COMPRA · VENDE<br>Y COBRA</div>
 <div class="m4">con Sam González</div>
 <div class="bar"><div class="p"></div><div class="t"></div><div class="s">Lección 1 de 6</div></div>
</div></div><div class="base"></div></div>
<div class="ph"><div class="in">
 <div class="hd"><img src="sam2.jpg"><div class="fd"></div><div class="t1">MÉTODO</div><div class="t2">4x4</div></div>
 <div class="cap">TUS LECCIONES</div>
 {lesson_html}
</div></div>
<div class="stk"><div class="a">PAGO ÚNICO</div><div class="b">$185</div><div class="d">MXN</div></div>
{box_html}
<div class="tag">El curso de Sam González para que tu negocio <b>deje de perder dinero</b></div>
<div class="bb">
 <div class="it">{ICON_PLAY}<span>6 LECCIONES<br>EN VIDEO</span></div><div class="sep"></div>
 <div class="it">{ICON_INF}<span>ACCESO<br>DE POR VIDA</span></div><div class="sep"></div>
 <div class="it">{ICON_WEB}<span>100%<br>EN LÍNEA</span></div>
</div>
</div></body></html>'''
open(os.path.join(D, "mockup.html"), "w", encoding="utf-8").write(html)
print("ok")
