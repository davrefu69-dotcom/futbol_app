from flask import Flask

app = Flask(__name__)

DATA_9999 = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>CLAYTON ENGINE ULTRA v9999</title>
    <style>
        :root { --bg: #060b13; --card: #111927; --inner: #1f2a3c; --green: #00e701; --gold: #ffdf00; --blue: #00bfff; --purple: #bd93f9; }
        body { font-family: system-ui, sans-serif; background: var(--bg); margin: 0; padding: 12px; color: #fff; }
        header { background: var(--card); border-bottom: 3px solid var(--green); padding: 12px; text-align: center; border-radius: 8px; margin-bottom: 12px; }
        .premium { background: linear-gradient(135deg, #0f172a, #1e1b4b); border: 2px dashed var(--green); border-radius: 12px; padding: 12px; margin-bottom: 14px; font-size: 11px; }
        .panel { background: var(--card); border-radius: 12px; padding: 12px; margin-bottom: 14px; border: 1px solid #2d3748; }
        .title { font-size: 15px; font-weight: 900; margin-bottom: 8px; border-bottom: 1px solid #2d3748; padding-bottom: 6px; }
        .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 6px; }
        .box { background: var(--inner); padding: 8px; border-radius: 6px; font-size: 11px; }
        .lbl { color: #9ca3af; font-size: 9px; font-weight: 800; text-transform: uppercase; }
        .val { font-weight: 700; margin-top: 2px; }
        .c-gold { color: var(--gold); } .c-green { color: var(--green); } .c-blue { color: var(--blue); } .c-purple { color: var(--purple); }
        .odds { display: flex; justify-content: space-around; background: rgba(0,0,0,0.3); padding: 6px; border-radius: 6px; margin-top: 8px; font-size: 11px; }
    </style>
</head>
<body>
    <header><h3 style="margin:0;">🧠 CLAYTON ENGINE PRO <span>v9999</span></h3></header>
    
    <div class="premium">
        <b style="color:var(--green);">🔒 COMBINADA INDESTRUCTIBLE (ÉXITO GLOBAL: 87.2%)</b>
        <p style="margin:4px 0 0 0;">• Brasil-Noruega: +8.5 Córners | • Madrid-Barca: +3.5 Tarjetas | • Argentina-Francia: Ambos Anotan</p>
    </div>

    <!-- P1 -->
    <div class="panel">
        <div class="title">Brasil 🇧🇷 vs Noruega 🇳🇴</div>
        <div class="grid">
            <div class="box"><div class="lbl">🔮 Resultado Exacto</div><div class="val c-gold">3 - 2 (21%)</div></div>
            <div class="box"><div class="lbl">📐 Córners Totales</div><div class="val c-green">Más de 9.5 (68%)</div></div>
            <div class="box"><div class="lbl">🟨 Tarjetas Proyectadas</div><div class="val c-purple">Total: 4 (Riesgo: Ostigard)</div></div>
            <div class="box"><div class="lbl">⏱️ Tramo Primer Gol</div><div class="val c-blue">Minuto 15 - 30</div></div>
        </div>
        <div class="odds"><span>L: 44%</span><span>X: 25%</span><span>V: 31%</span></div>
    </div>

    <!-- P2 -->
    <div class="panel">
        <div class="title">México 🇲🇽 vs Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿</div>
        <div class="grid">
            <div class="box"><div class="lbl">🔮 Resultado Exacto</div><div class="val c-gold">1 - 2 (18%)</div></div>
            <div class="box"><div class="lbl">📐 Córners Totales</div><div class="val c-green">Menos de 8.5 (55%)</div></div>
            <div class="box"><div class="lbl">🟨 Tarjetas Proyectadas</div><div class="val c-purple">Total: 6 (Árbitro Estricto)</div></div>
            <div class="box"><div class="lbl">⏱️ Tramo Primer Gol</div><div class="val c-blue">Minuto 30 - 45</div></div>
        </div>
        <div class="odds"><span>L: 34.3%</span><span>X: 25%</span><span>V: 40.7%</span></div>
    </div>

    <!-- P3 -->
    <div class="panel">
        <div class="title">Argentina 🇦🇷 vs Francia 🇫🇷</div>
        <div class="grid">
            <div class="box"><div class="lbl">🔮 Resultado Exacto</div><div class="val c-gold">2 - 2 (14%)</div></div>
            <div class="box"><div class="lbl">📐 Córners Totales</div><div class="val c-green">Más de 10.5 (52%)</div></div>
            <div class="box"><div class="lbl">🟨 Tarjetas Proyectadas</div><div class="val c-purple">Total: 5 (Riesgo: Romero)</div></div>
            <div class="box"><div class="lbl">⏱️ Tramo Primer Gol</div><div class="val c-blue">Minuto 0 - 15</div></div>
        </div>
        <div class="odds"><span>L: 38%</span><span>X: 29%</span><span>V: 33%</span></div>
    </div>

    <!-- P4 -->
    <div class="panel">
        <div class="title">Real Madrid 🇪🇸 vs Barcelona 🇪🇸</div>
        <div class="grid">
            <div class="box"><div class="lbl">🔮 Resultado Exacto</div><div class="val c-gold">3 - 1 (16%)</div></div>
            <div class="box"><div class="lbl">📐 Córners Totales</div><div class="val c-green">Más de 9.5 (60%)</div></div>
            <div class="box"><div class="lbl">🟨 Tarjetas Proyectadas</div><div class="val c-purple">Total: 7 (Riesgo: Gavi)</div></div>
            <div class="box"><div class="lbl">⏱️ Tramo Primer Gol</div><div class="val c-blue">Minuto 15 - 30</div></div>
        </div>
        <div class="odds"><span>L: 48%</span><span>X: 22%</span><span>V: 30%</span></div>
    </div>

    <!-- P5 -->
    <div class="panel">
        <div class="title">Man. City 🏴󠁧󠁢󠁥󠁮󠁧󠁿 vs Bayern Múnich 🇩🇪</div>
        <div class="grid">
            <div class="box"><div class="lbl">🔮 Resultado Exacto</div><div class="val c-gold">2 - 0 (22%)</div></div>
            <div class="box"><div class="lbl">📐 Córners Totales</div><div class="val c-green">Más de 10.5 (70%)</div></div>
            <div class="box"><div class="lbl">🟨 Tarjetas Proyectadas</div><div class="val c-purple">Total: 3 (Limpio)</div></div>
            <div class="box"><div class="lbl">⏱️ Tramo Primer Gol</div><div class="val c-blue">Minuto 0 - 15</div></div>
        </div>
        <div class="odds"><span>L: 55%</span><span>X: 20%</span><span>V: 25%</span></div>
    </div>

    <!-- P6 -->
    <div class="panel">
        <div class="title">Portugal 🇵🇹 vs Italia 🇮🇹</div>
        <div class="grid">
            <div class="box"><div class="lbl">🔮 Resultado Exacto</div><div class="val c-gold">1 - 1 (26%)</div></div>
            <div class="box"><div class="lbl">📐 Córners Totales</div><div class="val c-green">Menos de 9.5 (58%)</div></div>
            <div class="box"><div class="lbl">🟨 Tarjetas Proyectadas</div><div class="val c-purple">Total: 5 (Riesgo: Mancini)</div></div>
            <div class="box"><div class="lbl">⏱️ Tramo Primer Gol</div><div class="val c-blue">Minuto 60 - 75</div></div>
        </div>
        <div class="odds"><span>L: 35%</span><span>X: 33%</span><span>V: 32%</span></div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return DATA_9999

if __name__ == '__main__':
    app.run()
