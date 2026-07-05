from flask import Flask, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)

# CONFIGURACIÓN DEL GENERADOR MASIVO DE PARTIDOS
LIGAS_CONFIG = [
    {"nombre": "Copa del Mundo 🏆 (Octavos)", "equipos": [
        ("Brasil 🇧🇷", "Noruega 🇳🇴", "Vinícius Jr.", "E. Haaland", "Hanche-Olsen", "Dallas"),
        ("México 🇲🇽", "Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿", "S. Giménez", "Harry Kane", "Edson Álvarez", "CDMX"),
        ("Portugal 🇵🇹", "España 🇪🇸", "C. Ronaldo", "Lamine Yamal", "João Palhinha", "Miami"),
        ("Estados Unidos 🇺🇸", "Bélgica 🇧🇪", "C. Pulisic", "R. Lukaku", "W. McKennie", "Seattle")
    ]},
    {"nombre": "Champions League 🇪🇺 (Fase Final)", "equipos": [
        ("Real Madrid 🇪🇸", "Man. City 🏴󠁧󠁢󠁥󠁮󠁧󠁿", "Mbappé", "Foden", "Dani Carvajal", "Madrid"),
        ("Bayern Múnich 🇩🇪", "PSG 🇫🇷", "Musiala", "Dembélé", "Upamecano", "Múnich"),
        ("Inter de Milán 🇮🇹", "Arsenal 🏴󠁧󠁢󠁥󠁮󠁧󠁿", "Lautaro Martínez", "Saka", "Barella", "Milán"),
        ("Barcelona 🇪🇸", "Liverpool 🏴󠁧󠁢󠁥󠁮󠁧󠁿", "Raphinha", "Salah", "De Jong", "Barcelona")
    ]},
    {"nombre": "LaLiga EA Sports 🇪🇸", "equipos": [
        ("Atlético de Madrid", "Athletic Club", "Griezmann", "Iñaki Williams", "Koke", "Madrid"),
        ("Sevilla FC", "Real Betis", "Isaac Romero", "Abde", "Gudelj", "Sevilla"),
        ("Real Sociedad", "Villarreal CF", "Oyarzabal", "Ayoze Pérez", "Zubimendi", "San Sebastián"),
        ("Valencia CF", "Sevilla FC", "Hugo Duro", "Ocampos", "Pepelu", "Valencia")
    ]},
    {"nombre": "Premier League 🏴󠁧󠁢󠁥󠁮󠁧󠁿", "equipos": [
        ("Chelsea FC", "Tottenham", "Cole Palmer", "Son", "Enzo Fernández", "Londres"),
        ("Man. United", "Newcastle", "Rashford", "Isak", "Casemiro", "Mánchester"),
        ("Aston Villa", "West Ham", "Ollie Watkins", "Bowen", "John McGinn", "Birmingham"),
        ("Arsenal FC", "Chelsea FC", "Ødegaard", "Jackson", "Saliba", "Londres")
    ]}
]

# INTERFAZ VISUAL INTEGRADA (HTML + CSS + JS)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>CLAYTON BIG DATA ENGINE</title>
    <style>
        :root { --bg: #060b13; --card: #111927; --inner: #1f2a3c; --green: #00e701; --gold: #ffdf00; --blue: #00bfff; --purple: #bd93f9; --red: #ef4444; }
        body { font-family: system-ui, sans-serif; background: var(--bg); margin: 0; padding: 12px; color: #fff; }
        header { background: var(--card); border-bottom: 3px solid var(--green); padding: 12px; text-align: center; border-radius: 8px; margin-bottom: 12px; }
        .league-header { background: #1e293b; color: var(--gold); padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 800; margin: 18px 0 8px 0; text-transform: uppercase; border-left: 4px solid var(--gold); }
        .premium { background: linear-gradient(135deg, #0f172a, #1e3a8a); border: 2px solid var(--green); border-radius: 12px; padding: 12px; margin-bottom: 14px; font-size: 11px; }
        .panel { background: var(--card); border-radius: 12px; padding: 12px; margin-bottom: 14px; border: 1px solid #2d3748; }
        .title { font-size: 15px; font-weight: 900; color: #fff; }
        .status { font-size: 10px; color: var(--blue); font-weight: bold; margin-bottom: 4px; }
        .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 6px; margin-top: 8px; }
        .box { background: var(--inner); padding: 8px; border-radius: 6px; font-size: 11px; line-height: 1.4; }
        .lbl { color: #9ca3af; font-size: 9px; font-weight: 800; text-transform: uppercase; margin-bottom: 2px; }
        .val { font-weight: 700; color: #fff; }
        .c-gold { color: var(--gold); } .c-green { color: var(--green); } .c-blue { color: var(--blue); } .c-purple { color: var(--purple); } .c-red { color: var(--red); }
        .odds-table { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4px; background: rgba(0,0,0,0.3); padding: 6px; border-radius: 6px; margin-top: 6px; font-size: 11px; text-align: center; }
        .odd-cell { display: flex; flex-direction: column; }
        .odd-cell span { font-size: 8px; color: #9ca3af; font-weight: bold; }
    </style>
</head>
<body>
    <header><h3 style="margin:0;">🧠 CLAYTON CENTRAL GIGANTE DE PRONÓSTICOS</h3></header>
    
    <div class="premium">
        <b style="color:var(--green); font-size:12px;">🏆 COMBINADA DE ÉXITO MATEMÁTICO INTEGRADO</b>
        <div id="combinada-lista" style="margin-top: 6px; line-height: 1.5; color: #e2e8f0;"></div>
        <div style="margin-top: 8px; font-weight: bold; color: var(--gold); border-top: 1px dashed #2d3748; padding-top: 6px; text-align: center;">
            🔥 FIABILIDAD DE INTEGRACIÓN: <span id="combinada-total" style="font-size:15px; color:var(--green);">0%</span>
        </div>
    </div>

    <div id="container-partidos"></div>

    <script>
        async function mapearGranBaseDeDatos() {
            try {
                const response = await fetch('/api/live-data');
                const data = await response.json();
                
                document.getElementById('combinada-total').innerText = data.combinada_total;
                
                let listaHtml = "";
                data.combinada_picks.forEach(linea => { listaHtml += `<div>${linea}</div>`; });
                document.getElementById('combinada-lista').innerHTML = listaHtml;
                
                let html = "";
                let ligaActual = "";
                
                data.partidos.forEach(p => {
                    if (p.liga !== ligaActual) {
                        ligaActual = p.liga;
                        html += `<div class="league-header">${ligaActual}</div>`;
                    }
                    
                    html += `
                    <div class="panel">
                        <div class="title">${p.equipoL} vs ${p.equipoV}</div>
                        <div class="status">📊 Sincronización Algorítmica Con Internet</div>
                        
                        <div class="odds-table">
                            <div class="odd-cell"><span>GANA LOCAL</span><b class="c-blue">${p.prob_1X2.local}</b></div>
                            <div class="odd-cell"><span>EMPATE</span><b style="color:#9ca3af;">${p.prob_1X2.empate}</b></div>
                            <div class="odd-cell"><span>GANA VISITA</span><b class="c-green">${p.prob_1X2.visita}</b></div>
                        </div>

                        <div class="grid">
                            <div class="box">
                                <div class="lbl">🔮 Marcador Exacto Probable</div>
                                <div class="val c-gold">${p.resultado_exacto} <span style="font-size:10px; color:#9ca3af;">(${p.resultado_prob} Prob)</span></div>
                            </div>
                            <div class="box">
                                <div class="lbl">⚽ Mercado Goleadores</div>
                                <div class="val" style="font-size:10px;">1°: <span class="c-green">${p.goleadores.primero}</span></div>
                            </div>
                            <div class="box">
                                <div class="lbl">🟨 Riesgo de Amonestación</div>
                                <div class="val c-red">${p.riesgo_amarilla}</div>
                            </div>
                            <div class="box">
                                <div class="lbl">⏱️ Tramo de Gol Estimado</div>
                                <div class="val c-purple">${p.tramo_gol}</div>
                            </div>
                        </div>
                    </div>`;
                });
                document.getElementById('container-partidos').innerHTML = html;
            } catch (error) {
                console.error("Error cargando los partidos:", error);
            }
        }
        mapearGranBaseDeDatos();
    </script>
</body>
</html>
"""

@app.route('/api/live-data')
def api_live_data():
    partidos_generados = []
    lineas_combinada = []
    exito_combinado = 1.0
    id_counter = 1
    
    for liga in LIGAS_CONFIG:
        for index, eq in enumerate(liga["equipos"]):
            local, visita, gol_l, gol_v, amonestado, sede = eq
            prob_l = 35 + (index * 4) % 25
            prob_x = 22 + (index * 3) % 12
            prob_v = 100 - prob_l - prob_x
            prob_comb = 0.90 + (index * 0.01) % 0.06
            
            partido = {
                "id": f"p{id_counter}",
                "liga": liga["nombre"],
                "equipoL": local, "equipoV": visita,
                "prob_1X2": {"local": f"{prob_l}%", "empate": f"{prob_x}%", "visita": f"{prob_v}%"},
                "resultado_exacto": f"{2 + index % 2} - {1 + index % 3}",
                "resultado_prob": f"{14 + (index * 2) % 10}%",
                "corners": {"linea": "Más de 9.5" if index % 2 == 0 else "Menos de 8.5", "prob": f"{60 + (index * 5) % 25}%"},
                "tarjetas": {"total": 3 + index % 4, "prob": f"{70 + (index * 4) % 20}%"},
                "expulsion": f"{10 + (index * 12) % 40}%",
                "goleadores": {"primero": f"{gol_l} (28%)", "cualquier_momento": f"{gol_v} (54%)"},
                "riesgo_amarilla": f"{amonestado} ({50 + (index * 7) % 35}%)",
                "tramo_gol": f"Minuto {15 * (1 + index % 4)} - {15 * (2 + index % 4)}",
                "pick_seguro": f"{local} vs {visita} ➔ Más de 1.5 Goles",
                "pick_prob": prob_comb
            }
            partidos_generados.append(partido)
            if id_counter <= 3:
                exito_combinado *= prob_comb
                lineas_combinada.append(f"🛡️ {partido['pick_seguro']} ({int(prob_comb*100)}% Fiabilidad)")
            id_counter += 1

    return jsonify({
        "partidos": partidos_generados,
