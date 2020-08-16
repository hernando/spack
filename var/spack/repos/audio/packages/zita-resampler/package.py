from spack import *

import inspect

class ZitaResampler(Package):
    """Libzita-resampler is a C++ library for resampling audio signals. It
    is designed to be used within a real-time processing context, to be fast, and
    to provide high-quality sample rate conversion."""

    homepage = 'https://kokkinizita.linuxaudio.org/linuxaudio/zita-resampler/resampler.html'
    url = 'https://kokkinizita.linuxaudio.org/linuxaudio/downloads/zita-resampler-1.6.2.tar.bz2'

    version('1.6.2', sha256='233baefee297094514bfc9063e47f848e8138dc7c959d9cd957b36019b98c5d7')

    phases = ['build', 'install']

    patch('do_not_run_ldconfig.patch')

    def setup_build_environment(self, env):
        print(self.spec.prefix)
        env.set('PREFIX', self.spec.prefix)

    def build(self, spec, prefix):
        with working_dir(join_path(self.stage.source_path, 'source')):
            inspect.getmodule(self).make()

    def install(self, spec, prefix):

        with working_dir(join_path(self.stage.source_path, 'source')):
            inspect.getmodule(self).make('install')


