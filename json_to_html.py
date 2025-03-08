# json_to_html.py

import json

def generate_html_report(json_file, html_file):
    with open(json_file) as f:
        data = json.load(f)

    with open(html_file, 'w') as f:
        f.write('<html><head><title>Behave Report</title></head><body>')
        f.write('<h1>Behave Test Report</h1>')
        
        for feature in data['features']:
            f.write(f"<h2>Feature: {feature['name']}</h2>")
            for scenario in feature['elements']:
                f.write(f"<h3>Scenario: {scenario['name']}</h3>")
                for step in scenario['steps']:
                    f.write(f"<p>{step['keyword']} {step['name']} - {step['result']['status']}</p>")
        
        f.write('</body></html>')

if __name__ == "__main__":
    generate_html_report('report.json', 'reports/results.html')