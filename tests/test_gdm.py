from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import pytest
from plexapi.gdm import GDM


@pytest.mark.xfail(reason="Might fail on docker", strict=False)
def test_gdm(plex):
    gdm = GDM()

    gdm_enabled = plex.settings.get("GdmEnabled")

    gdm.scan(timeout=2)
    if gdm_enabled:
        assert len(gdm.entries)
    else:
        assert not len(gdm.entries)
