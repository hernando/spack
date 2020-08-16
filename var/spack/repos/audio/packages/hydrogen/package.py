from spack import *

class Hydrogen(CMakePackage):

    homepage = "http://hydrogen-music.org/"
    url      = "https://github.com/hydrogen-music/hydrogen/archive/1.0.0-rc1.zip"

    version('1.0.1', sha256='ad3479d589d3fe155b6a1d931059b645c5c345f05878c0878280a41d757a405b')
    version('0.9.7', sha256='6703ba1d33a8d953bb8115f38edf5ef323bfae6355706cafd62522e524fab162')
    version('0.9.6.1', sha256='6c4d20227c8b044596c1eb9138b6e0766853fb01238989c7241bb50f07543c51')
    version('0.9.6', sha256='5bb52609a3ca5fc5e5195ed18a760143f4ab3bda1fdd27208d530fd10826150d')

    depends_on("qt@5.12: +dbus +opengl")
    depends_on("jack", type=("build", "link", "run"))
    depends_on("libarchive")
    depends_on("sndfile")

    def cmake_args(self):
        args = []
        return args
