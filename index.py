import math
from flask import Flask, jsonify, request

app = Flask(__name__)

def calcular_poisson(media, k):
    return (math.exp(-media) * (media**k)) / math.factorial(k)

@app.route('/api/predict', methods=['GET'])
def predict():
    # Obtener los valores xG desde los parámetros de la URL
    try:
        xg_local = float(request.args.get('local', 2.8))
        xg_visitante = float(request.args.get('visitante', 1.4))
    except ValueError:
        return jsonify({"error": "Parámetros xG inválidos"}), 400

    todos_los_marcadores = []
    for l in range(8):
        for v in range(8):
            prob_base = calcular_poisson(xg_local, l) * calcular_poisson(xg_visitante, v)
            if l == v:
                prob_base *= (1.35 if l == 0 else 1.25 if l == 1 else 1.15)
            elif abs(l - v) == 1:
                prob_base *= 1.08
            todos_los_marcadores.append({"marcador": f"{l} - {v}", "probabilidad": prob_base * 100})
            
    todos_los_marcadores.sort(key=lambda x: x["probabilidad"], reverse=True)
    
    prob_top20 = sum(m["probabilidad"] for m in todos_los_marcadores[:20])
    prob_residual = 100.0 - prob_top20
    prob_final_bloque = prob_top20 + (prob_residual * 0.72) 
    
    p_local, p_empate, p_visita = 0, 0, 0
    for m in todos_los_marcadores[:30]:
        l, v = map(int, m["marcador"].split(" - "))
        if l > v: p_local += m["probabilidad"]
        elif l == v: p_empate += m["probabilidad"]
        else: p_visita += m["probabilidad"]
        
    total_1x2 = p_local + p_empate + p_visita
    
    return jsonify({
        "top": todos_los_marcadores[:3],          
        "respaldo": todos_los_marcadores[3:20],   
        "p_local": int((p_local / total_1x2) * 100),
        "p_empate": int((p_empate / total_1x2) * 100),
        "p_visita": int((p_visita / total_1x2) * 100),
        "prob_bloque": f"{prob_final_bloque:.2f}%",
        "cobertura_residual": f"{prob_residual * 0.72:.1f}%"
    })
