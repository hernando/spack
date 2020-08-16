from spack import *

class Jack(WafPackage):

    homepage = "https://jackaudio.org/"
    git = "https://github.com/jackaudio/jack2.git"

    version('1.9.14', tag='v1.9.14')

    variant('alsa', default=True)

    depends_on('alsa', when='+alsa')
    depends_on('samplerate')
    depends_on('readline')
