import os, json, re

agent_ids = [
    'aca1720f-9130-4c89-a279-3467030d412e',
    '2b6c3fcf-d237-4ea7-b1b5-f5dc266a8f6c',
    '22589abd-89bf-4a26-802b-9a12a8bb96ba',
    '6175abdb-6936-4200-9033-3f11dd59bd60',
    '1a1a2cb0-184e-44b1-95a7-3e81bb76743f'
]

brain_dir = r"C:\Users\jhunu\.gemini\antigravity\brain"
output_dir = r"d:\TOOLS WEB TOOLS\kiro calorie"

for aid in agent_ids:
    # ALways use transcript_full.jsonl
    transcript_path = os.path.join(brain_dir, aid, ".system_generated", "logs", "transcript_full.jsonl")
    if not os.path.exists(transcript_path):
        print(f"Transcript not found for {aid}")
        continue
        
    with open(transcript_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in reversed(lines):
        try:
            data = json.loads(line)
        except:
            continue
            
        if 'tool_calls' in data:
            for call in data['tool_calls']:
                if call.get('name') == 'write_to_file':
                    args = call.get('args', {})
                    if type(args) is str:
                        args = json.loads(args)
                        
                    target_file = args.get('TargetFile', '')
                    content = args.get('CodeContent', '')
                    
                    if not target_file or not content:
                        continue
                        
                    if content.startswith('"') and content.endswith('"'):
                        content = json.loads(content)
                    if target_file.startswith('"') and target_file.endswith('"'):
                        target_file = json.loads(target_file)
                    
                    rel_path = target_file.split("kiro calorie")[-1].lstrip("\\/")
                    dest_path = os.path.join(output_dir, rel_path)
                    
                    # Fix the faqs object keys! They used question and answer instead of q and a.
                    content = re.sub(r'question:\s*(["\'])', r'q: \1', content)
                    content = re.sub(r'answer:\s*(["\'])', r'a: \1', content)
                    
                    # Fix imports
                    content = content.replace("import Button from '../../../components/Button.astro'", "import Button from '../../../components/ui/Button.astro'")
                    content = re.sub(r'from [\'"]\.*/components/([^\'"]*)[\'"]', r"from '../../../components/\1'", content)
                    content = re.sub(r'from [\'"]\.*/layouts/([^\'"]*)[\'"]', r"from '../../../layouts/\1'", content)
                    
                    # Fix unescaped HTML inside ContentLayout props
                    c_lines = content.split('\n')
                    for i in range(min(200, len(c_lines))):
                        if 'title="' in c_lines[i] or 'description="' in c_lines[i] or 'h1="' in c_lines[i] or 'lead="' in c_lines[i]:
                            c_lines[i] = re.sub(r'<a href="[^"]*"[^>]*>(.*?)</a>', r'\1', c_lines[i])
                    content = '\n'.join(c_lines)

                    with open(dest_path, 'w', encoding='utf-8') as out_f:
                        out_f.write(content)
                    print(f"Restored and fixed {dest_path}")
                    break
            else:
                continue
            break
