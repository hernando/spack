from spack import *

class Kpp(MesonPackage):
    """ """

    homepage = 'https://github.com/olegkapitonov/Kapitonov-Plugins-Pack'
    git = 'https://github.com/olegkapitonov/Kapitonov-Plugins-Pack'

    version('1.2.1', tag='1.2.1')

    depends_on('boost@1.56:')
    depends_on('cairo')
    depends_on('xcb-util')
    depends_on('xcb-util-wm')
    depends_on('libxcb')
    depends_on('ladspa')
    depends_on('lv2')
    depends_on('zita-convolver')
    depends_on('zita-resampler')

    depends_on('faust', type='build')
    depends_on('ninja', type='build')
