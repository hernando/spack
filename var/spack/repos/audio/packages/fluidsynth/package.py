from spack import *

class Fluidsynth(CMakePackage):

    homepage = "http://www.fluidsynth.org/"
    git = "https://github.com/FluidSynth/fluidsynth"

    generator='Ninja'

    version('2.1.2', tag='v2.1.2')

    variant('ladspa', default=False)
    # Disabling readline by default because CMake doesn't seem to
    # add the linking to libtinfo that readline needs.
    variant('readline', default=False)

    depends_on('ninja', type='build')
    depends_on("ladspa", type="build", when="+ladspa")

    depends_on("alsa")
    depends_on("dbus")
    depends_on("jack")
    depends_on("readline", when="+readline")
    depends_on("sndfile")

    def cmake_args(self):

        if '+readline' not in self.spec:
            return ["-Denable-readline=OFF"]
        return []
