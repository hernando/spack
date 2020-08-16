from spack import *


class Rubberband(AutotoolsPackage):

    homepage = "https://github.com/breakfastquay/rubberband"
    url      = "https://github.com/breakfastquay/rubberband/archive/v1.8.2.zip"

    version('1.8.2', sha256='350eea8acb6329a78df17d51a306665d6f9bd65ee86e91599244975ff62f44bb')
    version('1.8.1', sha256='82b00ff89fa4227cb4c0e975963e10d560edc08b3902007ec87bea93d093f223')
    version('1.8',   sha256='d5addf9d66ee4aba663576ec584a82bb744d70c78e452fd0d2ec608f6cba1e36')
    version('1.7',   sha256='700094508e35b62cd733047f536a9954dd321705a8515eb0671af55957b790c9')
    version('1.6',   sha256='5cd2b3b3a69b4478781d6477e4f50ed5b7bc1ac8040ad7e4ec139eff92af64ce')
    version('1.5',   sha256='132534cb8227b43ab504b4afb38dac7ed9cd0e6f0d82fdd59b487becfc7ef36b')

    depends_on('libsamplerate')
    depends_on('sndfile')
    depends_on('fftw +openmp ~mpi')
    depends_on('vamp-plugin-sdk')
    depends_on('ladspa', type='link')

    patch('omit_jni.patch')
