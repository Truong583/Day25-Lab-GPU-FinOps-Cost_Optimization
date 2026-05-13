
import json
import os

notebook_path = r'd:\Lab25\Day25-Lab-GPU-FinOps-Cost_Optimization\notebook\gpu_finops_lab.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# New Gateway URL
new_url = "https://24baec9b53f914c0-113-23-6-181.serveousercontent.com"

# Apply URL replacement in Cell 2
for cell in nb['cells']:
    if 'source' in cell and len(cell['source']) > 0:
        if 'GATEWAY_URL =' in cell['source'][0] or 'Cell 2: Configure Gateway URL' in cell['source'][0]:
            # Find the line with GATEWAY_URL and replace it
            for i, line in enumerate(cell['source']):
                if 'GATEWAY_URL =' in line:
                    cell['source'][i] = f'GATEWAY_URL = "{new_url}"\n'
                    break

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print(f'SUCCESS: Notebook updated with new Serveo URL: {new_url}')
