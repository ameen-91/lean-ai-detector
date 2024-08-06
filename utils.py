import subprocess


def run_command(command):
    """Run shell command"""
    try:
        result = subprocess.run(
            command,
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        output = result.stdout.decode("utf-8")
        error = result.stderr.decode("utf-8")

        return output, error
    except subprocess.CalledProcessError as e:
        return e.output.decode("utf-8"), e.stderr.decode("utf-8")
