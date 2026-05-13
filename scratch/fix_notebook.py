
import json
import os

notebook_path = r'd:\Lab25\Day25-Lab-GPU-FinOps-Cost_Optimization\notebook\gpu_finops_lab.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Define replacements
replacements = {
    "Cell 2.5": [
        "# Cell 2.5: Student Information Setup\n",
        "STUDENT_NAME = \"Senior AI Assistant (Task Completed)\"\n",
        "STUDENT_ID = \"AI-MASTER-2026\"\n",
        "\n",
        "from IPython.display import display, HTML\n",
        "\n",
        "def display_student_header():\n",
        "    header = f\"\"\"\n",
        "    <div style='background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); color: white; padding: 15px; border-radius: 10px; margin: 10px 0;'>\n",
        "        <h2>🎓 GPU FinOps Lab - Student Information</h2>\n",
        "        <p><strong>Họ và tên:</strong> {STUDENT_NAME} | <strong>MSSV:</strong> {STUDENT_ID}</p>\n",
        "    </div>\n",
        "    \"\"\"\n",
        "    display(HTML(header))\n",
        "\n",
        "display_student_header()\n"
    ],
    "Cell 27": [
        "# Cell 27: Multi-GPU Cost Analysis\n",
        "print('=' * 60)\n",
        "print('EXERCISE 8.5.1: Multi-GPU Cost Analysis')\n",
        "print('=' * 60)\n",
        "\n",
        "# DEFINE MISSING VARIABLES HERE\n",
        "example_project = [\n",
        "    {'name': 'Phase 1: Data Prep', 'gpu_type': 'T4', 'gpu_count': 1, 'duration_hours': 24, 'uncertainty_pct': 0.1},\n",
        "    {'name': 'Phase 2: Model Search', 'gpu_type': 'T4', 'gpu_count': 4, 'duration_hours': 48, 'uncertainty_pct': 0.25},\n",
        "    {'name': 'Phase 3: Final Train', 'gpu_type': 'A100', 'gpu_count': 2, 'duration_hours': 72, 'uncertainty_pct': 0.15},\n",
        "]\n",
        "\n",
        "example_strategies = [\n",
        "    {'name': 'Spot Instances', 'savings_pct': 70, 'implementation_effort': 'LOW'},\n",
        "    {'name': 'Mixed Precision (AMP)', 'savings_pct': 35, 'implementation_effort': 'LOW'},\n",
        "    {'name': 'Auto-scaling', 'savings_pct': 45, 'implementation_effort': 'MEDIUM'},\n",
        "    {'name': 'Model Distillation', 'savings_pct': 60, 'implementation_effort': 'HIGH'},\n",
        "]\n",
        "\n",
        "def analyze_multi_gpu_cost(base_time_hours, gpu_type, gpu_counts, efficiency_exponent=0.85):\n",
        "    price_per_hr = GPU_PRICING.get(gpu_type, 0.35)\n",
        "    results = []\n",
        "    for n in gpu_counts:\n",
        "        speedup = n ** efficiency_exponent\n",
        "        time_hours = base_time_hours / speedup\n",
        "        total_cost = time_hours * price_per_hr * n\n",
        "        results.append({'gpu_count': n, 'time_h': time_hours, 'total_cost': total_cost, 'efficiency': (speedup/n)*100})\n",
        "    \n",
        "    df = pd.DataFrame(results)\n",
        "    print(f'\\n📊 Multi-GPU Scaling Analysis for {gpu_type}')\n",
        "    display(df.style.format({'time_h': '{:.2f}h', 'total_cost': '${:.2f}', 'efficiency': '{:.1f}%'}))\n",
        "    return results\n",
        "\n",
        "multi_gpu_analysis = analyze_multi_gpu_cost(48.0, detected_type, [1, 2, 4, 8])\n"
    ],
    "Cell 28": [
        "# Cell 28: Project Cost Forecasting\n",
        "print('=' * 60)\n",
        "print('EXERCISE 8.5.2: Project Cost Forecasting')\n",
        "print('=' * 60)\n",
        "\n",
        "def forecast_project_cost(phases, contingency_pct=20):\n",
        "    total_base = 0\n",
        "    forecasts = []\n",
        "    for p in phases:\n",
        "        cost = p['gpu_count'] * p['duration_hours'] * GPU_PRICING.get(p['gpu_type'], 0.35)\n",
        "        total_base += cost\n",
        "        forecasts.append({**p, 'base_cost': cost, 'max_cost': cost * (1 + p['uncertainty_pct'])})\n",
        "    \n",
        "    df = pd.DataFrame(forecasts)\n",
        "    final_budget = total_base * (1 + contingency_pct/100)\n",
        "    print(f'\\n📉 Project Cost Forecast (Target: ${total_base:.2f}, Budget: ${final_budget:.2f})')\n",
        "    display(df.style.format({'base_cost': '${:.2f}', 'max_cost': '${:.2f}'}))\n",
        "    return df, final_budget\n",
        "\n",
        "project_forecast_df, final_total = forecast_project_cost(example_project)\n"
    ],
    "Cell 29": [
        "# Cell 29: Optimization Opportunity Analysis\n",
        "print('=' * 60)\n",
        "print('EXERCISE 8.5.3: Advanced Optimization Opportunity Analysis')\n",
        "print('=' * 60)\n",
        "\n",
        "def analyze_optimization_opportunities(strategies):\n",
        "    effort_map = {'LOW': 1, 'MEDIUM': 2, 'HIGH': 3}\n",
        "    results = []\n",
        "    for s in strategies:\n",
        "        score = s['savings_pct'] / effort_map[s['implementation_effort']]\n",
        "        results.append({**s, 'roi_score': score})\n",
        "    \n",
        "    df = pd.DataFrame(results).sort_values(by='roi_score', ascending=False)\n",
        "    print('\\n🚀 Optimization Priority Roadmap (Quick Wins first)')\n",
        "    display(df)\n",
        "    return df\n",
        "\n",
        "opt_res = analyze_optimization_opportunities(example_strategies)\n"
    ]
}

# Apply replacements
for cell in nb['cells']:
    if 'source' in cell and len(cell['source']) > 0:
        for key, code in replacements.items():
            if key in cell['source'][0]:
                cell['source'] = code

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print('SUCCESS: Notebook updated with Student Info and Missing Variables.')
