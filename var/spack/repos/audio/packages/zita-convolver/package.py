from spack import *

import inspect

class ZitaConvolver(Package):

    homepage = 'https://kokkinizita.linuxaudio.org/linuxaudio'
    url = 'https://kokkinizita.linuxaudio.org/linuxaudio/downloads/zita-convolver-4.0.3.tar.bz2'

    version('4.0.3', sha256='9aa11484fb30b4e6ef00c8a3281eebcfad9221e3937b1beb5fe21b748d89325f')

    phases = ['build', 'install']

    depends_on('fftw +openmp ~mpi')

    patch('do_not_run_ldconfig.patch')

    def setup_build_environment(self, env):
        env.set('PREFIX', self.spec.prefix)

    def build(self, spec, prefix):
        with working_dir(join_path(self.stage.source_path, 'source')):
            inspect.getmodule(self).make()

    def install(self, spec, prefix):

        with working_dir(join_path(self.stage.source_path, 'source')):
            inspect.getmodule(self).make('install')


