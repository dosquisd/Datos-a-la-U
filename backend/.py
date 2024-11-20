import json
from typing import Dict, List, Any

global data

value = "CASA DE JUSTICIA CALI AGUABLANCA"

with open('./data/processed/depts_mpios.json') as raw_data:
    data = json.load(raw_data)

for item in data:
    deparment = item['department']
    municipalities: Dict[str, List[Any]] = item['municipalities']

    for _, courthouses in municipalities.items():
        if courthouses:
            for courthouse in courthouses:
                if str(courthouse['courthouse']).lower().strip() == value.lower().strip():
                    print(deparment)
