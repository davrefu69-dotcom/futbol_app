import os
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
        "combinada_picks": lineas_combinada,
        "combinada_total": f"{round(exito_combinado * 100, 1)}%",
        "last_update": datetime.now().strftime("%H:%M:%S")
    })

@app.route('/')
def home():
    try:
        # Localiza index.html de forma relativa al directorio del script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_html = os.path.join(base_dir, 'index.html')
        with open(ruta_html, 'r', encoding='utf-8') as f:
            return render_template_string(f.read())
    except Exception as e:
        return f"Error al cargar la interfaz: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
