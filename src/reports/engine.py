import json
import os
from datetime import datetime
from jinja2 import Template
from src.utils.logger import logger

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>OSINT INTEL - {{ target }}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap');
        
        body { 
            background-color: #050505; 
            color: #00ff41; 
            font-family: 'Fira Code', monospace; 
            margin: 0; 
            padding: 40px;
            background-image: radial-gradient(circle, #003b00 1px, transparent 1px);
            background-size: 30px 30px;
        }
        
        .container { 
            max-width: 1100px; 
            margin: 0 auto; 
            border: 1px solid #00ff41; 
            padding: 40px; 
            box-shadow: 0 0 20px #003b00;
            background-color: rgba(0, 10, 0, 0.9);
        }
        
        h1 { 
            text-align: center; 
            text-transform: uppercase; 
            letter-spacing: 5px; 
            border-bottom: 2px solid #00ff41;
            padding-bottom: 20px;
            color: #ffffff;
            text-shadow: 0 0 10px #00ff41;
        }
        
        .header-info {
            display: flex;
            justify-content: space-between;
            margin-bottom: 40px;
            font-size: 0.9em;
            color: #008f11;
        }
        
        .section { 
            margin-bottom: 40px; 
            border-left: 3px solid #00ff41;
            padding-left: 20px;
        }
        
        .section h2 { 
            color: #00ff41; 
            font-size: 1.5em; 
            margin-bottom: 20px;
            text-transform: uppercase;
        }
        
        .data-list {
            list-style: none;
            padding: 0;
        }
        
        .data-item {
            padding: 10px;
            border-bottom: 1px solid #003b00;
            display: flex;
            align-items: center;
        }
        
        .data-item::before {
            content: "> ";
            margin-right: 10px;
            color: #ffffff;
        }
        
        a { color: #ffffff; text-decoration: none; }
        a:hover { text-decoration: underline; color: #00ff41; }
        
        .tag {
            background: #00ff41;
            color: #000;
            padding: 2px 8px;
            font-size: 0.7em;
            font-weight: bold;
            margin-right: 10px;
            text-transform: uppercase;
        }

        .footer {
            text-align: center;
            font-size: 0.7em;
            margin-top: 50px;
            color: #003b00;
            border-top: 1px solid #003b00;
            padding-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>RECONNAISSANCE REPORT</h1>
        
        <div class="header-info">
            <span>TARGET: {{ target }}</span>
            <span>DATE: {{ timestamp }}</span>
            <span>STATUS: COMPLETED</span>
        </div>

        {% if social %}
        <div class="section">
            <h2>[ SOCIAL_GRID ]</h2>
            <ul class="data-list">
                {% for site in social %}
                <li class="data-item"><a href="{{ site }}" target="_blank">{{ site }}</a></li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}

        {% if email %}
        <div class="section">
            <h2>[ BREACH_DATABASE ]</h2>
            <ul class="data-list">
                {% for svc in email %}
                <li class="data-item"><span class="tag">DETECTED</span> {{ svc }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}

        {% if ip_data %}
        <div class="section">
            <h2>[ GEOLOCATION_SIGINT ]</h2>
            <ul class="data-list">
                <li class="data-item"><span class="tag">LOCATION</span> {{ ip_data.city }}, {{ ip_data.country }} ({{ ip_data.countryCode }})</li>
                <li class="data-item"><span class="tag">COORDINATES</span> Lat: {{ ip_data.lat }}, Lon: {{ ip_data.lon }}</li>
                <li class="data-item"><span class="tag">ISP</span> {{ ip_data.isp }}</li>
                <li class="data-item"><span class="tag">INFRA</span> {{ ip_data.org }} / {{ ip_data.as }}</li>
                <li class="data-item"><span class="tag">PROXIED</span> {{ 'TRUE' if ip_data.proxy or ip_data.hosting else 'FALSE' }}</li>
            </ul>
        </div>
        {% endif %}

        <div class="footer">
            GENESIS OSINT ENGINE v3.5 | ENCRYPTED OUTPUT | FOR AUTHORIZED USE ONLY
        </div>
    </div>
</body>
</html>
"""

class ReportEngine:
    def __init__(self, output_dir="results"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def generate(self, data, target):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        safe_target = "".join(x for x in target if x.isalnum())
        
        # Save JSON
        json_path = os.path.join(self.output_dir, f"report_{safe_target}.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        # Save HTML
        html_path = os.path.join(self.output_dir, f"report_{safe_target}.html")
        template = Template(HTML_TEMPLATE)
        html_content = template.render(
            target=target,
            timestamp=timestamp,
            social=data.get("social", []),
            email=data.get("email", []),
            ip_data=data.get("ip_intel", {})
        )
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        logger.info(f"[+] Reports generated: {json_path}, {html_path}")
        return html_path

report_engine = ReportEngine()
