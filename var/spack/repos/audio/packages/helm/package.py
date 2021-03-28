from spack import *

class Helm(AutotoolsPackage):
    """Helm is a software synthesizer. This package compiles the standalone and LV2 plugin variants"""

    homepage = "https://tytel.org/helm/"
    url = "https://github.com/mtytel/helm/archive/v0.9.0.zip"

    version('0.9.0', sha256='700e6b49a08e4c06a98444d52b48e420dadff075bb7da173d4a631f38fd6044b')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('alsa')
    depends_on('curl')
    depends_on('freetype')
    depends_on('jack')
    depends_on('libxcursor')
    depends_on('libxinerama')
    depends_on('lv2')

    patch('fix_install_path.patch')
    patch('fix_compilation_gcc10.patch')

    def setup_environment(self, spack_env, run_env):
        spack_env.set('DESTDIR', self.spec.prefix)
