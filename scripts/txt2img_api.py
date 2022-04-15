import tempfile
import os
from bottle import route, run, request, static_file
import subprocess

@route("/txt2img")
def txt2img():
    with tempfile.TemporaryDirectory() as temp_dir:
        prompt = request.query['prompt'] or 'A large stone dragon realistic photo'
        result = subprocess.run(['python3', os.path.join(os.path.dirname(__file__), 'txt2img.py'), '--outdir', temp_dir, '--prompt', prompt, '--ddim_eta', '0', '--n_samples', '4', '--n_iter', '4', '--scale', '5.0', '--ddim_steps', '35', '--plms'], stdout=subprocess.PIPE)
        files_in_dir = [f for f in os.listdir(temp_dir) if os.path.isfile(os.path.join(temp_dir, f))]
        return static_file(files_in_dir[0], root=temp_dir, mimetype='image/png')
run(host='0.0.0.0', port=5000, debug=True)