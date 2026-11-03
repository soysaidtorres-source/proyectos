# Genera el Bono 1: Calculadora 4x4 (xlsx que se sube a Google Drive y se convierte a Google Sheets).
# Uso: /usr/bin/python3 build_calculadora.py
import os, xlsxwriter

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Bono1-Calculadora-4x4.xlsx')
NAVY, TEAL, BLUE, SOFT, INPUT, GRAY = '#0B1660', '#00B3AD', '#0068A0', '#EAF7F6', '#FFF4CC', '#606060'

wb = xlsxwriter.Workbook(OUT)
F = 'Arial'
def fmt(**k):
    base = {'font_name': F, 'font_size': 10, 'valign': 'vcenter'}
    base.update(k); return wb.add_format(base)

title = fmt(bold=True, font_size=16, font_color='white', bg_color=NAVY, indent=1)
sub = fmt(italic=True, font_color='white', bg_color=NAVY, indent=1)
band = fmt(bold=True, font_color='white', bg_color=NAVY, indent=1)
sec = fmt(bold=True, font_color='white', bg_color=TEAL, indent=1)
lab = fmt(bold=True, font_color=NAVY, indent=1, text_wrap=True, border=1, border_color='#CFD8E6')
hint = fmt(italic=True, font_color=GRAY, font_size=9, text_wrap=True)
txt = fmt(text_wrap=True)
txtb = fmt(text_wrap=True, bold=True, font_color=NAVY)
inp_txt = fmt(bg_color=INPUT, border=1, border_color='#E0C25A')
inp_money = fmt(bg_color=INPUT, border=1, border_color='#E0C25A', num_format='$#,##0.00')
inp_num = fmt(bg_color=INPUT, border=1, border_color='#E0C25A', num_format='#,##0')
out_money = fmt(bg_color=SOFT, border=1, border_color='#9ED9D6', num_format='$#,##0.00', bold=True, font_color=NAVY)
out_num = fmt(bg_color=SOFT, border=1, border_color='#9ED9D6', num_format='#,##0', bold=True, font_color=NAVY, align='right')
out_pct = fmt(bg_color=SOFT, border=1, border_color='#9ED9D6', num_format='0.0%', bold=True, font_color=NAVY)
out_txt = fmt(bg_color=SOFT, border=1, border_color='#9ED9D6', bold=True, font_color=NAVY, text_wrap=True)
tot_lab = fmt(bold=True, font_color='white', bg_color=BLUE, indent=1)
tot_money = fmt(bold=True, font_color='white', bg_color=BLUE, num_format='$#,##0.00')
th = fmt(bold=True, font_color=NAVY, bg_color=SOFT, border=1, border_color='#CFD8E6', text_wrap=True, align='center')
diag = fmt(bold=True, font_size=11, font_color=NAVY, bg_color='#FFF8E1', border=2, border_color=TEAL, text_wrap=True, indent=1)
legend_in = fmt(bg_color=INPUT, border=1, border_color='#E0C25A', bold=True, font_color=NAVY, align='center')
legend_out = fmt(bg_color=SOFT, border=1, border_color='#9ED9D6', bold=True, font_color=NAVY, align='center')
foot = fmt(italic=True, font_color=GRAY, font_size=8, text_wrap=True)

def header(ws, t, s, last='E'):
    ws.hide_gridlines(2)
    ws.set_row(0, 34); ws.set_row(1, 20)
    ws.merge_range(f'A1:{last}1', t, title)
    ws.merge_range(f'A2:{last}2', s, sub)

# ---------------- INICIO ----------------
ws = wb.add_worksheet('Inicio'); ws.set_tab_color(NAVY)
ws.set_column('A:A', 4); ws.set_column('B:B', 26); ws.set_column('C:C', 70)
header(ws, 'CALCULADORA 4x4 · Costos, precio y punto de equilibrio', 'Bono 1 de la guía "Tu Negocio en 7 Días" · Método 4x4 de Sam González', 'C')
ws.set_row(3, 30)
ws.merge_range('B4:C4', 'ANTES DE EMPEZAR: en Google Sheets ve a Archivo → Hacer una copia. Así tendrás tu propia calculadora y podrás escribir en ella.', diag)
ws.write('B6', 'CÓMO USARLA', sec); ws.write('C6', '', sec)
rows = [
 ('Pestaña "1. Mis costos"', 'DÍA 4 · Hoja 10 de la guía. Anota tus costos de arranque, tus costos fijos del mes (incluido tu sueldo) y lo que te cuesta cada unidad que vendes.'),
 ('Pestaña "2. Punto de equilibrio"', 'DÍA 4 · Hojas 11 y 12. Escribe tu precio, tu meta de ganancia y cuántas unidades puedes producir o atender al mes. La calculadora te dice cuánto necesitas vender y si tu meta es viable.'),
 ('Pestaña "3. Simulador de precio"', 'DÍA 5 · Hoja 13. Prueba distintos precios y mira al instante cómo cambian tu ganancia por unidad, tu punto de equilibrio y tu utilidad del mes.'),
 ('Pestaña "Ejemplo · Pasteles"', 'El mismo ejemplo de la guía, ya lleno, para que veas cómo funciona.'),
]
r = 6
for a, b in rows:
    ws.set_row(r, 44); ws.write(r, 1, a, lab); ws.write(r, 2, b, txt); r += 1
r += 1
ws.write(r, 1, 'COLORES', sec); ws.write(r, 2, '', sec); r += 1
ws.write(r, 1, 'Celda amarilla', legend_in); ws.write(r, 2, 'Tú escribes aquí.', txt); r += 1
ws.write(r, 1, 'Celda turquesa', legend_out); ws.write(r, 2, 'Resultado automático. No la borres: tiene una fórmula.', txt); r += 2
ws.set_row(r, 54)
ws.merge_range(r, 1, r, 2, 'Recuerda la frase de Sam: "Ventas no es igual a utilidades." Tu sueldo es un costo y los impuestos no son ganancia. Esta calculadora te da estimaciones para decidir mejor; para temas fiscales, consulta a un contador.', txtb)
r += 2
ws.merge_range(r, 1, r, 2, '© Samuel González Guzmán · My 4x4 Academy. Para uso personal del comprador de la guía "Tu Negocio en 7 Días".', foot)

# ---------------- 1. MIS COSTOS ----------------
ws = wb.add_worksheet('1. Mis costos'); ws.set_tab_color(TEAL)
ws.set_column('A:A', 3); ws.set_column('B:B', 48); ws.set_column('C:C', 18); ws.set_column('D:D', 3); ws.set_column('E:E', 46)
header(ws, '1. MIS COSTOS', 'Día 4 · Hoja de trabajo 10 · Escribe en las celdas amarillas', 'E')

def block(ws, start, name, hint_text, n, prefill=None, total_name='TOTAL'):
    ws.write(start, 1, name, sec); ws.write(start, 2, '$', sec)
    ws.merge_range(start, 4, start + 3, 4, hint_text, hint)
    for i in range(n):
        rr = start + 1 + i
        ws.write(rr, 1, (prefill[i] if prefill and i < len(prefill) else ''), inp_txt)
        ws.write(rr, 2, None, inp_money)
    tr = start + 1 + n
    ws.write(tr, 1, total_name, tot_lab)
    ws.write_formula(tr, 2, f'=SUM(C{start + 2}:C{start + 1 + n})', tot_money)
    return tr

t1 = block(ws, 3, 'COSTOS DE ARRANQUE (una sola vez)',
           'Ejemplos: equipo y herramientas, primer inventario, permisos, logotipo, fotos, adecuaciones del local.', 10,
           total_name='TOTAL COSTOS DE ARRANQUE')                      # filas 5-14, total fila 15 (C15)
t2 = block(ws, t1 + 2, 'COSTOS FIJOS AL MES (vendas o no)',
           'Tu sueldo es un costo, no una ganancia. Otros ejemplos: renta, luz y gas extra, internet, teléfono, publicidad, plataformas.', 10,
           prefill=['Mi sueldo'], total_name='TOTAL COSTOS FIJOS AL MES')  # filas 18-27, total fila 28 (C28)
t3 = block(ws, t2 + 2, 'COSTO VARIABLE POR UNIDAD VENDIDA',
           'Ejemplos: materia prima o ingredientes, empaque, envío o entrega, comisión por cobro con tarjeta.', 8,
           total_name='TOTAL COSTO VARIABLE POR UNIDAD')                 # filas 31-38, total fila 39 (C39)
assert (t1, t2, t3) == (14, 27, 38)
ws.freeze_panes(3, 0)

# ---------------- 2. PUNTO DE EQUILIBRIO ----------------
ws = wb.add_worksheet('2. Punto de equilibrio'); ws.set_tab_color(TEAL)
ws.set_column('A:A', 3); ws.set_column('B:B', 52); ws.set_column('C:C', 22); ws.set_column('D:D', 3); ws.set_column('E:E', 44)
header(ws, '2. MI PUNTO DE EQUILIBRIO Y MI META', 'Día 4 · Hojas de trabajo 11 y 12', 'E')
ws.write('B4', 'TUS DATOS', sec); ws.write('C4', '', sec)
ws.write('B5', 'Precio de venta por unidad', lab); ws.write('C5', None, inp_money)
ws.write('E5', 'Provisional. En el Día 5 lo afinas con el simulador.', hint)
ws.write('B6', 'Costo variable por unidad (viene de "1. Mis costos")', lab); ws.write_formula('C6', "='1. Mis costos'!C39", out_money)
ws.write('B7', 'Costos fijos al mes (viene de "1. Mis costos")', lab); ws.write_formula('C7', "='1. Mis costos'!C28", out_money)
ws.write('B8', 'Utilidad que quiero ganar al mes (además de mi sueldo)', lab); ws.write('C8', None, inp_money)
ws.write('B9', 'Unidades que puedo producir o atender al mes', lab); ws.write('C9', None, inp_num)
ws.write('E9', 'Tu capacidad real: horas, equipo, ayuda.', hint)
ws.write('B10', 'Días que trabajo al mes', lab); ws.write('C10', 24, inp_num)

ws.write('B12', 'RESULTADOS', sec); ws.write('C12', '', sec)
res = [
 ('Me queda por cada unidad (precio − costo variable)', '=IF(C5="","",C5-C6)', out_money),
 ('Margen sobre el precio', '=IF(OR(C5="",C5=0),"",C13/C5)', out_pct),
 ('PUNTO DE EQUILIBRIO: unidades al mes para no perder', '=IF(OR(C5="",C13<=0),"—",ROUNDUP(C7/C13,0))', out_num),
 ('   … por semana', '=IF(ISNUMBER(C15),ROUNDUP(C15/4.33,0),"—")', out_num),
 ('   … por día de trabajo', '=IF(AND(ISNUMBER(C15),C10>0),ROUNDUP(C15/C10,0),"—")', out_num),
 ('Ventas en pesos para llegar al punto de equilibrio', '=IF(ISNUMBER(C15),C15*C5,"—")', out_money),
 ('MI META: unidades al mes para ganar mi utilidad', '=IF(OR(C5="",C13<=0),"—",ROUNDUP((C7+C8)/C13,0))', out_num),
 ('   … por semana', '=IF(ISNUMBER(C19),ROUNDUP(C19/4.33,0),"—")', out_num),
 ('Ventas en pesos para llegar a mi meta', '=IF(ISNUMBER(C19),C19*C5,"—")', out_money),
]
for i, (a, f, fm) in enumerate(res):
    ws.write(12 + i, 1, a, lab); ws.write_formula(12 + i, 2, f, fm)
ws.set_row(22, 48)
ws.write('B23', '¿ES VIABLE?', tot_lab)
ws.merge_range('C23:E23', '', diag)
ws.write_formula('C23', '=IF(C5="","Escribe tu precio de venta en la celda amarilla.",IF(C13<=0,"❌ Con este precio pierdes dinero en cada venta. Sube tu precio o baja tu costo variable.",IF(C9="","Escribe cuántas unidades puedes producir al mes para saber si tu meta es viable.",IF(C19>C9,"⚠️ Tu meta NO es viable con tu capacidad. Ajusta tu precio, tus costos, tu meta o tu capacidad.","✅ Tu meta es viable con tu capacidad. Ahora compruébalo vendiendo (Día 6)."))))', diag)

ws.write('B25', 'MI DINERO PARA ARRANCAR (Hoja 12)', sec); ws.write('C25', '', sec)
ws.write('B26', 'Total de costos de arranque (viene de "1. Mis costos")', lab); ws.write_formula('C26', "='1. Mis costos'!C15", out_money)
ws.write('B27', 'Meses que calculo para llegar al punto de equilibrio', lab); ws.write('C27', 3, inp_num)
ws.write('B28', 'Dinero para operar mientras llego (costos fijos × meses)', lab); ws.write_formula('C28', '=C7*C27', out_money)
ws.write('B29', 'TOTAL QUE NECESITO PARA ARRANCAR', tot_lab); ws.write_formula('C29', '=C26+C28', tot_money)
ws.set_row(30, 36)
ws.merge_range('B31:E31', 'Consejo de Sam: no te "emborraches" con tu idea ni te endeudes de más. Empieza con lo mínimo que te permita vender y crece con lo que el negocio genere.', txtb)

# ---------------- 3. SIMULADOR DE PRECIO ----------------
ws = wb.add_worksheet('3. Simulador de precio'); ws.set_tab_color(TEAL)
ws.set_column('A:A', 3); ws.set_column('B:B', 16); ws.set_column('C:G', 17); ws.set_column('H:H', 20)
header(ws, '3. SIMULADOR DE PRECIO', 'Día 5 · Hoja de trabajo 13 · "Establecer precios es un arte"', 'H')
ws.write('B4', 'TUS DATOS', sec)
for c in 'CDEFGH': ws.write(f'{c}4', '', sec)
ws.merge_range('B5:E5', 'Precio más bajo de tu competencia', lab); ws.write('F5', None, inp_money)
ws.merge_range('B6:E6', 'Precio más alto de tu competencia', lab); ws.write('F6', None, inp_money)
ws.merge_range('B7:E7', 'Unidades que calculo vender al mes', lab); ws.write('F7', None, inp_num)
ws.merge_range('B8:E8', 'Costo variable por unidad (viene de "1. Mis costos")', lab); ws.write_formula('F8', "='1. Mis costos'!C39", out_money)
ws.merge_range('B9:E9', 'Costos fijos al mes (viene de "1. Mis costos")', lab); ws.write_formula('F9', "='1. Mis costos'!C28", out_money)
ws.set_row(11, 42)
heads = ['Precio a probar', 'Me queda por unidad', 'Margen', 'Punto de equilibrio (unidades/mes)', 'Utilidad del mes con mis ventas', 'Frente a la competencia', 'Posicionamiento']
for i, h in enumerate(heads):
    ws.write(11, 1 + i, h, th)
mult = [0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.5]
for i, m in enumerate(mult):
    r = 12 + i; R = r + 1
    ws.write_formula(r, 1, f"=IF('2. Punto de equilibrio'!C5=\"\",\"\",ROUND('2. Punto de equilibrio'!C5*{m},0))", inp_money)
    ws.write_formula(r, 2, f'=IF(B{R}="","",B{R}-$F$8)', out_money)
    ws.write_formula(r, 3, f'=IF(OR(B{R}="",B{R}=0),"",C{R}/B{R})', out_pct)
    ws.write_formula(r, 4, f'=IF(B{R}="","",IF(C{R}<=0,"Pierdes",ROUNDUP($F$9/C{R},0)))', out_num)
    ws.write_formula(r, 5, f'=IF(OR(B{R}="",$F$7=""),"",$F$7*C{R}-$F$9)', out_money)
    ws.write_formula(r, 6, f'=IF(OR(B{R}="",$F$5="",$F$6=""),"",IF(B{R}<$F$5,"Más barato que todos",IF(B{R}>$F$6,"Más caro que todos","Dentro del rango")))', out_txt)
    ws.write_formula(r, 7, f'=IF(OR(B{R}="",$F$5="",$F$6=""),"",IF(B{R}<=$F$5+($F$6-$F$5)/3,"Económico",IF(B{R}<=$F$5+2*($F$6-$F$5)/3,"Intermedio","Premium")))', out_txt)
red = wb.add_format({'font_color': '#B42318', 'bg_color': '#FDE8E8'})
green = wb.add_format({'font_color': '#0B7A43', 'bg_color': '#E7F8EF'})
ws.conditional_format('F13:F19', {'type': 'cell', 'criteria': '<', 'value': 0, 'format': red})
ws.conditional_format('F13:F19', {'type': 'cell', 'criteria': '>', 'value': 0, 'format': green})
ws.conditional_format('C13:C19', {'type': 'cell', 'criteria': '<=', 'value': 0, 'format': red})
ws.set_row(20, 30)
ws.merge_range('B21:H21', 'Los precios de la tabla se llenan solos a partir del precio que pusiste en la pestaña 2 (−20% a +50%). Puedes escribir encima cualquier precio que quieras probar.', hint)
ws.set_row(22, 40)
ws.merge_range('B23:H23', 'Recuerda: el precio también comunica calidad. Evita la guerra de precios y busca clientes de calidad, los que compran por beneficios. Una vez que publicas un precio, es difícil cambiarlo.', txtb)
ws.freeze_panes(12, 0)

# ---------------- EJEMPLO ----------------
ws = wb.add_worksheet('Ejemplo · Pasteles'); ws.set_tab_color(GRAY)
ws.set_column('A:A', 3); ws.set_column('B:B', 52); ws.set_column('C:C', 22)
header(ws, 'EJEMPLO · PASTELES POR PEDIDO', 'El mismo ejemplo del Día 4 de la guía, ya lleno', 'C')
data = [('Mi sueldo (costo fijo)', 6000), ('Gas y luz extra', 700), ('Internet y teléfono', 400), ('Publicidad', 1200), ('Otros', 700)]
ws.write('B4', 'COSTOS FIJOS AL MES', sec); ws.write('C4', '$', sec)
for i, (a, v) in enumerate(data):
    ws.write(4 + i, 1, a, lab); ws.write(4 + i, 2, v, inp_money)
ws.write('B10', 'TOTAL COSTOS FIJOS', tot_lab); ws.write_formula('C10', '=SUM(C5:C9)', tot_money)
ws.write('B12', 'POR CADA PASTEL', sec); ws.write('C12', '$', sec)
for i, (a, v) in enumerate([('Ingredientes', 110), ('Caja y base', 25), ('Entrega', 15)]):
    ws.write(12 + i, 1, a, lab); ws.write(12 + i, 2, v, inp_money)
ws.write('B16', 'COSTO VARIABLE POR PASTEL', tot_lab); ws.write_formula('C16', '=SUM(C13:C15)', tot_money)
ws.write('B18', 'Precio de venta', lab); ws.write('C18', 350, inp_money)
ws.write('B19', 'Utilidad que quiero al mes', lab); ws.write('C19', 5000, inp_money)
ws.write('B20', 'Pasteles que puedo hacer al mes', lab); ws.write('C20', 80, inp_num)
ws.write('B22', 'Me queda por pastel', lab); ws.write_formula('C22', '=C18-C16', out_money)
ws.write('B23', 'Punto de equilibrio (pasteles al mes)', lab); ws.write_formula('C23', '=ROUNDUP(C10/C22,0)', out_num)
ws.write('B24', 'Pasteles al mes para mi meta', lab); ws.write_formula('C24', '=ROUNDUP((C10+C19)/C22,0)', out_num)
ws.set_row(25, 40)
ws.write('B26', '¿Es viable?', tot_lab)
ws.write_formula('C26', '=IF(C24>C20,"⚠️ No es viable con tu capacidad","✅ Viable: necesitas "&C24&" de "&C20&" posibles")', diag)

wb.close()
print(OUT, os.path.getsize(OUT))
