from flask import Flask

app = Flask(__name__)

# Tu diseño completo con las pantallas, botones y métricas avanzadas
DISEÑO_COMPLETO = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>CLAYTON COUPLING ENGINE v5</title>
    <style>
        :root {
            --bg-primary: #020617;
            --bg-secondary: #0f172a;
            --bg-card: #1e293b;
            --accent-clayton: #f97316;
            --accent-blue: #3b82f6;
            --accent-green: #22c55e;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border-color: #334155;
        }
        body { font-family: system-ui, -apple-system, sans-serif; background-color: var(--bg-primary); margin: 0; padding: 12px; color: var(--text-main); }
        .container { max-width: 100%; margin: 0 auto; }
        header { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px; margin-bottom: 16px; text-align: center; }
        .engine-title { margin: 0; font-size: 18px; font-weight: 800; letter-spacing: 0.5px; }
        .engine-title span { color: var(--accent-clayton); }
        .engine-sub { font-size: 11px; font-weight: 700; color: var(--accent-green); margin-top: 4px; }
        .combo-panel { background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%); border: 2px solid var(--accent-clayton); border-radius: 12px; padding: 14px; margin-bottom: 16px; }
        .combo-title { font-size: 13px; font-weight: 800; color: var(--accent-clayton); }
        .combo-list { margin: 10px 0 0 0; padding-left: 14px; font-size: 11px; color: #cbd5e1; line-height: 1.5; }
        .panel { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 12px; padding: 14px; margin-bottom: 14px; }
        .tournament-line { font-size: 11px; font-weight: 600; color: var(--text-muted); display: flex; justify-content: space-between; }
        .team-vs { font-size: 17px; font-weight: 800; margin: 8px 0 2px 0; }
        .weather-info { font-size: 11px; font-weight: 600; color: #cbd5e1; background: rgba(255,255,255,0.05); padding: 4px 8px; border-radius: 6px; display: inline-block; margin-bottom: 12px; }
        .prob-bar-container { display: flex; height: 28px; border-radius: 6px; overflow: hidden; margin: 12px 0; font-weight: 700; font-size: 10px; }
        .prob-bar { display: flex; align-items: center; justify-content: center; color: white; }
        .prob-local { background: var(--accent-blue); }
        .prob-draw { background: #475569; }
        .prob-visit { background: var(--accent-green); }
        .metrics-vertical-stack { display: flex; flex-direction: column; gap: 6px; }
        .metric-row-card { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 10px; display: flex; justify-content: space-between; }
        .metric-label { font-size: 11px; text-transform: uppercase; color: var(--text-muted); }
        .metric-value { font-size: 13px; font-weight: 700; }
        .config-box { background: rgba(255, 255, 255, 0.02); border: 1px dashed var(--border-color); border-radius: 8px; padding: 10px; margin-top: 10px; }
        .control-row { display: flex; flex-direction: column; gap: 4px; margin-bottom: 8px; }
        .control-row label { font-size: 11px; color: #cbd5e1; display: flex; justify-content: space-between; }
        .btn-clayton { width: 100%; background: linear-gradient(135deg, #f97316 0%, #ea580c 100%); color: white; border: none; padding: 11px; border-radius: 8px; font-size: 11px; font-weight: 800; margin-top: 14px; }
    </style>
</head>
<body>
<div class="container">
    <header>
        <div class="engine-title">CLAYTON COUPLING ENGINE <span>v5</span></div>
        <div class="engine-sub">● TOTALMENTE OPTIMIZADO PARA MULTIPANTALLA MÓVIL</div>
    </header>

    <div class="combo-panel">
        <div class="combo-title">🔮 APUESTA COMBINADA SUGERIDA (MÁS SEGURA)</div>
        <ul class="combo-list">
            <li><strong>Mundial:</strong> Brasil vs Noruega → Más de 1.5 Goles (95% Acierto)</li>
            <li><strong>Mundial:</strong> México vs Inglaterra → Más de 2.5 Tarjetas (89% Acierto)</li>
        </ul>
    </div>

    <!-- PARTIDO 1 -->
    <div class="panel">
        <div class="tournament-line"><span>Mundial 🏆 - Octavos</span><span style="color: var(--accent-clayton);">Hoy | 22:00h</span></div>
        <div class="team-vs">Brasil 🇧🇷 vs Noruega 🇳🇴</div>
        <div class="weather-info">🌤️ Clima: 29°C - Humedad 82%</div>
        <div class="prob-bar-container">
            <div class="prob-bar prob-local" style="width: 44%;">Brasil 44%</div>
            <div class="prob-bar prob-draw" style="width: 25%;">X 25%</div>
            <div class="prob-bar prob-visit" style="width: 31%;">Noruega 31%</div>
        </div>
        <div class="metrics-vertical-stack">
            <div class="metric-row-card"><span class="metric-label">🔮 Resultado Exacto</span><span class="metric-value" style="color: var(--accent-clayton);">3 - 2</span></div>
            <div class="metric-row-card" style="border-left: 3px solid var(--accent-green);"><span class="metric-label" style="color: var(--accent-green);">🎯 Apuesta Sugerida</span><span class="metric-value">Más de 1.5 Goles</span></div>
        </div>
        <div class="config-box">
            <div class="control-row"><label>Ataque Local: <input type="range" min="0.5" max="4.0" step="0.01" value="2.44"></label></div>
        </div>
        <button class="btn-clayton">PROCESAR CON CÓPULA DE CLAYTON</button>
    </div>

    <!-- PARTIDO 2 -->
    <div class="panel">
        <div class="tournament-line"><span>Mundial 🏆 - Octavos</span><span style="color: var(--accent-clayton);">Mañana | 02:00h</span></div>
        <div class="team-vs">México 🇲🇽 vs Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿</div>
        <div class="weather-info">🌋 Clima: 24°C - Altitud Extrema</div>
        <div class="prob-bar-container">
            <div class="prob-bar prob-local" style="width: 34.3%;">México 34.3%</div>
            <div class="prob-bar prob-draw" style="width: 25%;">X 25%</div>
            <div class="prob-bar prob-visit" style="width: 40.7%;">Inglaterra 40.7%</div>
        </div>
        <div class="metrics-vertical-stack">
            <div class="metric-row-card"><span class="metric-label">🔮 Resultado Exacto</span><span class="metric-value" style="color: var(--accent-clayton);">1 - 2</span></div>
            <div class="metric-row-card" style="border-left: 3px solid var(--accent-green);"><span class="metric-label" style="color: var(--accent-green);">🎯 Apuesta Sugerida</span><span class="metric-value">Más de 2.5 Tarjetas</span></div>
        </div>
        <div class="config-box">
            <div class="control-row"><label>Ataque Local: <input type="range" min="0.5" max="4.0" step="0.01" value="1.80"></label></div>
        </div>
        <button class="btn-clayton">PROCESAR CON CÓPULA DE CLAYTON</button>
    </div>
</div>
</body>
</html>
"""

@app.route('/')
def home():
    return DISEÑO_COMPLETO

if __name__ == '__main__':
    app.run()

