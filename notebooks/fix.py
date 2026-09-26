import json

with open('main.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)
    
src = json.dumps(nb)
src = src.replace('unknown_value=-1', '')
src = src.replace('handle_unknown="use_encoded_value"', 'handle_unknown="use_encoded_value", unknown_value=-1')
src = src.replace('model.jobplib', 'model.joblib')

with open('main.ipynb', 'w', encoding='utf-8') as f:
    f.write(src)
