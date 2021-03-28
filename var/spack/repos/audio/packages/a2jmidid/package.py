from spack import *

class A2jmidid(MesonPackage):

    homepage = "https://github.com/linuxaudio/a2jmidid"
    git = "https://github.com/linuxaudio/a2jmidid.git"

    version('9', tag='9')

    depends_on('alsa')
    depends_on('jack')

    depends_on('meson', type='build')

    def meson_args(self):
        return ['-Ddisable-dbus=true']
