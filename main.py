# Copyright (c) 2024, João Pedro de S.T.C
# Read EOF for more information

import CartographerModule

if __name__ != '__main__':
    RJ_MAP = CartographerModule.RJ_Map()
    gdf = RJ_MAP.load_map()
    RJ_MAP.plot_map()


import sys

sys.stdout.write("Muito obrigado, João Gabriel. "
                 "Vc eh pica\n")

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>