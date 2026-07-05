from flask import Flask

app = Flask(__name__)

SUPER_APP_DISEÑO = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>CLAYTON COUPLING ENGINE v5 - PREDICTOR PREMIUM</title>
    <style>
        :root {
            --bg-primary: #020617;
            --bg-secondary: #0f172a;
            --bg-card: #1e293b;
            --accent-clayton: #f97316;
            --accent-blue: #3b82f6;
            --accent-green: #22c55e;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border-color: #334155;
        }
        body { font-family: system-ui, -apple-system, sans-serif; background-color: var(--bg-primary); margin: 0; padding: 12px; color: var(--text-main); }
        .container { max-width: 100%; margin: 0 auto; }
        header { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px; margin-bottom: 16px; text-align: center; }
        .engine-title { margin: 0; font-size: 18px; font-weight: 800; }
        .engine-title span { color: var(--accent-clayton); }
        .panel { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 12px; padding: 14px; margin-bottom: 14px; }
        .team-vs { font-size: 18px; font-weight: 800; margin: 8px 0; border-bottom: 1px solid var(--border-color); padding-bottom: 6px; }
        
        .market-section { background: var(--bg-card); border-radius: 8px; padding: 10px; margin-top: 8px; border: 1px solid rgba(255,255,255,0.05); }
        .market-title { font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--accent-clayton); margin-bottom: 6px; display: flex; justify-content: space-between; }
        .market-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; font-size: 11px; text-align: center; }
        .market-box { background: rgba(0,0,0,0.2); padding: 6px; border-radius: 4px; border: 1px solid var(--border-color); }
        .market-box span { display: block; font-weight: bold; font-size: 13px; color: #fff; }
        
        .scorer-list { margin: 0; padding-left: 16px; font-size: 12px; color: #cbd5e1; }
        .scorer-list li span { color: var(--accent-green); font-weight: bold; }
        
        .prob-bar-container { display: flex; height: 24px; border-radius: 6px; overflow: hidden; margin: 8px 0; font-weight: 700; font-size: 10px; }
        .prob-bar { display: flex; align-items: center; justify-content: center; color: white; }
        .prob-local { background: var(--accent-blue); }
        .prob-draw { background: #475569; }
        .prob-visit { background: var(--accent-green); }
        .btn-clayton { width: 100%; background: linear-gradient(135deg, #f97316 0%, #ea580c 100%); color: white; border: none; padding: 11px; border-radius: 8px; font-size: 11px; font-weight: 800; margin-top: 10px; }
    </style>
</head>
<body>
<div class="container">
    <header>
        <div class="engine-title">⚽ DATA CENTRAL: CLAYTON ENGINE <span>v5</span></div>
    </header>

    <!-- PARTIDO 1 -->
    <div class="panel">
        <div class="team-vs">Brasil 🇧🇷 vs Noruega 🇳🇴</div>
        <div class="market-section">
            <div class="market-title">📊 PROBABILIDAD (1 X 2)</div>
            <div class="prob-bar-container">
                <div class="prob-bar prob-local" style="width: 44%;">44% Gana L</div>
                <div class="prob-bar prob-draw" style="width: 25%;">25% X</div>
                <div class="prob-bar prob-visit" style="width: 31%;">31% Gana V</div>
            </div>
        </div>
        <div class="market-section">
            <div class="market-title">🎯 MERCADO DE GOLES TOTALES</div>
            <div class="market-grid">
                <div class="market-box">Más 1.5<span>95%</span></div>
                <div class="market-box">Más 2.5<span>72%</span></div>
                <div class="market-box">Ambos Anotan<span>68%</span></div>
            </div>
        </div>
        <div class="market-section">
            <div class="market-title">👟 PROBABILIDAD DE ANOTADORES</div>
            <ul class="scorer-list">
                <li>Vinícius Jr. (Brasil) — <span>58%</span> primer gol</li>
                <li>Erling Haaland (Noruega) — <span>64%</span> marca en cualquier momento</li>
            </ul>
        </div>
        <button class="btn-clayton">ACTUALIZAR CUOTAS EN VIVO</button>
    </div>

    <!-- PARTIDO 2 -->
    <div class="panel">
        <div class="team-vs">México 🇲🇽 vs Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿</div>
        <div class="market-section">
            <div class="market-title">📊 PROBABILIDAD (1 X 2)</div>
            <div class="prob-bar-container">
                <div class="prob-bar prob-local" style="width: 34%;">34% Gana L</div>
                <div class="prob-bar prob-draw" style="width: 25%;">25% X</div>
                <div class="prob-bar prob-visit" style="width: 41%;">41% Gana V</div>
            </div>
        </div>
        <div class="market-section">
            <div class="market-title">🎯 MERCADO DE GOLES TOTALES</div>
            <div class="market-grid">
                <div class="market-box">Más 1.5<span>81%</span></div>
                <div class="market-box">Menos 2.5<span>62%</span></div>
                <div class="market-box">Ambos Anotan<span>48%</span></div>
            </div>
        </div>
        <div class="market-section">
            <div class="market-title">👟 PROBABILIDAD DE ANOTADORES</div>
            <ul class="scorer-list">
                <li>Harry Kane (Inglaterra) — <span>55%</span> primer gol</li>
                <li>Santiago Giménez (México) — <span>38%</span> marca en cualquier momento</li>
            </ul>
        </div>
        <button class="btn-clayton">ACTUALIZAR CUOTAS EN VIVO</button>
    </div>

    <!-- PARTIDO 3 -->
    <div class="panel">
        <div class="team-vs">Portugal 🇵🇹 vs España 🇪🇸</div>
        <div class="market-section">
            <div class="market-title">📊 PROBABILIDAD (1 X 2)</div>
            <div class="prob-bar-container">
                <div class="prob-bar prob-local" style="width: 38%;">38% Gana L</div>
                <div class="prob-bar prob-draw" style="width: 30%;">30% X</div>
                <div class="prob-bar prob-visit" style="width: 32%;">32% Gana V</div>
            </div>
        </div>
        <div class="market-section">
            <div class="market-title">🎯 MERCADO DE GOLES TOTALES</div>
            <div class="market-grid">
                <div class="market-box">Más 1.5<span>88%</span></div>
                <div class="market-box">Más 2.5<span>54%</span></div>
                <div class="market-box">Ambos Anotan<span>61%</span></div>
            </div>
        </div>
        <div class="market-section">
            <div class="market-title">👟 PROBABILIDAD DE ANOTADORES</div>
            <ul class="scorer-list">
                <li>Cristiano Ronaldo (Portugal) — <span>49%</span> primer gol</li>
                <li>Lamine Yamal (España) — <span>45%</span> marca en cualquier momento</li>
            </ul>
        </div>
        <button class="btn-clayton">ACTUALIZAR CUOTAS EN VIVO</button>
    </div>

    <!-- PARTIDO 4 -->
    <div class="panel">
        <div class="team-vs">Estados Unidos 🇺🇸 vs Bélgica 🇧🇪</div>
        <div class="market-section">
            <div class="market-title">📊 PROBABILIDAD (1 X 2)</div>
            <div class="prob-bar-container">
                <div class="prob-bar prob-local" style="width: 29%;">29% Gana L</div>
                <div class="prob-bar prob-draw" style="width: 28%;">28% X</div>
                <div class="prob-bar prob-visit" style="width: 43%;">43% Gana V</div>
            </div>
        </div>
        <div class="market-section">
            <div class="market-title">🎯 MERCADO DE GOLES TOTALES</div>
            <div class="market-grid">
                <div class="market-box">Más 1.5<span>91%</span></div>
                <div class="market-box">Más 2.5<span>67%</span></div>
                <div class="market-box">Ambos Anotan<span>70%</span></div>
            </div>
        </div>
        <div class="market-section">
            <div class="market-title">👟 PROBABILIDAD DE ANOTADORES</div>
            <ul class="scorer-list">
                <li>Christian Pulisic (EEUU) — <span>35%</span> primer gol</li>
                <li>Romelu Lukaku (Bélgica) — <span>51%</span> marca en cualquier momento</li>
            </ul>
        </div>
        <button class="btn-clayton">ACTUALIZAR CUOTAS EN VIVO</button>
    </div>

</div>
</body>
</html>
"""

@app.route('/')
def home():
    return SUPER_APP_DISEÑO

if __name__ == '__main__':
    app.run()
