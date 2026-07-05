
from flask import Flask, render_template_string

app = Flask(__name__)

# Diseño visual del motor de fútbol Clayton v5
HTML_GRAFICO = """
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
        .engine-title { margin: 0; font-size: 18px; font-weight: 800; letter-spacing: 0.5px; color: var(--text-main); }
        .engine-title span { color: var(--accent-clayton); }
        .engine-sub { font-size: 11px; font-weight: 700; color: var(--accent-green); margin-top: 4px; letter-spacing: 0.5px; }
        .combo-panel { background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%); border: 2px solid var(--accent-clayton); border-radius: 12px; padding: 14px; margin-bottom: 16px; box-shadow: 0 4px 15px rgba(249, 115, 22, 0.15); }
        .combo-title { font-size: 13px; font-weight: 800; text-transform: uppercase; color: var(--accent-clayton); letter-spacing: 0.5px; }
        .combo-list { margin: 10px 0 0 0; padding-left: 14px; font-size: 11px; color: #cbd5e1; line-height: 1.5; }
        .combo-list strong { color: #fff; }
        .panel { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 12px; padding: 14px; margin-bottom: 14px; }
        .tournament-line { font-size: 11px; font-weight: 600; color: var(--text-muted); display: flex; justify-content: space-between; align-items: center; }
        .team-vs { font-size: 17px; font-weight: 800; margin: 8px 0 2px 0; }
        .venue-info { color: var(--text-muted); font-size: 11px; margin-bottom: 4px; }
        .weather-info { font-size: 11px; font-weight: 600; color: #cbd5e1; background: rgba(255,255,255,0.05); padding: 4px 8px; border-radius: 6px; display: inline-block; margin-bottom: 12px; border: 1px solid rgba(255,255,255,0.05); }
        .prob-bar-container { display: flex; height: 28px; border-radius: 6px; overflow: hidden; margin: 12px 0; font-weight: 700; font-size: 10px; text-shadow: 1px 1px 1px rgba(0,0,0,0.6); }
        .prob-bar { display: flex; align-items: center; justify-content: center; color: white; }
        .prob-local { background: var(--accent-blue); }
        .prob-draw { background: #475569; }
        .prob-visit { background: var(--accent-green); }
        .metrics-vertical-stack { display: flex; flex-direction: column; gap: 6px; margin-top: 12px; }
        .metric-row-card { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 10px; display: flex; justify-content: space-between; align-items: center; }
        .metric-label { font-size: 11px; text-transform: uppercase; color: var(--text-muted); font-weight: 700; letter-spacing: 0.3px; }
        .metric-value { font-size: 13px; font-weight: 700; color: #f1f5f9; }
        .btn-clayton { width: 100%; background: linear-gradient(135deg, #f97316 0%, #ea580c 100%); color: white; border: none; padding: 11px; border-radius: 8px; font-size: 11px; font-weight: 800; letter-spacing: 0.8px; text-transform: uppercase; margin-top: 14px; box-shadow: 0 4px 6px rgba(234, 88, 12, 0.2); border: 1px solid rgba(255,255,255,0.1); }
    </style>
</head>
<body>
<div class="container">
    <header>
        <div class="engine-title">CLAYTON COUPLING ENGINE <span>v5</span></div>
        <div class="engine-sub">● TOTALMENTE OPTIMIZADO PARA 90 MINUTOS EN TIEMPO REGULAR</div>
    </header>
    <div class="combo-panel">
        <div class="combo-title">🔮 APUESTA COMBINADA SUGERIDA (MÁS SEGURA)</div>
        <ul class="combo-list">
            <li><strong>Mundial:</strong> Brasil vs Noruega &rarr; Más de 1.5 Goles (95% Acierto)</li>
            <li><strong>Mundial:</strong> México vs Inglaterra &rarr; Más de 2.5 Tarjetas (89% Acierto)</li>
            <li style="margin-top: 6px; color: var(--accent-green); font-weight: bold;">📊 Puntería Global: 71% de Probabilidad Estocástica</li>
        </ul>
    </div>
    <div class="panel">
        <div class="tournament-line">
            <span>Mundial 2026 🏆 - Octavos</span>
            <span style="color: var(--accent-clayton); font-weight: bold;">Hoy | 22:00h</span>
        </div>
        <div class="team-vs">Brasil 🇧🇷 vs Noruega 🇳🇴</div>
        <div class="venue-info">🏟️ MetLife Stadium, USA</div>
        <div class="weather-info">🌤️ Clima: 🌤️ 29°C - Humedad 82%</div>
        <div class="prob-bar-container">
            <div class="prob-bar prob-local" style="width: 44.0%;">Brasil 44%</div>
            <div class="prob-bar prob-draw" style="width: 25.0%;">X 25%</div>
            <div class="prob-bar prob-visit" style="width: 31.0%;">Noruega 31%</div>
        </div>
        <div class="metrics-vertical-stack">
            <div class="metric-row-card">
                <span class="metric-label">🔮 Resultado Exacto</span>
                <span class="metric-value" style="color: var(--accent-clayton);">3 - 2</span>
            </div>
            <div class="metric-row-card" style="border-left: 3px solid var(--accent-green);">
                <span class="metric-label" style="color: var(--accent-green);">🎯 Apuesta Sugerida</span>
                <span class="metric-value" style="color: #4ade80;">Más de 1.5 Goles</span>
            </div>
        </div>
        <button class="btn-clayton">PROCESAR CON CÓPULA DE CLAYTON</button>
    </div>
</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_GRAFICO)

if __name__ == '__main__':
    app.run(debug=True)
