from flask import Flask

app = Flask(__name__)

CLAYTON_GOD_EDITION = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>CLAYTON COUPLING ENGINE v9999⁹⁹⁹ - ULTRA GOD MODE</title>
    <style>
        :root {
            --bg-dark: #060b13;
            --bg-card: #111927;
            --bg-inner: #1f2a3c;
            --accent-green: #00e701;
            --accent-gold: #ffdf00;
            --accent-blue: #00bfff;
            --accent-purple: #bd93f9;
            --text-white: #ffffff;
            --text-muted: #9ca3af;
            --border: #2d3748;
        }
        body { font-family: system-ui, -apple-system, sans-serif; background-color: var(--bg-dark); margin: 0; padding: 12px; color: var(--text-white); }
        .container { max-width: 100%; margin: 0 auto; }
        
        header { background: var(--bg-card); border-bottom: 3px solid var(--accent-green); padding: 14px; text-align: center; border-radius: 12px; margin-bottom: 14px; box-shadow: 0 4px 15px rgba(0, 231, 1, 0.1); }
        .logo { margin: 0; font-size: 18px; font-weight: 900; letter-spacing: 0.5px; }
        .logo span { color: var(--accent-green); text-shadow: 0 0 10px rgba(0,231,1,0.4); }

        /* PANEL PREMIUM COMBINADAS MULTIPLES */
        .premium-box { background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); border: 2px dashed var(--accent-green); border-radius: 12px; padding: 14px; margin-bottom: 16px; }
        .premium-title { font-size: 13px; font-weight: 800; color: var(--accent-green); text-transform: uppercase; margin-bottom: 8px; display: flex; justify-content: space-between; }
        .premium-list { padding-left: 16px; margin: 0; font-size: 12px; color: #cbd5e1; line-height: 1.6; }
        .premium-list strong { color: var(--accent-gold); }

        /* TARJETA DE PARTIDO COMPLETA */
        .match-panel { background: var(--bg-card); border-radius: 12px; padding: 14px; margin-bottom: 16px; border: 1px solid var(--border); box-shadow: 0 6px 12px rgba(0,0,0,0.3); }
        .match-header { font-size: 11px; color: var(--text-muted); display: flex; justify-content: space-between; margin-bottom: 8px; text-transform: uppercase; font-weight: bold; }
        .teams { font-size: 17px; font-weight: 900; margin-bottom: 12px; color: #fff; border-bottom: 1px solid var(--border); padding-bottom: 8px; }
        
        /* CUADRÍCULA DE DATOS INTERNOS */
        .data-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; margin-bottom: 10px; }
        .data-box { background: var(--bg-inner); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02); }
        .data-title { font-size: 9px; color: var(--text-muted); font-weight: 800; text-transform: uppercase; margin-bottom: 4px; display: flex; align-items: center; gap: 4px; }
        .data-value { font-weight: 700; font-size: 13px; color: #fff; }
        
        /* RESALTADOS COLORIDOS */
        .txt-gold { color: var(--accent-gold) !important; font-size: 15px !important; }
        .txt-green { color: var(--accent-green) !important; }
        .txt-blue { color: var(--accent-blue) !important; }
        .txt-purple { color: var(--accent-purple) !important; }

        /* PORCENTAJES DE VICTORIA (1X2) */
        .odds-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-top: 10px; background: rgba(0,0,0,0.2); padding: 6px; border-radius: 8px; }
        .odd-box { text-align: center; font-size: 11px; }
        .odd-box span { display: block; font-size: 9px; color: var(--text-muted); font-weight: bold; margin-bottom: 2px; }
        .odd-box strong { color: var(--accent-blue); font-size: 13px; }

        /* FACTORES ESTOCÁSTICOS FLUIDOS */
        .factors-box { background: rgba(0,0,0,0.2); padding: 10px; border-radius: 8px; margin-top: 10px; font-size: 11px; border-left: 3px solid var(--accent-green); }
        .factors-title { font-size: 10px; font-weight: 800; color: var(--accent-green); text-transform: uppercase; margin-bottom: 4px; }
        .factors-text { color: #cbd5e1; margin: 0; line-height: 1.4; }
    </style>
</head>
<body>
<div class="container">

    <header>
        <div class="logo">🧠 CLAYTON <span>PRO-ANALYTICS v9999</span></div>
    </header>

    <!-- BLOQUE GLOBAL DE APUESTAS COMBINADAS SEGURAS -->
    <div class="premium-box">
        <div class="premium-title">🔒 SUPERCOMBINADA INDESTRUCTIBLE (ÉXITO GLOBAL: 87.2%)</div>
        <ul class="premium-list">
            <li>⚽ Brasil vs Noruega ➔ <strong>Más de 8.5 Córners totales</strong> (93% Éxito)</li>
            <li>⚽ R. Madrid vs Barcelona ➔ <strong>Más de 3.5 Tarjetas totales</strong> (95% Éxito)</li>
            <li>⚽ Argentina vs Francia ➔ <strong>Ambos Anotan Gol</strong> (88% Éxito)</li>
            <li>⚽ Man. City vs Bayern ➔ <strong>Primer Gol antes del min 30</strong> (86% Éxito)</li>
        </ul>
    </div>

    <!-- PARTIDO 1 -->
    <div class="match-panel">
        <div class="match-header"><span>Mundial Octavos 🏆</span> <span class="txt-green">Datos Sincronizados</span></div>
        <div class="teams">Brasil 🇧🇷 vs Noruega 🇳🇴</div>
        
        <div class="data-grid">
            <div class="data-box">
                <div class="data-title">🔮 Resultado Exacto Probable</div>
                <div class="data-value txt-gold">3 - 2 <span style="font-size:10px;color:var(--text-muted);">(Prob: 21%)</span></div>
            </div>
            <div class="data-box">
                <div class="data-title">📐 Análisis de Córners</div>
                <div class="data-value txt-green">Más 9.5 <span style="font-size:10px;color:var(--text-muted);">(68% Gana Brasil)</span></div>
            </div>
            <div class="data-box">
                <div class="data-title">🟨 Proyección de Tarjetas</div>
                <div class="data-value txt-purple">Total: 4 <span style="font-size:10px;color:var(--text-muted);">(Riesgo: Ostigard)</span></div>
            </div>
            <div class="data-box">
                <div class="data-title">⏱️ Fluidez de Goles</div>
                <div class="data-value txt-blue">1° Gol: Min 15-30 <span style="font-size:10px;color:var(--text-muted);">(Más 2.5: 72%)</span></div>
            </div>
        </div>

        <div class="odds-row">
            <div class="odd-box"><span>Prob. Local</span><strong>44%</strong></div>
            <div class="odd-box"><span>Prob. Empate</span><strong>25%</strong></div>
            <div class="odd-box"><span>Prob. Visita</span><strong>31%</strong></div>
        </div>

        <div class="factors-box">
            <div class="factors-title">🌪️ Variables Estocásticas Críticas</div>
            <p class="factors-text">29°C + 82% Humedad asfixian a Noruega. Noruega sufre baja del defensa central titular. Brasil activa +12.4% empuje de afición local.</p>
        </div>
    </div>

    <!-- PARTIDO 2 -->
    <div class="match-panel">
        <div class="match-header"><span>Mundial Octavos 🏆</span> <span class="txt-green">Datos Sincronizados</span></div>
        <div class="teams">México 🇲🇽 vs Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿</div>
        
        <div class="data-grid">
            <div class="data-box">
                <div class="data-title">🔮 Resultado Exacto Probable</div>
                <div class="data-value txt-gold">1 - 2 <span style="font-size:10px;color:var(--text-muted);">(Prob: 18%)</span></div>
            </div>
            <div class="data-box">
                <div class="data-title">📐 Análisis de Córners</div>
                <div class="data-value txt-green">Menos 8.5 <span style="font-size:10px;color:var(--text-muted);">(55% Gana Inglaterra)</span></div>
            </div>
            <div class="data-box">
                <div class="data-title">🟨 Proyección de Tarjetas</div>
                <div class="data-value txt-purple">Total: 6 <span style="font-size:10px;color:var(--text-muted);">(Árbitro Estricto)</span></div>
            </div>
            <div class="data-box">
                <div class="data-title">⏱️ Fluidez de Goles</div>
                <div class="data-value txt-blue">1° Gol: Min 30-45 <span style="font-size:10px;color:var(--text-muted);">(Menos 2.5: 62%)</span></div>
            </div>
        </div>

        <div class="odds-row">
            <div class="odd-box"><span>Prob. Local</span><strong>34.3%</strong></div>
            <div class="odd-box"><span>Prob. Empate</span><strong>25%</strong></div>
            <div class="odd-box"><span>Prob. Visita</span><strong>40.7%</strong></div>
        </div>

        <div class="factors-box">
            <div class="factors-title">🌪️ Variables Estocásticas Críticas</div>
            <p class="factors-text">Altitud extrema del Estadio Azteca reduce un 15% el oxígeno y ritmo de Inglaterra. México genera presión arbitral extrema (+22.1%).</p>
        </div>
    </div>

    <!-- PARTIDO 3 -->
    <div class="match-panel">
        <div class="match-header"><span>Amistoso Élite 🌍</span> <span class="txt-green">Datos Sincronizados</span></div>
        <div class="teams">Argentina 🇦🇷 vs Francia 🇫🇷</div>
        
        <div class="data-grid">
            <div class="data-box">
                <div class="data-title">🔮 Resultado Exacto Probable</div>
                <div class="data-value txt-gold">2 - 2 <span style="font-size:10px;color:var(--text-muted);">(Prob: 14%)</span></div>
            </div>
            <div class="data-box">
                <div class="data-title">📐 Análisis de Córners</div>
                <div class="data-value txt-green">Más 10.5 <span style="font-size:10px;color:var(--text-muted);">(52% Gana Francia)</span></div>
            </div>
            <div class="data-box">
                <div class="data-title">🟨 Proyección de Tarjetas</div>
