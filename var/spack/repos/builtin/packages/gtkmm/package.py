# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gtkmm(AutotoolsPackage):
    """Gtkmm is the official C++ interface for the popular GUI library GTK+."""

    homepage = "https://www.gtkmm.org/en/"
    url      = "https://ftp.acc.umu.se/pub/GNOME/sources/gtkmm/2.16/gtkmm-2.16.0.tar.gz"

    version('2.24.5', sha256='0680a53b7bf90b4e4bf444d1d89e6df41c777e0bacc96e9c09fc4dd2f5fe6b72')
    version('2.22.0', sha256='1cc8d26f9a0956092e61ecfbb029c5d6223cd7e49d4434653446ff190a990957')
    version('2.20.3', sha256='1cc8d26f9a0956092e61ecfbb029c5d6223cd7e49d4434653446ff190a990957')
    version('2.19.7', sha256='7cc8d26f9a0956092e61ecfbb029c5d6223cd7e49d4434653446ff190a990957')
    version('2.17.11', sha256='0ec15d7aa14a0528352adf91aa612079590ba377aa15f47f7c8d37611ffbfbcd')
    version('2.16.0', sha256='7b2cccda794531ecfa65c01e57614ecba526153ad2a29d580c6e8df028d56ec4')
    version('2.4.11', sha256='0754187a5bcf3795cd7c959de303e6a19a130b0c5927bff1504baa3524bee8c1')

    depends_on('glibmm')
    depends_on('atk')
    depends_on('atkmm', when='@2.24.0:')
    depends_on('gtkplus')
    depends_on('pangomm')
    depends_on('cairomm')

    def url_for_version(self, version):
        """Handle glib's version-based custom URLs."""
        url = "https://ftp.acc.umu.se/pub/GNOME/sources/gtkmm"
        ext = '.tar.gz' if version < Version('2.24.3') else '.tar.xz'
        return url + "/%s/gtkmm-%s%s" % (version.up_to(2), version, ext)
