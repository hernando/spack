from spack import *

class Ardour(WafPackage):

    homepage = "https://ardour.org/"
    git      = "https://github.com/Ardour/ardour.git"

    version('6.6', tag='6.6')
    version('6.2', tag='6.2')
    version('6.0', tag='6.0')

    depends_on('aubio@0.4.0:')
    depends_on('curl@7.0.0:')
    depends_on('boost@1.56:')
    depends_on('fftw +openmp ~mpi')
    depends_on('flac@1.2.1:')
    depends_on('fluidsynth')
    depends_on('jack')
    depends_on('libarchive@3.0.0:')
    depends_on('libsamplerate')
    depends_on('libusb')
    depends_on('libogg@1.1.2:')
    depends_on('lilv@0.24.2:')
    depends_on('lo@0.26:')
    depends_on('lv2')
    depends_on('ladspa', type='link')
    depends_on('lrdf@0.4.0:')
    depends_on('sndfile@1.0.18:')
    depends_on('serd@0.14.0:')
    depends_on('sord@0.8.0:')
    depends_on('sratom@0.2.0:')
    depends_on('suil@0.6.0:')
    depends_on('taglib@1.6:')
    depends_on('rubberband')
    depends_on('vamp-plugin-sdk@2.1:')

    # UI
    depends_on('cairo@1.17.2')
    depends_on('cairomm@1.12.2')
    depends_on('gtkplus@2.24.32')
    depends_on('gtkmm@2.24.5')
    depends_on('glibmm@2.60.0')
    depends_on('libsigcpp@2.9.3')
    depends_on('pangomm@2.42.1')

    patch('add_revision.cc.6.0.patch', when='@6.0')
    patch('add_revision.cc.6.2.patch', when='@6.2')
    patch('add_revision.cc.6.6.patch', when='@6.6')
    patch('fix_fftw3f_linking.patch')

    def configure_args(self):
        return ["--no-phone-home", "--optimize", "--lxvst", "--cxx11"]
