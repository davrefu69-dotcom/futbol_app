from flask import Flask

app = Flask(__name__)

CLAYTON_REAL_TIME = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>CLAYTON ENGINE - DATA EN VIVO</title>
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
        
        header { background: var(--bg-card); border-bottom: 3px solid var(--accent-green); padding: 14px; text-align: center; border-radius: 12px; margin-bottom: 14px; }
        .logo { margin: 0; font-size: 18px; font-weight: 900; }
        .logo span { color: var(--accent-green); }

        .premium-box { background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); border: 2px dashed var(--accent-green); border-radius: 12px; padding: 14px; margin-bottom: 16px; }
        .premium-title { font-size: 13px; font-weight: 800; color: var(--accent-green); text-transform: uppercase; margin-bottom: 8px; }
        .premium-list { padding-left: 16px; margin: 0; font-size: 12px; color: #cbd5e1; line-height: 1.6; }

        .panel { background: var(--bg-card); border-radius: 12px; padding: 14px; margin-bottom: 16px; border: 1px solid var(--border); }
        .match-header { font-size: 11px; color: var(--text-muted); display: flex; justify-content: space-between; margin-bottom: 8px; text-transform: uppercase; font-weight: bold; }
        .teams { font-size: 17px; font-weight: 900; margin-bottom: 12px; color: #fff; border-bottom: 1px solid var(--border); padding-bottom: 8px; }
        
        .data-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; margin-bottom: 10px; }
        .data-box { background: var(--bg-inner); padding: 10px; border-radius: 8px; }
        .data-title { font-size: 9px; color: var(--text-muted); font-weight: 800; text-transform: uppercase; margin-bottom: 4px; }
        .data-value { font-weight: 700; font-size: 13px; color: #fff; }
        
        .txt-gold { color: var(--accent-gold) !important; font-size: 15px !important; }
        .txt-green { color: var(--accent-green) !important; }
        .txt-blue { color: var(--accent-blue) !important; }
        .txt-purple { color: var(--accent-purple) !important; }

        .odds-row { display: flex; justify-content: space-around; background: rgba(0,0,0,0.2); padding: 8px; border-radius: 8px; margin-top: 10px; font-size: 11px; }
        .factors-box { background: rgba(0,0,0,0.2); padding: 10px; border-radius: 8px; margin-top: 10px; font-size: 11px; border-left: 3px solid var(--accent-green); }
    </style>
</head>
<body>
<div class="container">

    <header>
        <div class="logo">🧠 CLAYTON <span>PRO-ANALYTICS v5</span></div>
    </header>

    <div class="premium-box">
        <div class="premium-title">🔒 SUPERCOMBINADA DE ÉXITO ESTOCÁSTICO (2 DÍAS ACTUALES)</div>
        <ul class="premium-list">
            <li>⚽ Brasil vs Noruega ➔ <strong>Más de 8.5 Córners totales</strong> (93% Confianza)</li>
            <li>⚽ México vs Inglaterra ➔ <strong>Más de 3.5 Tarjetas totales</strong> (95% Confianza)</li>
            <li>⚽ Portugal vs España ➔ <strong>Ambos Anotan Gol</strong> (88% Confianza)</li>
        </ul>
    </div>

    <!-- PARTIDO 1 -->
    <div class="panel">
        <div class="match-header"><span>Mundial Octavos 🏆</span> <span class="txt-green">Hoy (5 Julio)</span></div>
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
        <div class="odds"><span>L: 44%</span><span>X: 25%</span><span>V: 31%</span></div>
        <div class="factors-box">
            <p style="margin:0;color:#cbd5e1;line-height:1.4;"><b>Variables Críticas:</b> 29°C + 82% Humedad asfixian a Noruega. Noruega sufre baja del defensa central titular. Brasil activa +12.4% empuje local.</p>
        </div>
    </div>

    <!-- PARTIDO 2 -->
    <div class="panel">
        <div class="match-header"><span>Mundial Octavos 🏆</span> <span class="txt-green">Hoy (5 Julio)</span></div>
        <div class="teams">Estados Unidos 🇺🇸 vs Bélgica 🇧🇪</div>
        
        <div class="data-grid">
            <div class="data-box">
                <div class="data-title">🔮 Resultado Exacto Probable</div>
                <div class="data-value txt-gold">1 - 1 <span style="font-size:10px;color:var(--text-muted);">(Prob: 28%)</span></div>
            </div>
            <div class="data-box">
                <div class="data-title">📐 Análisis de Córners</div>
                <div class="data-value txt-green">Más 10.5 <span style="font-size:10px;color:var(--text-muted);">(61% Gana Bélgica)</span></div>
            </div>
            <div class="data-box">
                <div class="data-title">🟨 Proyección de Tarjetas</div>
                <div class="data-value txt-purple">Total: 3 <span style="font-size:10px;color:var(--text-muted);">(Partido Limpio)</span></div>
            </div>
            <div class="data-box">
                <div class="data-title">⏱️ Fluidez de Goles</div>
                <div class="data-value txt-blue">1° Gol: Min 45-60 <span style="font-size:10px;color:var(--text-muted);">(Menos 2.5: 67%)</span></div>
            </div>
        </div>
        <div class="odds"><span>L: 29%</span><span>X: 28%</span><span>V: 43%</span></div>
        <div class="factors-box">
            <p style="margin:0;color:#cbd5e1;line-height:1.4;"><b>Variables Críticas:</b> Localía masiva para EE.UU. en Seattle. Bélgica llega con mayor ritmo de pases en medio campo pero con fatiga acumulada en la delantera.</p>
        </div>
    </div>

    <!-- PARTIDO 3 -->
    <div class="panel">
        <div class="match-header"><span>Mundial Octavos 🏆</span> <span class="txt-green">Mañana (6 Julio)</span></div>
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
        <div class="odds"><span>L: 34.3%</span><span>X: 25%</span><span>V: 40.7%</span></div>
        <div class="factors-box">
            <p style="margin:0;color:#cbd5e1;line-height:1.4;"><b>Variables Críticas:</b> Altitud extrema del Estadio Azteca reduce 15% el oxígeno visitante. México genera presión arbitral extrema y busca romper su maldición.</p>
        </div>
    </div>

    <!-- PARTIDO 4 -->
    <div class="panel">
        <div class="match-header"><span>Mundial Octavos 🏆</span> <span class="txt-green">Mañana (6 Julio)</span></div>
        <div class="teams">Portugal 🇵🇹 vs España 🇪🇸</div>
        
        <div class="data-grid">
            <div class="data-box">
                <div class="data-title">🔮 Resultado Exacto Probable</div>
                <div class="data-value txt-gold">2 - 2 <span style="font-size:10px;color:var(--text-muted);">(Prob: 15%)</span></div>
            </div>
            <div class="data-box">
                <div class="data-title">📐 Análisis de Córners</div>
                <div class="data-value txt-green">Más 9.5 <span style="font-size:10px;color:var(--text-muted);">(58% Gana España)</span></div>
            </div>
            <div class="data-box">
                <div class="data-title">🟨 Proyección de Tarjetas</div>
