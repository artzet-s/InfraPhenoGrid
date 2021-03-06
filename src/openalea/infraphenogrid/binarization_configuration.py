# -*- python -*-
#
#       Copyright 2015 INRIA - CIRAD - INRA
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
# ==============================================================================


class RegionOfInterest:
    def __init__(self):
        self.hsv_min = None
        self.hsv_max = None
        self.mask = None


class MeanShiftBinarizationFactor(object):
    def __init__(self):
        self._threshold = 0.3
        self._dark_background = False

    # ==========================================================================
    # threshold
    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        if isinstance(value, type(self._threshold)):
            self._threshold = value

    # ==========================================================================
    # dark_background
    @property
    def dark_background(self):
        return self._dark_background

    @dark_background.setter
    def dark_background(self, value):
        if isinstance(value, type(self._dark_background)):
            self._dark_background = value


class BinarizationConfig:
    def __init__(self):
        #   ===================================================================
        #   Default value
        self.meanshift_binarization_factor = MeanShiftBinarizationFactor()

        self.roi_main = RegionOfInterest()
        self.roi_stem = RegionOfInterest()
        self.roi_pot = RegionOfInterest()
        self.roi_panel = RegionOfInterest()
        self.roi_orange_band = RegionOfInterest()

        self.cubicle_domain = None
        self.background = None
