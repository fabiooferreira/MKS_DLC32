"""Build exact project core/auth in the pinned upstream Linux simulator. Never flashes hardware."""
from pathlib import Path
import argparse
import shutil
import subprocess
import tempfile
ROOT=Path(__file__).resolve().parents[1]
SIM_COMMIT='150e3f935e4b7cab7b90263b6b90b78912d9158d'

def run(*args,**kwargs):return subprocess.run(args,check=True,**kwargs)

def build(workdir,cmake):
    directory=Path(workdir)/'simulator';directory.parent.mkdir(parents=True,exist_ok=True)
    if not (directory/'.git').exists():
        run('git','init',str(directory))
        run('git','-C',str(directory),'remote','add','origin','https://github.com/grblHAL/Simulator.git')
        run('git','-C',str(directory),'fetch','--depth','1','origin',SIM_COMMIT)
        run('git','-C',str(directory),'checkout','--detach','FETCH_HEAD')
    head=subprocess.check_output(['git','-C',str(directory),'rev-parse','HEAD'],text=True).strip()
    if head!=SIM_COMMIT:raise ValueError('Use a disposable simulator directory at the pinned commit.')
    run('git','-C',str(directory),'submodule','update','--init','--depth','1','src/sdcard')
    source=directory/'src'
    shutil.copytree(ROOT/'firmware/main/grbl',source/'grbl',dirs_exist_ok=True)
    for name in ['ffst_auth.c','ffst_auth.h']:
        shutil.copyfile(ROOT/'firmware/main'/name,source/name)
    for name in ['host_env.h','sim_auth_env.c']:
        shutil.copyfile(ROOT/'tests/native'/name,source/name)
    def original(name):
        return subprocess.check_output(['git','-C',str(directory),'show','HEAD:'+name],text=True)
    make=original('CMakeLists.txt').replace('add_compile_definitions(F_CPU=16000000)',
        'add_compile_definitions(F_CPU=16000000 FFST_HOST_TEST=1 N_AXIS=4 LINE_BUFFER_SIZE=768 RX_BUFFER_SIZE=1024)')
    make+='\ntarget_sources(grblHAL_sim PRIVATE src/ffst_auth.c src/sim_auth_env.c)\ntarget_link_libraries(grblHAL_sim PRIVATE crypto)\n'
    (directory/'CMakeLists.txt').write_text(make)
    driver=original('src/driver.c').replace('\tboard_init();',
        '\tboard_init();\n    extern void ffst_auth_init(void);\n    ffst_auth_init();')
    (source/'driver.c').write_text(driver)
    run(cmake,'-S',str(directory),'-B',str(directory/'build'))
    run(cmake,'--build',str(directory/'build'),'--target','grblHAL_sim','-j2')
    print('NATIVE_SIMULATOR='+str(directory/'build/grblHAL_sim'))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workdir',default=None,help='Disposable build parent; default new temporary directory')
    parser.add_argument('--cmake',default=shutil.which('cmake') or 'cmake')
    args=parser.parse_args()
    build(args.workdir or tempfile.mkdtemp(prefix='ffst-native-'),args.cmake)
