from flask import Flask

app = Flask(__name__)

BETTING_APP_REAL = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>CLAYTON BETS v5</title>
    <style>
        :root {
            --bg-darker: #0b0e14;
            --bg-panel: #151a22;
            --bg-button: #202732;
            --accent-green: #00e701;
            --accent-gold: #f5a623;
            --text-white: #ffffff;
            --text-gray: #8a96a3;
            --border-line: #2a3543;
        }
        body { font-family: -apple-system, system-ui, sans-serif; background-color: var(--bg-darker); margin: 0; padding: 0; color: var(--text-white); padding-bottom: 90px; }
        
        /* Barra de Navegación de Deportes */
        .sports-nav { display: flex; overflow-x: auto; background: var(--bg-panel); padding: 10px; gap: 8px; border-bottom: 1px solid var(--border-line); white-space: nowrap; }
        .sport-chip { background: var(--bg-button); padding: 8px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; color: var(--text-gray); border: 1px solid transparent; }
        .sport-chip.active { background: rgba(0, 231, 1, 0.1); border-color: var(--accent-green); color: var(--accent-green); }
        
        /* Cabecera del Evento */
        .league-title { font-size: 11px; font-weight: 700; color: var(--text-gray); text-transform: uppercase; padding: 14px 12px 4px 12px; display: flex; justify-content: space-between; }
        
        /* Tarjeta de Partido Estilo Profesional */
        .match-card { background: var(--bg-panel); margin: 0 12px 10px 12px; border-radius: 8px; padding: 12px; border: 1px solid rgba(255,255,255,0.02); }
        .teams-container { font-size: 14px; font-weight: 700; margin-bottom: 10px; display: flex; flex-direction: column; gap: 4px; }
        .team-row { display: flex; justify-content: space-between; align-items: center; }
        .team-row span { font-weight: 400; font-size: 11px; color: var(--text-gray); }
        
        /* Botones de Cuotas (Odds) */
        .odds-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 8px; }
        .odd-btn { background: var(--bg-button); border: 1px solid var(--border-line); border-radius: 6px; padding: 10px; color: var(--text-white); cursor: pointer; text-align: center; transition: all 0.2s ease; }
        .odd-btn span { display: block; font-size: 10px; color: var(--text-gray); font-weight: bold; text-transform: uppercase; margin-bottom: 2px; }
        .odd-btn strong { font-size: 14px; color: var(--accent-green); }
        .odd-btn.selected { background: var(--accent-green) !important; color: #000 !important; border-color: var(--accent-green); }
        .odd-btn.selected span, .odd-btn.selected strong { color: #000 !important; }

        /* Panel Desplegable de Pronóstico */
        .forecast-panel { background: rgba(0,0,0,0.15); border-radius: 6px; margin-top: 8px; padding: 10px; font-size: 11px; border-left: 3px solid var(--accent-gold); display: none; }
        .forecast-grid { display: flex; justify-content: space-between; margin-bottom: 4px; }
        .forecast-grid strong { color: var(--accent-gold); }

        .btn-analizar { width: 100%; background: transparent; border: 1px solid var(--border-line); color: var(--text-gray); padding: 6px; font-size: 11px; border-radius: 4px; margin-top: 6px; font-weight: bold; }

        /* Ticket / Boleto de Apuestas Abajo */
        .bet-slip { position: fixed; bottom: 0; left: 0; right: 0; background: var(--bg-panel); border-top: 2px solid var(--accent-green); padding: 14px; display: none; box-shadow: 0 -4px 15px rgba(0,0,0,0.5); z-index: 100; }
        .slip-header { display: flex; justify-content: space-between; font-size: 13px; font-weight: 800; margin-bottom: 10px; text-transform: uppercase; }
        .slip-summary { display: flex; justify-content: space-between; align-items: center; background: var(--bg-darker); padding: 10px; border-radius: 6px; font-size: 12px; }
        .slip-summary input { background: transparent; border: none; color: #fff; font-size: 14px; font-weight: bold; text-align: right; width: 60px; outline: none; border-bottom: 1px solid var(--border-line); }
        .btn-place-bet { width: 100%; background: var(--accent-green); color: #000; border: none; padding: 12px; font-weight: 800; font-size: 13px; border-radius: 6px; text-transform: uppercase; margin-top: 10px; letter-spacing: 0.5px; }
    </style>
</head>
<body>

    <!-- Selector de Deportes de la App -->
    <div class="sports-nav">
        <div class="sport-chip active">⚽ Fútbol</div>
        <div class="sport-chip">🏀 Baloncesto</div>
        <div class="sport-chip">🎾 Tenis</div>
        <div class="sport-chip">🎮 eSports</div>
    </div>

    <div class="league-title"> Copa del Mundo 🏆 <span>Mercados principales</span></div>

    <!-- PARTIDO 1 -->
    <div class="match-card" id="m1">
        <div class="teams-container">
            <div class="team-row">Brasil 🇧🇷 <span>Goles prom: 2.64</span></div>
            <div class="team-row">Noruega 🇳🇴 <span>Goles prom: 1.85</span></div>
        </div>
        <div class="odds-row">
            <div class="odd-btn" onclick="selectOdd(this, 'Brasil', 1.85, 'Brasil vs Noruega')"><span>1</span><strong>1.85</strong></div>
            <div class="odd-btn" onclick="selectOdd(this, 'Empate', 3.40, 'Brasil vs Noruega')"><span>X</span><strong>3.40</strong></div>
            <div class="odd-btn" onclick="selectOdd(this, 'Noruega', 4.20, 'Brasil vs Noruega')"><span>2</span><strong>4.20</strong></div>
        </div>
        <button class="btn-analizar" onclick="toggleForecast('m1-f')">🤖 FACTORES Y PRONÓSTICO CLAYTON</button>
        <div class="forecast-panel" id="m1-f">
            <div class="forecast-grid">🎯 Resultado Probable: <strong>3 - 2</strong> <span>(Prob: 21%)</span></div>
            <div class="forecast-grid">👟 Anotador Clave: <span>Haaland (64%)</span></div>
            <div class="forecast-grid">🌡️ Factor Influyente: <span>29°C + 82% Humedad (Sufre Noruega)</span></div>
        </div>
    </div>

    <!-- PARTIDO 2 -->
    <div class="match-card" id="m2">
        <div class="teams-container">
            <div class="team-row">México 🇲🇽 <span>Goles prom: 1.10</span></div>
            <div class="team-row">Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿 <span>Goles prom: 2.10</span></div>
        </div>
        <div class="odds-row">
            <div class="odd-btn" onclick="selectOdd(this, 'México', 3.20, 'México vs Inglaterra')"><span>1</span><strong>3.20</strong></div>
            <div class="odd-btn" onclick="selectOdd(this, 'Empate', 3.10, 'México vs Inglaterra')"><span>X</span><strong>3.10</strong></div>
            <div class="odd-btn" onclick="selectOdd(this, 'Inglaterra', 2.10, 'México vs Inglaterra')"><span>2</span><strong>2.10</strong></div>
        </div>
        <button class="btn-analizar" onclick="toggleForecast('m2-f')">🤖 FACTORES Y PRONÓSTICO CLAYTON</button>
        <div class="forecast-panel" id="m2-f">
            <div class="forecast-grid">🎯 Resultado Probable: <strong>1 - 2</strong> <span>(Prob: 18%)</span></div>
            <div class="forecast-grid">👟 Anotador Clave: <span>Harry Kane (55%)</span></div>
            <div class="forecast-grid">🏔️ Factor Influyente: <span>Altitud Estadio Azteca (Ahoga a Inglaterra)</span></div>
        </div>
    </div>

    <!-- PARTIDO 3 -->
    <div class="match-card" id="m3">
        <div class="teams-container">
            <div class="team-row">Argentina 🇦🇷 <span>Goles prom: 2.30</span></div>
            <div class="team-row">Francia 🇫🇷 <span>Goles prom: 2.40</span></div>
        </div>
        <div class="odds-row">
            <div class="odd-btn" onclick="selectOdd(this, 'Argentina', 2.45, 'Argentina vs Francia')"><span>1</span><strong>2.45</strong></div>
            <div class="odd-btn" onclick="selectOdd(this, 'Empate', 3.20, 'Argentina vs Francia')"><span>X</span><strong>3.20</strong></div>
            <div class="odd-btn" onclick="selectOdd(this, 'Francia', 2.60, 'Argentina vs Francia')"><span>2</span><strong>2.60</strong></div>
        </div>
        <button class="btn-analizar" onclick="toggleForecast('m3-f')">🤖 FACTORES Y PRONÓSTICO CLAYTON</button>
        <div class="forecast-panel" id="m3-f">
            <div class="forecast-grid">🎯 Resultado Probable: <strong>2 - 2</strong> <span>(Prob: 14%)</span></div>
            <div class="forecast-grid">👟 Anotador Clave: <span>Mbappé (59%)</span></div>
            <div class="forecast-grid">⚔️ Factor Influyente: <span>H2H con alta tasa de goles (+3.5)</span></div>
        </div>
    </div>

    <!-- PARTIDO 4 -->
    <div class="match-card" id="m4">
        <div class="teams-container">
            <div class="team-row">Real Madrid 🇪🇸 <span>Goles prom: 2.80</span></div>
            <div class="team-row">Barcelona 🇪🇸 <span>Goles prom: 1.90</span></div>
        </div>
        <div class="odds-row">
            <div class="odd-btn" onclick="selectOdd(this, 'Real Madrid', 1.90, 'R. Madrid vs Barcelona')"><span>1</span><strong>1.90</strong></div>
            <div class="odd-btn" onclick="selectOdd(this, 'Empate', 3.80, 'R. Madrid vs Barcelona')"><span>X</span><strong>3.80</strong></div>
            <div class="odd-btn" onclick="selectOdd(this, 'Barcelona', 3.40, 'R. Madrid vs Barcelona')"><span>2</span><strong>3.40</strong></div>
        </div>
        <button class="btn-analizar" onclick="toggleForecast('m4-f')">🤖 FACTORES Y PRONÓSTICO CLAYTON</button>
        <div class="forecast-panel" id="m4-f">
            <div class="forecast-grid">🎯 Resultado Probable: <strong>3 - 1</strong> <span>(Prob: 16%)</span></div>
            <div class="forecast-grid">👟 Anotador Clave: <span>Vinícius Jr (51%)</span></div>
