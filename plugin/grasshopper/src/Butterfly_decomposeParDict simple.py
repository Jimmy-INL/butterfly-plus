# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Simple decomposeParDict. Dictionary for parallel runs.

-

    Args:
        _xyz_div_: Number of subdomains in x, y, z as a list (default: (2, 1, 1)).
        _delta_: Cell skew factor (default: 0.001).
    Returns:
        decompose_par_dict: decomposeParDict.
"""

ghenv.Component.Name = "Butterfly_decomposeParDict simple"
ghenv.Component.NickName = "decomposeParDict_simple"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "08::Etc"
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    from butterfly.decomposeParDict import DecomposeParDict
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

try:
    x, y, z = _xyz_div_
except:
    x, y, z = 2, 1, 1

decompose_par_dict = DecomposeParDict.simple((x, y, z), _delta_)

