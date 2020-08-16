from spack import *

import inspect

class Faust(Package):
    """Faust (Functional Audio Stream) is a functional programming language
    specifically designed for real-time signal processing and synthesis. A
    distinctive characteristic of Faust is to be fully compiled."""

    homepage = 'https://faust.grame.fr/'
    git = 'https://github.com/grame-cncm/faust'

    version('develop', branch='master-dev')

    phases = ['build', 'install']

    def setup_build_environment(self, env):
        env.set('PREFIX', self.spec.prefix)

    def build(self, spec, prefix):
        inspect.getmodule(self).make()

    def install(self, spec, prefix):
        inspect.getmodule(self).make('install')


