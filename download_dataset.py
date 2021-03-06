import subprocess
import glob


def get_dataset(target: str):
    if "/" in target:
        isCompetition = False
        dirname = target.split("/")[1]
        download_command = 'kaggle datasets download -d '
    else:
        isCompetition = True
        dirname = target
        download_command = 'kaggle competitions download -c '

    # prepare libraries and dirs
    commands = [
        'mkdir ../input'
    ]
    for c in commands:
        r = subprocess.run(c, shell=True, capture_output=True)

    # download and unzip
    print('Donwloading: ' + target)
    commands = [
        download_command + target + ' -p ./download/' + dirname,
        'unzip -n ./download/' + dirname + '/*.zip -d ../input/' + dirname,
    ]
    for c in commands:
        r = subprocess.run(c, shell=True, capture_output=True)
        if r.returncode != 0:
            print(r.args)
            if len(r.stderr) == 0:
                raise Exception(r.stdout)
            else:
                raise Exception(r.stderr)
    files = glob.glob('./download/' + dirname + '/*')
    for f in files:
        if not f.endswith('.zip'):
            subprocess.run(f'mv {f} ../input/{dirname}/', shell=True, capture_output=True)
    print('Donwload Completed: ' + target)
