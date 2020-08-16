from spack import *

class Eq10q(CMakePackage):
    """EQ10Q is an audio plugin bundle over the LV2 standard (http://lv2plug.in)
    implementing a powerful and flexible parametric equalizer and more"""

    homepage = 'http://eq10q.sourceforge.net/'
    url = 'https://downloads.sourceforge.net/project/eq10q/eq10q-2.2.tar.gz'

    generator='Ninja'

    version('2.2', sha256='337f4c703ba31902565faad1cd450cf0312ad5a48dc499661277f287b662b09a')

    depends_on('fftw +openmp ~mpi')
    depends_on('gtkmm@2.24.5')
    depends_on('lv2')

    # Fixing this dependencies to whatever we have in ardour to avoid rebuilding the packages
    depends_on('cairo@1.17.2')
    depends_on('gtkplus@2.24.32')
    depends_on('pangomm@2.42.1')

    patch('compilation_fixes.patch', when='@2.2')
    patch('fix_install_prefix.patch', when='@2.2')
