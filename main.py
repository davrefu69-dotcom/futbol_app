from flask import Flask

app = Flask(__name__)

SUPER_APP_DISEÑO = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>CLAYTON COUPLING ENGINE v5 - PREDICTOR FACTORIAL</title>
    <style>
        :root {
            --bg-primary: #020617;
            --bg-secondary: #0f172a;
            --bg-card: #1e293b;
            --accent-clayton: #f97316;
            --accent-blue: #3b82f6;
            --accent-green: #22c55e;
            --accent-red: #ef4444;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border-color: #334155;
        }
        body { font-family: system-ui, -apple-system, sans-serif; background-color: var(--bg-primary); margin: 0; padding: 12px; color: var(--text-main); }
        .container { max-width: 100%; margin: 0 auto; }
        header { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px; margin-bottom: 16px; text-align: center; }
        .engine-title { margin: 0; font-size: 18px; font-weight: 800; }
        .engine-title span { color: var(--accent-clayton); }
        
        .combo-panel { background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%); border: 2px solid var(--accent-clayton); border-radius: 12px; padding: 14px; margin-bottom: 16px; }
        .combo-title { font-size: 14px; font-weight: 800; color: var(--accent-clayton); text-transform: uppercase; }
        .combo-list { margin: 10px 0 0 0; padding-left: 16px; font-size: 12px; color: #cbd5e1; line-height: 1.6; }

        .panel { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 12px; padding: 14px; margin-bottom: 14px; }
        .team-vs { font-size: 18px; font-weight: 800; margin: 8px 0; border-bottom: 1px solid var(--border-color); padding-bottom: 6px; }
        
        .market-section { background: var(--bg-card); border-radius: 8px; padding: 10px; margin-top: 8px; border: 1px solid rgba(255,255,255,0.05); }
        .market-title { font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--accent-clayton); margin-bottom: 6px; }
        
        /* Factores Influyentes Estilo Lista */
        .factor-list { list-style: none; padding: 0; margin: 0; font-size: 11px; }
        .factor-item { display: flex; justify-content: space-between; padding: 4px 0; border-bottom: 1px dashed rgba(255,255,255,0.05); }
        .factor-item:last-child { border-bottom: none; }
        .factor-name { color: var(--text-muted); }
        .factor-val { font-weight: bold; }
        .val-good { color: var(--accent-green); }
        .val-warn { color: #f59e0b; }
        .val-bad { color: var(--accent-red); }

        .prob-bar-container { display: flex; height: 24px; border-radius: 6px; overflow: hidden; margin: 8px 0; font-weight: 700; font-size: 10px; }
        .prob-bar { display: flex; align-items: center; justify-content: center; color: white; }
        .prob-local { background: var(--accent-blue); }
        .prob-draw { background: #475569; }
        .prob-visit { background: var(--accent-green); }
        .btn-clayton { width: 100%; background: linear-gradient(135deg, #f97316 0%, #ea580c 100%); color: white; border: none; padding: 11px; border-radius: 8px; font-size: 11px; font-weight: 800; margin-top: 10px; }
    </style>
</head>
<body>
<div class="container">
    <header>
        <div class="engine-title">🧠 COUPLING ENGINE v5 - MULTIFACTORIAL</div>
    </header>

    <!-- COMBINADA -->
    <div class="combo-panel">
        <div class="combo-title">🔮 APUESTA COMBINADA RECOMENDADA</div>
        <ul class="combo-list">
            <li><strong>Brasil vs Noruega</strong> ➔ Más de 1.5 Goles totales (95% confianza)</li>
            <li><strong>México vs Inglaterra</strong> ➔ Más de 2.5 Tarjetas totales (89% confianza)</li>
        </ul>
    </div>

    <!-- PARTIDO 1 -->
    <div class="panel">
        <div class="team-vs">Brasil 🇧🇷 vs Noruega 🇳🇴</div>
        
        <div class="market-section">
            <div class="market-title">📊 PROBABILIDAD GENERAL (1 X 2)</div>
            <div class="prob-bar-container">
                <div class="prob-bar prob-local" style="width: 44%;">44% L</div>
                <div class="prob-bar prob-draw" style="width: 25%;">25% X</div>
                <div class="prob-bar prob-visit" style="width: 31%;">31% V</div>
            </div>
        </div>

        <!-- SECCIÓN DE FACTORES INFLUYENTES -->
        <div class="market-section">
            <div class="market-title">🌪️ FACTORES COGNITIVOS E INFLUYENTES</div>
            <ul class="factor-list">
                <li class="factor-item">
                    <span class="factor-name">🌡️ Clima (29°C + 82% Humedad)</span>
                    <span class="factor-val val-warn">Frena Ritmo / Ventaja Físico Local</span>
                </li>
                <li class="factor-item">
                    <span class="factor-name">✈️ Desgaste por Viajes / Fatiga</span>
                    <span class="factor-val val-good">Bajo (4 días de descanso total)</span>
                </li>
                <li class="factor-item">
                    <span class="factor-name">🏟️ Factor de Presión del Público</span>
                    <span class="factor-val val-good">Brasil +12.4% Empuje Estocástico</span>
                </li>
                <li class="factor-item">
                    <span class="factor-name">🩹 Coeficiente de Bajas / Lesiones</span>
                    <span class="factor-val val-bad">Noruega sin Defensa Central Titular</span>
                </li>
                <li class="factor-item">
                    <span class="factor-name">⚖️ Tendencia Arbitral (Tarjetas)</span>
                    <span class="factor-val">Promedio: 3.4 por partido</span>
                </li>
            </ul>
        </div>
        <button class="btn-clayton">CALCULAR COEFICIENTES EN VIVO</button>
    </div>

    <!-- PARTIDO 2 -->
    <div class="panel">
        <div class="team-vs">México 🇲🇽 vs Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿</div>
        
        <div class="market-section">
            <div class="market-title">📊 PROBABILIDAD GENERAL (1 X 2)</div>
            <div class="prob-bar-container">
                <div class="prob-bar prob-local" style="width: 34.3%;">34.3% L</div>
                <div class="prob-bar prob-draw" style="width: 25%;">25% X</div>
                <div class="prob-bar prob-visit" style="width: 40.7%;">40.7% V</div>
            </div>
        </div>

        <!-- SECCIÓN DE FACTORES INFLUYENTES -->
        <div class="market-section">
            <div class="market-title">🌪️ FACTORES COGNITIVOS E INFLUYENTES</div>
            <ul class="factor-list">
                <li class="factor-item">
                    <span class="factor-name">🏔️ Altitud Extrema (Estadio Azteca)</span>
                    <span class="factor-val val-bad">Reduce Oxígeno Visitante (-15% Ritmo)</span>
                </li>
                <li class="factor-item">
                    <span class="factor-name">✈️ Desgaste por Viajes / Fatiga</span>
                    <span class="factor-val val-warn">Inglaterra: Viaje Trasatlántico Reciente</span>
                </li>
                <li class="factor-item">
                    <span class="factor-name">🏟️ Factor de Presión del Público</span>
                    <span class="factor-val val-good">México +22.1% Impacto en Árbitro</span>
                </li>
                <li class="factor-item">
                    <span class="factor-name">🩹 Coeficiente de Bajas / Lesiones</span>
                    <span class="factor-val val-good">Plantillas completas al 100%</span>
                </li>
                <li class="factor-item">
                    <span class="factor-name">⚖️ Tendencia Arbitral (Tarjetas)</span>
                    <span class="factor-val val-bad">Árbitro estricto: Proyección alta</span>
                </li>
            </ul>
        </div>
        <button class="btn-clayton">CALCULAR COEFICIENTES EN VIVO</button>
    </div>

</div>
</body>
</html>
"""

@app.route('/')
def home():
    return SUPER_APP_DISEÑO

if __name__ == '__main__':
    app.run()
