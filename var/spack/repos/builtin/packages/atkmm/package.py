from spack import *


class Atkmm(AutotoolsPackage):
    """atkmm is the official C++ interface for the ATK accessibility toolkit
    library. It may be used, for instance, by user interfaces implemented
    with gtkmm."""

    homepage = "https://developer.gnome.org/atk/"
    url      = "https://ftp.gnome.org/pub/gnome/sources/atkmm/2.28/atkmm-2.28.0.tar.xz"
    list_url = "https://ftp.gnome.org/pub/gnome/sources/atkmm"
    list_depth = 1

    version('2.28.0', sha256='4c4cfc917fd42d3879ce997b463428d6982affa0fb660cafcc0bc2d9afcedd3a')

    depends_on('atk@1.18:')
    depends_on('glibmm@2.60.0:')

    def url_for_version(self, version):
        """Handle glibmm's version-based custom URLs."""
        url = "https://ftp.gnome.org/pub/gnome/sources/atkmm"
        return url + "/%s/atkmm-%s.tar.xz" % (version.up_to(2), version)
