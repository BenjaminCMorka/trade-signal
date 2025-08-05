import subprocess

def test_pipeline_runs():
    result = subprocess.run(["bash", "run.sh"], capture_output=True)
    assert result.returncode == 0
