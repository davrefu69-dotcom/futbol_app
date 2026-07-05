from flask import Flask

app = Flask(__name__)

CLAYTON_CENTER_PURE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>CLAYTON MATCH CENTER v5</title>
    <style>
        :root {
            --bg-dark: #0f212e;
            --bg-card: #1a2c38;
            --bg-inner: #213743;
            --accent-green: #00e701;
            --accent-gold: #feeb1a;
            --accent-blue: #2f80ed;
            --text-white: #ffffff;
            --text-muted: #b1b6bb;
            --border: #2c3f4b;
        }
        body { font-family: system-ui, -apple-system, sans-serif; background-color: var(--bg-dark); margin: 0; padding: 12px; color: var(--text-white); }
        .container { max-width: 100%; margin: 0 auto; }
        
        header { background: var(--bg-card); border-bottom: 2px solid var(--accent-green); padding: 12px; text-align: center; border-radius: 8px; margin-bottom: 12px; }
        .logo { font-size: 16px; font-weight: 900; letter-spacing: 0.5px; }
        .logo span { color: var(--accent-green); }

        /* MÓDULO SUPERCOMBINADA DESTACADO */
        .premium-box { background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); border: 2px solid var(--accent-green); border-radius: 10px; padding: 12px; margin-bottom: 16px; }
        .premium-title { font-size: 12px; font-weight: 800; color: var(--accent-green); text-transform: uppercase; margin-bottom: 6px; }
        .premium-list { padding-left: 14px; margin: 0; font-size: 11px; color: #e2e8f0; line-height: 1.5; }
        .premium-list strong { color: var(--accent-gold); }

        /* TARJETA DE PARTIDO */
        .match-panel { background: var(--bg-card); border-radius: 10px; padding: 12px; margin-bottom: 14px; border: 1px solid var(--border); }
        .match-info { font-size: 11px; color: var(--text-muted); display: flex; justify-content: space-between; margin-bottom: 6px; }
        .teams { font-size: 15px; font-weight: 800; margin-bottom: 10px; color: #fff; }
        
        /* BLOQUES DE INFORMACIÓN DIRECTA */
        .data-row { background: var(--bg-inner); padding: 8px 10px; border-radius: 6px; margin-bottom: 6px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; }
        .data-label { color: var(--text-muted); font-weight: 600; font-size: 11px; text-transform: uppercase; }
        .data-value { font-weight: 700; color: #fff; }
        .highlight-gold { color: var(--accent-gold); font-size: 14px; }
        .highlight-green { color: var(--accent-green); }

        /* PROBABILIDADES DE RESULTADO FINAL (1X2) */
        .odds-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-top: 10px; }
        .odd-item { background: var(--bg-inner); border: 1px solid var(--border); padding: 8px; border-radius: 6px; text-align: center; color: #fff; font-size: 11px; font-weight: bold; }
        .odd-item span { display: block; font-size: 9px; color: var(--text-muted); margin-bottom: 2px; }
        .odd-item strong { color: var(--accent-blue); font-size: 13px; }
    </style>
</head>
<body>
<div class="container">

    <header>
        <div class="logo">🎯 CLAYTON <span>ANÁLISIS ESTOCÁSTICO v5</span></div>
    </header>

    <!-- BLOQUE GLOBAL DE APUESTAS COMBINADAS SEGURAS -->
    <div class="premium-box">
        <div class="premium-title">🔒 COMBINADA DE ÉXITO RECOMENDADA (CONFIANZA GLOBAL: 84%)</div>
        <ul class="premium-list">
            <li>⚽ Brasil vs Noruega ➔ <strong>Más de 1.5 Goles</strong> (95% Éxito)</li>
            <li>⚽ R. Madrid vs Barcelona ➔ <strong>Ambos marcan gol</strong> (92% Éxito)</li>
            <li>⚽ Argentina vs Francia ➔ <strong>Más de 2.5 Tarjetas</strong> (89% Éxito)</li>
        </ul>
    </div>

    <!-- PARTIDO 1 -->
    <div class="match-panel">
        <div class="match-info"><span>Copa del Mundo 🏆</span> <span style="color:var(--accent-green);">Análisis Sincronizado</span></div>
        <div class="teams">Brasil 🇧🇷 vs Noruega 🇳🇴</div>
        
        <div class="data-row">
            <span class="data-label">🔮 Resultado Exacto</span>
            <span class="data-value highlight-gold">3 - 2</span>
        </div>
        <div class="data-row">
            <span class="data-label">📈 Probabilidad Goles</span>
            <span class="data-value">Más de 2.5 Goles (72% Prob)</span>
        </div>
        <div class="data-row">
            <span class="data-label">👟 Quién Marcará</span>
            <span class="data-value">E. Haaland (64%) / Vinícius Jr (58%)</span>
        </div>
        <div class="data-row">
            <span class="data-label">🌪 shrink Factor Influyente</span>
            <span class="data-value highlight-green">29°C + Humedad Alta (Ventaja Local)</span>
        </div>

        <div class="odds-grid">
            <div class="odd-item"><span>Prob. Victoria Local</span><strong>44%</strong></div>
            <div class="odd-item"><span>Prob. Empate</span><strong>25%</strong></div>
            <div class="odd-item"><span>Prob. Victoria Visita</span><strong>31%</strong></div>
        </div>
    </div>

    <!-- PARTIDO 2 -->
    <div class="match-panel">
        <div class="match-info"><span>Copa del Mundo 🏆</span> <span>Análisis Sincronizado</span></div>
        <div class="teams">México 🇲🇽 vs Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿</div>
        
        <div class="data-row">
            <span class="data-label">🔮 Resultado Exacto</span>
            <span class="data-value highlight-gold">1 - 2</span>
        </div>
        <div class="data-row">
            <span class="data-label">📈 Probabilidad Goles</span>
            <span class="data-value">Menos de 2.5 Goles (62% Prob)</span>
        </div>
        <div class="data-row">
            <span class="data-label">👟 Quién Marcará</span>
            <span class="data-value">Harry Kane (55%) / S. Giménez (38%)</span>
        </div>
        <div class="data-row">
            <span class="data-label">🌪 Factor Influyente</span>
            <span class="data-value highlight-green">Altitud Estadio Azteca (Ahoga Visita)</span>
        </div>

        <div class="odds-grid">
            <div class="odd-item"><span>Prob. Victoria Local</span><strong>34%</strong></div>
            <div class="odd-item"><span>Prob. Empate</span><strong>25%</strong></div>
            <div class="odd-item"><span>Prob. Victoria Visita</span><strong>41%</strong></div>
        </div>
    </div>

    <!-- PARTIDO 3 -->
    <div class="match-panel">
        <div class="match-info"><span>Amistoso Internacional 🌍</span> <span>Análisis Sincronizado</span></div>
        <div class="teams">Argentina 🇦🇷 vs Francia 🇫🇷</div>
        
        <div class="data-row">
            <span class="data-label">🔮 Resultado Exacto</span>
            <span class="data-value highlight-gold">2 - 2</span>
        </div>
        <div class="data-row">
            <span class="data-label">📈 Probabilidad Goles</span>
            <span class="data-value">Ambos Anotan (88% Prob)</span>
        </div>
        <div class="data-row">
            <span class="data-label">👟 Quién Marcará</span>
            <span class="data-value">K. Mbappé (59%) / L. Messi (52%)</span>
        </div>
        <div class="data-row">
            <span class="data-label">🌪 Factor Influyente</span>
            <span class="data-value highlight-green">Historial H2H con Alta Tasa de Goles</span>
        </div>

        <div class="odds-grid">
            <div class="odd-item"><span>Prob. Victoria Local</span><strong>38%</strong></div>
            <div class="odd-item"><span>Prob. Empate</span><strong>29%</strong></div>
            <div class="odd-item"><span>Prob. Victoria Visita</span><strong>33%</strong></div>
        </div>
    </div>

    <!-- PARTIDO 4 -->
    <div class="match-panel">
        <div class="match-info"><span>El Clásico 🇪🇸</span> <span>Análisis Sincronizado</span></div>
        <div class="teams">Real Madrid 🇪🇸 vs Barcelona 🇪🇸</div>
        
        <div class="data-row">
            <span class="data-label">🔮 Resultado Exacto</span>
            <span class="data-value highlight-gold">3 - 1</span>
        </div>
        <div class="data-row">
            <span class="data-label">📈 Probabilidad Goles</span>
            <span class="data-value">Más de 2.5 Goles (82% Prob)</span>
        </div>
        <div class="data-row">
            <span class="data-label">👟 Quién Marcará</span>
            <span class="data-value">Vinícius Jr (51%) / R. Lewandowski (47%)</span>
        </div>
        <div class="data-row">
            <span class="data-label">🌪 Factor Influyente</span>
            <span class="data-value highlight-green">Barcelona llega sin Portero Titular</span>
        </div>

        <div class="odds-grid">
            <div class="odd-item"><span>Prob. Victoria Local</span><strong>48%</strong></div>
            <div class="odd-item"><span>Prob. Empate</span><strong>22%</strong></div>
            <div class="odd-item"><span>Prob. Victoria Visita</span><strong>30%</strong></div>
        </div>
    </div>

    <!-- PARTIDO 5 -->
    <div class="match-panel">
        <div class="match-info"><span>Champions League 🇪🇺</span> <span>Análisis Sincronizado</span></div>
        <div class="teams">Man. City 🏴󠁧󠁢󠁥󠁮󠁧󠁿 vs Bayern Múnich 🇩🇪</div>
        
        <div class="data-row">
            <span class="data-label">🔮 Resultado Exacto</span>
            <span class="data-value highlight-gold">2 - 0</span>
        </div>
        <div class="data-row">
            <span class="data-label">📈 Probabilidad Goles</span>
            <span class="data-value">Menos de 3.5 Goles (78% Prob)</span>
        </div>
        <div class="data-row">
            <span class="data-label">👟 Quién Marcará</span>
            <span class="data-value">K. De Bruyne (44%) / H. Kane (40%)</span>
        </div>
