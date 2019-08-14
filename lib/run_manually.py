import os
import sys
import xbmc
import xbmcaddon
import xbmcgui
import inputstreamhelper

ADDON = xbmcaddon.Addon('script.module.inputstreamhelper')
LANGUAGE = ADDON.getLocalizedString

is_helper = inputstreamhelper.Helper('mpd', drm='com.widevine.alpha')

print(is_helper._addon_cdm_path())

if os.path.lexists(is_helper._widevine_config_path()):
    os.remove(is_helper._widevine_config_path())
    if os.path.lexists(is_helper._widevine_path()):
        os.remove(is_helper._widevine_path())

if (not is_helper._helper_disabled()) and is_helper.check_inputstream():
    dialog = xbmcgui.Dialog()
    dialog.ok(LANGUAGE(30037), LANGUAGE(30003))
