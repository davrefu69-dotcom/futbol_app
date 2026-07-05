from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CLAYTON COUPLING ENGINE v5</title>
        <style>
            body { background-color: #020617; color: white; font-family: sans-serif; padding: 20px; }
            .card { background: #0f172a; border: 1px solid #334155; padding: 15px; border-radius: 12px; margin-bottom: 15px; }
            h1 { color: #f97316; font-size: 20px; }
            .btn { width: 100%; background: #f97316; color: white; border: none; padding: 10px; border-radius: 8px; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>CLAYTON COUPLING ENGINE v5</h1>
            <p>● OPTIMIZADO PARA 90 MINUTOS</p>
        </div>
        <div class="card">
            <h3>Brasil 🇧🇷 vs Noruega 🇳🇴</h3>
            <p>🔮 Resultado Exacto: 3 - 2</p>
            <p style="color: #22c55e;">🎯 Apuesta: Más de 1.5 Goles</p>
            <button class="btn">PROCESAR CÓPULA</button>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()

