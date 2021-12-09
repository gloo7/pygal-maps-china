# -*- coding: utf-8 -*-

# A python svg graph plotting library
# Copyright © 2016-2021 Gloo
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
"""
China chart
"""

# TODO Add english localization

# TODO Add tests

from __future__ import division
from pygal.graph.map import BaseMap
import os

REGIONS = {
    'AH': '安徽',
    'BJ': '北京',
    'CQ': '重庆',
    'FJ': '福建',
    'GD': '广东',
    'GS': '甘肃',
    'GX': '广西',
    'GZ': '贵州',
    'HA': '河南',
    'HB': '湖北',
    'HE': '河北',
    'HI': '海南',
    'HK': '香港',
    'HL': '黑龙江',
    'HN': '湖南',
    'JL': '吉林',
    'JS': '江苏',
    'JX': '江西',
    'LN': '辽宁',
    'MO': '澳门',
    'NM': '内蒙古',
    'NX': '宁夏',
    'QH': '青海',
    'SC': '四川',
    'SD': '山东',
    'SH': '上海',
    'SN': '陕西',
    'SX': '山西',
    'TJ': '天津',
    'TW': '台湾',
    'XJ': '新疆',
    'XZ': '西藏',
    'YN': '云南',
    'ZJ': '浙江',
}

with open(os.path.join(
        os.path.dirname(__file__),
        'china.svg')) as file:
    CHINA_MAP = file.read()


class Regions(BaseMap):
    """China graph"""
    x_labels = list(REGIONS.keys())
    area_names = REGIONS
    area_prefix = 'CN-'
    svg_map = CHINA_MAP
    kind = 'region'
