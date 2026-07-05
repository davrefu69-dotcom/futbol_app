from flask import Flask

app = Flask(__name__)

STAKE_STYLE_APP = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>CLAYTON ENGINE PRO</title>
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
        body { font-family: system-ui, -apple-system, sans-serif; background-color: var(--bg-dark); margin: 0; padding: 12px; color: var(--text-white); padding-bottom: 100px; }
        .container { max-width: 100%; margin: 0 auto; }
        
        header { background: var(--bg-card); border-bottom: 2px solid var(--accent-green); padding: 12px; text-align: center; border-radius: 8px; margin-bottom: 12px; }
        .logo { font-size: 16px; font-weight: 900; letter-spacing: 0.5px; }
        .logo span { color: var(--accent-green); }

        /* MÓDULO SUPERCOMBINADA DESTACADO */
        .premium-box { background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); border: 2px solid var(--accent-green); border-radius: 10px; padding: 12px; margin-bottom: 16px; }
        .premium-title { font-size: 12px; font-weight: 800; color: var(--accent-green); text-transform: uppercase; margin-bottom: 6px; }
        .premium-list { padding-left: 14px; margin: 0; font-size: 11px; color: #e2e8f0; line-height: 1.5; }
        .premium-list strong { color: var(--accent-gold); }

        /* TARJETA DE PARTIDO REAL */
        .match-panel { background: var(--bg-card); border-radius: 10px; padding: 12px; margin-bottom: 14px; border: 1px solid var(--border); }
        .match-info { font-size: 11px; color: var(--text-muted); display: flex; justify-content: space-between; margin-bottom: 6px; }
        .teams { font-size: 15px; font-weight: 800; margin-bottom: 10px; color: #fff; }
        
        /* BLOQUES DE INFORMACIÓN DIRECTA */
        .data-row { background: var(--bg-inner); padding: 8px 10px; border-radius: 6px; margin-bottom: 6px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; }
        .data-label { color: var(--text-muted); font-weight: 600; font-size: 11px; text-transform: uppercase; }
        .data-value { font-weight: 700; color: #fff; }
        .highlight-gold { color: var(--accent-gold); font-size: 14px; }
        .highlight-green { color: var(--accent-green); }

        /* BOTONES DE CASAS DE APUESTAS (1X2) */
        .odds-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-top: 10px; }
        .odd-item { background: var(--bg-inner); border: 1px solid var(--border); padding: 8px; border-radius: 6px; text-align: center; color: #fff; cursor: pointer; font-size: 11px; font-weight: bold; }
        .odd-item span { display: block; font-size: 9px; color: var(--text-muted); margin-bottom: 2px; }
        .odd-item strong { color: var(--accent-green); font-size: 13px; }
        .odd-item.selected { background: var(--accent-green) !important; color: #000 !important; }
        .odd-item.selected strong, .odd-item.selected span { color: #000 !important; }

        /* BOLETO FLOTANTE ABAJO */
        .ticket-bar { position: fixed; bottom: 0; left: 0; right: 0; background: var(--bg-card); border-top: 3px solid var(--accent-green); padding: 12px; display: none; box-shadow: 0 -5px 15px rgba(0,0,0,0.5); }
        .ticket-flex { display: flex; justify-content: space-between; font-size: 12px; font-weight: bold; align-items: center; }
        .bet-input { background: var(--bg-inner); border: 1px solid var(--border); color: #fff; padding: 6px; width: 50px; text-align: center; border-radius: 4px; font-weight: bold; }
        .btn-bet { width: 100%; background: var(--accent-green); color: #000; border: none; padding: 10px; border-radius: 6px; font-weight: 800; font-size: 12px; text-transform: uppercase; margin-top: 8px; }
    </style>
</head>
<body>
<div class="container">

    <header>
        <div class="logo">🎯 CLAYTON <span>MATCH CENTER v5</span></div>
    </header>

    <!-- BLOQUE GLOBAL DE APUESTAS COMBINADAS SEGURAS -->
    <div class="premium-box">
        <div class="premium-title">🔒 COMBINADA DE ÉXITO SEGURO (CONFIANZA GLOBAL: 84%)</div>
        <ul class="premium-list">
            <li>⚽ Brasil vs Noruega ➔ <strong>Más de 1.5 Goles</strong> (95% Éxito)</li>
            <li>⚽ R. Madrid vs Barcelona ➔ <strong>Ambos marcan gol</strong> (92% Éxito)</li>
            <li>⚽ Argentina vs Francia ➔ <strong>Más de 2.5 Tarjetas</strong> (89% Éxito)</li>
        </ul>
    </div>

    <!-- PARTIDO 1 -->
    <div class="match-panel">
        <div class="match-info"><span>Copa del Mundo 🏆</span> <span style="color:var(--accent-green);">En Vivo</span></div>
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
            <span class="data-label">🌪️ Factores de Entorno</span>
            <span class="data-value highlight-green">29°C + Humedad Alta (Ventaja Local)</span>
        </div>

        <div class="odds-grid">
            <div class="odd-item" onclick="marcarCuota(this, 1.85)"><span>Gana Local</span><strong>1.85</strong></div>
            <div class="odd-item" onclick="marcarCuota(this, 3.40)"><span>Empate</span><strong>3.40</strong></div>
            <div class="odd-item" onclick="marcarCuota(this, 4.20)"><span>Gana Visita</span><strong>4.20</strong></div>
        </div>
    </div>

    <!-- PARTIDO 2 -->
    <div class="match-panel">
        <div class="match-info"><span>Copa del Mundo 🏆</span> <span>Hoy | 22:00h</span></div>
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
            <span class="data-label">🌪️ Factores de Entorno</span>
            <span class="data-value highlight-green">Altitud Estadio Azteca (Ahoga Visita)</span>
        </div>

        <div class="odds-grid">
            <div class="odd-item" onclick="marcarCuota(this, 3.20)"><span>Gana Local</span><strong>3.20</strong></div>
            <div class="odd-item" onclick="marcarCuota(this, 3.10)"><span>Empate</span><strong>3.10</strong></div>
            <div class="odd-item" onclick="marcarCuota(this, 2.10)"><span>Gana Visita</span><strong>2.10</strong></div>
        </div>
    </div>

    <!-- PARTIDO 3 -->
    <div class="match-panel">
        <div class="match-info"><span>Amistoso Internacional 🌍</span> <span>Hoy | 23:45h</span></div>
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
            <span class="data-label">🌪️ Factores de Entorno</span>
            <span class="data-value highlight-green">H2H Reciente Directo Histórico Alto</span>
        </div>

        <div class="odds-grid">
            <div class="odd-item" onclick="marcarCuota(this, 2.45)"><span>Gana Local</span><strong>2.45</strong></div>
            <div class="odd-item" onclick="marcarCuota(this, 3.20)"><span>Empate</span><strong>3.20</strong></div>
            <div class="odd-item" onclick="marcarCuota(this, 2.60)"><span>Gana Visita</span><strong>2.60</strong></div>
        </div>
    </div>

    <!-- PARTIDO 4 -->
    <div class="match-panel">
        <div class="match-info"><span>El Clásico 🇪🇸</span> <span>Mañana | 21:00h</span></div>
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
            <span class="data-label">🌪️ Factores de Entorno</span>
