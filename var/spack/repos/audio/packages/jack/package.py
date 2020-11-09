from spack import *

class Jack(WafPackage):

    homepage = "https://jackaudio.org/"
    git = "https://github.com/jackaudio/jack2.git"

    version('1.9.14', tag='v1.9.14')

    variant('alsa', default=True)
    variant('dbus', default=True)

    depends_on('alsa', when='+alsa')
    depends_on('dbus', when='+dbus')
    depends_on('samplerate')
    depends_on('libsndfile')
    depends_on('readline')

    def configure_args(self):

        if '+dbus' in self.spec:
            return ["--dbus", "--classic"]
        return []
