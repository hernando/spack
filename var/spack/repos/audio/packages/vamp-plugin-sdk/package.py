from spack import *

class VampPluginSdk(AutotoolsPackage):

    homepage = "https://www.vamp-plugins.org/develop.html"
    url      = "https://code.soundsoftware.ac.uk/attachments/download/2691/vamp-plugin-sdk-2.10.0.tar.gz"

    version('2.10.0', sha256='aeaf3762a44b148cebb10cde82f577317ffc9df2720e5445c3df85f3739ff75f')

    depends_on('sndfile')
