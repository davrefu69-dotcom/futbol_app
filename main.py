from flask import Flask

app = Flask(__name__)

SUPER_APP_INTERACTIVA = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>CLAYTON COUPLING ENGINE v9999⁹⁹⁹</title>
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
        header { background: var(--bg-secondary); border: 2px solid var(--accent-clayton); border-radius: 10px; padding: 14px; margin-bottom: 16px; text-align: center; }
        .engine-title { margin: 0; font-size: 18px; font-weight: 900; }
        .engine-title span { color: var(--accent-clayton); }
        
        .combo-panel { background: linear-gradient(135deg, #1e1b4b 0%, #020617 100%); border: 2px dashed var(--accent-green); border-radius: 12px; padding: 14px; margin-bottom: 16px; }
        .combo-title { font-size: 13px; font-weight: 800; color: var(--accent-green); text-transform: uppercase; }
        .combo-list { margin: 8px 0 0 0; padding-left: 16px; font-size: 11px; color: #cbd5e1; line-height: 1.5; }

        .panel { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 12px; padding: 14px; margin-bottom: 14px; }
        .team-vs { font-size: 16px; font-weight: 800; margin-bottom: 8px; border-bottom: 1px solid var(--border-color); padding-bottom: 6px; display: flex; justify-content: space-between; }
        
        .market-section { background: var(--bg-card); border-radius: 8px; padding: 10px; margin-top: 8px; border: 1px solid rgba(255,255,255,0.05); }
        .market-title { font-size: 10px; font-weight: 800; text-transform: uppercase; color: var(--accent-clayton); margin-bottom: 6px; }
        
        .market-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; font-size: 11px; text-align: center; }
        .market-box { background: rgba(0,0,0,0.2); padding: 6px; border-radius: 4px; border: 1px solid var(--border-color); }
        .market-box span { display: block; font-weight: bold; font-size: 12px; color: #fff; }
        .exact-score { color: #f59e0b !important; font-size: 14px !important; }

        .factor-list { list-style: none; padding: 0; margin: 0; font-size: 11px; }
        .factor-item { display: flex; justify-content: space-between; padding: 4px 0; border-bottom: 1px dashed rgba(255,255,255,0.05); }
        
        .prob-bar-container { display: flex; height: 22px; border-radius: 6px; overflow: hidden; margin: 6px 0; font-weight: 700; font-size: 10px; }
        .prob-bar { display: flex; align-items: center; justify-content: center; color: white; transition: width 0.5s ease; }
        .prob-local { background: var(--accent-blue); }
        .prob-draw { background: #475569; }
        .prob-visit { background: var(--accent-green); }
        
        .btn-clayton { width: 100%; background: linear-gradient(135deg, #f97316 0%, #ea580c 100%); color: white; border: none; padding: 10px; border-radius: 8px; font-size: 11px; font-weight: 800; margin-top: 8px; cursor: pointer; }
        .btn-clayton:active { transform: scale(0.98); }
    </style>
</head>
<body>
<div class="container">
    <header>
        <div class="engine-title">⚡ CLAYTON GOD-MODE INTERACTIVO <span>v9999⁹⁹⁹</span></div>
    </header>

    <div class="combo-panel">
        <div class="combo-title">🔮 SUPERCOMBINADA INDESTRUCTIBLE (ÉXITO GLOBAL: 81.4%)</div>
        <ul class="combo-list">
            <li>⚽ Brasil vs Noruega ➔ <strong>Más de 1.5 Goles</strong> (95%)</li>
            <li>⚽ Real Madrid vs Barcelona ➔ <strong>Más de 2.5 Tarjetas</strong> (92%)</li>
        </ul>
    </div>

    <!-- PARTIDO 1 -->
    <div class="panel" id="p1">
        <div class="team-vs"><span>Brasil 🇧🇷 vs Noruega 🇳🇴</span> <span class="cuota" style="color:var(--accent-green);">CUOTA: 1.85</span></div>
        <div class="prob-bar-container">
            <div class="prob-bar prob-local" style="width: 44%;">44% L</div>
            <div class="prob-bar prob-draw" style="width: 25%;">25% X</div>
            <div class="prob-bar prob-visit" style="width: 31%;">31% V</div>
        </div>
        <div class="market-grid">
            <div class="market-box">Resultado Exacto<span class="exact-score">3 - 2</span>(Prob: 21%)</div>
            <div class="market-box">Goles Totales<span>Más 2.5 (72%)</span></div>
            <div class="market-box">Anotador Clave<span>Haaland (64%)</span></div>
        </div>
        <div class="market-section">
            <div class="market-title">🌪️ INFLUENCIA ULTRA-ESTOCÁSTICA</div>
            <ul class="factor-list">
                <li class="factor-item"><span style="color:var(--text-muted);">🌡️ Clima:</span><span class="factor-dinamico">29°C + 82% Humedad</span></li>
            </ul>
        </div>
        <button class="btn-clayton" onclick="recalcular('p1', 44, 25, 31, '3 - 2', '1.85')">PROCESAR EN VIVO</button>
    </div>

    <!-- PARTIDO 2 -->
    <div class="panel" id="p2">
        <div class="team-vs"><span>México 🇲🇽 vs Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿</span> <span class="cuota" style="color:var(--accent-green);">CUOTA: 2.10</span></div>
        <div class="prob-bar-container">
            <div class="prob-bar prob-local" style="width: 34%;">34% L</div>
            <div class="prob-bar prob-draw" style="width: 25%;">25% X</div>
            <div class="prob-bar prob-visit" style="width: 41%;">41% V</div>
        </div>
        <div class="market-grid">
            <div class="market-box">Resultado Exacto<span class="exact-score">1 - 2</span>(Prob: 18%)</div>
            <div class="market-box">Goles Totales<span>Menos 2.5 (62%)</span></div>
            <div class="market-box">Anotador Clave<span>Harry Kane (55%)</span></div>
        </div>
        <div class="market-section">
            <div class="market-title">🌪️ INFLUENCIA ULTRA-ESTOCÁSTICA</div>
            <ul class="factor-list">
                <li class="factor-item"><span style="color:var(--text-muted);">🏔️ Altitud:</span><span class="factor-dinamico">Estadio Azteca (Estable)</span></li>
            </ul>
        </div>
        <button class="btn-clayton" onclick="recalcular('p2', 34, 25, 41, '1 - 2', '2.10')">PROCESAR EN VIVO</button>
    </div>

    <!-- PARTIDO 3 -->
    <div class="panel" id="p3">
        <div class="team-vs"><span>Argentina 🇦🇷 vs Francia 🇫🇷</span> <span class="cuota" style="color:var(--accent-green);">CUOTA: 2.45</span></div>
        <div class="prob-bar-container">
            <div class="prob-bar prob-local" style="width: 38%;">38% L</div>
            <div class="prob-bar prob-draw" style="width: 29%;">29% X</div>
            <div class="prob-bar prob-visit" style="width: 33%;">33% V</div>
        </div>
        <div class="market-grid">
            <div class="market-box">Resultado Exacto<span class="exact-score">2 - 2</span>(Prob: 14%)</div>
            <div class="market-box">Goles Totales<span>Ambos Anotan (88%)</span></div>
            <div class="market-box">Anotador Clave<span>Mbappé (59%)</span></div>
        </div>
        <div class="market-section">
            <div class="market-title">🌪️ INFLUENCIA ULTRA-ESTOCÁSTICA</div>
            <ul class="factor-list">
                <li class="factor-item"><span style="color:var(--text-muted);">⚔️ Historial:</span><span class="factor-dinamico">H2H Intenso (+3.5 goles)</span></li>
            </ul>
        </div>
        <button class="btn-clayton" onclick="recalcular('p3', 38, 29, 33, '2 - 2', '2.45')">PROCESAR EN VIVO</button>
    </div>

    <!-- PARTIDO 4 -->
    <div class="panel" id="p4">
        <div class="team-vs"><span>Real Madrid 🇪🇸 vs Barcelona 🇪🇸</span> <span class="cuota" style="color:var(--accent-green);">CUOTA: 1.90</span></div>
        <div class="prob-bar-container">
            <div class="prob-bar prob-local" style="width: 48%;">48% L</div>
            <div class="prob-bar prob-draw" style="width: 22%;">22% X</div>
            <div class="prob-bar prob-visit" style="width: 30%;">30% V</div>
        </div>
        <div class="market-grid">
            <div class="market-box">Resultado Exacto<span class="exact-score">3 - 1</span>(Prob: 16%)</div>
            <div class="market-box">Goles Totales<span>Más 2.5 (82%)</span></div>
            <div class="market-box">Anotador Clave<span>Vinícius Jr. (51%)</span></div>
        </div>
        <div class="market-section">
            <div class="market-title">🌪️ INFLUENCIA ULTRA-ESTOCÁSTICA</div>
            <ul class="factor-list">
                <li class="factor-item"><span style="color:var(--text-muted);">🩹 Bajas:</span><span class="factor-dinamico">Sin novedades médicas</span></li>
            </ul>
        </div>
        <button class="btn-clayton" onclick="recalcular('p4', 48, 22, 30, '3 - 1', '1.90')">PROCESAR EN VIVO</button>
    </div>

    <!-- PARTIDO 5 -->
    <div class="panel" id="p5">
        <div class="team-vs"><span>Man. City 🏴󠁧󠁢󠁥󠁮󠁧󠁿 vs Bayern Múnich 🇩🇪</span> <span class="cuota" style="color:var(--accent-green);">CUOTA: 1.65</span></div>
        <div class="prob-bar-container">
            <div class="prob-bar prob-local" style="width: 55%;">55% L</div>
            <div class="prob-bar prob-draw" style="width: 20%;">20% X</div>
            <div class="prob-bar prob-visit" style="width: 25%;">25% V</div>
        </div>
        <div class="market-grid">
