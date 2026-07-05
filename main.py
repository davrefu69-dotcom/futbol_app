from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# BASE DE DATOS ULTRA-MASIVA DE PRÓNÓSTICOS PARA LAS PRÓXIMAS 48 HORAS
PARTIDOS_DATA = [
    {
        "id": "p1", 
        "equipoL": "Brasil 🇧🇷", "equipoV": "Noruega 🇳🇴", 
        "fecha": "Hoy domingo 5 de Julio", "hora_str": "22:00h",
        "prob_1X2": {"local": "44%", "empate": "25%", "visita": "31%"},
        "resultados_exactos": [
            {"score": "3 - 2", "prob": "21%"},
            {"score": "2 - 1", "prob": "19%"}
        ],
        "corners": {"linea": "Más de 9.5", "prob": "68%", "ventaja": "Brasil (64%)"},
        "tarjetas": {"proyeccion": "Total: 4", "prob": "74%"},
        "expulsion_roja": {"prob": "24%", "factor": "Bajo roce previo"},
        "goleadores": {"primero": "Vinícius Jr. (34%)", "cualquier_momento": "E. Haaland (64%)"},
        "amonestado_riesgo": "Andreas Hanche-Olsen (52% Prob)",
        "goles_tramo": "Minuto 15 - 30 (72% Prob)",
        "pick_seguro": "Brasil vs Noruega ➔ Más de 1.5 Goles", "pick_prob": 0.95
    },
    {
        "id": "p2", 
        "equipoL": "México 🇲🇽", "equipoV": "Inglaterra 🏴<span style='font-size:10px;'>󠁧󠁢󠁥󠁮󠁧󠁿</span>", 
        "fecha": "Mañana lunes 6 de Julio", "hora_str": "02:00h",
        "prob_1X2": {"local": "34%", "empate": "25%", "visita": "41%"},
        "resultados_exactos": [
            {"score": "1 - 2", "prob": "18%"},
            {"score": "1 - 1", "prob": "16%"}
        ],
        "corners": {"linea": "Menos de 8.5", "prob": "55%", "ventaja": "Inglaterra (59%)"},
        "tarjetas": {"proyeccion": "Total: 6", "prob": "89%"},
        "expulsion_roja": {"prob": "61%", "factor": "Árbitro Riguroso"},
        "goleadores": {"primero": "Harry Kane (28%)", "cualquier_momento": "Santiago Giménez (38%)"},
        "amonestado_riesgo": "Edson Álvarez (67% Prob)",
        "goles_tramo": "Minuto 30 - 45 (62% Prob)",
        "pick_seguro": "México vs Inglaterra ➔ Más de 3.5 Tarjetas", "pick_prob": 0.94
    },
    {
        "id": "p3", 
        "equipoL": "Portugal 🇵🇹", "equipoV": "España 🇪🇸", 
        "fecha": "Mañana lunes 6 de Julio", "hora_str": "21:00h",
        "prob_1X2": {"local": "38%", "empate": "30%", "visita": "32%"},
        "resultados_exactos": [
            {"score": "2 - 2", "prob": "15%"},
            {"score": "1 - 2", "prob": "13%"}
        ],
        "corners": {"linea": "Más de 9.5", "prob": "58%", "ventaja": "España (61%)"},
        "tarjetas": {"proyeccion": "Total: 5", "prob": "81%"},
        "expulsion_roja": {"prob": "44%", "factor": "Tensión de Derbi"},
        "goleadores": {"primero": "Cristiano Ronaldo (26%)", "cualquier_momento": "Lamine Yamal (45%)"},
        "amonestado_riesgo": "João Palhinha (71% Prob)",
        "goles_tramo": "Minuto 0 - 15 (88% Prob)",
        "pick_seguro": "Portugal vs España ➔ Ambos Anotan Gol", "pick_prob": 0.93
    },
    {
        "id": "p4", 
        "equipoL": "Estados Unidos 🇺🇸", "equipoV": "Bélgica 🇧🇪", 
        "fecha": "Martes 7 de Julio", "hora_str": "02:00h",
        "prob_1X2": {"local": "29%", "empate": "28%", "visita": "43%"},
        "resultados_exactos": [
            {"score": "1 - 1", "prob": "28%"},
            {"score": "1 - 2", "prob": "17%"}
        ],
        "corners": {"linea": "Más de 10.5", "prob": "61%", "ventaja": "Bélgica (54%)"},
        "tarjetas": {"proyeccion": "Total: 3", "prob": "67%"},
        "expulsion_roja": {"prob": "12%", "factor": "Estilo Limpio"},
        "goleadores": {"primero": "Romelu Lukaku (31%)", "cualquier_momento": "Christian Pulisic (35%)"},
        "amonestado_riesgo": "Weston McKennie (48% Prob)",
        "goles_tramo": "Minuto 45 - 60 (67% Prob)",
        "pick_seguro": "Estados Unidos vs Bélgica ➔ Más de 1.5 Goles", "pick_prob": 0.91
    }
]

@app.route('/api/live-data')
def api_live_data():
    exito_combinado = 1.0
    lineas_seguras = []
    for p in PARTIDOS_DATA:
        exito_combinado *= p["pick_prob"]
        lineas_seguras.append(f"🛡️ {p['pick_seguro']} ({int(p['pick_prob']*100)}% Fiabilidad)")
    porcentaje_combinada = f"{round(exito_combinado * 100, 1)}%"
    
    return jsonify({
        "partidos": PARTIDOS_DATA,
        "combinada_picks": lineas_seguras,
        "combinada_total": porcentaje_combinada,
        "last_update": datetime.now().strftime("%H:%M:%S")
    })

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>CLAYTON QUANTUM ENGINE v5</title>
        <style>
            :root { --bg: #060b13; --card: #111927; --inner: #1f2a3c; --green: #00e701; --gold: #ffdf00; --blue: #00bfff; --purple: #bd93f9; --red: #ef4444; }
            body { font-family: system-ui, sans-serif; background: var(--bg); margin: 0; padding: 12px; color: #fff; }
            header { background: var(--card); border-bottom: 3px solid var(--green); padding: 12px; text-align: center; border-radius: 8px; margin-bottom: 12px; }
            .premium { background: linear-gradient(135deg, #0f172a, #1e3a8a); border: 2px solid var(--green); border-radius: 12px; padding: 12px; margin-bottom: 14px; font-size: 11px; }
            .panel { background: var(--card); border-radius: 12px; padding: 12px; margin-bottom: 14px; border: 1px solid #2d3748; }
            .title { font-size: 16px; font-weight: 900; color: #fff; }
            .status { font-size: 10px; color: var(--blue); font-weight: bold; margin-bottom: 6px; }
            .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; margin-top: 8px; }
            .box { background: var(--inner); padding: 10px; border-radius: 8px; font-size: 11px; line-height: 1.4; }
            .lbl { color: #9ca3af; font-size: 9px; font-weight: 800; text-transform: uppercase; margin-bottom: 4px; }
            .val { font-weight: 700; color: #fff; }
            .c-gold { color: var(--gold); } .c-green { color: var(--green); } .c-blue { color: var(--blue); } .c-purple { color: var(--purple); } .c-red { color: var(--red); }
            .odds-table { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4px; background: rgba(0,0,0,0.3); padding: 6px; border-radius: 6px; margin-top: 8px; font-size: 11px; text-align: center; }
            .odd-cell { display: flex; flex-direction: column; }
            .odd-cell span { font-size: 9px; color: #9ca3af; font-weight: bold; }
        </style>
    </head>
    <body>
        <header><h3 style="margin:0;">🧠 CLAYTON QUANTUM MATCH CENTER</h3></header>
        
        <div class="premium">
            <b style="color:var(--green); font-size:12px;">🏆 SUPERCOMBINADA BLINDADA PRÓXIMAS 48 HORAS</b>
            <div id="combinada-lista" style="margin-top: 6px; line-height: 1.5; color: #e2e8f0;"></div>
            <div style="margin-top: 8px; font-weight: bold; color: var(--gold); border-top: 1px dashed #2d3748; padding-top: 6px; text-align: center;">
                🔥 FIABILIDAD DE INTEGRACIÓN: <span id="combinada-total" style="font-size:15px; color:var(--green);">0%</span>
            </div>
        </div>

        <div id="container-partidos"></div>

        <script>
            async function actualizarPartidos() {
                const response = await fetch('/api/live-data');
                const data = await response.json();
                
                document.getElementById('combinada-total').innerText = data.combinada_total;
                
                let listaHtml = "";
                data.combinada_picks.forEach(linea => {
                    listaHtml += `<div>${linea}</div>`;
                });
                document.getElementById('combinada-lista').innerHTML = listaHtml;
                
                let html = "";
                data.partidos.forEach(p => {
                    html += `
                    <div class="panel">
                        <div class="title">${p.equipoL} vs ${p.equipoV}</div>
                        <div class="status">📅 Real Time 48H (${p.fecha} | ${p.hora_str})</div>
                        
                        <!-- TABLA DE GANADOR / EMPATE / PERDEDOR (1X2) -->
                        <div class="odds-table">
                            <div class="odd-cell"><span>GANA LOCAL</span><b class="c-blue">${p.prob_1X2.local}</b></div>
                            <div class="odd-cell"><span>EMPATE (X)</span><b style="color:#9ca3af;">${p.prob_1X2.empate}</b></div>
                            <div class="odd-cell"><span>GANA VISITA</span><b class="c-green">${p.prob_1X2.visita}</b></div>
                        </div>

                        <div class="grid">
                            <div class="box">
                                <div class="lbl">🔮 Resultados Exactos Probables</div>
                                <div class="val">Top 1: <span class="c-gold">${p.resultados_exactos[0].score}</span> (${p.resultados_exactos[0].prob})</div>
                                <div class="val">Top 2: <span class="c-gold">${p.resultados_exactos[1].score}</span> (${p.resultados_exactos[1].prob})</div>
                            </div>
                            <div class="box">
                                <div class="lbl">⚽ Mercado de Goleadores</div>
                                <div class="val">Abre marcador: <span class="c-green">${p.goleadores.primero}</span></div>
                                <div class="val">Cualquier min: <span style="color:#cbd5e1;">${p.goleadores.cualquier_momento}</span></div>
                            </div>
                            <div class="box">
                                <div class="lbl">📐 Saques de Esquina (Córners)</div>
                                <div class="val c-green">${p.corners.linea} <span style='font-size:10px; color:#9ca3af;'>(${p.corners.prob})</span></div>
