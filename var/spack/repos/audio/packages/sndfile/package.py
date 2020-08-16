from spack import *

class Sndfile(AutotoolsPackage):

    homepage = "http://www.mega-nerd.com/SRC"
    url = "http://www.mega-nerd.com/libsndfile/files/libsndfile-1.0.28.tar.gz"

    depends_on("flac")
    depends_on("libogg")
    depends_on("libvorbis")

    version('1.0.28', sha256="1ff33929f042fa333aed1e8923aa628c3ee9e1eb85512686c55092d1e5a9dfa9")

