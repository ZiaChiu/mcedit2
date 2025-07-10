### 2025-07-10
- **create change log** [`24a5217`]
  **Files changed:** README.md, changelog.md

### 2025-07-10
- **change IF UNICODE_CACHE to def and if** [`88887b3`]
  **Files changed:** mceditlib/nbt.pyx

### 2025-06-05
- **py2to3:PyTypeObject** [`02aec1c`]
  **Files changed:** mceditlib/nbt.pyx

### 2025-06-05
- **corrected the source code path** [`52844ab`]
  **Files changed:** setup_mceditlib.py

### 2025-06-05
- **removed the pyside6 version request** [`0bb49c0`]
  **Files changed:** requirements.txt

### 2025-06-01
- **update environment details** [`c0ee8ab`]
  **Files changed:** requirements.txt

### 2025-06-01
- **update to new path** [`38bd7cd`]
  **Files changed:** setup_mcedit2.py

### 2025-06-01
- **py2to3** [`cad1bfb`]
  **Files changed:** mcedit2/util/resources.py

### 2025-06-01
- **no zlib and update all to latest version** [`527e012`]
  **Files changed:** requirements.txt

### 2025-06-01
- **change to command line compiling.** [`7bc75f9`]
  **Files changed:** mcedit2/util/gen_ui.py

### 2025-06-01
- **1. PEP N802 2. make "return none" explicit** [`4cee082`]
  **Files changed:** mcedit2/dialogs/configure_blocks.py

### 2025-06-01
- **1. py2to3 2. float to int** [`e1ec0d4`]
  **Files changed:** mcedit2/rendering/blockmodels.pyx

### 2024-05-19
- **Update README.md** [`bc967c3`]
  **Files changed:** README.md

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`14b31e5`]
  Imports:
  **Files changed:** Updated imports for PySide6., Changed from PySide import QtGui to from PySide6 import QtGui, QtCore., mcedit2/util/mceaction.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`28b3ce1`]
  Imports:
  **Files changed:** Updated imports for PySide6., Changed from PySide import QtUiTools, QtCore, QtGui to from PySide6 import QtUiTools, QtCore, QtWidgets., Widget Check:, Changed the assert statement to check for QtWidgets.QWidget instead of QtGui.QWidget., mcedit2/util/load_ui.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`b40f9e9`]
  Imports:
  **Files changed:** Updated imports for PySide6., Changed from PySide.QtOpenGL import QGLWidget to from PySide6 import QtOpenGL., Exception Handling:, Changed raise ValueError, "message" to raise ValueError("message")., Changed raise IOError, "message" to raise IOError("message")., Conversion:, Replaced numpy.fromstring with numpy.frombuffer since fromstring is deprecated for binary data in Python 3., String Formatting:, Updated to use f-strings for better readability and compatibility., mcedit2/util/load_png.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`196f05c`]
  # TODO: ipython.lib.gui_support does not support pyside6 or qt 6
  **Files changed:** # TODO: from the QT documentation to find a way replace gui_support, mcedit2/util/ipython_widget.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`15d15e5`]
  # TODO: ipython.lib.gui_support does not support pyside6 or qt 6
  **Files changed:** # TODO: from the QT documentation to find a way replace gui_support, mcedit2/util/ipython_widget.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`b32c6e5`]
  # TODO: ipython.lib.gui_support does not support pyside6 or qt 6
  **Files changed:** # TODO: from the QT documentation to find a way replace gui_support, mcedit2/util/ipython_widget.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`a6dcd77`]
  Imports:
  **Files changed:** Removed the import of sys which was not used., Replaced numpy with numpy as np to match common usage patterns and improve readability., Imported functools for reduce function., Class and Method Updates:, Updated context managers and method implementations to be more Pythonic., Used functools.reduce directly for attribute combination., Modern Python Features:, Used modern Python string formatting (format method)., Ensured code is compatible with Python 3.12., mcedit2/util/glutils.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`bdd4f59`]
  Import Update:
  **Files changed:** Changed the import to use PySide6.scripts.pyside_tool.pyside6_uic for compiling UI files., Module Update:, The function compileUiDir from PySide is replaced with a custom compile_ui_dir function that uses pyside6_uic.compileUi to compile .ui files., Function Update:, Added compile_ui_dir function to iterate through the directory and compile each .ui file it finds into a .py file using pyside6_uic.compileUi., Logging:, Added logging to show which files are being compiled., mcedit2/util/gen_ui.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`925bcf3`]
  Import Update:
  **Files changed:** Changed the import to use PySide6.scripts.pyside_tool.pyside6_uic for compiling UI files., Module Update:, The function compileUiDir from PySide is replaced with a custom compile_ui_dir function that uses pyside6_uic.compileUi to compile .ui files., Function Update:, Added compile_ui_dir function to iterate through the directory and compile each .ui file it finds into a .py file using pyside6_uic.compileUi., Logging:, Added logging to show which files are being compiled., mcedit2/util/gen_ui.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`ce4ddd8`]
  Import Update:
  **Files changed:** Changed the import from PySide to PySide6., Module Update:, Updated the import from QtGui to QtWidgets, as QMessageBox is now part of QtWidgets in PySide6., Function Update:, The function NotImplementedYet remains the same, but it uses QtWidgets.QMessageBox instead of QtGui.QMessageBox., mcedit2/util/dialogs.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`48246e2`]
  This script customizes the traceback module to include the class name of the self parameter when printing tracebacks. It modifies the functions extract_tb, format_list, print_list, and print_tb and installs them to override the default behavior of the traceback module.
  **Files changed:** mcedit2/util/custom_traceback.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`b8797bc`]
  Changed import from PySide to PySide6 for compatibility with PySide6.
  **Files changed:** Updated log statements to use log.warning instead of log.warn, which is deprecated in Python 3.12., Removed from __future__ import absolute_import, division, print_function, unicode_literals as it's unnecessary for Python 3.12., Updated the testReencodeWithDataTag function to use json instead of demjson, which is not commonly used., mcedit2/util/commandblock.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`7d58bd7`]
  **Files changed:** mcedit2/util/bugfixes.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`be4d6f3`]
  Updated function signatures to remove tuple unpacking in the parameters.
  **Files changed:** Converted print statements to use Python 3's print() function., Changed map() calls to use list(map()) where necessary for compatibility with Python 3., Removed unused imports (collections and functools)., mcedit2/util/bresenham.py

### 2024-05-18
- **updated requirements.txt** [`f3022bd`]
  Refactored the getUserFilesDirectory function to improve its readability and add support for multiple platforms under directories in win32.py. It now includes documentation and clear branching for different scenarios, i.e., running from a frozen build or from source. Distinguished between win32 platform and others for frozen builds.
  **Files changed:** requirements.txt

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`1be61dd`]
  Refactored the getUserFilesDirectory function to improve its readability and add support for multiple platforms under directories in win32.py. It now includes documentation and clear branching for different scenarios, i.e., running from a frozen build or from source. Distinguished between win32 platform and others for frozen builds.
  **Files changed:** tests/test_mcedit2/player_server_test.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`e0870a0`]
  Refactored the getUserFilesDirectory function to improve its readability and add support for multiple platforms under directories in win32.py. It now includes documentation and clear branching for different scenarios, i.e., running from a frozen build or from source. Distinguished between win32 platform and others for frozen builds.
  **Files changed:** mcedit2/util/directories/win32.py

### 2024-05-18
- **Update comment for clarity in posix.py** [`be49feb`]
  Refined a comment in posix.py to improve clarity and readability. The term 'installs' was replaced with 'installations' to enhance understanding for future code maintainability.
  **Files changed:** mcedit2/util/directories/posix.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`2f760c2`]
  **Files changed:** mcedit2/util/directories/posix.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`657eb34`]
  **Files changed:** mcedit2/synth/l_system.py, mcedit2/synth/l_system_plugin.py, mcedit2/util/directories/__init__.py, mcedit2/util/directories/mac.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`fc0b8ab`]
  **Files changed:** mcedit2/rendering/worldscene.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`af78974`]
  **Files changed:** mcedit2/rendering/textureatlas.py

### 2024-05-18
- **Py2/PySide to Py3/PySide6** [`c3145db`]
  **Files changed:** mcedit2/rendering/textureatlas.py

### 2024-05-18
- **# TODO: find some way of pyside6 to replace the QTimer of pyside** [`95cfed6`]
  **Files changed:** mcedit2/rendering/selection.py

### 2024-05-18
- **# TODO: find some way of pyside6 to replace the QTimer of pyside** [`d6077c4`]
  **Files changed:** mcedit2/rendering/selection.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`4930f33`]
  **Files changed:** mcedit2/rendering/selection.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`0e382b0`]
  **Files changed:** mcedit2/rendering/players.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`558095d`]
  **Files changed:** mcedit2/rendering/modelmesh.pyx

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`17da2f0`]
  Updated import statements and usage for numpy to np.
  **Files changed:** Used Python 3.x syntax for super() calls., Replaced .iteritems() with .items() for dictionary iteration., mcedit2/rendering/loadablechunks.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`58575df`]
  Updated function names to snake_case.
  **Files changed:** Replaced range with np.zeros for light_brightness_table., Used np.ndindex for iteration., Ensured floating point calculations and array manipulations are clear and correct., Used f-strings for string formatting., mcedit2/rendering/lightmap.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`cc8cc13`]
  Updated the super() call to use the modern syntax.
  **Files changed:** Replaced itervalues() with values() for compatibility with Python 3., Used f-strings for formatting the size in cache_stats()., mcedit2/rendering/geometrycache.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`111e3b5`]
  Updated the import statements for numpy and OpenGL.
  **Files changed:** Used more Pythonic syntax and idioms for compatibility with Python 3.12., Ensured the code uses consistent formatting and removed deprecated functions., mcedit2/rendering/frustum.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`4b2038e`]
  **Files changed:** mcedit2/rendering/cubes.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`eb6c457`]
  **Files changed:** mcedit2/rendering/compass.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`d9a2ea9`]
  **Files changed:** mcedit2/rendering/command_visuals.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`1ab9b43`]
  Updated the import statements to PySide6.
  **Files changed:** Changed the super() calls to Python 3 syntax., Updated the method containsChunkNode to accept a tuple instead of unpacking it directly., Updated dictionary iteration to use .values() instead of .itervalues()., Used f-strings for better readability in string formatting., mcedit2/rendering/chunknode.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`f86d68d`]
  Updated the import statements to PySide6.
  **Files changed:** Changed the super() calls to Python 3 syntax., Updated tuple unpacking and annotations for functions to be compatible with Python 3., Updated string formatting to f-strings for better readability., Changed next method to __next__ to comply with Python 3 iterator protocol., mcedit2/rendering/chunkloader.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`99ee368`]
  **Files changed:** mcedit2/rendering/blockmodels.pyx

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`a547fc8`]
  **Files changed:** mcedit2/rendering/blockmeshes.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`f18b2fd`]
  **Files changed:** mcedit2/rendering/scenegraph/texture_atlas.py, mcedit2/rendering/scenegraph/vertex_array.py

### 2024-05-18
- **updated to Cython 3.0.10** [`8ea2544`]
  **Files changed:** mcedit2/rendering/blockmodels.pxd

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`9355254`]
  **Files changed:** mcedit2/rendering/scenegraph/scenenode.py

### 2024-05-18
- **Py2/Pyside to Py3/PySide6** [`ca8da24`]
  **Files changed:** mcedit2/plugins/registry.py

### 2024-05-18
- **PEP 803** [`aaf60f3`]
  **Files changed:** mcedit2/rendering/scenegraph/depth_test.py

### 2024-05-17
- **Py2/Pyside to Py3/PySide6** [`1eecf27`]
  **Files changed:** mcedit2/plugins/command.py

### 2024-05-17
- **replaced imp to importlib** [`c92afb1`]
  **Files changed:** mcedit2/plugins/__init__.py

### 2024-05-17
- **Py2/PySide convert to Py3/PySide6** [`12f75d3`]
  **Files changed:** mcedit2/panels/worldinfo.py, mcedit2/plugins/__init__.py

### 2024-05-17
- **Py2/PySide convert to Py3/PySide6** [`39ec73d`]
  **Files changed:** mcedit2/panels/player.py

### 2024-05-17
- **TODO: PySide6 clicked connection problem** [`d57f0b3`]
  **Files changed:** mcedit2/panels/pending_imports.py

### 2024-05-17
- **Py2/PySide to Py3/PySide6** [`7b475f4`]
  **Files changed:** mcedit2/panels/pending_imports.py

### 2024-05-17
- **Py2/PySide to Py3/PySide6** [`80ba26d`]
  **Files changed:** mcedit2/handles/boxhandle.py, mcedit2/panels/map.py, setup_mcedit2.py

### 2024-05-17
- **Py2/PySide to Py3/PySide6 conversion** [`5f80f86`]
  **Files changed:** mcedit2/dialogs/configure_blocks.py, mcedit2/dialogs/error_dialog.py, mcedit2/dialogs/plugins_dialog.py, mcedit2/editorcommands/analyze.py, mcedit2/editorcommands/fill.py, mcedit2/editorcommands/find_replace/__init__.py, mcedit2/editorcommands/find_replace/command_text.py, mcedit2/editorcommands/find_replace/nbt.py, mcedit2/editorcommands/find_replace/replace_blocks.py, mcedit2/editortools/__init__.py, mcedit2/editortools/brush/__init__.py, mcedit2/editortools/brush/masklevel.py, mcedit2/editortools/brush/modes.py, mcedit2/editortools/brush/shapes.py, mcedit2/editortools/clone.py, mcedit2/editortools/edit_chunk.py, mcedit2/editortools/generate.py, mcedit2/editortools/move.py, mcedit2/editortools/select.py, mcedit2/editortools/select_block.py, mcedit2/editortools/select_entity.py, mcedit2/widgets/shapewidget.py

### 2024-05-17
- **move out from src** [`3dae853`]
  **Files changed:** mcedit2/dialogs/__init__.py, mcedit2/editorcommands/__init__.py

### 2024-05-17
- **move out from src** [`d286cd2`]
  **Files changed:** mcedit2/__init__.py, mcedit2/appsettings.py, mcedit2/assets/mcedit2/block_unknown.png, mcedit2/assets/mcedit2/clock/dawn.png, mcedit2/assets/mcedit2/clock/evening.png, mcedit2/assets/mcedit2/clock/night.png, mcedit2/assets/mcedit2/clock/noon.png, mcedit2/assets/mcedit2/dialogicons/dialog-error-7.png, mcedit2/assets/mcedit2/dialogicons/dialog-information-3.png, mcedit2/assets/mcedit2/dialogicons/dialog-warning-2.png, mcedit2/assets/mcedit2/dialogicons/dialog-warning-4.png, mcedit2/assets/mcedit2/icons/add.png, mcedit2/assets/mcedit2/icons/edit_map.png, mcedit2/assets/mcedit2/icons/edit_player.png, mcedit2/assets/mcedit2/icons/edit_worldinfo.png, mcedit2/assets/mcedit2/icons/fill.png, mcedit2/assets/mcedit2/icons/history.png, mcedit2/assets/mcedit2/icons/library.png, mcedit2/assets/mcedit2/icons/mirror.png, mcedit2/assets/mcedit2/icons/remove.png, mcedit2/assets/mcedit2/icons/right_angle.png, mcedit2/assets/mcedit2/icons/save.png, mcedit2/assets/mcedit2/icons/save_ok.png, mcedit2/assets/mcedit2/icons/shapes/chunk.png, mcedit2/assets/mcedit2/icons/shapes/cylinder.png, mcedit2/assets/mcedit2/icons/shapes/diamond.png, mcedit2/assets/mcedit2/icons/shapes/parabolic_dome.png, mcedit2/assets/mcedit2/icons/shapes/round.png, mcedit2/assets/mcedit2/icons/shapes/square.png, mcedit2/assets/mcedit2/icons/toolbar_text.png, mcedit2/assets/mcedit2/mcediticon.png, mcedit2/assets/mcedit2/mcediticonbig.png, mcedit2/assets/mcedit2/nbticons/LICENSE.txt, mcedit2/assets/mcedit2/nbticons/array.png, mcedit2/assets/mcedit2/nbticons/byte.png, mcedit2/assets/mcedit2/nbticons/compound.png, mcedit2/assets/mcedit2/nbticons/double.png, mcedit2/assets/mcedit2/nbticons/float.png, mcedit2/assets/mcedit2/nbticons/int.png, mcedit2/assets/mcedit2/nbticons/list.png, mcedit2/assets/mcedit2/nbticons/long.png, mcedit2/assets/mcedit2/nbticons/short.png, mcedit2/assets/mcedit2/nbticons/text.png, mcedit2/assets/mcedit2/reload.png, mcedit2/assets/mcedit2/textures/compass.png, mcedit2/assets/mcedit2/textures/compass_small.png, mcedit2/assets/mcedit2/toolicons/brush.png, mcedit2/assets/mcedit2/toolicons/clone.png, mcedit2/assets/mcedit2/toolicons/edit_block.png, mcedit2/assets/mcedit2/toolicons/edit_chunk.png, mcedit2/assets/mcedit2/toolicons/edit_entity.png, mcedit2/assets/mcedit2/toolicons/flood_fill.png, mcedit2/assets/mcedit2/toolicons/generate.png, mcedit2/assets/mcedit2/toolicons/move.png, mcedit2/assets/mcedit2/toolicons/select_blocks.png, mcedit2/assets_raw/compass.svg, mcedit2/assets_raw/icons.svg, mcedit2/assets_raw/playerskins/Vechs_skin_cover.png, mcedit2/assets_raw/playerskins/capt_world.png, mcedit2/assets_raw/reload.svg, mcedit2/command.py, mcedit2/editorapp.py, mcedit2/editorsession.py, mcedit2/editortools/flood_fill.py, mcedit2/editortools/tool_settings.py, mcedit2/handles/__init__.py, mcedit2/handles/boxhandle.py, mcedit2/i18n/en.qm, mcedit2/imports.py, mcedit2/library.py, mcedit2/main.py, mcedit2/panels/__init__.py, mcedit2/panels/map.py, mcedit2/panels/pending_imports.py, mcedit2/panels/player.py, mcedit2/panels/worldinfo.py, mcedit2/plugins/__init__.py, mcedit2/plugins/command.py, mcedit2/plugins/registry.py, mcedit2/rendering/__init__.py, mcedit2/rendering/blockmeshes.py, mcedit2/rendering/blockmodels.pxd, mcedit2/rendering/blockmodels.pyx, mcedit2/rendering/chunkloader.py, mcedit2/rendering/chunkmeshes/__init__.py, mcedit2/rendering/chunkmeshes/chunksections.py, mcedit2/rendering/chunkmeshes/entity/__init__.py, mcedit2/rendering/chunkmeshes/entity/armorstand.py, mcedit2/rendering/chunkmeshes/entity/biped.py, mcedit2/rendering/chunkmeshes/entity/chest.py, mcedit2/rendering/chunkmeshes/entity/creeper.py, mcedit2/rendering/chunkmeshes/entity/modelrenderer.py, mcedit2/rendering/chunkmeshes/entity/models.py, mcedit2/rendering/chunkmeshes/entity/player.py, mcedit2/rendering/chunkmeshes/entity/quadruped.py, mcedit2/rendering/chunkmeshes/entity/shulker.py, mcedit2/rendering/chunkmeshes/entity/spider.py, mcedit2/rendering/chunkmeshes/entity/villager.py, mcedit2/rendering/chunkmeshes/entitymesh.py, mcedit2/rendering/chunkmeshes/heightlevel.py, mcedit2/rendering/chunkmeshes/lowdetail.py, mcedit2/rendering/chunkmeshes/mobspawns.py, mcedit2/rendering/chunkmeshes/terrainpop.py, mcedit2/rendering/chunkmeshes/tileticks.py, mcedit2/rendering/chunknode.py, mcedit2/rendering/chunkupdate.py, mcedit2/rendering/command_visuals.py, mcedit2/rendering/compass.py, mcedit2/rendering/cubes.py, mcedit2/rendering/depths.py, mcedit2/rendering/frustum.py, mcedit2/rendering/geometrycache.py, mcedit2/rendering/hiddenstates_19.json, mcedit2/rendering/hiddenstates_1_10.json, mcedit2/rendering/hiddenstates_1_11.json, mcedit2/rendering/hiddenstates_1_12.json, mcedit2/rendering/layers.py, mcedit2/rendering/lightmap.py, mcedit2/rendering/loadablechunks.py, mcedit2/rendering/minecraft_hiddenstates_raw.json, mcedit2/rendering/modelmesh.pyx, mcedit2/rendering/players.py, mcedit2/rendering/renderstates.py, mcedit2/rendering/scenegraph/__init__.py, mcedit2/rendering/scenegraph/bind_texture.py, mcedit2/rendering/scenegraph/depth_test.py, mcedit2/rendering/scenegraph/matrix.py, mcedit2/rendering/scenegraph/misc.py, mcedit2/rendering/scenegraph/rendernode.py, mcedit2/rendering/scenegraph/scenenode.py, mcedit2/rendering/scenegraph/states.py, mcedit2/rendering/scenegraph/texture_atlas.py, mcedit2/rendering/scenegraph/vertex_array.py, mcedit2/rendering/selection.py, mcedit2/rendering/sky.py, mcedit2/rendering/slices.py, mcedit2/rendering/textureatlas.py, mcedit2/rendering/vertexarraybuffer.py, mcedit2/rendering/workplane.py, mcedit2/rendering/worldscene.py, mcedit2/resourceloader.py, mcedit2/sentry.py, mcedit2/styles/mcedit2.qcss, mcedit2/support_modules.py, mcedit2/synth/__init__.py, mcedit2/synth/l_system.py, mcedit2/synth/l_system_plugin.py, mcedit2/ui/Makefile, mcedit2/ui/__init__.py, mcedit2/ui/analyze.ui, mcedit2/ui/block_replacements.ui, mcedit2/ui/blocktype_list.ui, mcedit2/ui/dialogs/__init__.py, mcedit2/ui/dialogs/configure_blocks.ui, mcedit2/ui/dialogs/error_dialog.ui, mcedit2/ui/dialogs/plugins.ui, mcedit2/ui/dialogs/preferences.ui, mcedit2/ui/editortools/__init__.py, mcedit2/ui/editortools/brush.ui, mcedit2/ui/editortools/select_block.ui, mcedit2/ui/editortools/select_chunk.ui, mcedit2/ui/editortools/select_entity.ui, mcedit2/ui/fill.ui, mcedit2/ui/find_replace.ui, mcedit2/ui/find_replace_blocks.ui, mcedit2/ui/find_replace_command_results.ui, mcedit2/ui/find_replace_commands.ui, mcedit2/ui/find_replace_nbt.ui, mcedit2/ui/find_replace_nbt_results.ui, mcedit2/ui/images/config.png, mcedit2/ui/images/query.png, mcedit2/ui/images/update.png, mcedit2/ui/import_map.ui, mcedit2/ui/inspector.ui, mcedit2/ui/library.ui, mcedit2/ui/log_view.ui, mcedit2/ui/main_window.ui, mcedit2/ui/mcedit2.qrc, mcedit2/ui/minecraft_installs.ui, mcedit2/ui/panels/__init__.py, mcedit2/ui/panels/map.ui, mcedit2/ui/panels/player.ui, mcedit2/ui/panels/worldinfo.ui, mcedit2/ui/rotation_widget.ui, mcedit2/ui/scale_widget.ui, mcedit2/ui/selection_coord_widget.ui, mcedit2/ui/widgets/__init__.py, mcedit2/ui/widgets/block_picker_multiple.ui, mcedit2/ui/widgets/coord_widget.ui, mcedit2/ui/world_list.ui, mcedit2/util/__init__.py, mcedit2/util/bresenham.py, mcedit2/util/bugfixes.py, mcedit2/util/commandblock.py, mcedit2/util/custom_traceback.py, mcedit2/util/dialogs.py, mcedit2/util/directories/__init__.py, mcedit2/util/directories/mac.py, mcedit2/util/directories/posix.py, mcedit2/util/directories/win32.py, mcedit2/util/gen_ui.py, mcedit2/util/glutils.py, mcedit2/util/ipython_widget.py, mcedit2/util/load_png.py, mcedit2/util/load_ui.py, mcedit2/util/mceaction.py, mcedit2/util/mimeformats.py, mcedit2/util/minecraftinstall.py, mcedit2/util/objgraphwidget.py, mcedit2/util/player_server.py, mcedit2/util/profiler.py, mcedit2/util/profilerui.py, mcedit2/util/qglcontext.py, mcedit2/util/raycast.py, mcedit2/util/resources.py, mcedit2/util/screen.py, mcedit2/util/settings.py, mcedit2/util/showprogress.py, mcedit2/util/undostack.py, mcedit2/util/worldloader.py, mcedit2/widgets/__init__.py, mcedit2/widgets/block_replacement_list.py, mcedit2/widgets/blockpicker.py, mcedit2/widgets/blockpicker_util.py, mcedit2/widgets/blocktype_list.py, mcedit2/widgets/brushmode.py, mcedit2/widgets/coord_widget.py, mcedit2/widgets/flowlayout.py, mcedit2/widgets/infopanel.py, mcedit2/widgets/inspector/__init__.py, mcedit2/widgets/inspector/tileentities/__init__.py, mcedit2/widgets/inspector/tileentities/chest.py, mcedit2/widgets/inspector/tileentities/command.py, mcedit2/widgets/inspector/tileentities/sign.py, mcedit2/widgets/inventory.py, mcedit2/widgets/itemtype_list.py, mcedit2/widgets/layout.py, mcedit2/widgets/log_view.py, mcedit2/widgets/mcedockwidget.py, mcedit2/widgets/nbttree/__init__.py, mcedit2/widgets/nbttree/nbteditor.py, mcedit2/widgets/nbttree/nbttreemodel.py, mcedit2/widgets/objectinspector.py, mcedit2/widgets/prefsdialog/__init__.py, mcedit2/widgets/prefsdialog/camera.py, mcedit2/widgets/propertylist.py, mcedit2/widgets/rotation_widget.py, mcedit2/widgets/scale_widget.py, mcedit2/widgets/spinslider.py, mcedit2/worldlist.py, mcedit2/worldview/__init__.py, mcedit2/worldview/camera.py, mcedit2/worldview/cutaway.py, mcedit2/worldview/fourup.py, mcedit2/worldview/iso.py, mcedit2/worldview/minimap.py, mcedit2/worldview/overhead.py, mcedit2/worldview/schematic_worldview.py, mcedit2/worldview/viewaction.py, mcedit2/worldview/viewcontrols.py, mcedit2/worldview/worldruler.py, mcedit2/worldview/worldview.py, mceditlib/__init__.py, mceditlib/anvil/__init__.py, mceditlib/anvil/adapter.py, mceditlib/anvil/biome_types.py, mceditlib/anvil/biomes.csv, mceditlib/anvil/entities.py, mceditlib/anvil/worldfolder.py, mceditlib/block_copy.py, mceditlib/blocktypes/__init__.py, mceditlib/blocktypes/blockdumper/1.10/BlockDumper.java, mceditlib/blocktypes/blockdumper/1.11/BlockDumper.java, mceditlib/blocktypes/blockdumper/1.12/BlockDumper.java, mceditlib/blocktypes/blockdumper/1.8/BlockDumper.java, mceditlib/blocktypes/blockdumper/1.9/BlockDumper.java, mceditlib/blocktypes/idmapping.json, mceditlib/blocktypes/idmapping_raw.json, mceditlib/blocktypes/idmapping_raw_19.json, mceditlib/blocktypes/idmapping_raw_1_10.json, mceditlib/blocktypes/idmapping_raw_1_11.json, mceditlib/blocktypes/idmapping_raw_1_12.json, mceditlib/blocktypes/itemtypes.py, mceditlib/blocktypes/json_resources.py, mceditlib/blocktypes/minecraft.json, mceditlib/blocktypes/minecraft_raw.json, mceditlib/blocktypes/minecraft_raw_19.json, mceditlib/blocktypes/minecraft_raw_1_10.json, mceditlib/blocktypes/minecraft_raw_1_11.json, mceditlib/blocktypes/minecraft_raw_1_12.json, mceditlib/blocktypes/rotation.py, mceditlib/blocktypes/tmp_itemblocks.json, mceditlib/blocktypes/tmp_items.json, mceditlib/cachefunc.py, mceditlib/directories.py, mceditlib/exceptions.py, mceditlib/export.py, mceditlib/faces.py, mceditlib/fakechunklevel.py, mceditlib/findadapter.py, mceditlib/geometry.py, mceditlib/heightmaps.py, mceditlib/items.txt, mceditlib/java.py, mceditlib/minecraft_server.py, mceditlib/multi_block.py, mceditlib/nbt.pyx, mceditlib/nbtattr.py, mceditlib/operations/__init__.py, mceditlib/operations/analyze.py, mceditlib/operations/block_fill.py, mceditlib/operations/entity.py, mceditlib/pc/__init__.py, mceditlib/pc/regionfile.py, mceditlib/pocket.py, mceditlib/relight/__init__.py, mceditlib/relight/pure_python.py, mceditlib/relight/with_cython.pyx, mceditlib/relight/with_sections.py, mceditlib/relight/with_setblocks.py, mceditlib/revisionhistory.py, mceditlib/schematic.py, mceditlib/selection/__init__.py, mceditlib/selection/hollow.py, mceditlib/structure.py, mceditlib/transform.py, mceditlib/util/__init__.py, mceditlib/util/demjson.py, mceditlib/util/lazyprop.py, mceditlib/util/progress.py, mceditlib/util/unique_nd.py, mceditlib/worldeditor.py, plugins/city.py, plugins/count_blocks.py, plugins/hilbert.py, plugins/koch.py, plugins/simple_options.py, plugins/storagedrawers.py, plugins/world_editing_demo.py, requirements-mceditlib.txt, requirements.txt

### 2018-08-14
- **Pin PyInstaller** [`4bb98da`]
  **Files changed:** .travis.yml, appveyor.yml

### 2018-08-13
- **Roll back Cython** [`aad765a`]
  **Files changed:** requirements-mceditlib.txt

### 2018-08-13
- **Fix NBT name search matching unnamed tags** [`83e3935`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/nbt.py

### 2018-02-26
- **Don't translate this string** [`3284e98`]
  **Files changed:** src/mcedit2/editorsession.py

### 2018-02-02
- **Fix #370 - error in docstring** [`7a99da5`]
  **Files changed:** src/mceditlib/transform.py

### 2018-02-02
- **Increase maximum repeat count** [`af48a76`]
  **Files changed:** src/mcedit2/editortools/clone.py

### 2018-02-02
- **Fix sections being created immediately above build height** [`ff1dbfa`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2018-02-02
- **Fix clone tool coordinate input not updating on initial use and in relative mode** [`7a6663b`]
  **Files changed:** src/mcedit2/editortools/clone.py

### 2018-02-02
- **Fix incorrectly rethrown exception on erroring chunks** [`33cc35b`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2018-02-02
- **Move painting TileX adjustment to painting class** [`bf5923c`]
  **Files changed:** src/mceditlib/anvil/entities.py

### 2018-02-02
- **NBT search with both tag name and value matches both, not either** [`a79621d`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/nbt.py

### 2017-12-15
- **Change ID_SHORT_ARRAY to ID_LONG_ARRAY** [`54f5efe`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbttreemodel.py, tests/test_mceditlib/nbt_test.py

### 2017-12-15
- **Issue #371 - implement worldEditor.getWorldVersionInfo()** [`1bd31fb`]
  **Files changed:** src/mceditlib/anvil/adapter.py, src/mceditlib/worldeditor.py

### 2017-12-15
- **Use `Version` tag of level.dat to display version in world list** [`169309d`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2017-12-14
- **Implement TAG_Long_Array** [`e30dbea`]
  **Files changed:** src/mceditlib/nbt.pyx

### 2017-12-12
- **Also trap UnicodeErrors as LevelFormatErrors** [`243e306`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2017-12-08
- **Try to fix travis error "Homebrew must be run under Ruby 2.3! You're running 2.0.0."** [`76afe27`]
  **Files changed:** .travis.yml

### 2017-12-08
- **Don't report any plugin loading/unloading errors** [`97fb234`]
  **Files changed:** src/mcedit2/dialogs/error_dialog.py

### 2017-12-02
- **Reject MCEdit 1.0 filters explicitly, without reporting an error** [`ef557db`]
  **Files changed:** src/mcedit2/dialogs/plugins_dialog.py, src/mcedit2/editorapp.py

### 2017-12-02
- **Disallow opening the same world in multiple tabs** [`90c4739`]
  **Files changed:** src/mcedit2/editorapp.py

### 2017-12-02
- **Fix dock widgets disappearing when changing/closing tabs** [`4721146`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/widgets/mcedockwidget.py

### 2017-12-02
- **Fix "integer expected, got float" and similar errors related to SpinSlider value** [`685c0c9`]
  **Files changed:** src/mcedit2/widgets/spinslider.py

### 2017-10-07
- **Fix "NoneType has no attribute 'any'" when brushing** [`32988f9`]
  **Files changed:** src/mcedit2/editortools/brush/modes.py

### 2017-07-25
- **Fix "unsupported operand" after some sequence of selections** [`8874265`]
  **Files changed:** src/mcedit2/handles/boxhandle.py

### 2017-07-25
- **Fix delete operations attempted with no selection** [`84faf55`]
  **Files changed:** src/mcedit2/editorsession.py

### 2017-07-24
- **Fix excess command block visuals** [`3f79c61`]
  **Files changed:** src/mcedit2/widgets/inspector/__init__.py

### 2017-07-24
- **Inspector doesn't keep refs to objects no longer being inspected** [`df47148`]
  **Files changed:** src/mcedit2/widgets/inspector/__init__.py, src/mcedit2/widgets/nbttree/nbteditor.py

### 2017-07-24
- **Implement find/replace NBT in chunks** [`5f63a55`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/nbt.py, src/mcedit2/editorsession.py, src/mcedit2/ui/find_replace_nbt.ui

### 2017-07-22
- **Fix box face highlight not staying put when moving selection** [`cbdafb3`]
  **Files changed:** src/mcedit2/handles/boxhandle.py

### 2017-07-22
- **Using inspector to delete entity/tile entity does not break inspector** [`02917b7`]
  **Files changed:** src/mcedit2/widgets/inspector/__init__.py

### 2017-07-22
- **Select Entity refreshes hits on each undo/redo** [`eefb2f0`]
  **Files changed:** src/mcedit2/editortools/select_entity.py

### 2017-07-22
- **Improved Select Entity hit detection** [`2e90cf5`]
  **Files changed:** src/mcedit2/editortools/select_entity.py

### 2017-07-22
- **Select Entity tool no longer adds undos for each click** [`2194bfd`]
  **Files changed:** src/mcedit2/editortools/select_entity.py

### 2017-07-22
- **Inspector window refreshes on each undo/redo** [`f08e033`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/nbt.py, src/mcedit2/editorsession.py, src/mcedit2/editortools/select_entity.py, src/mcedit2/ui/inspector.ui, src/mcedit2/widgets/inspector/__init__.py, src/mceditlib/anvil/entities.py

### 2017-07-22
- **Don't allow NBT value editing for arrays, lists and compounds (for now)** [`1c288b3`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2017-07-20
- **Fix TypeError when dragging outside of selection(?)** [`7912f9e`]
  **Files changed:** src/mcedit2/handles/boxhandle.py

### 2017-07-20
- **Actually fix brush cursor not completely removed** [`92fb889`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py

### 2017-07-20
- **Fix OverflowError when value is too large/small for NBT tag type** [`d760856`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2017-07-20
- **Fix AttributeError when shift-clicking with select tool with no selection** [`cd0749d`]
  **Files changed:** src/mcedit2/handles/boxhandle.py

### 2017-07-19
- **Remove all calls to glPushClientAttrib** [`9094d59`]
  Some drivers don't implement it correctly, not resetting vertex array
  **Files changed:** attributes when popped, causing access violations even when the vertex, array is unused., src/mcedit2/rendering/cubes.py, src/mcedit2/util/glutils.py

### 2017-07-19
- **Rewrite CompassNode using node states** [`2438912`]
  **Files changed:** src/mcedit2/rendering/compass.py, src/mcedit2/rendering/scenegraph/matrix.py, src/mcedit2/rendering/scenegraph/misc.py, src/mcedit2/rendering/scenegraph/vertex_array.py

### 2017-07-18
- **fix signal name in configure_blocks dialog** [`cc266a4`]
  As per the documentation at http://pyside.github.io/docs/pyside/PySide/QtGui/QComboBox.html, the correct name for the signal is `editTextChanged`, not `textChanged`.
  **Files changed:** src/mcedit2/dialogs/configure_blocks.py

### 2017-07-13
- **Be more resilient in setWidgetError xxxxx** [`915266c`]
  TODO: More sensible error display here
  **Files changed:** src/mcedit2/widgets/layout.py

### 2017-07-13
- **Disable TEXTURE_2D on TEXTURE1 when vertex data is not given** [`3ed3bb0`]
  **Files changed:** src/mcedit2/rendering/scenegraph/vertex_array.py

### 2017-07-13
- **Squish some loggers** [`898847e`]
  **Files changed:** src/mcedit2/handles/boxhandle.py

### 2017-07-13
- **Allow stealing back the session lock, with appropriate warnings.** [`adf3659`]
  **Files changed:** src/mcedit2/editorsession.py, src/mceditlib/anvil/adapter.py, src/mceditlib/worldeditor.py

### 2017-07-03
- **Fix brush cursor not being fully removed in all cases** [`5119324`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py

### 2017-07-03
- **Actually use 1.12 blocks** [`9fd6905`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/util/minecraftinstall.py, src/mceditlib/blocktypes/__init__.py

### 2017-07-03
- **Fix #340 - incomplete redstone wire rendering** [`b7d86a9`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2017-07-03
- **Add 1.12 block defs** [`a5c0fc3`]
  **Files changed:** src/mcedit2/rendering/hiddenstates_1_12.json, src/mceditlib/blocktypes/blockdumper/1.12/BlockDumper.java, src/mceditlib/blocktypes/idmapping_raw_1_12.json, src/mceditlib/blocktypes/minecraft_raw_1_12.json

### 2017-07-03
- **Koch plugin: Ignore empty selection in boundsChanged** [`91645f1`]
  **Files changed:** src/plugins/koch.py

### 2017-07-03
- **Create fake names for unknown blocks** [`288afd7`]
  **Files changed:** src/mceditlib/blocktypes/__init__.py

### 2017-07-03
- **Partially disable inventory edits in read-only mode** [`4aa0c20`]
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2017-07-03
- **Disable editing commands in read-only mode** [`63f8bb6`]
  **Files changed:** src/mcedit2/widgets/inspector/tileentities/command.py

### 2017-07-03
- **Disable "Add Block" button when no block is named** [`1001597`]
  **Files changed:** src/mcedit2/dialogs/configure_blocks.py

### 2017-07-02
- **Use session.beginSimpleCommand in a few places** [`0cf5371`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/nbt.py, src/mcedit2/widgets/inspector/__init__.py, src/mcedit2/widgets/nbttree/nbteditor.py

### 2017-07-02
- **Add read-only mode to block/chunk inspector** [`acdc51b`]
  **Files changed:** src/mcedit2/widgets/inspector/__init__.py

### 2017-07-02
- **Add read-only mode to NBT editor** [`ddc3b15`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbteditor.py, src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2017-07-02
- **Catch errors when loading PNG file** [`abb0089`]
  **Files changed:** src/mcedit2/rendering/players.py

### 2017-07-01
- **Fix "Replace" commands being enabled in read-only mode** [`8135971`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/nbt.py, src/mcedit2/editorcommands/find_replace/replace_blocks.py

### 2017-07-01
- **Fix global mouse movement breaking after right-clicking in camera view** [`35b688d`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2017-07-01
- **Fix Select/Remove buttons being usable on empty installs table** [`8b144d7`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2017-07-01
- **Add raven to requirements** [`3cc6f3f`]
  **Files changed:** requirements.txt

### 2017-06-30
- **Fix move tool weirdness when no selection is made** [`c2d4544`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2017-06-29
- **Disable threaded buffer swap to see if it causes "invalid context"** [`3ac859d`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2017-06-27
- **Releasing right mouse button cancels sticky pan, even after a mouse drag** [`1200484`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2017-06-27
- **Fix entity inspector allowing double-deletes** [`f05c576`]
  **Files changed:** src/mcedit2/widgets/inspector/__init__.py

### 2017-06-27
- **Fix Inspect Entity list being editable** [`08d8561`]
  **Files changed:** src/mcedit2/editortools/select_entity.py

### 2017-06-27
- **Fix #328 - Missing terracotta map colors** [`525ca96`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2017-06-27
- **Fix #332 - imports allowed when read-only** [`d41c298`]
  **Files changed:** src/mcedit2/editorsession.py

### 2017-06-27
- **Fix #330 - "Delete Map" unimplemented** [`055a947`]
  **Files changed:** src/mcedit2/panels/map.py, src/mceditlib/anvil/adapter.py, src/mceditlib/worldeditor.py

### 2017-06-27
- **Install Sentry error reporting system** [`4b86472`]
  **Files changed:** src/mcedit2/dialogs/error_dialog.py, src/mcedit2/editorapp.py, src/mcedit2/main.py, src/mcedit2/sentry.py, src/mcedit2/ui/dialogs/error_dialog.ui

### 2017-06-18
- **Fix EditorSession not being released after tab is closed** [`1e2eda9`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py, src/mcedit2/widgets/block_replacement_list.py

### 2017-06-17
- **Add Patreon heads to Edit Player icon** [`9abe610`]
  **Files changed:** src/mcedit2/assets/mcedit2/icons/edit_player.png, src/mcedit2/assets_raw/icons.svg, src/mcedit2/assets_raw/playerskins/Vechs_skin_cover.png

### 2017-06-16
- **Fix build script to copy lang files** [`6042053`]
  **Files changed:** mcedit2.spec

### 2017-06-16
- **Change window titles from "Form"** [`835fd51`]
  **Files changed:** src/mcedit2/ui/block_replacements.ui, src/mcedit2/ui/find_replace_blocks.ui, src/mcedit2/ui/find_replace_command_results.ui, src/mcedit2/ui/find_replace_commands.ui, src/mcedit2/ui/find_replace_nbt.ui, src/mcedit2/ui/find_replace_nbt_results.ui, src/mcedit2/ui/inspector.ui, src/mcedit2/ui/log_view.ui, src/mcedit2/ui/rotation_widget.ui, src/mcedit2/ui/scale_widget.ui, src/mcedit2/ui/selection_coord_widget.ui

### 2017-06-15
- **Finish adding language menu, make it remember the language** [`bea5c96`]
  **Files changed:** src/mcedit2/editorapp.py

### 2017-06-15
- **Fix #324 - World List not catching all invalid-world errors** [`18cada9`]
  **Files changed:** src/mcedit2/worldlist.py

### 2017-06-14
- **Fix "Restart" button putting mcedit2.exe in the args list twice** [`34fa322`]
  **Files changed:** src/mcedit2/dialogs/error_dialog.py

### 2017-06-14
- **Fix #320: argv is `str` but our filenames must be `unicode`** [`59f3c0b`]
  TODO: figure out why argparse sometimes gets the exe as a filename
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/main.py

### 2017-06-14
- **Add translations menu and include qm files in built app** [`39add23`]
  **Files changed:** mcedit2.spec, src/mcedit2/editorapp.py, src/mcedit2/i18n/en.qm, src/mcedit2/i18n/en_US.ts

### 2017-03-30
- **Remove debug logs** [`6969cae`]
  **Files changed:** src/mcedit2/worldview/worldview.py, src/mceditlib/transform.py

### 2017-03-30
- **Add scale/flip options to Clone and Move** [`ea32ca8`]
  **Files changed:** src/mcedit2/editortools/clone.py, src/mcedit2/editortools/move.py, src/mcedit2/imports.py, src/mcedit2/rendering/scenegraph/matrix.py, src/mcedit2/ui/scale_widget.ui, src/mcedit2/widgets/scale_widget.py, src/mcedit2/widgets/spinslider.py, src/mceditlib/transform.py

### 2017-03-30
- **Eliminate feedback loop between BoxHandle and PendingImportNode** [`204045a`]
  **Files changed:** src/mcedit2/handles/boxhandle.py

### 2017-03-30
- **Move many computed properties from BoundingBox up to SelectionBox** [`08cfe20`]
  **Files changed:** src/mceditlib/selection/__init__.py

### 2017-03-30
- **SpinSlider no longer sets value back-and-forth between slider and spinbox** [`8d3b90d`]
  Prevents feedback loops when float values can't be converted exactly
  **Files changed:** src/mcedit2/widgets/spinslider.py

### 2017-03-30
- **SpinSlider now supports "live" value changes** [`e583a91`]
  **Files changed:** src/mcedit2/widgets/spinslider.py

### 2017-03-30
- **SpinSlider has sensible default value** [`9f50829`]
  **Files changed:** src/mcedit2/widgets/spinslider.py

### 2017-03-30
- **Ignore nonsense in blockstate strings (from user-defined blocks?)** [`d27c5d0`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2017-03-28
- **Mirror icon** [`7a421ba`]
  **Files changed:** src/mcedit2/assets/mcedit2/icons/mirror.png, src/mcedit2/assets_raw/icons.svg

### 2017-03-27
- **Use element size as default UV coords if not given** [`56cd05f`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2017-03-27
- **Handle bad "cullface" values that MC also handles** [`c9b7bec`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2017-03-27
- **Fix #309 - Unbounded texture variable lookup** [`354888c`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2017-03-27
- **Fix #309 - Squelch paranoid users** [`f85b441`]
  **Files changed:** src/mcedit2/__init__.py

### 2017-03-23
- **Fix #306 - Bad default value handling in SpinSlider** [`f0547b6`]
  **Files changed:** src/mcedit2/widgets/spinslider.py

### 2017-03-23
- **Fix #307 - Nonsense value for LastPlayed?** [`6234f25`]
  **Files changed:** src/mcedit2/worldlist.py

### 2017-03-23
- **Add CI status badges to readme [ci skip]** [`9c2b991`]
  **Files changed:** README.md

### 2017-03-19
- **OS X CI: Install pyside+qt from third party source** [`cd6e4b6`]
  **Files changed:** .travis.yml

### 2017-03-19
- **Use 1.11 block defs** [`b3c41cf`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mceditlib/blocktypes/__init__.py

### 2017-03-19
- **Add tripwire rendering** [`68168e2`]
  **Files changed:** src/mcedit2/rendering/modelmesh.pyx

### 2017-03-19
- **Fix broken multipart models** [`fd0e8da`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx

### 2017-03-19
- **Dump 1.11 blocks** [`d6ae004`]
  **Files changed:** src/mcedit2/rendering/hiddenstates_1_11.json, src/mceditlib/blocktypes/blockdumper/1.11/BlockDumper.java, src/mceditlib/blocktypes/idmapping_raw_1_11.json, src/mceditlib/blocktypes/minecraft_raw_1_11.json

### 2017-03-13
- **Fix #289 - Clarify "source folder" and explain virtualenv** [`0505ca0`]
  **Files changed:** README.md

### 2017-03-13
- **Fix #298 - Cope with irregularly shaped imports (e.g. entire worlds)** [`2b4beb6`]
  **Files changed:** src/mcedit2/imports.py, src/mcedit2/util/worldloader.py

### 2017-03-13
- **Fix #291 - FillCommandWidget cached globally instead of per-session** [`db38556`]
  **Files changed:** src/mcedit2/editorcommands/fill.py

### 2017-03-13
- **Fix #295 - Cope with broken texture references in mod/respack models** [`b5d0553`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2017-03-13
- **Fix #302 - TypeError when selecting MC install** [`2adc7c3`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2017-02-26
- **Add "Prune World" command** [`c50827d`]
  **Files changed:** src/mcedit2/editorsession.py

### 2017-01-13
- **Add Patreon supporter** [`119caae`]
  **Files changed:** src/mcedit2/editorapp.py

### 2016-10-30
- **Add Patreon supporter** [`2b7c458`]
  **Files changed:** src/mcedit2/editorapp.py

### 2016-10-24
- **Fix integer signedness mismatch in analyze.py** [`55cd86c`]
  Fixes #283
  **Files changed:** src/mceditlib/operations/analyze.py

### 2016-10-15
- **Merge pull request #277 from nikitakit/nikita/py3** [`4652e53`]
  Allow read-only use of mceditlib in python3

### 2016-10-06
- **Limited support for writing nbt files** [`08da5a3`]
  **Files changed:** src/mceditlib/nbt.pyx

### 2016-10-05
- **Fix integer width mismatch in analyze.py** [`55a83b1`]
  Fixes #278
  **Files changed:** src/mceditlib/operations/analyze.py

### 2016-10-04
- **Allow installing mceditlib in python3 using 2to3** [`ef0572b`]
  **Files changed:** setup_mceditlib.py

### 2016-10-04
- **Read-only python3 codepath in nbt.pyx** [`bf8aed5`]
  **Files changed:** setup_mceditlib.py, src/mceditlib/nbt.pyx

### 2016-10-04
- **Remove parameter unpacking that was confusing 2to3** [`5250b28`]
  **Files changed:** src/mceditlib/selection/__init__.py

### 2016-10-04
- **Use floor division in regionfile.py** [`14d1b83`]
  **Files changed:** src/mceditlib/pc/regionfile.py

### 2016-10-04
- **Replace file constructor with open throughout mceditlib** [`dcdda83`]
  **Files changed:** setup_mceditlib.py, src/mceditlib/anvil/adapter.py, src/mceditlib/anvil/worldfolder.py, src/mceditlib/blocktypes/json_resources.py, src/mceditlib/findadapter.py, src/mceditlib/java.py, src/mceditlib/minecraft_server.py, src/mceditlib/pc/regionfile.py, src/mceditlib/pocket.py, src/mceditlib/revisionhistory.py

### 2016-09-30
- **Implement cobblestone wall rendering** [`0743971`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx

### 2016-09-30
- **Fix None parts being passed to BlockModels.loadModelParts** [`412f1fc`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2016-09-30
- **Fix NBTUUIDAttr not creating tags if missing** [`cca4cc7`]
  **Files changed:** src/mceditlib/nbtattr.py

### 2016-09-22
- **Fix TAG_String value returned as `str` (should be `unicode`)** [`356565a`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/nbt.py

### 2016-09-22
- **Fix "Save" command not usable after certain (very few) actions.** [`f1224f6`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/select.py

### 2016-09-16
- **Fix AnvilWorldAdapter selecting the wrong revision during saveChanges** [`314334b`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2016-09-16
- **Rewrite a docstring in RevisionHistory** [`8a65da6`]
  **Files changed:** src/mceditlib/revisionhistory.py

### 2016-09-16
- **Add button to error dialog for post mortem debugging (src checkout only)** [`dd4e271`]
  **Files changed:** src/mcedit2/dialogs/error_dialog.py, src/mcedit2/ui/dialogs/error_dialog.ui

### 2016-09-16
- **showErrorDialog defaults to the current exc_info if none is given** [`9620b86`]
  **Files changed:** src/mcedit2/dialogs/error_dialog.py

### 2016-09-16
- **Split placeSchematic from importSchematic for already-loaded schematics** [`4aff8bb`]
  **Files changed:** src/mcedit2/editorsession.py

### 2016-09-16
- **Fix move tool adding spurious "Move Object" undos in many cases** [`4ed9d10`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2016-09-16
- **Fix move tool adding spurious "Rotate Object" undo entries in some cases** [`d2268a3`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2016-09-16
- **Add function to convert some filter options to simple command options** [`66e9046`]
  **Files changed:** src/mcedit2/plugins/command.py

### 2016-09-16
- **Catch and display errors while instantiating command plugins** [`add129b`]
  Should generalize for all plugin types
  **Files changed:** src/mcedit2/plugins/command.py

### 2016-09-16
- **Add increment key to simple options** [`5314a2c`]
  **Files changed:** src/mcedit2/plugins/command.py

### 2016-09-16
- **Fix default min/max for simple options being too small (was 0-99)** [`8f89a0f`]
  **Files changed:** src/mcedit2/plugins/command.py

### 2016-09-16
- **Allow SimpleCommandPlugin.perform to return a schematic** [`d037603`]
  **Files changed:** src/mcedit2/plugins/command.py

### 2016-09-16
- **Add increment arg to SpinSlider** [`ad4a235`]
  **Files changed:** src/mcedit2/widgets/spinslider.py

### 2016-09-16
- **Fix badly formatted ValueError in AnvilWorldAdapter** [`fe061bf`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2016-09-16
- **Allow BlockType to be used in `if block` to test for air** [`a86bb1e`]
  **Files changed:** src/mceditlib/blocktypes/__init__.py

### 2016-09-16
- **Rename presave->reversion** [`fc7eab8`]
  **Files changed:** src/mceditlib/revisionhistory.py

### 2016-09-16
- **Fix wacky progress bars stemming from RevisionHistory operations** [`c0cb29f`]
  **Files changed:** src/mceditlib/revisionhistory.py

### 2016-09-16
- **Remove unused `isPresave` attr on RevisionHistoryNode** [`c6a1a4d`]
  **Files changed:** src/mceditlib/revisionhistory.py

### 2016-09-16
- **Add more notes and comments to RevisionHistory** [`773f1ab`]
  **Files changed:** src/mceditlib/revisionhistory.py

### 2016-09-16
- **Fix "cannot get length of iterator" in RevisionHistory** [`f9df465`]
  **Files changed:** src/mceditlib/revisionhistory.py

### 2016-09-10
- **Fix incorrect find_packages globs** [`84b8bb3`]
  **Files changed:** setup_mcedit2.py, setup_mceditlib.py

### 2016-09-10
- **Ignore pyupdater folder** [`e4a581a`]
  **Files changed:** .gitignore

### 2016-09-10
- **Install all necessary deps on readthedocs** [`c48654e`]
  Fixes problems where inline method docs did not appear
  **Files changed:** because relevant modules failed to import due to, missing dependencies., doc/conf.py, environment.yml, readthedocs.yml, setup_mcedit2.py, setup_mceditlib.py

### 2016-09-10
- **Include main requirements in makedoc reqs** [`87a238e`]
  **Files changed:** doc/makedoc-requirements.txt

### 2016-09-10
- **fixup: Use 1.10 block dumps** [`47bc3c2`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2016-09-09
- **Fix blocktype list's parent type not being cleared as needed** [`0deab72`]
  **Files changed:** src/mcedit2/widgets/blockpicker_util.py

### 2016-09-09
- **Use 1.10 block dumps** [`23b47d5`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/util/minecraftinstall.py, src/mceditlib/blocktypes/__init__.py

### 2016-09-09
- **1.10 json dumps** [`cb6a885`]
  **Files changed:** src/mcedit2/rendering/hiddenstates_1_10.json, src/mceditlib/blocktypes/blockdumper/1.10/BlockDumper.java, src/mceditlib/blocktypes/idmapping_raw_1_10.json, src/mceditlib/blocktypes/minecraft_raw_1_10.json

### 2016-09-09
- **Dump renderLayer as string, not ordinal** [`ee7da76`]
  **Files changed:** src/mceditlib/blocktypes/blockdumper/1.9/BlockDumper.java, src/mceditlib/blocktypes/minecraft_raw_19.json

### 2016-09-07
- **Add "Remove Tags" commands to Find/Replace NBT results** [`34ec62b`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/nbt.py, src/mcedit2/ui/find_replace_nbt.ui, src/mcedit2/ui/find_replace_nbt_results.ui

### 2016-09-07
- **Colorize acacia and dark oak leaves** [`64eb73d`]
  **Files changed:** src/mceditlib/blocktypes/minecraft.json

### 2016-09-06
- **Document `dimension.getEntities`** [`2bb1e9e`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2016-09-06
- **Document "Editing Entities"** [`0175ade`]
  **Files changed:** doc/plugin_basics.rst, doc/plugin_tasks.rst, doc/plugins/command.rst

### 2016-09-06
- **Tweak command.rst formatting, describe `type="blocktype"`** [`285f981`]
  **Files changed:** doc/plugins/command.rst

### 2016-09-06
- **Stub out some doc files** [`81418fe`]
  **Files changed:** doc/plugin_basics.rst, doc/plugin_types.rst, doc/plugins/brush_mode.rst, doc/plugins/generate.rst, doc/plugins/inspector.rst, doc/plugins/tile_entity.rst

### 2016-09-06
- **More work on plugin docs** [`6a97822`]
  **Files changed:** doc/index.rst, doc/plugin_basics.rst, doc/plugin_examples.rst, doc/plugin_tasks.rst, doc/plugin_types.rst, doc/plugins.rst, doc/plugins/brush_shape.rst, doc/plugins/tool.rst, src/mcedit2/plugins/command.py, src/mceditlib/anvil/entities.py, src/mceditlib/worldeditor.py, src/plugins/world_editing_demo.py

### 2016-09-05
- **Fix typo in "Switch to homemade PySide"** [`89d17ea`]
  **Files changed:** appveyor.yml

### 2016-09-05
- **Guard against zero-length model variant lists** [`2f837fd`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2016-09-05
- **Adjust display and sort order of NBT item tags in NBT Editor** [`8d7bee0`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2016-09-05
- **Switch to homemade PySide build for windows** [`97d9574`]
  **Files changed:** appveyor.yml

### 2016-08-25
- **Start work on Prefs Dialog, add Max View Distance setting** [`3f7e66c`]
  **Files changed:** src/mcedit2/ui/dialogs/preferences.ui, src/mcedit2/ui/preferences_dialog.ui, src/mcedit2/widgets/prefsdialog.py, src/mcedit2/widgets/prefsdialog/__init__.py, src/mcedit2/widgets/prefsdialog/camera.py, src/mcedit2/worldview/camera.py

### 2016-08-25
- **Handle "None" texture in model json/configured blocks** [`05ee264`]
  Model json needs to be more strict...
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2016-08-25
- **Only enable "Configure Blocks" while a session is open** [`00d939d`]
  **Files changed:** src/mcedit2/editorapp.py

### 2016-08-25
- **Ignore user files in src folder** [`8bb1c80`]
  **Files changed:** .gitignore

### 2016-08-25
- **Fix mousewheel zooming in overhead view** [`45599b0`]
  **Files changed:** src/mcedit2/worldview/overhead.py, src/mcedit2/worldview/viewaction.py

### 2016-08-25
- **Ask to retry download or configure installs if MC download fails** [`ac42eae`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2016-08-25
- **Fix dimno parsing only working for negative dimnos** [`446c4de`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2016-08-24
- **Fix 'view is None' in viewChanged when closing viewports** [`4624749`]
  **Files changed:** src/mcedit2/editorsession.py

### 2016-08-24
- **Fix selection size blowing up after unticking "Edit Size"** [`a8c6ad8`]
  **Files changed:** src/mcedit2/editortools/select.py

### 2016-08-23
- **Automatically download Minecraft jar** [`3f5da72`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/main.py, src/mcedit2/util/minecraftinstall.py

### 2016-08-20
- **Set up Travis-CI build scripts** [`9a92ebb`]
  **Files changed:** .travis.yml, mcedit2.spec

### 2016-08-16
- **Get builds going for OS X** [`9b60287`]
  **Files changed:** mcedit2.icns, mcedit2.spec, requirements.txt, setup_mcedit2.py, setup_mceditlib.py, src/mcedit2/main.py

### 2016-02-25
- **Set up appveyor build scripts** [`2f97bf4`]
  Also changes mcedit2.spec to handle distribution packaging
  **Files changed:** .gitignore, appveyor.yml, mcedit2.spec, requirements-mceditlib.txt

### 2016-08-16
- **Pin pyzmq==15.0.0 due to pyinstaller issue** [`42ba3be`]
  **Files changed:** requirements.txt

### 2016-08-14
- **Import support modules explicitly rather than using hiddenimports** [`8475149`]
  **Files changed:** mcedit2.spec, src/mcedit2/main.py, src/mcedit2/support_modules.py

### 2016-08-16
- **User files folder is now "MCEdit 2 Files"** [`42fdb9a`]
  Was previously inconsistent
  **Files changed:** src/mcedit2/util/directories/mac.py, src/mcedit2/util/directories/posix.py, src/mcedit2/util/directories/win32.py

### 2016-08-10
- **Quiet down this test** [`53b691c`]
  **Files changed:** tests/test_mceditlib/relight_test.py

### 2016-08-09
- **Copied entities now have new UUIDs** [`65f0c1b`]
  **Files changed:** src/mceditlib/anvil/entities.py

### 2016-08-09
- **Progress dialog is closed even if the task raises an exception.** [`c3a8aaa`]
  **Files changed:** src/mcedit2/util/showprogress.py

### 2016-08-08
- **Fix passing unsigned longs to TAG_Long, which requires signed longs** [`78b6ebf`]
  **Files changed:** src/mceditlib/nbtattr.py

### 2016-08-08
- **Export structure nbt larger than 32x32x32** [`07edbc8`]
  **Files changed:** src/mcedit2/editorsession.py, src/mceditlib/structure.py

### 2016-08-08
- **Fix wrong default ref class created for TileEntities** [`a9dff5c`]
  **Files changed:** src/mceditlib/anvil/entities.py, src/mceditlib/nbtattr.py

### 2016-07-29
- **Disable tools that modify the world when it is opened read-only** [`d47b184`]
  **Files changed:** src/mcedit2/editortools/__init__.py, src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/clone.py, src/mcedit2/editortools/flood_fill.py, src/mcedit2/editortools/generate.py, src/mcedit2/editortools/move.py

### 2016-07-29
- **Add missed self.tr calls** [`2c4bcf0`]
  **Files changed:** src/mcedit2/panels/map.py, src/mcedit2/panels/player.py

### 2016-07-29
- **Many editing actions are now disabled in readonly mode** [`bae09c1`]
  **Files changed:** src/mcedit2/editorsession.py

### 2016-07-17
- **Handle UnicodeDecodeError in setWidgetError** [`d55be3d`]
  **Files changed:** src/mcedit2/widgets/layout.py

### 2016-07-17
- **Add "Remove Entities And Items" command.** [`21a5a3f`]
  **Files changed:** src/mcedit2/editorsession.py, src/mceditlib/operations/entity.py

### 2016-07-17
- **Remove getInputsList from LSystemPlugin** [`c17d8b6`]
  **Files changed:** src/mcedit2/synth/l_system_plugin.py

### 2016-07-17
- **More work on docs** [`2c1ca37`]
  **Files changed:** doc/apidocs.rst, doc/editorsession.rst, doc/index.rst, doc/plugins/command.rst, doc/selection.rst, doc/worldeditor.rst

### 2016-06-29
- **Crudely handle NBTFormatError thrown by getPlayer** [`c4aa8bb`]
  **Files changed:** src/mcedit2/panels/player.py, src/mcedit2/rendering/players.py, src/mcedit2/worldlist.py, src/mceditlib/anvil/adapter.py

### 2016-06-26
- **Fix bug where SceneNode was readded later but no RenderNodes created** [`661503d`]
  **Files changed:** src/mcedit2/rendering/scenegraph/rendernode.py

### 2016-06-26
- **Rewrite some docstrings in NumpyDoc** [`042bfa7`]
  **Files changed:** src/mcedit2/editortools/brush/shapes.py, src/mcedit2/rendering/chunkloader.py, src/mcedit2/rendering/worldscene.py, src/mceditlib/fakechunklevel.py

### 2016-06-26
- **Add sphinx.ext.napoleon to read NumPyDoc docstrings** [`55b0dc9`]
  **Files changed:** doc/conf.py

### 2016-06-26
- **Remove apidoc for now** [`0031892`]
  **Files changed:** doc/Makefile, doc/apidoc/mcedit2.dialogs.rst, doc/apidoc/mcedit2.editorcommands.find_replace.rst, doc/apidoc/mcedit2.editorcommands.rst, doc/apidoc/mcedit2.editortools.brush.rst, doc/apidoc/mcedit2.editortools.rst, doc/apidoc/mcedit2.handles.rst, doc/apidoc/mcedit2.panels.rst, doc/apidoc/mcedit2.plugins.rst, doc/apidoc/mcedit2.rendering.chunkmeshes.entity.rst, doc/apidoc/mcedit2.rendering.chunkmeshes.rst, doc/apidoc/mcedit2.rendering.rst, doc/apidoc/mcedit2.rendering.scenegraph.rst, doc/apidoc/mcedit2.rst, doc/apidoc/mcedit2.synth.rst, doc/apidoc/mcedit2.util.directories.rst, doc/apidoc/mcedit2.util.rst, doc/apidoc/mcedit2.widgets.inspector.rst, doc/apidoc/mcedit2.widgets.inspector.tileentities.rst, doc/apidoc/mcedit2.widgets.nbttree.rst, doc/apidoc/mcedit2.widgets.rst, doc/apidoc/mcedit2.worldview.rst, doc/apidoc/mceditlib.anvil.rst, doc/apidoc/mceditlib.blocktypes.rst, doc/apidoc/mceditlib.operations.rst, doc/apidoc/mceditlib.pc.rst, doc/apidoc/mceditlib.relight.rst, doc/apidoc/mceditlib.rst, doc/apidoc/mceditlib.selection.rst, doc/apidoc/mceditlib.util.rst, doc/apidoc/modules.rst, doc/index.rst

### 2016-06-26
- **Docstring fix** [`c1956e3`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbteditor.py

### 2016-06-26
- **Update apidocs** [`48e8280`]
  **Files changed:** doc/apidoc/mcedit2.dialogs.rst, doc/apidoc/mcedit2.editorcommands.find_replace.rst, doc/apidoc/mcedit2.editorcommands.rst, doc/apidoc/mcedit2.editortools.brush.rst, doc/apidoc/mcedit2.editortools.rst, doc/apidoc/mcedit2.handles.rst, doc/apidoc/mcedit2.panels.rst, doc/apidoc/mcedit2.plugins.rst, doc/apidoc/mcedit2.rendering.chunkmeshes.entity.rst, doc/apidoc/mcedit2.rendering.chunkmeshes.rst, doc/apidoc/mcedit2.rendering.rst, doc/apidoc/mcedit2.rendering.scenegraph.rst, doc/apidoc/mcedit2.rst, doc/apidoc/mcedit2.synth.rst, doc/apidoc/mcedit2.util.directories.rst, doc/apidoc/mcedit2.util.rst, doc/apidoc/mcedit2.widgets.inspector.rst, doc/apidoc/mcedit2.widgets.inspector.tileentities.rst, doc/apidoc/mcedit2.widgets.nbttree.rst, doc/apidoc/mcedit2.widgets.rst, doc/apidoc/mcedit2.worldview.rst, doc/apidoc/mceditlib.anvil.rst, doc/apidoc/mceditlib.blocktypes.rst, doc/apidoc/mceditlib.operations.rst, doc/apidoc/mceditlib.pc.rst, doc/apidoc/mceditlib.relight.rst, doc/apidoc/mceditlib.rst, doc/apidoc/mceditlib.selection.rst, doc/apidoc/mceditlib.util.rst

### 2016-06-24
- **SimpleCommandPlugin now gets the dimension and selection** [`f0c509d`]
  **Files changed:** src/mcedit2/plugins/command.py, src/plugins/simple_options.py

### 2016-06-24
- **Begin documenting plugin APIs** [`5afb3b2`]
  **Files changed:** doc/apidocs.rst, doc/index.rst, doc/plugins.rst, doc/plugins/command.rst

### 2016-06-24
- **Add makedoc requirements** [`d3ddd8c`]
  **Files changed:** doc/makedoc-requirements.txt

### 2016-06-24
- **PluginCommand -> CommandPlugin** [`8616c9e`]
  **Files changed:** src/mcedit2/plugins/__init__.py, src/mcedit2/plugins/command.py, src/mcedit2/plugins/registry.py, src/plugins/count_blocks.py, src/plugins/simple_options.py

### 2016-06-23
- **Implement add/remove tile entity in block inspector** [`9ea24fd`]
  **Files changed:** src/mcedit2/ui/inspector.ui, src/mcedit2/widgets/inspector/__init__.py, src/mceditlib/anvil/entities.py, src/mceditlib/worldeditor.py

### 2016-06-23
- **Add sign editor and entity ref** [`f31a5b1`]
  **Files changed:** src/mcedit2/widgets/inspector/__init__.py, src/mcedit2/widgets/inspector/tileentities/command.py, src/mcedit2/widgets/inspector/tileentities/sign.py, src/mceditlib/anvil/entities.py

### 2016-06-22
- **Spruce and Birch Leaves and Vines are now colorized (again)** [`544e083`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pxd, src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx, src/mceditlib/blocktypes/minecraft.json

### 2016-06-22
- **Add function for recursively printing a SceneNode** [`2cf5378`]
  **Files changed:** src/mcedit2/rendering/scenegraph/scenenode.py

### 2016-06-22
- **Add "Hollow" option to brush tool** [`f8828fc`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/brush/shapes.py, src/mcedit2/ui/editortools/brush.ui, src/mceditlib/selection/hollow.py

### 2016-06-21
- **Remove views from EditorTab before clearing self.editorsession** [`279c04e`]
  Should avoid mouse events firing after editorSession is set to None.
  **Files changed:** src/mcedit2/editorsession.py

### 2016-06-20
- **Dump renderLayer attribute of blocks** [`305f873`]
  **Files changed:** src/mceditlib/blocktypes/minecraft_raw_19.json

### 2016-06-20
- **Hook up the 180 degree rotation** [`3f14618`]
  **Files changed:** src/mceditlib/transform.py

### 2016-06-20
- **Stairs now rotate more sensibly around the x/z axes** [`b019825`]
  **Files changed:** src/mceditlib/blocktypes/rotation.py

### 2016-06-20
- **Cleanup** [`1da790a`]
  **Files changed:** src/mcedit2/editortools/clone.py

### 2016-06-18
- **Begin implementing 180 degree rotations** [`d77c9c9`]
  **Files changed:** src/mceditlib/blocktypes/rotation.py

### 2016-06-17
- **Docstrings** [`bee6915`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2016-06-17
- **DimensionTransform calls BlockRotations to get rotated block IDs** [`120d12c`]
  **Files changed:** src/mceditlib/transform.py

### 2016-06-17
- **Fix y-axis rotation reversed** [`1a522be`]
  **Files changed:** src/mceditlib/blocktypes/rotation.py

### 2016-06-17
- **Remove manual overrides for 1.9 blocks** [`5aa8337`]
  **Files changed:** src/mceditlib/blocktypes/idmapping.json, src/mceditlib/blocktypes/minecraft.json

### 2016-06-17
- **Remove old blockrotation file** [`9b78da6`]
  **Files changed:** src/mceditlib/blockrotation.py

### 2016-06-16
- **Fix animated textures rendering wrong** [`bd3024a`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2016-06-16
- **Add block rotation mappings for X and Z axis, optimize block search** [`3235108`]
  **Files changed:** src/mceditlib/blocktypes/__init__.py, src/mceditlib/blocktypes/rotation.py

### 2016-06-15
- **Move conftest.py up a level** [`0a164dd`]
  **Files changed:** tests/conftest.py

### 2016-06-15
- **Update 1.9 BlockDumper** [`2670bd1`]
  **Files changed:** src/mceditlib/blocktypes/blockdumper/1.9/BlockDumper.java

### 2016-06-15
- **Implement Minecraft 1.9 block models** [`4b0d0d2`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pxd, src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/hiddenstates_19.json, src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/util/minecraftinstall.py, src/mceditlib/anvil/adapter.py, src/mceditlib/blocktypes/__init__.py, src/mceditlib/blocktypes/minecraft_raw_19.json

### 2016-06-15
- **Fix typo in removing configured blocks** [`ff1056c`]
  **Files changed:** src/mcedit2/editorsession.py

### 2016-06-14
- **Guard against players with no UUID tags (this shouldn't happen)** [`448eab0`]
  **Files changed:** src/mcedit2/rendering/players.py, src/mcedit2/util/player_server.py

### 2016-06-13
- **Add "Loading plugins" to editor load progress** [`5459c20`]
  **Files changed:** src/mcedit2/editorsession.py

### 2016-06-09
- **Fix texture misalignment when u1 > u2** [`f6021f1`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2016-06-09
- **1.9 BlockDumper.java** [`3e9834c`]
  **Files changed:** src/mceditlib/blocktypes/blockdumper/1.9/BlockDumper.java

### 2016-06-09
- **Add dummy modelTexture to ModelPlayer** [`e8eef09`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entity/player.py

### 2016-06-09
- **Fix new-style player textures being flipped** [`fcab430`]
  **Files changed:** src/mcedit2/rendering/players.py

### 2016-06-08
- **Add 1.9 blocktypes** [`458a31c`]
  **Files changed:** src/mceditlib/blocktypes/blockdumper/1.9/BlockDumper.java, src/mceditlib/blocktypes/idmapping_raw_19.json, src/mceditlib/blocktypes/minecraft_raw_19.json

### 2016-06-07
- **Render player models with textures** [`d790e40`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entity/models.py, src/mcedit2/rendering/chunkmeshes/entity/player.py, src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/players.py, src/mcedit2/rendering/worldscene.py

### 2016-06-07
- **Actually fetch player textures from session server** [`7bd6a0f`]
  **Files changed:** src/mcedit2/util/player_server.py

### 2016-06-07
- **Dirty dirty hack to use loadPNGFile for paths not in MCEdit's datafiles** [`7c5a662`]
  **Files changed:** src/mcedit2/util/load_png.py

### 2016-06-07
- **Add Enable state for scene nodes** [`4f9992c`]
  **Files changed:** src/mcedit2/rendering/scenegraph/misc.py, src/mcedit2/rendering/scenegraph/vertex_array.py, src/mcedit2/rendering/vertexarraybuffer.py

### 2016-06-04
- **Switch to perspective view when zooming to player's view** [`4adb800`]
  **Files changed:** src/mcedit2/panels/player.py

### 2016-06-03
- **Fetch player names and textures from Mojang session server** [`2477bb9`]
  **Files changed:** src/mcedit2/panels/player.py, src/mcedit2/util/player_server.py, tests/test_mcedit2/player_server_test.py

### 2016-05-31
- **Create testbed schematic with all block types** [`36e58fc`]
  **Files changed:** test_files/create_testbed.py, test_files/testbed.schematic

### 2016-05-31
- **Get SchematicWorldView working again, tweak zoom limits** [`1c5d244`]
  **Files changed:** src/mcedit2/worldview/schematic_worldview.py

### 2016-05-31
- **Adapter classes not required to implement listPlayers** [`b8865c8`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2016-05-31
- **Cleanup** [`c8c69bb`]
  **Files changed:** src/mceditlib/schematic.py

### 2016-05-31
- **Add dimNo property to WorldEditorDimension** [`89f865d`]
  Fix dimNo 0 not returned for overworld
  **Files changed:** src/mceditlib/worldeditor.py

### 2016-05-31
- **Tweak docstrings** [`c39e454`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2016-05-31
- **Fix single-select block pickers acting like multi-select ones** [`533f93b`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/brush/modes.py, src/mcedit2/widgets/blockpicker.py

### 2016-05-31
- **Tweak docstrings** [`e54f050`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2016-05-31
- **Quietly skip badly damaged/unreadable region files.** [`89bd601`]
  **Files changed:** src/mceditlib/anvil/worldfolder.py

### 2016-05-31
- **Don't pad out file size of region files opened read-only.** [`fcb0f8a`]
  **Files changed:** src/mceditlib/pc/regionfile.py

### 2016-05-30
- **Update contributing guidelines** [`28b4d84`]
  **Files changed:** .github/CONTRIBUTING.md

### 2016-05-30
- **Add issue template** [`61ae0dc`]
  **Files changed:** .github/CONTRIBUTING.md, .github/ISSUE_TEMPLATE.md

### 2016-05-30
- **Fix block position offset in structure files** [`6eea8d5`]
  **Files changed:** src/mceditlib/structure.py

### 2016-05-30
- **Add progress bar to structure export** [`e00a3b2`]
  **Files changed:** src/mcedit2/editorsession.py

### 2016-05-29
- **Add structure block export** [`cb8d6e1`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/library.py, src/mceditlib/blocktypes/__init__.py, src/mceditlib/findadapter.py, src/mceditlib/selection/__init__.py, src/mceditlib/structure.py, src/mceditlib/worldeditor.py, tests/test_mceditlib/structure_test.py

### 2016-05-29
- **Add PCEntityMobRefBase** [`a1c70bc`]
  **Files changed:** src/mceditlib/anvil/entities.py

### 2016-05-29
- **NBTListAttr also accepts one-char tag types** [`0669cbf`]
  **Files changed:** src/mcedit2/library.py, src/mceditlib/anvil/adapter.py, src/mceditlib/nbtattr.py

### 2016-05-28
- **Add shorthands for NBTAttr types** [`b7a7f5c`]
  **Files changed:** src/mceditlib/anvil/entities.py, src/mceditlib/nbtattr.py

### 2016-05-28
- **Add more entity tags and types** [`6271d4a`]
  **Files changed:** src/mceditlib/anvil/entities.py

### 2016-05-28
- **Implement mark/unmark chunks for repop** [`5fc3a2c`]
  **Files changed:** src/mcedit2/editorsession.py

### 2016-05-28
- **Update several docstrings** [`28c045e`]
  **Files changed:** src/mcedit2/editorsession.py, src/mceditlib/selection/__init__.py, src/mceditlib/worldeditor.py

### 2016-05-28
- **Rewrite editorSession.deleteChunks** [`b06f747`]
  **Files changed:** src/mcedit2/editorsession.py

### 2016-05-28
- **Create contextmanager for SimpleRevisionCommand** [`d2eb981`]
  **Files changed:** src/mcedit2/editorsession.py

### 2016-05-28
- **Remove unused functions** [`8d2d26f`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/util/undostack.py

### 2016-05-27
- **Tweak options in simple options demo** [`470795f`]
  **Files changed:** src/plugins/simple_options.py

### 2016-05-27
- **Wrap text in labels, use spinboxes instead of spinsliders w/no min+max** [`7699892`]
  **Files changed:** src/mcedit2/plugins/command.py

### 2016-05-27
- **Set title of SimplePluginDialog and give it a larger minimum size** [`883b9e4`]
  **Files changed:** src/mcedit2/plugins/command.py

### 2016-05-25
- **Add SimplePluginCommand with dict-based option configuration** [`dd59894`]
  **Files changed:** src/mcedit2/plugins/command.py, src/plugins/count_blocks.py, src/plugins/simple_options.py

### 2016-05-25
- **Un-private the registerClass and unregisterClass functions** [`389ef9a`]
  **Files changed:** src/mcedit2/plugins/__init__.py

### 2016-05-25
- **Add editorSession.beginCommand() to simplify undo code** [`d232d66`]
  **Files changed:** src/mcedit2/editorsession.py

### 2016-05-22
- **Simple command plugin for testing** [`5d10e8a`]
  **Files changed:** src/plugins/count_blocks.py

### 2016-05-21
- **Add some more logging to plugin load/unload** [`02b7a55`]
  **Files changed:** src/mcedit2/plugins/__init__.py

### 2016-05-21
- **Actually load plugins back in during auto-reload** [`2f03c94`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/plugins/__init__.py

### 2016-05-21
- **Create PluginClassRegistry class to handle class loading/unloading** [`bea7d8e`]
  Implements signals emitted when a plugin class is loaded/unloaded and
  **Files changed:** defers registration of classes until the plugin module is fully loaded., src/mcedit2/editortools/generate.py, src/mcedit2/plugins/__init__.py, src/mcedit2/plugins/command.py, src/mcedit2/plugins/registry.py

### 2016-05-21
- **Put vital unload code in a finally block** [`a5584de`]
  **Files changed:** src/mcedit2/plugins/__init__.py

### 2016-05-21
- **_CommandPlugins emits added and removed signals** [`7445852`]
  **Files changed:** src/mcedit2/plugins/__init__.py, src/mcedit2/plugins/command.py

### 2016-05-21
- **Refactor some methods onto PluginRef** [`6163371`]
  **Files changed:** src/mcedit2/plugins/__init__.py

### 2016-05-21
- **PluginRef.fullpath is now taken from the result of PluginRef.findModule()** [`4f4a0c9`]
  **Files changed:** src/mcedit2/plugins/__init__.py

### 2016-05-21
- **Fix return value of PluginsTableModel.getData** [`ad1e2ac`]
  **Files changed:** src/mcedit2/dialogs/plugins_dialog.py

### 2016-05-20
- **Wire up command plugins** [`c276d93`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/__init__.py

### 2016-05-20
- **Change mcedit2.plugins to package, start work on command plugins** [`7fc9d4c`]
  **Files changed:** src/mcedit2/plugins/__init__.py, src/mcedit2/plugins/command.py

### 2016-05-17
- **Fix AttributeError when getting tag name for undo description** [`9d3e503`]
  Fall back to "(root)" if the tag has no parent
  **Files changed:** src/mcedit2/widgets/nbttree/nbteditor.py

### 2016-05-12
- **Undoing transforms now updates the move tool UI** [`96b3f10`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2016-05-12
- **Fix transformed inputs not using the correct bounds when overlapping** [`8987e33`]
  **Files changed:** src/mcedit2/imports.py

### 2016-05-12
- **Block picker now selects the first matching block when searching** [`a2a660a`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2016-05-06
- **Fix move tool misbehaving on overlapping source/dest areas** [`a84b004`]
  - Move tool clears before copying when areas overlap
  **Files changed:** src/mcedit2/editortools/move.py

### 2016-05-06
- **Get DifferenceBox working again** [`524ed31`]
  **Files changed:** src/mceditlib/selection/__init__.py, tests/test_mceditlib/selection_test.py

### 2016-05-06
- **Clearing a selection with a single click now clears the highlighted blocks** [`5e2449a`]
  **Files changed:** src/mcedit2/editortools/select.py, src/mcedit2/rendering/selection.py

### 2016-05-05
- **Holding a modifier while releasing a movement key no longer keeps moving** [`3a00423`]
  Button and key release events now ignore modifiers and notify all
  **Files changed:** matching view actions of the release event, src/mcedit2/worldview/camera.py, src/mcedit2/worldview/viewaction.py, src/mcedit2/worldview/worldview.py

### 2016-05-05
- **Second draft of heuristic-based block rotation** [`3b647c7`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mceditlib/blocktypes/__init__.py, src/mceditlib/blocktypes/rotation.py

### 2016-05-05
- **Fix `sys._MEIPASS` not decoded to unicode** [`55d66b8`]
  **Files changed:** src/mcedit2/util/resources.py

### 2016-04-22
- **First draft of heuristic-based block rotation** [`30bb188`]
  **Files changed:** src/mceditlib/blocktypes/rotation.py

### 2016-04-21
- **Rewrite docstrings** [`e589475`]
  **Files changed:** src/mceditlib/transform.py

### 2016-03-30
- **Remove redundant exists check in getSrcFolder** [`e4bb8ee`]
  **Files changed:** src/mcedit2/util/resources.py

### 2016-03-28
- **Auto-compile .ui files when running from source.** [`98fd8f5`]
  **Files changed:** src/mcedit2/main.py, src/mcedit2/util/gen_ui.py

### 2016-03-27
- **Fall back to 1.8 jar when rendering, if models are 1.9 format** [`37fc89a`]
  ...or if they are otherwise unusable
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/resourceloader.py, src/mcedit2/util/minecraftinstall.py

### 2016-03-27
- **Improve error reporting when a world fails to open** [`84c7c24`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/widgets/layout.py, src/mcedit2/worldlist.py

### 2016-03-27
- **Fix snapshots option overriding "jar exists" check.** [`9127dcd`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2016-03-27
- **Fall back to first version found when selected version is not found.** [`06e874e`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2016-03-27
- **Be more lenient when a block model fails to parse** [`98c6f68`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2016-03-27
- **Add "Snapshots" option to minecraft installs dialog** [`20533b6`]
  **Files changed:** src/mcedit2/ui/minecraft_installs.ui, src/mcedit2/util/minecraftinstall.py

### 2016-03-27
- **Make minecraft installation list more robust** [`9fdf601`]
  Current install is now stored as the install's path rather than its
  **Files changed:** index. None install is now checked more often., src/mcedit2/editorsession.py, src/mcedit2/util/minecraftinstall.py, src/mcedit2/worldlist.py

### 2016-03-27
- **Catch and display any exception while loading a file to edit** [`49e40cc`]
  **Files changed:** src/mcedit2/editorapp.py

### 2016-03-27
- **Make model loading more robust** [`9bfd9ed`]
  Fixes #218
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2016-03-24
- **SelectionCursorNode and SelectionFaceNode now use 4-tuple colors** [`52a137d`]
  **Files changed:** src/mcedit2/editortools/select.py, src/mcedit2/handles/boxhandle.py, src/mcedit2/rendering/selection.py, src/mcedit2/util/settings.py

### 2016-03-24
- **Add "Sticky Selection" and "Classic Selection" options** [`ab0f193`]
  **Files changed:** src/mcedit2/editortools/select.py, src/mcedit2/handles/boxhandle.py

### 2016-03-23
- **Skip over mod zips that fail for any reason.** [`7a2237d`]
  **Files changed:** src/mcedit2/resourceloader.py

### 2016-03-18
- **Fix error dialog not showing when mouse is not grabbed?** [`3c21b85`]
  **Files changed:** src/mcedit2/dialogs/error_dialog.py

### 2016-03-11
- **Display the default `?` icon in inventories and itemtype lists** [`6055a4d`]
  **Files changed:** src/mcedit2/widgets/inventory.py, src/mcedit2/widgets/itemtype_list.py

### 2016-03-02
- **Skylight update now draws light in below changed columns.** [`03af37b`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2016-03-02
- **Re-enable lighting update for "Replace Blocks"** [`d5c3e31`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/replace_blocks.py

### 2016-02-17
- **Move brush mode widget below size widgets** [`7d53403`]
  **Files changed:** src/mcedit2/ui/editortools/brush.ui

### 2016-02-14
- **Starting selections on nearby blocks no longer defaults to face Y+** [`e964924`]
  **Files changed:** src/mcedit2/handles/boxhandle.py

### 2016-02-14
- **Mess around with the appearance of selection boxes** [`971fa25`]
  **Files changed:** src/mcedit2/editortools/select.py, src/mcedit2/handles/boxhandle.py, src/mcedit2/rendering/selection.py

### 2016-02-14
- **Right-click now toggles mouselook** [`dfe9aa9`]
  This can be disabled with the "Sticky Mouselook" option.
  **Files changed:** src/mcedit2/dialogs/error_dialog.py, src/mcedit2/rendering/compass.py, src/mcedit2/worldview/camera.py, src/mcedit2/worldview/viewcontrols.py

### 2016-02-12
- **Fix Square shape returning the existing shaped selection** [`12dae3d`]
  **Files changed:** src/mcedit2/editortools/brush/shapes.py

### 2016-02-12
- **Make sure BoundingBoxes of different classes compare differently** [`94757bd`]
  **Files changed:** src/mceditlib/selection/__init__.py

### 2016-02-12
- **Changing min values resizes selection instead of moving it** [`7dd5dd8`]
  **Files changed:** src/mcedit2/editortools/select.py

### 2016-02-09
- **Add brush mode "Replace"** [`fd66486`]
  **Files changed:** src/mcedit2/editortools/brush/modes.py

### 2016-02-09
- **Add a button widget for selecting block replacements** [`106623f`]
  **Files changed:** src/mcedit2/widgets/block_replacement_list.py

### 2016-02-08
- **Add a new supporter** [`fb20234`]
  **Files changed:** src/mcedit2/editorapp.py

### 2016-02-08
- **Add default impl for BrushMode.getOptions** [`4d53483`]
  **Files changed:** src/mcedit2/editortools/brush/modes.py

### 2016-02-08
- **BrushTool.updateCursor handles missing cursors/boxes** [`45d50da`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py

### 2016-02-08
- **Lower log to debug level in BlockTypeIcon** [`18578b5`]
  **Files changed:** src/mcedit2/widgets/blockpicker_util.py

### 2016-02-08
- **Brush tool option layout has better flow now** [`0d3ebf1`]
  **Files changed:** src/mcedit2/editortools/brush/modes.py, src/mcedit2/ui/editortools/brush.ui

### 2016-02-08
- **BlockTypes.allBlocks now remains sorted and enforces uniqueness** [`114e334`]
  **Files changed:** src/mcedit2/editorsession.py, src/mceditlib/anvil/adapter.py, src/mceditlib/blocktypes/__init__.py

### 2016-02-07
- **Remove BrushMode.createOptionsWidget; start on Replace mode** [`1b49c25`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/brush/modes.py

### 2016-02-07
- **Handle very short brush drags; extract method hoverPosition** [`7a29eb7`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py

### 2016-02-07
- **New rows in replacement list start empty on the left** [`90302bc`]
  **Files changed:** src/mcedit2/widgets/block_replacement_list.py

### 2016-02-07
- **BlockTypesButton or BlockTypesItemWidget can display "No blocks"** [`0542161`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py, src/mcedit2/widgets/blockpicker_util.py

### 2016-02-07
- **Fix display issues with multi-blocktype icons** [`f33065c`]
  **Files changed:** src/mcedit2/widgets/blockpicker_util.py

### 2016-02-07
- **Extract block replacement list to its own widget** [`bfafe53`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/__init__.py, src/mcedit2/editorcommands/find_replace/command_text.py, src/mcedit2/editorcommands/find_replace/replace_blocks.py, src/mcedit2/ui/block_replacements.ui, src/mcedit2/ui/find_replace.ui, src/mcedit2/ui/find_replace_blocks.ui, src/mcedit2/widgets/block_replacement_list.py

### 2016-02-07
- **Remove unused .ui file** [`1470297`]
  **Files changed:** src/mcedit2/ui/replace.ui

### 2016-02-06
- **Make threaded WorldView buffer swaps optional** [`35cf39d`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2016-02-06
- **Add Remove Entity button to entity inspector** [`2ec18c1`]
  **Files changed:** src/mcedit2/ui/inspector.ui, src/mcedit2/widgets/inspector/__init__.py

### 2016-02-06
- **EntityListProxy will now dirty its chunk on changes/inserts/removes** [`d05a5e3`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2016-02-06
- **Collect garbage after changing views in WorldList** [`6fe1d4b`]
  If the old view is reaped mid-frame, it calls makeCurrent and screws
  **Files changed:** with the current rendering., src/mcedit2/worldlist.py

### 2016-02-06
- **Fix waiting for wrong variable in waitForSwapThread** [`fbec27a`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2016-02-06
- **Fix NoContext error because buffer swap thread fires after it is awaited** [`2be0290`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2016-02-06
- **Fix empty editor tab captions** [`078e9ba`]
  **Files changed:** src/mcedit2/editorsession.py

### 2016-02-04
- **Implement EntityListProxy.remove()** [`5b7dace`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2016-02-04
- **Parent MCEDockWidgets to the main window, make Inspector floating** [`e6b0e7c`]
  **Files changed:** src/mcedit2/editorsession.py

### 2016-02-04
- **WorldView now waits for the swap thread before calling makeCurrent.** [`98fea77`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2016-02-04
- **WorldList's list of saves folders now includes saves from all installs** [`9c0b119`]
  And MMC instances.  Saves folders picked with the "choose" button, and
  **Files changed:** the most recently picked saves folder, are now saved to the app, settings., TODO: Automatically switch install/version to match the chosen saves, folder., src/mcedit2/worldlist.py

### 2016-02-02
- **In FillBlocksOperation, make sure skipped and sections match** [`af04686`]
  **Files changed:** src/mceditlib/operations/block_fill.py

### 2016-02-02
- **Fix bad parameter in bench_temp_file** [`a8ef77d`]
  Need a real fix, py.path.local.mkdtemp isn't a nice as I thought
  **Files changed:** benchmarks/__init__.py

### 2016-02-02
- **Add benchmark for filling at ceiling level, to test skylight performance** [`b089d6f`]
  **Files changed:** benchmarks/mceditlib/time_fill_ceiling.py

### 2016-02-01
- **Restore single-click brush action** [`4389c46`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py

### 2016-02-01
- **Max texture size is fetched using an offscreen context** [`a7f123d`]
  **Files changed:** src/mcedit2/rendering/textureatlas.py

### 2016-02-01
- **Remove incorrect super call in EditorTab.dealloc** [`d3aa593`]
  **Files changed:** src/mcedit2/editorsession.py

### 2016-01-31
- **Separate TextureAtlas image building from GL resource creation** [`0d46eed`]
  Fixes the problem with initial brush cursors not appearing by allowing
  **Files changed:** brushes to create cursor geometry before the world view is created., src/mcedit2/editortools/brush/modes.py, src/mcedit2/rendering/textureatlas.py

### 2016-01-31
- **IntersectionBox now uses a list of selections rather than just two** [`ee16ede`]
  **Files changed:** src/mceditlib/selection/__init__.py

### 2016-01-31
- **Biome brush is now a chunkwise operation** [`483ab6c`]
  **Files changed:** src/mcedit2/editortools/brush/modes.py

### 2016-01-31
- **Stop error dialog from displaying many times at once** [`49f4f70`]
  **Files changed:** src/mcedit2/dialogs/error_dialog.py

### 2016-01-31
- **Rewrite UnionBox.contains_coords for subselection list** [`5683804`]
  **Files changed:** src/mceditlib/selection/__init__.py

### 2016-01-31
- **Implement `positions()` on SelectionBox (slow)** [`f3ff47a`]
  **Files changed:** src/mceditlib/selection/__init__.py

### 2016-01-31
- **Rewrite docstrings in SelectionBox** [`d897aaa`]
  **Files changed:** src/mceditlib/selection/__init__.py

### 2016-01-31
- **Fix divide-by-zero in rescaleProgress** [`a7b0b64`]
  **Files changed:** src/mceditlib/util/progress.py

### 2016-01-31
- **BrushCommand uses UnionBox instead of reduce to combine selections** [`76090f6`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py

### 2016-01-31
- **ShapeFuncSelection creates coordinate array using mgrid, not indices** [`2c7045d`]
  **Files changed:** src/mceditlib/selection/__init__.py

### 2016-01-31
- **FillBlocksOperation skips sections outside the selection** [`5a132b7`]
  **Files changed:** src/mceditlib/operations/block_fill.py

### 2016-01-31
- **Close gaps in dragged brushes by drawing lines** [`2458f3c`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py

### 2016-01-31
- **UnionBox now accepts any number of component selections** [`f82c7a5`]
  **Files changed:** src/mceditlib/selection/__init__.py

### 2016-01-31
- **BrushMode.applyToSelection now returns a progress iterator** [`fa1ddb4`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/brush/modes.py

### 2016-01-31
- **Brush tool is now draggable** [`daf2a91`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py

### 2016-01-31
- **Change docstrings to numpydoc** [`3a4751b`]
  **Files changed:** src/mcedit2/editortools/__init__.py

### 2016-01-31
- **Brush command combines multiple selections instead of using the first** [`91f9dfa`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/brush/modes.py

### 2016-01-31
- **Handle UnionBox components returning None from box_mask** [`d94b807`]
  **Files changed:** src/mceditlib/selection/__init__.py

### 2016-01-30
- **Remove stray debuglog** [`ef9032b`]
  **Files changed:** src/mcedit2/rendering/scenegraph/rendernode.py

### 2016-01-30
- **Rename 'destroy' methods to 'dealloc'** [`b6d372e`]
  Removes confusion with QWidget::destroy, which is not virtual and thus
  **Files changed:** is never dispatched into Python code., src/mcedit2/editorapp.py, src/mcedit2/editorsession.py, src/mcedit2/rendering/scenegraph/rendernode.py, src/mcedit2/util/glutils.py, src/mcedit2/worldlist.py, src/mcedit2/worldview/worldview.py

### 2016-01-30
- **In custom tracebacks, print object name if present** [`f5238b9`]
  **Files changed:** src/mcedit2/util/custom_traceback.py

### 2016-01-30
- **MobSpawnsBlockMesh checks for barrier blocks being defined** [`cf79a77`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/mobspawns.py

### 2016-01-20
- **Avoid creating world view when world list is offscreen.** [`358de35`]
  Seems to fix the access violations, but that's not at all certain.
  **Files changed:** Hours of bisecting and single-stepping also blamed the simple import of, one of the UI files for the violations., In any case, this avoids doubly creating the world view both when the, window is initialized and when it is shown on screen., src/mcedit2/worldlist.py

### 2016-01-19
- **Propagate 'readonly' flag to RegionFile** [`7a622bc`]
  Makes sure region files are opened in read-only mode.
  **Files changed:** src/mceditlib/anvil/adapter.py, src/mceditlib/anvil/worldfolder.py, src/mceditlib/pc/regionfile.py

### 2016-01-19
- **Disable a WorldView's rendering if an error occurs.** [`9809f27`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2016-01-11
- **Add hard-coded flag for rendering without display lists.** [`6092309`]
  **Files changed:** src/mcedit2/rendering/scenegraph/rendernode.py

### 2016-01-10
- **`-debug` enables ERROR_LOGGING and CONTEXT_CHECKING** [`6591ed9`]
  **Files changed:** src/mcedit2/main.py

### 2016-01-10
- **KeyboardInterrupt no longer triggers the error handler dialog.** [`c1d3240`]
  **Files changed:** src/mcedit2/main.py

### 2016-01-10
- **Remove unused variable** [`3ef0662`]
  **Files changed:** src/mcedit2/rendering/worldscene.py

### 2016-01-10
- **Assert display list is not None instead of is not truthy.** [`3ad11dc`]
  bool(array[0]) is not truthy but is still a valid display list.
  **Files changed:** src/mcedit2/util/glutils.py

### 2016-01-10
- **Add GL rendering profile to debug output** [`346c945`]
  **Files changed:** src/mcedit2/util/qglcontext.py

### 2015-12-20
- **Handle dirty flag on unparented entities.** [`ee078dd`]
  Parenting the entity should automatically dirty the parent.
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-12-16
- **Enable "View" button on world list.** [`c367941`]
  **Files changed:** src/mcedit2/worldlist.py

### 2015-12-16
- **More work on "Choose folder..." button.** [`136b685`]
  **Files changed:** src/mcedit2/worldlist.py

### 2015-12-16
- **Read-only worlds display "Read-only" in tab title.** [`22675c5`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-12-16
- **Worlds may be opened read-only from the command line** [`ff0fb67`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-12-13
- **Implement "Choose folder" button on world list** [`3660cd6`]
  **Files changed:** src/mcedit2/worldlist.py

### 2015-12-07
- **Add coordinate inputs to block inspector** [`aefa3f7`]
  **Files changed:** src/mcedit2/ui/inspector.ui, src/mcedit2/widgets/inspector/__init__.py

### 2015-12-07
- **Get NBT Editor working again after the switch to compiled ui files.** [`d299a9a`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/nbt.py

### 2015-12-06
- **NBT Editor will look up names for numeric item IDs in "id" tags.** [`fd99c4c`]
  **Files changed:** src/mcedit2/panels/player.py, src/mcedit2/widgets/nbttree/nbteditor.py, src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2015-12-06
- **Don't automatically remove tile entities when replacing blocks** [`396653f`]
  Minecraft should be able to do that. I hope.
  **Files changed:** src/mceditlib/operations/block_fill.py

### 2015-11-27
- **Exclude autogenerated pyfiles in ui/** [`20bacee`]
  **Files changed:** .gitignore

### 2015-11-27
- **Compile all ui files using pyside-uic** [`66524b4`]
  **Files changed:** src/mcedit2/dialogs/configure_blocks.py, src/mcedit2/dialogs/error_dialog.py, src/mcedit2/dialogs/plugins_dialog.py, src/mcedit2/editorapp.py, src/mcedit2/editorcommands/analyze.py, src/mcedit2/editorcommands/fill.py, src/mcedit2/editorcommands/find_replace/__init__.py, src/mcedit2/editorcommands/find_replace/command_text.py, src/mcedit2/editorcommands/find_replace/nbt.py, src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/edit_chunk.py, src/mcedit2/editortools/select.py, src/mcedit2/editortools/select_block.py, src/mcedit2/editortools/select_entity.py, src/mcedit2/editortools/tool_settings.py, src/mcedit2/library.py, src/mcedit2/main.py, src/mcedit2/panels/map.py, src/mcedit2/panels/player.py, src/mcedit2/panels/worldinfo.py, src/mcedit2/plugins.py, src/mcedit2/ui/__init__.py, src/mcedit2/ui/analyze.ui, src/mcedit2/ui/blocktype_list.ui, src/mcedit2/ui/dialogs/__init__.py, src/mcedit2/ui/dialogs/configure_blocks.ui, src/mcedit2/ui/dialogs/error_dialog.ui, src/mcedit2/ui/dialogs/plugins.ui, src/mcedit2/ui/editortools/__init__.py, src/mcedit2/ui/editortools/brush.ui, src/mcedit2/ui/editortools/select_block.ui, src/mcedit2/ui/editortools/select_chunk.ui, src/mcedit2/ui/editortools/select_entity.ui, src/mcedit2/ui/fill.ui, src/mcedit2/ui/find_replace.ui, src/mcedit2/ui/find_replace_command_results.ui, src/mcedit2/ui/find_replace_commands.ui, src/mcedit2/ui/find_replace_nbt.ui, src/mcedit2/ui/find_replace_nbt_results.ui, src/mcedit2/ui/import_map.ui, src/mcedit2/ui/inspector.ui, src/mcedit2/ui/library.ui, src/mcedit2/ui/log_view.ui, src/mcedit2/ui/main_window.ui, src/mcedit2/ui/panels/__init__.py, src/mcedit2/ui/panels/map.ui, src/mcedit2/ui/panels/player.ui, src/mcedit2/ui/panels/worldinfo.ui, src/mcedit2/ui/preferences_dialog.ui, src/mcedit2/ui/replace.ui, src/mcedit2/ui/rotation_widget.ui, src/mcedit2/ui/selection_coord_widget.ui, src/mcedit2/ui/widgets/__init__.py, src/mcedit2/ui/widgets/block_picker.ui, src/mcedit2/ui/widgets/block_picker_multiple.ui, src/mcedit2/ui/widgets/coord_widget.ui, src/mcedit2/util/gen_ui.py, src/mcedit2/util/minecraftinstall.py, src/mcedit2/widgets/blockpicker.py, src/mcedit2/widgets/blockpicker_util.py, src/mcedit2/widgets/blocktype_list.py, src/mcedit2/widgets/brushmode.py, src/mcedit2/widgets/coord_widget.py, src/mcedit2/widgets/inspector/__init__.py, src/mcedit2/widgets/log_view.py, src/mcedit2/widgets/prefsdialog.py, src/mcedit2/widgets/rotation_widget.py, src/mcedit2/widgets/shapewidget.py, src/mcedit2/worldlist.py

### 2015-11-23
- **Fix Vanilla name<->state mappings not being overridden by FML ones correctly** [`193ea92`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-11-20
- **Clean up some imports** [`86f7769`]
  **Files changed:** src/mcedit2/panels/player.py

### 2015-11-20
- **Change [Tile]EntityRef.dirty to be consistent with all other dirty flags** [`4e55976`]
  I don't like how these are all properties. Most of the usages just set dirty=True, and the only time dirty=False is set is when the chunk is written or the scene node is redrawn.
  **Files changed:** src/mcedit2/editorcommands/find_replace/nbt.py, src/mceditlib/anvil/entities.py

### 2015-11-18
- **Fix AttributeError when moving mouse over worldview after closing tab** [`ac5c61a`]
  There is probably something wrong with overloading QWidget.destroy like this. I should rewrite the entire thing in C++ and regain control over object destruction.
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py, src/mcedit2/worldview/worldview.py

### 2015-11-18
- **Move several .ui files to ui/dialogs and ui/widgets** [`d6049ca`]
  **Files changed:** src/mcedit2/dialogs/configure_blocks.py, src/mcedit2/dialogs/error_dialog.py, src/mcedit2/dialogs/plugins_dialog.py, src/mcedit2/ui/dialogs/configure_blocks.ui, src/mcedit2/ui/dialogs/error_dialog.ui, src/mcedit2/ui/dialogs/plugins.ui, src/mcedit2/ui/widgets/block_picker.ui, src/mcedit2/ui/widgets/block_picker_multiple.ui, src/mcedit2/ui/widgets/coord_widget.ui, src/mcedit2/widgets/blockpicker.py, src/mcedit2/widgets/coord_widget.py

### 2015-11-18
- **Move configureblocksdialog to dialogs.configure_blocks** [`c1bab59`]
  Sidenote: I am very impressed that PyCharm auto-organized my imports using my favored scheme - builtin modules, then third party modules, then application modules
  **Files changed:** src/mcedit2/dialogs/configure_blocks.py, src/mcedit2/editorapp.py

### 2015-11-18
- **The ResourceLoader created when loading a world now tries to find a "mods" folder alongside the "saves" folder.** [`83f2d1c`]
  **Files changed:** src/mcedit2/resourceloader.py, src/mcedit2/util/minecraftinstall.py

### 2015-11-17
- **Fix mob spawns renderer for numpy 1.10** [`ca80102`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/mobspawns.py

### 2015-11-16
- **Select -> Inspect** [`e9b4041`]
  **Files changed:** src/mcedit2/editortools/select_block.py, src/mcedit2/editortools/select_entity.py

### 2015-11-16
- **Inspect Chunk now switches to the correct widget in inspector panel** [`4fbad34`]
  **Files changed:** src/mcedit2/widgets/inspector/__init__.py

### 2015-11-16
- **Revise method for finding places where mobs can spawn.** [`12d2ef9`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/mobspawns.py, src/mceditlib/blocktypes/__init__.py

### 2015-11-13
- **Add more block json keys: materialBlocksMovement, normalCube, fullBlock, materialMapColorIndex, materialLiquid** [`bb084f6`]
  Remove 'collidable'
  **Files changed:** src/mceditlib/blocktypes/minecraft_raw.json

### 2015-11-13
- **Reformat minecraft_raw.json** [`c8fe5c6`]
  **Files changed:** src/mceditlib/blocktypes/minecraft_raw.json

### 2015-11-13
- **Add chunk renderer for positions that can spawn mobs** [`df1be77`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/mobspawns.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/layers.py

### 2015-11-12
- **Profiler uses time.clock on win32 for more accuracy** [`5fe2468`]
  **Files changed:** src/mcedit2/util/profiler.py

### 2015-11-12
- **Reorganize WorldView methods** [`1b6d9d0`]
  **Files changed:** src/mcedit2/worldview/camera.py, src/mcedit2/worldview/iso.py, src/mcedit2/worldview/worldview.py

### 2015-11-12
- **Compile non-visible nodes** [`bbc3263`]
  Otherwise they never get compiled again, as setting visible doesn't mark the parent as childNeedsRecompile
  **Files changed:** src/mcedit2/rendering/scenegraph/rendernode.py

### 2015-11-09
- **Update README** [`f8b30d0`]
  **Files changed:** README.md

### 2015-11-08
- **DisplayList no longer remembers its drawFunc or calls compile() automatically.** [`d36d88c`]
  Pass drawFunc when calling compile().
  **Files changed:** src/mcedit2/util/glutils.py

### 2015-11-09
- **Issue #169: Init X11 threads for threaded buffer swap** [`39a717b`]
  Ref: http://blog.qt.io/blog/2011/06/03/threaded-opengl-in-4-8/
  **Files changed:** src/mcedit2/main.py

### 2015-11-07
- **Add function for gathering node statistics** [`b5889d5`]
  **Files changed:** src/mcedit2/rendering/scenegraph/rendernode.py

### 2015-11-07
- **Collapse some one-child nodes in WorldScene into their parents** [`df15798`]
  **Files changed:** src/mcedit2/rendering/worldscene.py

### 2015-11-07
- **Skip emitting empty nodes for entity meshes** [`983bec6`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entitymesh.py

### 2015-11-07
- **Add names to almost all scene nodes** [`311a714`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/clone.py, src/mcedit2/editortools/generate.py, src/mcedit2/editortools/move.py, src/mcedit2/editortools/select.py, src/mcedit2/imports.py, src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/chunkmeshes/lowdetail.py, src/mcedit2/rendering/chunknode.py, src/mcedit2/rendering/command_visuals.py, src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/rendering/scenegraph/scenenode.py, src/mcedit2/widgets/inspector/__init__.py

### 2015-11-05
- **Move setup.cfg to pytest.ini** [`e2cd8d2`]
  **Files changed:** pytest.ini

### 2015-11-04
- **Finish fixing up test_relight** [`ea88d7b`]
  **Files changed:** tests/test_mceditlib/relight_test.py

### 2015-11-03
- **Custom traceback frames are now compatible with IPython** [`df48834`]
  **Files changed:** src/mcedit2/util/custom_traceback.py

### 2015-11-02
- **Add more excludes to specfile, don't mass-include all source files, only the ones that aren't imported internally** [`e9feb01`]
  **Files changed:** mcedit2.spec

### 2015-11-02
- **Update IPython widget for IPython 4.0** [`c7cfcd7`]
  **Files changed:** requirements.txt, src/mcedit2/main.py, src/mcedit2/util/ipython_widget.py

### 2015-11-01
- **Fix incorrect dtype in updateLightsByCoord** [`bfd2bd9`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-11-01
- **Update mcedit2.spec for PyInstaller 3 (really, this time).** [`48e51a1`]
  **Files changed:** mcedit2.spec

### 2015-11-01
- **Add match and exclude patterns for pytest** [`9d0dab3`]
  **Files changed:** setup.cfg

### 2015-10-30
- **Log region reads/writes at a new, lower level than DEBUG.** [`459de55`]
  **Files changed:** src/mceditlib/pc/regionfile.py

### 2015-10-30
- **Remove logging.basicConfig calls from tests** [`261df22`]
  And remove one from blocktypes. What was it even doing there?
  **Files changed:** src/mceditlib/blocktypes/__init__.py, tests/test_mceditlib/__init__.py, tests/test_mceditlib/cache_test.py, tests/test_mceditlib/relight_test.py, tests/test_mceditlib/revisionhistory_test.py

### 2015-10-30
- **Fix test_relight and `history` fixture.** [`b92ac82`]
  **Files changed:** tests/test_mceditlib/relight_test.py, tests/test_mceditlib/revisionhistory_test.py

### 2015-10-30
- **Travis: Upgrade pip version and install wheel** [`3c1abfe`]
  **Files changed:** .travis.yml

### 2015-10-30
- **Patch up a few remaining tests** [`0091330`]
  **Files changed:** tests/test_mceditlib/extended_id_test.py, tests/test_mceditlib/nbt_test.py, tests/test_mceditlib/relight_test.py, tests/test_mceditlib/revisionhistory_test.py

### 2015-10-30
- **Remove all remaining references to `test.templevel`** [`58ab4d3`]
  **Files changed:** benchmarks/__init__.py, benchmarks/mceditlib/__init__.py, benchmarks/mceditlib/time_exportimport.py, benchmarks/mceditlib/time_fill.py, benchmarks/mceditlib/time_getsetblocks.py, benchmarks/mceditlib/time_loadsave.py, benchmarks/mceditlib/time_relight_manmade.py, benchmarks/mceditlib/time_relight_natural.py, benchmarks/mceditlib/time_storagechain.py, tests/__init__.py, tests/test_mceditlib/schematic_test.py, tests/test_mceditlib/server_test.py, tests/test_mceditlib/session_lock_test.py

### 2015-10-30
- **Enable cached pip packages** [`7f1b7d3`]
  **Files changed:** .travis.yml

### 2015-10-30
- **Fix a few tests that had collection errors.** [`0edb548`]
  **Files changed:** tests/test_mceditlib/conftest.py, tests/test_mceditlib/nbt_test.py, tests/test_mceditlib/relight_test.py, tests/test_mceditlib/revisionhistory_test.py

### 2015-10-29
- **Remove logging from RenderNode** [`f5f6ab0`]
  This reverts commit fd795bf79cfc0e068d0d7b8e58acc0f034150f69.
  **Files changed:** src/mcedit2/rendering/scenegraph/rendernode.py

### 2015-10-28
- **ChunkLoader now notifies clients of deleted chunks via chunkInvalid** [`91f6b2b`]
  **Files changed:** src/mcedit2/rendering/chunkloader.py, src/mcedit2/worldview/cutaway.py, src/mcedit2/worldview/worldview.py

### 2015-10-28
- **Begin naming Nodes** [`af26449`]
  **Files changed:** src/mcedit2/rendering/scenegraph/scenenode.py, src/mcedit2/worldview/worldview.py

### 2015-10-28
- **Increase camera initial speed.** [`45c6ab9`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-10-28
- **Fix deleted chunks not being purged from caches.** [`787e8ba`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-10-28
- **Camera update ticks now tick relative to the time interval between updates.** [`ced819a`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-10-28
- **Fix blocktypes not being created on newly created worlds** [`d364e5d`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-10-28
- **Finish modifying old tests to run under pytest** [`c858d4e`]
  **Files changed:** tests/test_mceditlib/anvil_test.py, tests/test_mceditlib/cache_test.py, tests/test_mceditlib/conftest.py, tests/test_mceditlib/extended_id_test.py, tests/test_mceditlib/nbt_test.py

### 2015-10-28
- **Skip transform tests (TODO: these are not automated tests, fix)** [`fc82c17`]
  **Files changed:** tests/test_mceditlib/transform_test.py

### 2015-10-28
- **Increase cache limit in testThrashing to be more than the maxsize of recentChunks** [`1e65b6e`]
  **Files changed:** tests/test_mceditlib/cache_test.py

### 2015-10-28
- **Rewrite test fixtures using _temp_file and _temp_level** [`5f01a1b`]
  **Files changed:** tests/test_mceditlib/conftest.py

### 2015-10-17
- **Rearrange tests/ folder so tests/mceditlib doesn't overload src/mceditlib in module searches** [`1a80d4b`]
  **Files changed:** tests/mceditlib/conftest.py, tests/mceditlib/extended_id_test.py, tests/mceditlib/nbt_test.py, tests/mceditlib/templevel.py, tests/test_mceditlib/__init__.py, tests/test_mceditlib/anvil_test.py, tests/test_mceditlib/cache_test.py, tests/test_mceditlib/conftest.py, tests/test_mceditlib/editing_test.py, tests/test_mceditlib/entity_test.py, tests/test_mceditlib/extended_id_test.py, tests/test_mceditlib/nbt_test.py, tests/test_mceditlib/relight_test.py, tests/test_mceditlib/revisionhistory_test.py, tests/test_mceditlib/run_regression_test.py, tests/test_mceditlib/schematic_test.py, tests/test_mceditlib/server_test.py, tests/test_mceditlib/session_lock_test.py, tests/test_mceditlib/transform_test.py

### 2015-10-16
- **Install xdist and catchlog for tests** [`f459f3d`]
  **Files changed:** tests/requirements.txt

### 2015-10-16
- **Add travis.yml** [`92f2715`]
  **Files changed:** .travis.yml

### 2015-10-16
- **Move cython to mceditlib reqs** [`bf9a278`]
  **Files changed:** requirements-mceditlib.txt, requirements.txt

### 2015-10-16
- **Split setup.py into two files** [`8c33e43`]
  **Files changed:** setup.py, setup_mcedit2.py, setup_mceditlib.py

### 2015-10-16
- **requirements.txt now references requirements-mceditlib.txt** [`fa02b40`]
  **Files changed:** requirements-mceditlib.txt, requirements.txt

### 2015-10-16
- **Move all tests/benchmarks out of src/ and into tests/ and benchmarks/** [`b4c605c`]
  **Files changed:** benchmarks/mcedit2/time_loadmodels.py, benchmarks/mcedit2/time_raycast.py, benchmarks/mcedit2/time_selectionrender.py, benchmarks/mceditlib/time_exportimport.py, benchmarks/mceditlib/time_fill.py, benchmarks/mceditlib/time_getsetblocks.py, benchmarks/mceditlib/time_loadsave.py, benchmarks/mceditlib/time_nbt.py, benchmarks/mceditlib/time_relight_manmade.py, benchmarks/mceditlib/time_relight_natural.py, benchmarks/mceditlib/time_storagechain.py, tests/mceditlib/__init__.py, tests/mceditlib/anvil_test.py, tests/mceditlib/cache_test.py, tests/mceditlib/conftest.py, tests/mceditlib/editing_test.py, tests/mceditlib/entity_test.py, tests/mceditlib/extended_id_test.py, tests/mceditlib/nbt_test.py, tests/mceditlib/relight_test.py, tests/mceditlib/revisionhistory_test.py, tests/mceditlib/run_regression_test.py, tests/mceditlib/schematic_test.py, tests/mceditlib/server_test.py, tests/mceditlib/session_lock_test.py, tests/mceditlib/templevel.py, tests/mceditlib/transform_test.py, tests/requirements.txt

### 2015-10-27
- **Swap GL buffers on a second thread to improve chunk loading speed and UI responsiveness.** [`81c65fb`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-10-27
- **Increase maxFPS, improving perceived smoothness** [`f71f0f7`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-10-27
- **Camera movement is smoother. Tweak camera tick rate, acceleration, and min speed.** [`ee9e6ae`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-10-27
- **Add crude, half-implemented "Go To" buttons to the CommandBlock inspector** [`db76266`]
  **Files changed:** src/mcedit2/widgets/inspector/tileentities/command.py

### 2015-10-26
- **Status bar now updates in response to viewport movement (as when holding camera keys)** [`e3b602d`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-10-26
- **Refactor Scenegraph nodes to allow states attached to each Node. (Big, messy change!)** [`33d2537`]
  States have an enter() and exit() function to setup and teardown GL states. Previously, states were their own nodes, so each state created its own display list. Now, creating a node for each state is optional.
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/generate.py, src/mcedit2/editortools/select.py, src/mcedit2/imports.py, src/mcedit2/rendering/blockmeshes.py, src/mcedit2/rendering/chunkmeshes/chunksections.py, src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/chunkmeshes/heightlevel.py, src/mcedit2/rendering/chunkmeshes/lowdetail.py, src/mcedit2/rendering/chunkmeshes/terrainpop.py, src/mcedit2/rendering/chunknode.py, src/mcedit2/rendering/command_visuals.py, src/mcedit2/rendering/depths.py, src/mcedit2/rendering/loadablechunks.py, src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/rendering/renderstates.py, src/mcedit2/rendering/scenegraph/bind_texture.py, src/mcedit2/rendering/scenegraph/depth_test.py, src/mcedit2/rendering/scenegraph/matrix.py, src/mcedit2/rendering/scenegraph/misc.py, src/mcedit2/rendering/scenegraph/rendernode.py, src/mcedit2/rendering/scenegraph/scenenode.py, src/mcedit2/rendering/scenegraph/states.py, src/mcedit2/rendering/scenegraph/texture_atlas.py, src/mcedit2/rendering/selection.py, src/mcedit2/rendering/workplane.py, src/mcedit2/rendering/worldscene.py, src/mcedit2/widgets/inspector/__init__.py, src/mcedit2/worldview/camera.py, src/mcedit2/worldview/cutaway.py, src/mcedit2/worldview/iso.py, src/mcedit2/worldview/minimap.py, src/mcedit2/worldview/overhead.py, src/mcedit2/worldview/schematic_worldview.py, src/mcedit2/worldview/worldview.py

### 2015-10-25
- **xxx destroy this commit, adds logging to rendernode** [`fd795bf`]
  **Files changed:** src/mcedit2/rendering/scenegraph/rendernode.py

### 2015-10-25
- **Add command visuals for /give, /playsound, /summon, /testforblock, /blockdata, /fill, /setblock** [`333e0e6`]
  Register command visuals using a decorator
  **Files changed:** src/mcedit2/rendering/command_visuals.py

### 2015-10-25
- **Add half-done command parsers for /fill, /give, /playsound, /clone, /blockdata** [`d1e2a76`]
  Register command parsers using a decorator
  **Files changed:** src/mcedit2/util/commandblock.py

### 2015-10-25
- **Shaped selection renderer feels slightly more responsive.** [`e2f41ba`]
  Load chunks immediately over a very short duration when the box is resized.
  **Files changed:** src/mcedit2/editortools/select.py, src/mcedit2/rendering/selection.py

### 2015-10-25
- **Tweak the formula used for LineArcNode** [`81e1753`]
  **Files changed:** src/mcedit2/rendering/command_visuals.py

### 2015-10-25
- **Stub out the "Find/Replace Command Text" window** [`b271508`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/__init__.py, src/mcedit2/editorcommands/find_replace/command_text.py, src/mcedit2/ui/find_replace_command_results.ui, src/mcedit2/ui/find_replace_commands.ui

### 2015-10-25
- **Show command visuals when inspecting blocks.** [`2f742a7`]
  **Files changed:** src/mcedit2/widgets/inspector/__init__.py

### 2015-10-25
- **Add command visualizers for /execute, /setblock, /clone** [`f43e5e0`]
  **Files changed:** src/mcedit2/rendering/command_visuals.py

### 2015-10-25
- **Add command parsers for /execute, /clone, /setblock** [`5e273b1`]
  **Files changed:** src/mcedit2/util/commandblock.py

### 2015-10-24
- **Reformat EditorSession menu creation code** [`bd76d3e`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-10-24
- **Inspector now outlines the selected block/entity/chunk** [`60775a4`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/widgets/inspector/__init__.py

### 2015-10-24
- **Improve block inspector with ID number, light level, and block name readouts** [`fec40e9`]
  **Files changed:** src/mcedit2/ui/inspector.ui, src/mcedit2/widgets/inspector/__init__.py

### 2015-10-24
- **Add blocktypes for new command blocks** [`119fab3`]
  **Files changed:** src/mceditlib/blocktypes/idmapping.json, src/mceditlib/blocktypes/minecraft.json

### 2015-10-24
- **Replace GL.GL_LINES with glPolygonMode(..., GL.GL_LINE)** [`3234216`]
  glPolygonMode is affected by polygon offset, GL.GL_LINES is not
  **Files changed:** src/mcedit2/editortools/select.py, src/mcedit2/rendering/selection.py

### 2015-10-24
- **The log said to update progressMax to 7, so I did.** [`c2f128e`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-10-24
- **find_replace.blocks -> find_replace.replace_blocks** [`b2cb186`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/__init__.py, src/mcedit2/editorcommands/find_replace/replace_blocks.py

### 2015-10-23
- **AnalyzeOutputDialog does not call exec during __init__** [`2639967`]
  **Files changed:** src/mcedit2/editorcommands/analyze.py, src/mcedit2/editorsession.py

### 2015-10-23
- **Refactor editorcommands.find_replace to a package with one module for each find/replace action** [`0856fe6`]
  **Files changed:** src/mcedit2/editorcommands/find_replace/__init__.py, src/mcedit2/editorcommands/find_replace/blocks.py, src/mcedit2/editorcommands/find_replace/nbt.py

### 2015-10-23
- **Add one command for each tab of the Find/Replace dialog** [`46ba2e3`]
  **Files changed:** src/mcedit2/editorcommands/find_replace.py, src/mcedit2/editorsession.py

### 2015-10-23
- **Double-check current selection in EditorSession.export()** [`a58d7c5`]
  This action should be disabled when the selection is None, but whatever.
  **Files changed:** src/mcedit2/editorsession.py

### 2015-10-20
- **Disable log view for now. I never use it anyway.** [`4417947`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/widgets/__init__.py, src/mcedit2/widgets/log_view.py

### 2015-10-20
- **Move tool and coord widget now support relative offsets** [`af6a72a`]
  **Files changed:** src/mcedit2/editortools/move.py, src/mcedit2/ui/coord_widget.ui, src/mcedit2/widgets/coord_widget.py

### 2015-10-18
- **Rewrite BlockTypesItemWidget to not create widgets during updateContents** [`a5801f1`]
  Consequently does not create widgets during the paint() of a view with a BlockTypeListItemDelegate
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2015-10-18
- **Fake states are now "[meta=%d]" instead of "[%d]"** [`5319da5`]
  **Files changed:** src/mcedit2/editorsession.py, src/mceditlib/anvil/adapter.py

### 2015-10-17
- **Don't create multiple "ghost" imports when importing a second time.** [`d4f1656`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-10-17
- **Add docstrings to createSchematic, extractSchematicFrom and Ray** [`de03b74`]
  **Files changed:** src/mceditlib/export.py, src/mceditlib/geometry.py, src/mceditlib/schematic.py

### 2015-10-17
- **Handle MaxDistanceError when importing schematics** [`aece427`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-10-16
- **Merge pull request #161 from straemer/master** [`1bfb781`]
  Add instructions to set virtualenv to use python2

### 2015-10-16
- **Add instructions to set virtualenv to use python2 when python3 is the default.** [`b8bef5f`]
  **Files changed:** README.md

### 2015-10-14
- **pointInputChanged now goes through importDidMove** [`8f47d67`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-10-14
- **Transform import positions using 3x3 matrix to skip tuple resize** [`db44717`]
  **Files changed:** src/mcedit2/editortools/clone.py

### 2015-10-14
- **Align import positions to the block grid** [`8edd6c8`]
  **Files changed:** src/mcedit2/editortools/clone.py

### 2015-10-14
- **Actually return the bounds for temp schematics** [`ca9617b`]
  **Files changed:** src/mcedit2/imports.py

### 2015-10-14
- **Cache some computed points and bounds instead of computing them in properties** [`cca9ed3`]
  **Files changed:** src/mcedit2/imports.py

### 2015-10-14
- **Vector now returns an ndarray when multiplied with one.** [`8c02496`]
  **Files changed:** src/mceditlib/geometry.py

### 2015-10-14
- **Return import bounds for temporary copies** [`5a1170b`]
  **Files changed:** src/mcedit2/imports.py

### 2015-10-14
- **showProgress handles reentrant calls by completing these calls non-interactively.** [`156dfa2`]
  **Files changed:** src/mcedit2/util/showprogress.py

### 2015-10-14
- **Non-transformed world loader for PendingImportNode only instantly loads the first clone** [`457c6ad`]
  **Files changed:** src/mcedit2/imports.py

### 2015-10-14
- **BoundingBox.intersect always returns a BoundingBox** [`3182931`]
  **Files changed:** src/mceditlib/selection/__init__.py

### 2015-10-14
- **PendingImport uses the correct bounds for extracting temp schematics, and returns the source selection for imports** [`169de72`]
  **Files changed:** src/mcedit2/editortools/clone.py, src/mcedit2/editortools/move.py, src/mcedit2/imports.py

### 2015-10-14
- **Repeated clone previews now rotate repeated rotations synchronously** [`6f9583a`]
  **Files changed:** src/mcedit2/editortools/clone.py, src/mcedit2/imports.py

### 2015-10-14
- **Non-primary PendingImportNodes can have their BoxHandles disabled** [`743cce9`]
  **Files changed:** src/mcedit2/editortools/clone.py, src/mcedit2/imports.py

### 2015-10-14
- **Cache PendingImport.transformOffset** [`cd0bef1`]
  **Files changed:** src/mcedit2/imports.py

### 2015-10-13
- **Clone tool now has rotation settings** [`9a05736`]
  **Files changed:** src/mcedit2/editortools/clone.py, src/mcedit2/imports.py

### 2015-10-13
- **Extract and move getSourceForDim from MoveTool to PendingImport** [`f3d65b8`]
  **Files changed:** src/mcedit2/editortools/move.py, src/mcedit2/imports.py

### 2015-10-12
- **Begin adding rotation inputs to Clone tool** [`d1b06bf`]
  **Files changed:** src/mcedit2/editortools/clone.py

### 2015-10-11
- **Move/Clone tools return to Select tool after confirm.** [`a12574d`]
  **Files changed:** src/mcedit2/editortools/clone.py, src/mcedit2/editortools/move.py

### 2015-10-11
- **Extract RotationWidget to widgets/rotation_widget.py** [`05d844c`]
  **Files changed:** src/mcedit2/editortools/move.py, src/mcedit2/widgets/rotation_widget.py

### 2015-10-09
- **Expand transform bounds when not on a block edge.** [`35d7317`]
  **Files changed:** src/mceditlib/transform.py

### 2015-10-09
- **Load block mapping only after all attempts at loading/creating metadataTag** [`9ec4545`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-10-09
- **Implement camera acceleration** [`feb3252`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-10-08
- **Transformation matrix accounts for coordinates being the lower-left corner of cells.** [`4778a3c`]
  **Files changed:** src/mceditlib/transform.py

### 2015-10-08
- **Setting the actual rotation of PendingImportNode also updates the rotation of the non-transformed preview.** [`adf70cf`]
  **Files changed:** src/mcedit2/imports.py

### 2015-10-08
- **Fix calculation of transformed bounds not using inverse matrix** [`010fea7`]
  **Files changed:** src/mceditlib/transform.py

### 2015-10-08
- **Rot90 buttons no longer checkable** [`c932f2a`]
  **Files changed:** src/mcedit2/ui/rotation_widget.ui

### 2015-10-08
- **Add exact values for sin/cos of 90 degree angles.** [`92833b7`]
  **Files changed:** src/mceditlib/transform.py

### 2015-10-08
- **Create icons for and implement right-angle rotation buttons.** [`63c578f`]
  **Files changed:** src/mcedit2/assets/mcedit2/icons/right_angle.png, src/mcedit2/assets_raw/icons.svg, src/mcedit2/editortools/move.py

### 2015-10-08
- **Change default distance when raycast fails to same as raycast distance** [`8713704`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-10-08
- **Update Move tool's rotation input when pendingImport is changed** [`d99ccf2`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-10-08
- **Remove multi-imports from PasteImportCommand** [`9e2004d`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-10-08
- **Reduce maximum raycast distance.** [`6def097`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-10-08
- **Move PendingImport and PendingImportNode to imports.py, disable multi-imports (for now)** [`2557df5`]
  Rewrite much of them for clarity.
  **Files changed:** src/mcedit2/editortools/move.py, src/mcedit2/imports.py, src/mcedit2/panels/pending_imports.py

### 2015-10-07
- **Move PendingImport and PendingImportNode to imports.py** [`df25824`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/clone.py, src/mcedit2/editortools/move.py, src/mcedit2/imports.py

### 2015-10-07
- **Library widget starts on Schematics tab** [`7c89720`]
  **Files changed:** src/mcedit2/ui/library.ui

### 2015-10-07
- **Adjust colors of greyed-out Save icon.** [`b446465`]
  **Files changed:** src/mcedit2/assets_raw/icons.svg

### 2015-10-07
- **Don't raise ValueError when creating non-creatable sections, return None instead.** [`bb05c9b`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-10-07
- **TranslateNode.translateOffset is now Vector typed.** [`83a882e`]
  **Files changed:** src/mcedit2/rendering/scenegraph/matrix.py

### 2015-10-07
- **Painfully fixed recursion depth error when undoing Move Finish commands.** [`f0145de`]
  This is very, very unsatisfactory. It isn't clear which object is the definitive source for a pending import's position, transformed or not.
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/move.py

### 2015-10-06
- **Fix progress dialog suddenly reappearing after a delay.** [`cf34b41`]
  **Files changed:** src/mcedit2/util/showprogress.py

### 2015-10-06
- **Create MCEProgressDialog, which cannot be closed by any means.** [`c2ff80a`]
  **Files changed:** src/mcedit2/dialogs/error_dialog.py, src/mcedit2/editorapp.py, src/mcedit2/editorsession.py, src/mcedit2/util/showprogress.py

### 2015-10-06
- **WorldLoader now has a startLoader function with a minimum duration.** [`0b1f47c`]
  The minimum duration tells how long to load chunks immediately before starting the async loader.
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/generate.py, src/mcedit2/editortools/move.py, src/mcedit2/util/worldloader.py, src/mcedit2/worldview/schematic_worldview.py

### 2015-10-06
- **Flood fill tool now has hover and flood direction options.** [`7bdcd2c`]
  **Files changed:** src/mcedit2/editortools/flood_fill.py

### 2015-10-06
- **Progress dialog is once again cancelable, and has a minimum time before displaying.** [`dbbacea`]
  **Files changed:** src/mcedit2/util/showprogress.py

### 2015-10-06
- **SimplePerformCommand uses showProgress to show commitUndo progress.** [`7fd9744`]
  Makes Flood Fill tool show progress when committing undo.
  **Files changed:** src/mcedit2/command.py

### 2015-10-05
- **Add some docstrings to editorsession.py** [`95fceb8`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-10-05
- **Schematics dropped into the editor window have a more sensible initial position** [`fba8778`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-10-04
- **Add top toolbar buttons for Save and Fill** [`21df3c4`]
  Save icon changes to indicate whether there are unsaved changes. The icon does not distinguish between modifying and non-modifying (e.g. selection size) commands.
  **Files changed:** src/mcedit2/assets/mcedit2/icons/fill.png, src/mcedit2/assets/mcedit2/icons/save.png, src/mcedit2/assets/mcedit2/icons/save_ok.png, src/mcedit2/assets/mcedit2/toolicons/flood_fill.png, src/mcedit2/assets_raw/icons.svg, src/mcedit2/editorapp.py, src/mcedit2/editorsession.py

### 2015-10-04
- **Fix zero division when printing copy stats.** [`41a1cbb`]
  **Files changed:** src/mceditlib/block_copy.py

### 2015-10-04
- **Move tool finally has "Copy Air" option.** [`c5e2b12`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-10-04
- **Fix rotated objects not moving with their box handle.** [`a6d754a`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-10-04
- **Add explicit copyAir flag to copyBlocksIter** [`1131632`]
  **Files changed:** src/mceditlib/block_copy.py

### 2015-10-04
- **Fix clone tool not resetting offset when used a second time.** [`e24aebd`]
  **Files changed:** src/mcedit2/editortools/clone.py

### 2015-10-04
- **Make imported objects not sunken one block into the ground.** [`dbc62d5`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-10-04
- **Set EditorSession.currentDimension earlier to try to fix a weird AttributeError** [`c571877`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-10-04
- **Allow files to be imported by drag and drop into editor window.** [`6dd9e6f`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-10-03
- **Rewrite CloneTool to use PendingImportNode's mouse event handling.** [`cb88acf`]
  **Files changed:** src/mcedit2/editortools/clone.py

### 2015-10-03
- **Do not emit handleBoundsChangedDone for non-changes.** [`23f7106`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-10-03
- **PendingImportNode now forwards mouse events to its handleNode** [`1167d93`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-10-03
- **Greatly simplify extractSchematicFromIter** [`63d0276`]
  **Files changed:** src/mceditlib/export.py

### 2015-10-03
- **Move tool now imports the transformed form of the moved object** [`911aa28`]
  ... as you would expect from looking at the live preview of the moved object. Also, intermediate schematics are skipped when the source and destination boxes do not intersect.
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/move.py

### 2015-10-02
- **transform_test now tests selection, rotation, and selection+rotation** [`9be6563`]
  **Files changed:** src/mceditlib/test/transform_test.py

### 2015-10-02
- **Move tool now displays live previews of the rotated blocks** [`1656571`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-10-02
- **PendingImport now has rotate/scale and transformedDim attributes** [`2c53192`]
  transformedDim is recreated whenever the rotate/scale are changed. Its chunks are lazily evaluated.
  **Files changed:** src/mcedit2/editorsession.py

### 2015-10-02
- **Fix movable-only BoxHandles not actually being movable.** [`fc00800`]
  **Files changed:** src/mcedit2/handles/boxhandle.py

### 2015-10-02
- **RotateNode allows degrees and axis to be changed.** [`d6f5b98`]
  **Files changed:** src/mcedit2/rendering/scenegraph/matrix.py

### 2015-10-02
- **Refactor RotationTransform, create SelectionTransform** [`986a4fb`]
  **Files changed:** src/mceditlib/transform.py

### 2015-10-01
- **Use Tool action now has "any" modifiers.** [`c96a856`]
  May have undesirable side effects.
  **Files changed:** src/mcedit2/worldview/viewaction.py

### 2015-10-01
- **BoxHandle now uses explicit isMoving, isCreating, isResizing flags instead of inferring them from other state** [`37bd7e0`]
  **Files changed:** src/mcedit2/handles/boxhandle.py

### 2015-10-01
- **Resizing selection box only triggers immediate chunk loads when mouse button is released.** [`db584cf`]
  **Files changed:** src/mcedit2/editortools/select.py, src/mcedit2/rendering/selection.py

### 2015-10-01
- **Refactor drag-to-move out of MoveTool and into BoxHandle.** [`a5e54c6`]
  This is a bit icky - PendingImportNode emits a signal that MoveTool handles by moving the "current import", instead of by moving the PendingImportNode's import.
  **Files changed:** TODO: Give CloneTool the same treatment., src/mcedit2/editortools/move.py

### 2015-10-01
- **Refactor drag-to-move out of MoveTool and into BoxHandle.** [`5deb2f2`]
  This is a bit icky - PendingImportNode emits a signal that MoveTool handles by moving the "current import", instead of by moving the PendingImportNode's import.
  **Files changed:** TODO: Give CloneTool the same treatment., src/mcedit2/editortools/generate.py, src/mcedit2/editortools/move.py, src/mcedit2/editortools/select.py, src/mcedit2/handles/boxhandle.py

### 2015-10-01
- **Refactor PendingImportNode to contain a translate node rather than be one** [`cc569bc`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-10-01
- **Create rotation input widget in preparation for live rotation.** [`a91d6b3`]
  **Files changed:** src/mcedit2/editortools/move.py, src/mcedit2/ui/rotation_widget.ui

### 2015-10-01
- **Move modifier condition to ViewAction.matchModifiers, handle modifiers==None as "any"** [`f5c860f`]
  TrackingMouseAction now has "any" modifiers.
  **Files changed:** src/mcedit2/worldview/viewaction.py, src/mcedit2/worldview/worldview.py

### 2015-10-01
- **Refactor BoxHandle in preparation of making it movable.** [`dd195c3`]
  **Files changed:** src/mcedit2/handles/boxhandle.py

### 2015-10-01
- **Add RotationTransform, a proxy dimension that rotates blocks.** [`4015ec0`]
  Blocks are rotated as their sections are accessed, making this proxy responsive for live editing.
  **Files changed:** src/mceditlib/test/transform_test.py, src/mceditlib/transform.py

### 2015-10-01
- **TextureAtlas can handle worlds without filenames** [`c0e403e`]
  **Files changed:** src/mcedit2/rendering/textureatlas.py

### 2015-10-01
- **ChunkUpdate.areaLights returns an appropriately-sized array for lights** [`257cd3f`]
  ... when the level in question has no light arrays.
  **Files changed:** src/mcedit2/rendering/chunkupdate.py

### 2015-10-01
- **displaySchematic updates as chunks are loaded instead of preloading chunks** [`50c441f`]
  **Files changed:** src/mcedit2/worldview/schematic_worldview.py

### 2015-10-01
- **displaySchematic accepts either a schematic or a dimension** [`bc70ff8`]
  **Files changed:** src/mcedit2/worldview/schematic_worldview.py

### 2015-10-01
- **WorldView.__str__ can handle dimensions without filenames or dimension names.** [`b35e61a`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-10-01
- **WorldEditor.importSchematic[Iter] now accepts either a schematic or a dimension** [`ee699a1`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-09-29
- **Create a SchematicWorldView and a displaySchematic function** [`e814841`]
  SchematicWorldView is a world view variant with specialized controls for orbiting a world from a fixed distance and center point, and zooming in and out on this world.
  **Files changed:** displaySchematic can be used, even from non-GUI code, to open a window displaying a single world., src/mcedit2/worldview/camera.py, src/mcedit2/worldview/schematic_worldview.py, src/mcedit2/worldview/worldview.py

### 2015-09-28
- **Fix logic for deciding if a cell needs a light update.** [`bcbf61f`]
  When a light-emitting block is replaced with one that emits less light, and the light drawn into the block from neighbors is greater than the light emitted by the new block, the drawn light should be considered the new light rather than the block's brightness.
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-09-28
- **Collect more stats in relight/with_cython and add some comments** [`eb6facc`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-09-28
- **Cache absent sections' coords in RelightCtx and handle ValueError from uncreatable sections.** [`7c58091`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-09-28
- **Add more logging info to block_copy relights, and skip empty lists** [`16d3aa1`]
  **Files changed:** src/mceditlib/block_copy.py

### 2015-09-28
- **Skip SkyLight update for Nether and End dimensions** [`c162faa`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx, src/mceditlib/worldeditor.py

### 2015-09-28
- **Kill dead code in relight_test.py** [`32c1c44`]
  **Files changed:** src/mceditlib/test/relight_test.py

### 2015-09-28
- **Better handling of named/unknown BlockTypeSets in SchematicFileAdapter** [`a816937`]
  **Files changed:** src/mceditlib/schematic.py

### 2015-09-23
- **Demote lightmap logger to DEBUG** [`41d5214`]
  **Files changed:** src/mcedit2/rendering/lightmap.py

### 2015-09-22
- **Rework test suite to use pytest fixtures in conftest.py** [`9ef15e0`]
  **Files changed:** src/mceditlib/bench/time_storagechain.py, src/mceditlib/test/anvil_test.py, src/mceditlib/test/cache_test.py, src/mceditlib/test/conftest.py, src/mceditlib/test/editing_test.py, src/mceditlib/test/nbt_test.py, src/mceditlib/test/relight_test.py, src/mceditlib/test/revisionhistory_test.py, src/mceditlib/test/schematic_test.py, src/mceditlib/test/server_test.py, src/mceditlib/test/templevel.py

### 2015-09-22
- **Add report options for py.test** [`fd98d50`]
  **Files changed:** setup.cfg

### 2015-09-21
- **Add Quit button to error dialog** [`45c5e71`]
  **Files changed:** src/mcedit2/dialogs/error_dialog.py, src/mcedit2/ui/error_dialog.ui

### 2015-09-21
- **Implement "Restart MCEdit" button on error dialog** [`8ccc717`]
  **Files changed:** src/mcedit2/dialogs/error_dialog.py

### 2015-09-20
- **Fix misplaced import in main.py** [`a4106ad`]
  This was causing OpenGL.GL to be loaded too early
  **Files changed:** src/mcedit2/main.py

### 2015-09-17
- **Cleanup** [`c1d6484`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-09-17
- **Error reporting dialog can (finally) upload error reports to Pastebin.** [`39a113d`]
  **Files changed:** requirements.txt, src/mcedit2/dialogs/error_dialog.py, src/mcedit2/ui/error_dialog.ui

### 2015-09-17
- **centerWidgetInScreen now centers the widget on the screen containing its parent widget.** [`e11787a`]
  **Files changed:** src/mcedit2/util/screen.py

### 2015-09-17
- **Show error reporting dialog on all unhandled exceptions.** [`abcc812`]
  **Files changed:** src/mcedit2/main.py

### 2015-09-17
- **Put ShapeWidget in a neat GroupBox with the shape's name in the caption.** [`83cf434`]
  **Files changed:** src/mcedit2/editortools/brush/shapes.py, src/mcedit2/ui/editortools/brush.ui, src/mcedit2/widgets/shapewidget.py

### 2015-09-17
- **Add brush shape icons** [`4758e6f`]
  **Files changed:** src/mcedit2/assets/mcedit2/icons/shapes/chunk.png, src/mcedit2/assets/mcedit2/icons/shapes/cylinder.png, src/mcedit2/assets/mcedit2/icons/shapes/diamond.png, src/mcedit2/assets/mcedit2/icons/shapes/parabolic_dome.png, src/mcedit2/assets/mcedit2/icons/shapes/round.png, src/mcedit2/assets/mcedit2/icons/shapes/square.png, src/mcedit2/assets_raw/icons.svg, src/mcedit2/editortools/brush/shapes.py

### 2015-09-16
- **Use QSignalMapper instead of function closures for inventory slots.** [`29c9609`]
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2015-09-16
- **showProgress no longer shows immediately and no longer processes events** [`17d7afa`]
  Not processing events means "Cancel" is broken, but it was already broken anyway.
  **Files changed:** Processing events before the modal dialog is shown can cause edits to occur while the level is saved. (Oops.), src/mcedit2/util/showprogress.py

### 2015-09-16
- **Handle invalid meta values when getting item names** [`779c84a`]
  A warning is emitted and a placeholder name is returned.
  **Files changed:** src/mceditlib/blocktypes/itemtypes.py

### 2015-09-16
- **Inventory editor now allows items to be dragged from the item list** [`bfeb5c7`]
  **Files changed:** src/mcedit2/library.py, src/mcedit2/util/mimeformats.py, src/mcedit2/widgets/inventory.py, src/mcedit2/widgets/itemtype_list.py

### 2015-09-16
- **Cleanup** [`0775308`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mceditlib/relight/__init__.py, src/mceditlib/selection/__init__.py

### 2015-09-16
- **Touch up history icon** [`0bf29a7`]
  **Files changed:** src/mcedit2/assets/mcedit2/icons/history.png, src/mcedit2/assets_raw/icons.svg

### 2015-09-16
- **Add create argument to getChunks** [`78ce512`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-09-15
- **Add option to copyBlocks for replacing unknown blocks with a specific block ID** [`eaff7ef`]
  **Files changed:** src/mceditlib/block_copy.py, src/mceditlib/blocktypes/__init__.py, src/mceditlib/worldeditor.py

### 2015-09-15
- **Fix brush mode always resetting to "Biome"** [`9967550`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py

### 2015-09-15
- **Brutal solution to making sure EditorSession gets dealloc'd.** [`6690a1c`]
  Brutal.
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py

### 2015-09-15
- **Make some more dockwidgets fade to transparent** [`a658f2f`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py

### 2015-09-15
- **DON'T EVER capture `self` in a closure like this!** [`047978e`]
  When a Qt signal is connected to a function that closes over any references, the GC can't ever detect this cycle: self -> some QObject -> Signal handler wrapper -> function with closure -> self.
  **Files changed:** ALWAYS use QSignalMapper instead of doing this crap!, src/mcedit2/editorsession.py

### 2015-09-15
- **Touch up some more icons.** [`8f48191`]
  **Files changed:** src/mcedit2/assets/mcedit2/icons/edit_player.png, src/mcedit2/assets/mcedit2/toolicons/edit_entity.png, src/mcedit2/assets_raw/icons.svg

### 2015-09-15
- **Version/Resource Pack buttons reorganize when toolbar labels are off.** [`dbb9f58`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py

### 2015-09-15
- **Remove logger.** [`e9ec1e7`]
  **Files changed:** src/mcedit2/widgets/mcedockwidget.py

### 2015-09-14
- **Add some new icons, touch up some existing icons** [`9da20b1`]
  **Files changed:** src/mcedit2/assets/mcedit2/icons/edit_map.png, src/mcedit2/assets/mcedit2/icons/edit_worldinfo.png, src/mcedit2/assets/mcedit2/icons/library.png, src/mcedit2/assets/mcedit2/toolicons/edit_block.png, src/mcedit2/assets/mcedit2/toolicons/edit_chunk.png, src/mcedit2/assets_raw/icons.svg, src/mcedit2/editorapp.py, src/mcedit2/panels/map.py

### 2015-09-14
- **MCEDockWidget has an optional fade in/out when mouse enters/leaves.** [`bde6ab2`]
  **Files changed:** src/mcedit2/widgets/mcedockwidget.py

### 2015-09-14
- **Don't show debug windows in the panels toolbar.** [`b6dc6ff`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-09-14
- **Create custom QDockWidget subclass** [`01bb815`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorcommands/find_replace.py, src/mcedit2/editorsession.py, src/mcedit2/widgets/mcedockwidget.py

### 2015-09-14
- **Add icons for "Toolbar Text" and "History"** [`affdddf`]
  **Files changed:** src/mcedit2/assets/mcedit2/icons/history.png, src/mcedit2/assets/mcedit2/icons/toolbar_text.png, src/mcedit2/assets_raw/icons.svg, src/mcedit2/editorapp.py

### 2015-09-14
- **Changing the time of day also changes the sky color.** [`0d49345`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/worldview/worldview.py

### 2015-09-14
- **Add setDayTime function to SkyNode** [`b236de9`]
  TODO: Stars?
  **Files changed:** src/mcedit2/rendering/sky.py

### 2015-09-14
- **NBT edits only create edit commands when the value is actually changed.** [`dfe7c2f`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2015-09-14
- **Fix chunk inspector widgets causing edit commands on load.** [`659826b`]
  **Files changed:** src/mcedit2/widgets/inspector/__init__.py

### 2015-09-14
- **Numpy warning: Fix float division result used for shape of unpacked data.** [`3f32fe0`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-09-14
- **Add button to toggle toolbar text** [`c804a5e`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-09-14
- **Changing resource pack/minecraft version displays a (static) progress window.** [`48e7116`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-09-14
- **Numpy warning: Explicitly use 'unsafe' casting when scaling uint8 colors.** [`0d5a50e`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/lowdetail.py

### 2015-09-14
- **Numpy warning: Fix float result of division used for array shape** [`fc4f89d`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entitymesh.py

### 2015-09-14
- **Capture -W warnings to logging module** [`1ef0e6c`]
  **Files changed:** src/mcedit2/main.py

### 2015-09-14
- **Pin numpy version to <1.10.0** [`2d4df57`]
  Numpy 1.10 changes casting rules for in-place operations, and I don't feel like adapting to that yet.
  **Files changed:** requirements.txt

### 2015-09-14
- **Fix typo in drawBox** [`cb7f7f6`]
  **Files changed:** src/mcedit2/rendering/cubes.py

### 2015-09-14
- **Remove usage of glPushClientAttrib** [`9b770c2`]
  **Files changed:** src/mcedit2/rendering/cubes.py, src/mcedit2/rendering/loadablechunks.py, src/mcedit2/rendering/sky.py, src/mcedit2/util/glutils.py

### 2015-09-10
- **Brush modes are now instantiated by BrushTool instead of globally.** [`3526f6c`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/brush/modes.py

### 2015-09-10
- **Cleanup** [`2a290d3`]
  **Files changed:** src/mcedit2/editortools/clone.py, src/mcedit2/editortools/move.py

### 2015-09-10
- **Added repeat count to Clone tool** [`e1a6c51`]
  **Files changed:** src/mcedit2/editortools/clone.py

### 2015-09-10
- **showProgress is now able to combine multiple iterable tasks into one progress bar** [`10ce774`]
  **Files changed:** src/mcedit2/util/showprogress.py

### 2015-09-10
- **rescaleProgress now deals with two-element and non-tuple yields** [`c7b009b`]
  **Files changed:** src/mceditlib/util/progress.py

### 2015-09-10
- **Move rescaleProgress+enumProgress to mceditlib.util.progress** [`800ab23`]
  **Files changed:** src/mceditlib/revisionhistory.py, src/mceditlib/util/progress.py

### 2015-09-10
- **Use updateView() convenience function in EditorSession** [`084613e`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-09-10
- **Fix translucent blocks below column height not updating skylight level.** [`35d1f13`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-09-10
- **Fix typo in node.removeParent** [`29a921d`]
  **Files changed:** src/mcedit2/rendering/scenegraph/rendernode.py, src/mcedit2/rendering/scenegraph/scenenode.py

### 2015-09-10
- **Change SceneNode/RenderNode to support multiple parents.** [`67a0031`]
  This allows the same node to appear multiple times in the graph.
  **Files changed:** src/mcedit2/rendering/scenegraph/rendernode.py, src/mcedit2/rendering/scenegraph/scenenode.py

### 2015-09-10
- **Add clone tool icon** [`66a2222`]
  **Files changed:** src/mcedit2/assets/mcedit2/toolicons/clone.png, src/mcedit2/assets_raw/icons.svg, src/mcedit2/editortools/clone.py

### 2015-09-10
- **Double SpinSlider has a smaller singleStep** [`41da9d2`]
  **Files changed:** src/mcedit2/widgets/spinslider.py

### 2015-09-10
- **Change Brightness slider to use the 'gamma' argument to generateLightmap** [`ce5ea42`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/rendering/lightmap.py, src/mcedit2/rendering/textureatlas.py

### 2015-09-10
- **Cleanup in Move tool** [`8a5bcd6`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-09-10
- **Absolutely terrible first draft of Clone tool.** [`fcdc743`]
  It is a clone of the Move tool without the multiple imports and without clearing the area after copying.
  **Files changed:** src/mcedit2/editortools/__init__.py, src/mcedit2/editortools/clone.py

### 2015-09-09
- **Add info to logger in FillBlocksOperation** [`b16918b`]
  **Files changed:** src/mceditlib/operations/block_fill.py

### 2015-09-09
- **Update HeightMap using actual block opacity, and drop height correctly.** [`49a2fd5`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-09-09
- **Add note to resourcePath** [`2484610`]
  **Files changed:** src/mcedit2/util/resources.py

### 2015-09-09
- **Simplify expression in MoveFinishCommand** [`c83382e`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-09-09
- **Extract CoordinateWidget to its own file** [`8d7c5e8`]
  **Files changed:** src/mcedit2/editortools/move.py, src/mcedit2/widgets/coord_widget.py

### 2015-09-09
- **Use try...finally in SimpleRevisionCommand** [`85972c7`]
  **Files changed:** src/mcedit2/command.py

### 2015-09-09
- **Reformat** [`71503ba`]
  **Files changed:** src/mcedit2/rendering/renderstates.py

### 2015-09-09
- **Add layer for rendering stored HeightMaps** [`9ab9d12`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/heightlevel.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/layers.py, src/mcedit2/rendering/renderstates.py

### 2015-09-09
- **Not all view layers are enabled on first run.** [`4c8b548`]
  View layer toggles now respect DefaultVisibleLayers.
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-09-08
- **Adjust appearance of Version/ResourcePack buttons.** [`ef5fa31`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py

### 2015-09-08
- **Copy-paste no longer clears previous selection.** [`daf729e`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/move.py

### 2015-09-08
- **Move tool no longer makes a copy immediately.** [`6674746`]
  Now it creates a reference to the area to be moved and renders that instead.
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/move.py

### 2015-09-08
- **SceneUpdateTask now considers the worldScene's bounds when accepting/rejecting chunks** [`555b316`]
  **Files changed:** src/mcedit2/rendering/worldscene.py

### 2015-09-08
- **WorldLoader accepts an optional list of chunks to load** [`3a57a77`]
  **Files changed:** src/mcedit2/util/worldloader.py

### 2015-09-07
- **Add logger for settings change, don't call setValue if no change.** [`9f571d2`]
  **Files changed:** src/mcedit2/util/settings.py

### 2015-09-07
- **Molest the logging module to make string formatting safer for unicode strings.** [`92265cd`]
  **Files changed:** src/mcedit2/main.py

### 2015-09-07
- **Fix first change of settings value not triggering setting-changed signal.** [`7c8d2d3`]
  The new value was mistakenly used as the default value.
  **Files changed:** src/mcedit2/util/settings.py

### 2015-09-06
- **Remove useless glGenerateMipmap check** [`5614e10`]
  **Files changed:** src/mcedit2/rendering/textureatlas.py

### 2015-09-07
- **Merge pull request #154 from vorburger/patch-1** [`e89e69e`]
  README.md Linux build instructions updated

### 2015-09-07
- **README.md Linux build instructions updated** [`7cfb44d`]
  Thank you guys for MCEdit - I was exploring it for use with kids for http://blog.tinkercad.com/2013/08/15/tinkercraft/
  **Files changed:** README.md

### 2015-09-06
- **Workaround for OverflowError** [`ffcbc3d`]
  OverflowError results from Python `long` not converting to `QVariant` correctly.
  **Files changed:** Pass TAG_Long values through Qt models as `str` (eww)., src/mcedit2/widgets/nbttree/nbteditor.py, src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2015-09-06
- **Remove implicit texture loading in Texture.bind()** [`6ccd462`]
  Loading a texture during bind() may cause the glTexImage commands to be compiled into a display list. Not a great idea.
  **Files changed:** src/mcedit2/rendering/compass.py, src/mcedit2/rendering/scenegraph/bind_texture.py, src/mcedit2/util/glutils.py

### 2015-09-06
- **BindTextureNode once again resets GL_TEXTURE matrix** [`ca0dbc0`]
  **Files changed:** src/mcedit2/rendering/scenegraph/bind_texture.py

### 2015-09-06
- **Overhaul glutils.Texture** [`63dfb0d`]
  Texture no longer has a textureFunc callback. Instead, it has image, width, and height attributes.
  **Files changed:** Texture no longer calls glGenTexture on init; instead, this is deferred until load., Texture gains a 'name' attribute, mostly used for logging., TextureAtlas._lightTexture is now reloaded whenever TextureAtlas.dayTime or TextureAtlas.minBrightness is changed., This commit does too many things and I will probably be punished for it., src/mcedit2/rendering/loadablechunks.py, src/mcedit2/rendering/textureatlas.py, src/mcedit2/rendering/worldscene.py, src/mcedit2/util/glutils.py, src/mcedit2/util/load_png.py, src/mcedit2/worldview/worldview.py

### 2015-09-06
- **Fix areaLights getting the wrong above/below sections.** [`9bc4a2f`]
  **Files changed:** src/mcedit2/rendering/chunkupdate.py

### 2015-09-06
- **Fix blocklight/skylight values for fluid renderers** [`d8a834c`]
  **Files changed:** src/mcedit2/rendering/modelmesh.pyx

### 2015-09-06
- **Avoid OverflowError in WorldListItemDelegate** [`c2f46ee`]
  OverflowError is caused by passing a namedtuple containing a `long` value through the PySide binding for QModelIndex.data. Only occurs on Linux, apparently.
  **Files changed:** Work around by calling WorldListModel.data directly., src/mcedit2/worldlist.py

### 2015-09-06
- **Move a profiler logger to DEBUG level** [`edcc085`]
  **Files changed:** src/mcedit2/util/profiler.py

### 2015-09-06
- **User data folder is no longer found relative to sys.argv[0]** [`bb0e7b1`]
  For source checkouts from git, the data folder is in the checkout folder. Otherwise, it is in the user's home folder.
  **Files changed:** src/mcedit2/util/directories/mac.py, src/mcedit2/util/directories/posix.py, src/mcedit2/util/directories/win32.py, src/mcedit2/util/resources.py

### 2015-09-05
- **Pin some requirements.** [`fc9c8b8`]
  These two both moved ahead and became incompatible with each other, and IPython 4 is incompatible with MCEdit.
  **Files changed:** requirements.txt

### 2015-09-05
- **Suppress a logger in skylight update** [`ab538a3`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-09-05
- **Clean up lightmap texture generating code** [`966aa9f`]
  **Files changed:** src/mcedit2/rendering/lightmap.py

### 2015-09-05
- **View switching toolbar now has sliders for time-of-day and minimum brightness** [`b586f5b`]
  These will modify the texture image for the block and sky lighting
  **Files changed:** src/mcedit2/editorsession.py

### 2015-09-05
- **SpinSlider now accepts floating-point values (mainly those between 0.0 and 1.0)** [`31b411b`]
  **Files changed:** src/mcedit2/widgets/spinslider.py

### 2015-09-05
- **Make custom traceback print_list compatible with standard tracebacks** [`0cb359f`]
  **Files changed:** src/mcedit2/util/custom_traceback.py

### 2015-09-05
- **'-debug' argument is no longer forwarded to OptionParser** [`ad301d7`]
  **Files changed:** src/mcedit2/main.py

### 2015-09-05
- **Biome renderer is now compatible with non-Biomes levels** [`fe50e3f`]
  **Files changed:** src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/modelmesh.pyx, src/mceditlib/fakechunklevel.py

### 2015-09-05
- **copyBlocks now defaults to the "all" lighting update scheme** [`8ac3afb`]
  **Files changed:** src/mceditlib/block_copy.py, src/mceditlib/worldeditor.py

### 2015-09-05
- **Minor rename and refactor in copyBlocksIter** [`f7bed06`]
  **Files changed:** src/mceditlib/block_copy.py

### 2015-09-05
- **Heightmap update doesn't cache old heightmap, and scans entire columns** [`f13de9c`]
  When the height drops, it scans the entire column to find the new height. Instead, it could only scan the portion of the column changed in the given coordinates, but I'm lazy.
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-09-05
- **Fix wrong index order when selecting lighting updates during copy** [`703a9ec`]
  **Files changed:** src/mceditlib/block_copy.py

### 2015-09-05
- **AnvilSection fills SkyLight with 15** [`3689f7b`]
  Assumes that sections are created naturally from bottom to top with no gaps
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-09-05
- **copyBlocksIter yields progress info for relight operation** [`f463e8d`]
  **Files changed:** src/mceditlib/block_copy.py

### 2015-09-05
- **updateLightsByCoord now respects hasLights attribute of dimension** [`f046a1e`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx, src/mceditlib/worldeditor.py

### 2015-09-04
- **Fix swapped blocklight and skylight in modelmesh** [`21a7195`]
  **Files changed:** src/mcedit2/rendering/modelmesh.pyx

### 2015-09-04
- **Decent, yet slow attempt at updating SkyLight and HeightMap.** [`304329a`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-09-04
- **Add some not-so-useless junk back into validateWidgetQGLContext** [`301f178`]
  **Files changed:** src/mcedit2/util/qglcontext.py

### 2015-09-02
- **Fix some mis-named, forwarded argument names to match the actual function call** [`35419ca`]
  **Files changed:** src/mcedit2/worldview/camera.py, src/mcedit2/worldview/fourup.py, src/mcedit2/worldview/overhead.py

### 2015-09-02
- **Remove some useless junk from validateWidgetQGLContext** [`8bc0458`]
  **Files changed:** src/mcedit2/util/qglcontext.py

### 2015-09-02
- **Initialize some attributes earlier so we can str() the widget from inside validateWidgetQGLContext (if needed)** [`cadf29c`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-09-02
- **Make specfile compatible with PyInstaller 2+3** [`af9b2c3`]
  **Files changed:** mcedit2.spec

### 2015-09-01
- **Add a getWorldInfo method to WorldEditor** [`6c425d6`]
  This allows the WorldList to get summary info for each world without loading it and parsing its blocktypes, etc
  **Files changed:** src/mcedit2/worldlist.py, src/mceditlib/anvil/adapter.py, src/mceditlib/findadapter.py, src/mceditlib/util/__init__.py, src/mceditlib/worldeditor.py

### 2015-09-01
- **Add minecraftinstall option to show snapshots (i.e. versions we can't parse)** [`1a11979`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2015-09-01
- **WorldListWidget no longer creates a texture atlas nor loads block models.** [`4edb129`]
  **Files changed:** src/mcedit2/rendering/worldscene.py, src/mcedit2/worldlist.py, src/mcedit2/worldview/worldview.py

### 2015-08-31
- **Center and rescale map panel when shown.** [`0f2ef1f`]
  **Files changed:** src/mcedit2/panels/map.py

### 2015-08-30
- **Add toolbar buttons to change MC version and resource pack.** [`3d61d7b`]
  TODO: Reconsider the global settings for MC version and resource pack...
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py, src/mcedit2/util/minecraftinstall.py

### 2015-08-30
- **EditorSession is now responsible for creating its own ResourceLoader** [`d011eb8`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py

### 2015-08-30
- **Move getResourceLoaderForFilename to minecraftinstall.py** [`3c3e029`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/util/minecraftinstall.py, src/mcedit2/worldlist.py

### 2015-08-30
- **Add cameraVector property to CutawayWorldView** [`801c122`]
  **Files changed:** src/mcedit2/worldview/cutaway.py

### 2015-08-22
- **Add custom editor widget for TAG_Long tags in NBT Editor.** [`73447be`]
  Should hopefully solve OverflowError caused by coercing a TAG_Long's value to int.
  **Files changed:** src/mcedit2/widgets/nbttree/nbteditor.py, src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2015-08-20
- **Fix var decl ordering for cython 0.20** [`95413d2`]
  cython 0.20 is for Ubuntu 14.04
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mceditlib/relight/with_cython.pyx

### 2015-08-20
- **Attempt to fix weird QGLContext bug by holding a reference to the QGLContext** [`e3a785e`]
  **Files changed:** src/mcedit2/util/qglcontext.py, src/mcedit2/worldview/worldview.py

### 2015-08-19
- **Add shulker model for MC 1.9** [`481eb0f`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entity/models.py, src/mcedit2/rendering/chunkmeshes/entity/shulker.py

### 2015-08-19
- **Handle missing 'variants' in blockstates json** [`75d229a`]
  json may have 'multipart' instead. Handle this!!
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-08-19
- **Handle entity not found when zooming to entity** [`f32212b`]
  **Files changed:** src/mcedit2/editorcommands/find_replace.py

### 2015-08-19
- **Tweak boundingbox for getting entity from find results.** [`caa1ee2`]
  Need a better way to get entity by UUID...
  **Files changed:** src/mcedit2/editorcommands/find_replace.py

### 2015-08-19
- **Move data collection to mcedit2.spec. Remove hook-mcedit2.py.** [`e5b9c67`]
  Specfile update for PyInstaller 3
  **Files changed:** hook-mcedit2.py, mcedit2.spec

### 2015-07-29
- **Rename "Edit Chunk" to "Inspect Chunk" and move most of its code to inspector** [`4cdf7cf`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/edit_chunk.py, src/mcedit2/ui/editortools/edit_chunk.ui, src/mcedit2/ui/editortools/select_chunk.ui, src/mcedit2/ui/inspector.ui, src/mcedit2/widgets/inspector/__init__.py

### 2015-07-23
- **Print repr of GL_VENDOR and GL_RENDERER for drivers that return non-ascii strings.** [`8c98350`]
  **Files changed:** src/mcedit2/util/qglcontext.py

### 2015-07-20
- **Embedded profiler now records only samples over the past 10 seconds.** [`b05b923`]
  Makes live profiling more responsive.
  **Files changed:** src/mcedit2/util/profiler.py

### 2015-07-20
- **Some work on a numpy-based raycast method. Not yet used.** [`3b6d6d6`]
  **Files changed:** src/mcedit2/util/raycast.py

### 2015-07-20
- **CONTRIBUTING.md: Link to wiki page on mcedit2 repo.** [`115ee5b`]
  **Files changed:** CONTRIBUTING.md

### 2015-07-19
- **Change BindTextureRenderNode to make fewer GL calls when the texture scale is None.** [`8fadb2b`]
  **Files changed:** src/mcedit2/rendering/scenegraph/bind_texture.py

### 2015-07-19
- **Document createRenderNode, updateRenderNode, and updateChildren to make intentions more clear.** [`5125fdf`]
  Change updateChildren to be non-recursive.
  **Files changed:** updateRenderNode now descends into children and calls updateChildren as needed., The rendergraph is now slightly less creepy., src/mcedit2/rendering/scenegraph/rendernode.py, src/mcedit2/rendering/scenegraph/scenenode.py

### 2015-07-19
- **Stop rendering rainbow creepers for unknown entities.** [`f66e2a8`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entitymesh.py

### 2015-07-19
- **Skip blank itemframes.** [`544214e`]
  This may be done improperly. Accessing ref.Item may create an empty compound, and I haven't checked if blank frames have an empty compound for Item or not.
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entitymesh.py

### 2015-07-19
- **Add Chest and Large Chest models** [`5b963e6`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entity/chest.py, src/mcedit2/rendering/chunkmeshes/entity/models.py, src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/chunkupdate.py

### 2015-07-19
- **Add ScaleRenderNode** [`f32c8b1`]
  **Files changed:** src/mcedit2/rendering/scenegraph/matrix.py

### 2015-07-19
- **Remove wonky block model for chests** [`63737e8`]
  **Files changed:** src/mceditlib/blocktypes/minecraft.json

### 2015-07-18
- **Fix configured block models not being used.** [`bfae698`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-07-18
- **Add armor stand model (with extra arms!)** [`48dd2b2`]
  That's why they call it an arm-or stand.
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entity/armorstand.py, src/mcedit2/rendering/chunkmeshes/entity/models.py

### 2015-07-17
- **Change docs to alabaster theme, skip Qt staticMetaObjects** [`4db059f`]
  Add github user/repo for theme purposes
  **Files changed:** More mceditlib->mcedit2, doc/conf.py, doc/index.rst

### 2015-07-17
- **Change NBTAttrs a bit so sphinx documents them quietly** [`5b25e95`]
  Both of these changes make them more like the builtin property()
  **Files changed:** NBTAttr access on classes returns self, so sphinx can document the class, NBTAttr constructors take a docstring argument and replace the instance's doc so sphinx doesn't repeat NBTAttr's doc everywhere, src/mceditlib/nbtattr.py

### 2015-07-17
- **Add getActualBlockState rules for doors and redstone** [`c7a19c4`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pxd, src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx

### 2015-07-17
- **Add target to doc/Makefile for running sphinx-apidoc** [`697fa78`]
  Replace 'mceditlib' with 'mcedit2' in doc info
  **Files changed:** doc/Makefile, doc/apidoc/mcedit2.dialogs.rst, doc/apidoc/mcedit2.editorcommands.rst, doc/apidoc/mcedit2.editortools.brush.rst, doc/apidoc/mcedit2.editortools.rst, doc/apidoc/mcedit2.handles.rst, doc/apidoc/mcedit2.panels.rst, doc/apidoc/mcedit2.rendering.chunkmeshes.entity.rst, doc/apidoc/mcedit2.rendering.chunkmeshes.rst, doc/apidoc/mcedit2.rendering.rst, doc/apidoc/mcedit2.rendering.scenegraph.rst, doc/apidoc/mcedit2.rst, doc/apidoc/mcedit2.synth.rst, doc/apidoc/mcedit2.util.directories.rst, doc/apidoc/mcedit2.util.rst, doc/apidoc/mcedit2.widgets.inspector.rst, doc/apidoc/mcedit2.widgets.inspector.tileentities.rst, doc/apidoc/mcedit2.widgets.nbttree.rst, doc/apidoc/mcedit2.widgets.rst, doc/apidoc/mcedit2.worldview.rst, doc/apidoc/mceditlib.anvil.rst, doc/apidoc/mceditlib.blocktypes.rst, doc/apidoc/mceditlib.operations.rst, doc/apidoc/mceditlib.pc.rst, doc/apidoc/mceditlib.relight.rst, doc/apidoc/mceditlib.rst, doc/apidoc/mceditlib.selection.rst, doc/apidoc/mceditlib.util.rst, doc/apidoc/modules.rst, doc/conf.py, doc/index.rst, doc/mcedit2.editortools.brush.rst, doc/mcedit2.panels.rst, doc/mcedit2.prefs.rst, doc/mcedit2.ui.rst, doc/mceditlib.blocktypes.rst, doc/mceditlib.test.rst, doc/mceditlib.util.rst

### 2015-07-17
- **Allow blockStatesByResourcePathVariant to have multiple entries for a path,variant pair as intended** [`1649dcf`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-07-16
- **Add a special case to preserve the color of stained glass when rendering** [`cd2d6b7`]
  **Files changed:** src/mcedit2/rendering/modelmesh.pyx

### 2015-07-16
- **Fix all issues related to improperly rotated, lit, and culled models that use variant rotation** [`6203847`]
  Buttons, levers, quartz pillars and others are now oriented, lit, and culled correctly
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-07-16
- **Removed variantZrot, which never appears in the variant files.** [`e018234`]
  I feel dumb.
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/widgets/configureblocksdialog.py, src/mceditlib/blocktypes/__init__.py

### 2015-07-16
- **Set default blockstate of unknowns to ''** [`559555c`]
  **Files changed:** src/mceditlib/blocktypes/__init__.py

### 2015-07-16
- **Fix zero-length arrays appearing in setBlocks** [`09879c1`]
  **Files changed:** src/mceditlib/multi_block.py

### 2015-07-16
- **time_getsetblocks is working again and produces fairer results** [`c827444`]
  **Files changed:** src/mceditlib/bench/time_getsetblocks.py

### 2015-07-15
- **Add `getActualBlockState` rules for fences and panes/bars.** [`12f93e8`]
  This method is done with Python and is very slow.
  **Files changed:** src/mcedit2/rendering/modelmesh.pyx

### 2015-07-15
- **blockmodels.pyx: cookedModelsByBlockState keys are now split into components** [`47ee219`]
  Splitting the blockState into properties and sorting them makes property order no longer matter.
  **Files changed:** Also, all models are added into cookedModelsByBlockState and not just those for hidden states. Soon, I should be able to remove resourcePath and resourceVariant from the base block data dump and only keep them in the states dump., blockStatesByResourcePathVariant value elements are also split into internalName and blockState, src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx

### 2015-07-15
- **Update raw data dump: Remove unused material* fields, add materialName field, remove duplicate renderType field** [`e598265`]
  **Files changed:** src/mceditlib/blocktypes/minecraft_raw.json

### 2015-07-15
- **Don't duplicate code from blocktypes and also don't get it completely wrong** [`9ce23e8`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-07-15
- **Hidden block states are stashed in cookedModelsByBlockState** [`5037655`]
  getActualBlockState rule written for grass with snow on top.
  **Files changed:** src/mcedit2/rendering/blockmodels.pxd, src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx

### 2015-07-15
- **Load "hidden" blockstates from a json file.** [`4263b18`]
  These new models are cooked and then thrown away as there is nowhere to put them! :(
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/minecraft_hiddenstates_raw.json, src/mceditlib/blocktypes/__init__.py

### 2015-07-15
- **Store uncooked models with model variants separate from blockstates** [`e65817b`]
  Uncooked models are stored in quadsByResourcePathVariant {(path, variant): quads}
  **Files changed:** blockState mapping is stored in blockStatesByResourcePathVariant {(path, variant): [nameAndState]}, This allows us to skip cooking models twice when one model (path, variant) is used for more than one blockState, src/mcedit2/rendering/blockmodels.pxd, src/mcedit2/rendering/blockmodels.pyx

### 2015-07-15
- **Create dataDir on Mac and Linux** [`79963a5`]
  **Files changed:** src/mcedit2/util/directories/mac.py, src/mcedit2/util/directories/posix.py

### 2015-07-15
- **Add special cases for face culling for Slabs and other blocks** [`68cfbc4`]
  Also includes leaves with fancyGraphics=True, which is just asserted to be True for now...
  **Files changed:** src/mcedit2/rendering/modelmesh.pyx

### 2015-07-15
- **Remove unused layers from AllLayers** [`7443e6a`]
  SceneUpdateTask doesn't know if a layer isn't provided by any chunk meshes...
  **Files changed:** src/mcedit2/rendering/layers.py

### 2015-07-14
- **Incredibly brutal fix for blocks (e.g. slabs, stairs) with useNeighborBrightness** [`7c05881`]
  What this flag does is make the block report its brightest neighbor's light as its own for rendering purposes, since these blocks are technically opaque but still expose that face of their neighbors.
  **Files changed:** Next, fix up face culling, src/mcedit2/rendering/chunkupdate.py, src/mceditlib/blocktypes/__init__.py

### 2015-07-14
- **Add /setblock and /testforblock commands** [`79354dd`]
  Refactor some parts of SummonCommand into functions
  **Files changed:** Someday I'll want a parse language or something..., src/mcedit2/util/commandblock.py

### 2015-07-14
- **Rearrange color hash functions, add comments** [`0317532`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entitymesh.py

### 2015-07-14
- **Add color coding to command blocks, split locations from colors** [`f5ddfa7`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/layers.py

### 2015-07-14
- **Add LineWidthNode** [`379ffea`]
  **Files changed:** src/mcedit2/rendering/scenegraph/misc.py

### 2015-07-13
- **Start work on a command parser** [`628c2a8`]
  **Files changed:** src/mcedit2/util/commandblock.py

### 2015-07-13
- **Add command block tile inspector** [`d03d8c9`]
  **Files changed:** src/mcedit2/widgets/inspector/__init__.py, src/mcedit2/widgets/inspector/tileentities/command.py

### 2015-07-13
- **Add Command block entity ref** [`6aca9d8`]
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-07-13
- **registerBlockInspectorWidget expects a tileEntityID attribute instead of an ID argument** [`dce11f8`]
  **Files changed:** src/mcedit2/plugins.py, src/mcedit2/widgets/inspector/__init__.py, src/mcedit2/widgets/inspector/tileentities/chest.py, src/plugins/storagedrawers.py

### 2015-07-13
- **Add demjson.py with modifications for compact command block output** [`912f105`]
  **Files changed:** src/mceditlib/util/demjson.py

### 2015-07-13
- **Add Villager entity model** [`1cae9b6`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entity/modelrenderer.py, src/mcedit2/rendering/chunkmeshes/entity/models.py, src/mcedit2/rendering/chunkmeshes/entity/villager.py, src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mceditlib/anvil/entities.py

### 2015-07-13
- **BindTextureRenderNode is allowed to have texture == None** [`ee730ed`]
  **Files changed:** src/mcedit2/rendering/scenegraph/bind_texture.py

### 2015-07-13
- **Set default value for PCPaintingEntityRefBase.Facing** [`cb90fcb`]
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-07-13
- **Raise ValueError in NBTAttr for missing default value** [`ef7b3d4`]
  **Files changed:** src/mceditlib/nbtattr.py

### 2015-07-13
- **Refactor: Move tile entity inspector widgets under widgets.inspector.tileentity** [`9d2eb9a`]
  **Files changed:** src/mcedit2/widgets/inspector/__init__.py, src/mcedit2/widgets/inspector/tileentities/__init__.py, src/mcedit2/widgets/inspector/tileentities/chest.py, src/plugins/storagedrawers.py

### 2015-07-12
- **Sheep now have wool. Not colored yet.** [`77665d2`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entity/models.py, src/mcedit2/rendering/chunkmeshes/entity/quadruped.py, src/mcedit2/rendering/chunkmeshes/entitymesh.py

### 2015-07-12
- **Properly move an entity model's expected texture size to the models** [`2310a24`]
  Allows high res entity textures and also isn't completely disgusting.
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entity/biped.py, src/mcedit2/rendering/chunkmeshes/entity/creeper.py, src/mcedit2/rendering/chunkmeshes/entity/models.py, src/mcedit2/rendering/chunkmeshes/entity/quadruped.py, src/mcedit2/rendering/chunkmeshes/entity/spider.py, src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/worldscene.py

### 2015-07-12
- **Add cow, pig, sheep models** [`32a09b5`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entity/modelrenderer.py, src/mcedit2/rendering/chunkmeshes/entity/models.py, src/mcedit2/rendering/chunkmeshes/entity/quadruped.py

### 2015-07-12
- **Scenegraph refactor part 3** [`5de1f76`]
  Change fully qualified imports to name imports
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/generate.py, src/mcedit2/editortools/move.py, src/mcedit2/rendering/chunkmeshes/chunksections.py, src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/chunkmeshes/lowdetail.py, src/mcedit2/rendering/chunkmeshes/terrainpop.py, src/mcedit2/rendering/chunkmeshes/tileticks.py, src/mcedit2/rendering/chunknode.py, src/mcedit2/rendering/workplane.py, src/mcedit2/rendering/worldscene.py, src/mcedit2/worldview/worldview.py

### 2015-07-12
- **Scenegraph refactor part 2** [`9f0b337`]
  Move Node types into separate files and keep them with their RenderNodes
  **Files changed:** Eww, fully qualified imports everywhere, src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/generate.py, src/mcedit2/editortools/move.py, src/mcedit2/rendering/chunkmeshes/chunksections.py, src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/chunkmeshes/lowdetail.py, src/mcedit2/rendering/chunkmeshes/terrainpop.py, src/mcedit2/rendering/chunkmeshes/tileticks.py, src/mcedit2/rendering/chunknode.py, src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/rendering/scenegraph/bind_texture.py, src/mcedit2/rendering/scenegraph/depth_test.py, src/mcedit2/rendering/scenegraph/matrix.py, src/mcedit2/rendering/scenegraph/misc.py, src/mcedit2/rendering/scenegraph/rendernode.py, src/mcedit2/rendering/scenegraph/scenenode.py, src/mcedit2/rendering/scenegraph/texture_atlas.py, src/mcedit2/rendering/scenegraph/vertex_array.py, src/mcedit2/rendering/selection.py, src/mcedit2/rendering/workplane.py, src/mcedit2/rendering/worldscene.py, src/mcedit2/synth/l_system.py, src/mcedit2/worldview/worldview.py, src/plugins/hilbert.py

### 2015-07-12
- **Scenegraph refactor part 1** [`d23f575`]
  scenegraph -> scenegraph.scenenode
  **Files changed:** rendergraph -> scenegraph.rendernode, src/mcedit2/editorsession.py, src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/edit_chunk.py, src/mcedit2/editortools/generate.py, src/mcedit2/editortools/move.py, src/mcedit2/editortools/select.py, src/mcedit2/handles/boxhandle.py, src/mcedit2/rendering/chunkmeshes/chunksections.py, src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/chunkmeshes/lowdetail.py, src/mcedit2/rendering/chunkmeshes/terrainpop.py, src/mcedit2/rendering/chunkmeshes/tileticks.py, src/mcedit2/rendering/chunknode.py, src/mcedit2/rendering/compass.py, src/mcedit2/rendering/loadablechunks.py, src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/rendering/renderstates.py, src/mcedit2/rendering/scenegraph/__init__.py, src/mcedit2/rendering/scenegraph/rendernode.py, src/mcedit2/rendering/scenegraph/scenenode.py, src/mcedit2/rendering/selection.py, src/mcedit2/rendering/sky.py, src/mcedit2/rendering/workplane.py, src/mcedit2/rendering/worldscene.py, src/mcedit2/synth/l_system.py, src/mcedit2/util/objgraphwidget.py, src/mcedit2/worldview/cutaway.py, src/mcedit2/worldview/minimap.py, src/mcedit2/worldview/worldview.py, src/plugins/hilbert.py

### 2015-07-11
- **Add a really rough version of an entity renderer.** [`b2eff71`]
  Has an interface similar to Minecraft's internal renderer.
  **Files changed:** Renders Zombies, Skeletons, Spiders, Creepers, and Zombie Pigmen., src/mcedit2/rendering/chunkmeshes/entity/__init__.py, src/mcedit2/rendering/chunkmeshes/entity/biped.py, src/mcedit2/rendering/chunkmeshes/entity/creeper.py, src/mcedit2/rendering/chunkmeshes/entity/modelrenderer.py, src/mcedit2/rendering/chunkmeshes/entity/models.py, src/mcedit2/rendering/chunkmeshes/entity/spider.py, src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/chunkupdate.py

### 2015-07-11
- **Monster bounding boxes are now visible through walls** [`875a5d5`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entitymesh.py

### 2015-07-11
- **Add scale option to BindTextureNode for scaling the texture matrix** [`0822f87`]
  **Files changed:** src/mcedit2/rendering/rendergraph.py, src/mcedit2/rendering/scenegraph.py

### 2015-07-11
- **Add scenegraph nodes for matrix rotate and depth test function.** [`421ae4f`]
  **Files changed:** src/mcedit2/rendering/rendergraph.py, src/mcedit2/rendering/scenegraph.py

### 2015-07-11
- **Add method to SceneUpdateTask to get a model texture.** [`514b315`]
  Uses the ResourceLoader from the texture atlas.
  **Files changed:** Puts the texture size on the texture where the entity model renderer can find it. Which is wrong., Kinda gross., src/mcedit2/rendering/textureatlas.py, src/mcedit2/rendering/worldscene.py

### 2015-07-11
- **Fix face culling for glass/stained glass blocks.** [`eee4b5b`]
  18 more blocks to go!
  **Files changed:** src/mcedit2/rendering/modelmesh.pyx

### 2015-07-11
- **Display red boxes for entities as wireframes** [`725ee72`]
  Added PolygonModeNode
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/rendergraph.py, src/mcedit2/rendering/scenegraph.py

### 2015-07-11
- **WorldView now accepts dropped map items dragged from Library panel** [`fd76076`]
  Map items are placed immediately with no "movable" intermediate.
  **Files changed:** xxx still need placement preview!, and xxx should allow URLs/schematic files/etc to be dropped from Library's Schematic panel, file explorer, etc!, src/mcedit2/editorsession.py, src/mcedit2/worldview/worldview.py

### 2015-07-11
- **Library panel now shows a list of the current session's maps, for dragging and dropping** [`31aec2a`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/library.py, src/mcedit2/ui/library.ui

### 2015-07-11
- **Add mimeformats.py to support drag and drop** [`844049b`]
  **Files changed:** src/mcedit2/util/mimeformats.py

### 2015-07-11
- **Map item frames now render correctly, right-side up and facing the right direction.** [`f127d86`]
  A missing mapTex is now "handled" by omitting the BindTextureNode (should have a placeholder tex)
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entitymesh.py

### 2015-07-11
- **Red entity boxes no longer intersect the floor.** [`e6f7513`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entitymesh.py

### 2015-07-11
- **Add function to translate MCEdit `Face` to Painting/ItemFrame `Facing`** [`2e83d19`]
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-07-11
- **Fix bad default value in Painting.TilePos** [`a84ddb8`]
  xxx make TilePos version aware
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-07-11
- **Error messages: ItemStackRef -> ItemRef** [`bf380cd`]
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-07-11
- **Add rough `createEntity` method to WorldEditor** [`cadcd74`]
  Add creation support to PCEntityRef
  **Files changed:** ItemRef.id now handles an absent `id` tag on newly created ItemRefs, src/mceditlib/anvil/entities.py, src/mceditlib/worldeditor.py

### 2015-07-11
- **SetNBTDefaults now recurses through NBTCompoundAttrs** [`90b4678`]
  **Files changed:** src/mceditlib/nbtattr.py

### 2015-07-11
- **Fix bad default value for Item's 'tag' tag** [`1f4b01e`]
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-07-10
- **Fix typo in createMap** [`5cad086`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-07-10
- **libraryView -> libraryWidget** [`22778a9`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-07-09
- **Add ItemFrameMesh to render maps in item frames.** [`548e214`]
  Added getMapTexture to SceneUpdateTask
  **Files changed:** Added ItemFrames rendering layer, Removed ItemFrame from MonsterRenderer, src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/layers.py, src/mcedit2/rendering/worldscene.py

### 2015-07-09
- **Add PCItemFrameEntityRef and bases, rearrange entities.py** [`2812a41`]
  EntityRef creation is now dispatched to different classes by ID
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-07-09
- **Split ItemRef off of ItemStackRef** [`5579497`]
  **Files changed:** src/mceditlib/anvil/entities.py, src/mceditlib/schematic.py, src/plugins/storagedrawers.py

### 2015-07-09
- **NBTCompoundAttr now parents the CompoundRef it returns to its own CompoundRef** [`3112a27`]
  **Files changed:** src/mceditlib/nbtattr.py

### 2015-07-09
- **AnvilMapData is now an NBTCompoundRef to parent it to the adapter** [`ae8925a`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-07-09
- **Added BindTextureNode** [`52c9dd4`]
  **Files changed:** src/mcedit2/rendering/rendergraph.py, src/mcedit2/rendering/scenegraph.py

### 2015-07-09
- **Fix wall torches being tilted into their attached block** [`1cc058c`]
  Need to check all other models to see what this affected!
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-07-09
- **Import Image as Map now implemented.** [`f46ce88`]
  Removed mapCache from WorldEditor (questionable)
  **Files changed:** createMap ignores idcounts.dat and updates it., Catch LevelFormatErrors while getting map datas., src/mcedit2/panels/map.py, src/mcedit2/ui/import_map.ui, src/mceditlib/anvil/adapter.py, src/mceditlib/worldeditor.py

### 2015-07-09
- **Change "Expand" checkbox to "Stretch Tiles" in map import UI** [`d60ff4c`]
  **Files changed:** src/mcedit2/ui/import_map.ui

### 2015-07-09
- **Display error text in long description** [`926b873`]
  **Files changed:** src/mcedit2/dialogs/error_dialog.py

### 2015-07-09
- **Don't reverse tracebacks** [`740dcb0`]
  **Files changed:** src/mcedit2/util/custom_traceback.py

### 2015-07-08
- **Add an error dialog and use it to show plugin load/unload errors.** [`5c4ab7a`]
  Will be used later for errors in plugin execution and general errors from signal handlers and etc.
  **Files changed:** "Copy to PasteBin" still not implemented., src/mcedit2/dialogs/error_dialog.py, src/mcedit2/dialogs/plugins_dialog.py, src/mcedit2/editorapp.py, src/mcedit2/plugins.py, src/mcedit2/ui/error_dialog.ui, src/mcedit2/util/qglcontext.py

### 2015-07-07
- **Fix duplicate entries in generator types list, add some loggers** [`0584827`]
  **Files changed:** src/mcedit2/editortools/generate.py

### 2015-07-07
- **Fool around with an L-system for drawing Hilbert curves.** [`6bf52bb`]
  **Files changed:** src/mcedit2/synth/l_system_plugin.py, src/plugins/hilbert.py

### 2015-07-07
- **Add a DefaultVisibleLayers for WorldScenes which don't get their visible layers configured by a WorldView** [`72f7bd0`]
  **Files changed:** src/mcedit2/rendering/layers.py, src/mcedit2/rendering/worldscene.py

### 2015-07-06
- **More work on map editor UI.** [`3f260ab`]
  Displays existing maps and the splits for the imported map. Still can't actually import maps or edit them externally.
  **Files changed:** src/mcedit2/panels/map.py, src/mcedit2/ui/import_map.ui, src/mcedit2/ui/panels/map.ui, src/mceditlib/anvil/adapter.py

### 2015-07-05
- **Some nonsense to help debug a WTF error** [`fdd30f3`]
  AttributeError: 'PySide.QtOpenGL.QGLContext' object has no attribute 'setData'
  **Files changed:** src/mcedit2/widgets/log_view.py

### 2015-07-05
- **Begin working on map item editor** [`339a75e`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/panels/map.py, src/mcedit2/ui/panels/map.ui, src/mceditlib/anvil/adapter.py, src/mceditlib/anvil/worldfolder.py, src/mceditlib/revisionhistory.py, src/mceditlib/worldeditor.py

### 2015-07-05
- **NBTFormatError is now a kind of LevelFormatError** [`bc2e24a`]
  **Files changed:** src/mceditlib/nbt.pyx

### 2015-07-05
- **Disable profiling in with_cython.pyx** [`43c4c3c`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-07-05
- **Remove unused var and obsolete comment** [`8142379`]
  **Files changed:** src/mcedit2/util/directories/win32.py, src/mceditlib/schematic.py

### 2015-07-05
- **updateLightsByCoord coerces its coord arrays to ndarray for faster iteration** [`dce1495`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-07-05
- **Platform specific directories now have one module for each platform.** [`d1eda07`]
  Added some notes about install mode and build scripts
  **Files changed:** sys.executable is no longer used., Added getSrcFolder for finding the src/ folder of a source checkout., src/mcedit2/util/directories.py, src/mcedit2/util/directories/__init__.py, src/mcedit2/util/directories/mac.py, src/mcedit2/util/directories/posix.py, src/mcedit2/util/directories/win32.py, src/mcedit2/util/resources.py

### 2015-07-03
- **Experiment with having copyBlocks issue lighting updates only for blocks whose opacity or brightness changed.** [`1e4ae2e`]
  copyBlocks accepts more values for updateLights
  **Files changed:** time_relight_manmade has another option to select the scheme of issuing updates, Add some tests results, conclusions, and blabber to time_relight_manmade, src/mceditlib/bench/time_relight_manmade.py, src/mceditlib/block_copy.py, src/mceditlib/worldeditor.py

### 2015-06-30
- **setLight doesn't dirty the chunk if no section was found/created.** [`12e0ff3`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-06-30
- **Same tweaks for block_copy output** [`b5a8148`]
  **Files changed:** src/mceditlib/block_copy.py

### 2015-06-30
- **Tweak benchmark output** [`d85a6f9`]
  **Files changed:** src/mceditlib/bench/time_relight_manmade.py, src/mceditlib/bench/time_relight_natural.py

### 2015-06-30
- **Fix a really stupid bug in the relight benchmark.** [`2509b7e`]
  **Files changed:** src/mceditlib/bench/time_relight_manmade.py, src/mceditlib/bench/time_relight_natural.py

### 2015-06-30
- **Try very hard to fix solid blocks getting light values.** [`d347035`]
  Caused by overflow of signed char value: 255 opacity treated as -128
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-06-30
- **Odd shaped chunk sections are now forbidden. Begin removing special cases.** [`4d878c8`]
  SchematicFileAdapter tries very hard to present uniformly shaped sections and so should you.
  **Files changed:** src/mceditlib/block_copy.py, src/mceditlib/selection/__init__.py

### 2015-06-30
- **Note negative result with unordered_map** [`0d59ad9`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-06-30
- **Disable initialized check for memory views.** [`8dabab6`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-06-30
- **Call stats are now conditionally compiled.** [`cbfe5c9`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-06-30
- **Disable Cython array bounds checking, assert array shapes in cacheSection** [`9103c36`]
  An assert is fine here - if any WorldEditor adapters don't validate the array shapes, you lose.
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-06-30
- **Cast array indices to unsigned to skip negative index wraparound check** [`369d5da`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-06-30
- **Declare RelightCtx as final to omit Cython vtables** [`5a8bc5d`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-06-30
- **Avoid doing extra map lookups** [`2a883ad`]
  In getSection, return the pointer from the find() iterator if found
  **Files changed:** In cacheSection, do some flips to get the pointer from the operator[] that finally caches the section, src/mceditlib/relight/with_cython.pyx

### 2015-06-30
- **Extract cacheSection() from getSection()** [`41b6db0`]
  Skips some initializers used only by cacheSection for a good speedup.
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-06-29
- **findFadedCells in with_cython.pyx now uses STL containers instead of Python ones** [`c99cde9`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-06-29
- **Add option to output statistics for RelightCtx** [`7e18deb`]
  **Files changed:** src/mceditlib/relight/with_cython.pyx

### 2015-06-29
- **Ignore with_cython outputs** [`5ebfa1c`]
  **Files changed:** .gitignore

### 2015-06-29
- **time_relight now relights as many sections as it can in 10 seconds.** [`ba83a68`]
  **Files changed:** src/mceditlib/bench/time_relight_manmade.py, src/mceditlib/bench/time_relight_natural.py

### 2015-06-29
- **ObjGraphWidget.showGraph doesn't crash on a failed eval.** [`eea61a7`]
  **Files changed:** src/mcedit2/util/objgraphwidget.py

### 2015-06-29
- **Add cython implementation of lighting update.** [`6fe4155`]
  Relies on direct access to the section arrays provided by chunk sections through the WorldEditor class. Caches section arrays to avoid repeated calls through the Python WorldEditor's getChunk/getSection
  **Files changed:** Currently does not create new sections., setup.py, src/mceditlib/relight/__init__.py, src/mceditlib/relight/with_cython.pyx

### 2015-06-29
- **In time_relight, block coords are signed (duh)** [`0f7378e`]
  **Files changed:** src/mceditlib/bench/time_relight_manmade.py, src/mceditlib/bench/time_relight_natural.py

### 2015-06-26
- **Add updateLightsInSelection to pure_python.py** [`c003ffc`]
  **Files changed:** src/mceditlib/relight/pure_python.py

### 2015-06-23
- **Remove unused variable from FillBlocksOperation** [`ad505ce`]
  **Files changed:** src/mceditlib/operations/block_fill.py

### 2015-06-23
- **Begin testing multiple implementations of relight algorithm.** [`9da7b28`]
  Change relight API to have updateLightsByCoord, updateLightsInSelection, updateLightsInSection (incomplete)
  **Files changed:** Move time_xxx.py files from test/ into bench/, Split time_relight into manmade and natural., Get time_relight_xxx working again., Add get/set BlockLight/SkyLight to WorldEditor for pure python relight., Implement pure python relight. Seems to work right., src/mceditlib/bench/time_exportimport.py, src/mceditlib/bench/time_fill.py, src/mceditlib/bench/time_getsetblocks.py, src/mceditlib/bench/time_loadsave.py, src/mceditlib/bench/time_nbt.py, src/mceditlib/bench/time_relight_manmade.py, src/mceditlib/bench/time_relight_natural.py, src/mceditlib/bench/time_storagechain.py, src/mceditlib/fakechunklevel.py, src/mceditlib/multi_block.py, src/mceditlib/operations/block_fill.py, src/mceditlib/relight/__init__.py, src/mceditlib/relight/pure_python.py, src/mceditlib/relight/with_cython.pyx, src/mceditlib/relight/with_sections.py, src/mceditlib/relight/with_setblocks.py, src/mceditlib/test/time_relight.py, src/mceditlib/worldeditor.py

### 2015-06-18
- **Brush shapes are now able to provide options widgets.** [`987aa3e`]
  BrushShape inherits from QObject so it can have signals
  **Files changed:** BrushShape provides an optionsChanged signal, ShapeWidget for some reason forwards the optionsChanged signal to its client., Probably because it "owns" the BrushShape instances, which is kind of dumb?, No shapes implement useful options widgets yet, src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/brush/shapes.py, src/mcedit2/editortools/select.py, src/mcedit2/widgets/shapewidget.py

### 2015-06-18
- **Add wrapper for glActiveTexture** [`0ae5213`]
  Use the `alternate` function from OpenGL.extensions to choose the first one from (glActiveTexture, glActiveTextureARB) that is available.
  **Files changed:** src/mcedit2/rendering/rendergraph.py, src/mcedit2/util/glutils.py

### 2015-06-14
- **Update heightmap even when lighting is disabled.** [`0d9d562`]
  **Files changed:** src/mceditlib/relight.py

### 2015-06-14
- **Add rendering layer for chunk section edges.** [`cc4d4f5`]
  Reveals that far too many chunk sections are being created.
  **Files changed:** Edges have odd diagonals but I'll leave it for now., src/mcedit2/rendering/chunkmeshes/chunksections.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/layers.py

### 2015-06-13
- **Actually skip over erroring worlds in WorldListModel, for real this time.** [`ffa4c0a`]
  Fixes #118
  **Files changed:** src/mcedit2/worldlist.py

### 2015-06-12
- **Check minor and major versions from GL_VERSION** [`60c4026`]
  GL_MAJOR_VERSION is only supported on OpenGL 3.0+
  **Files changed:** Fixes #116, src/mcedit2/util/qglcontext.py

### 2015-06-12
- **Check minor and major versions returned by glGet instead of QGLFormat** [`c9076b2`]
  QGLFormat's values are wrong with Qt 4.8.6 on OS X (QTBUG-40415)
  **Files changed:** Fixes #115, src/mcedit2/util/qglcontext.py

### 2015-06-12
- **Log editor commands as they are pushed** [`b1dad4b`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-06-12
- **worldinfo.ui: "Commands" -> "Allow Commands"** [`33acbaf`]
  **Files changed:** src/mcedit2/ui/panels/worldinfo.ui

### 2015-06-12
- **Fix edits being added when world info panel is reloaded.** [`33a01de`]
  Yes, this is what editsDisabled is for.
  **Files changed:** src/mcedit2/panels/worldinfo.py

### 2015-06-12
- **Fix crash with non-standard world generator names, allow custom generator names to be entered.** [`9db66f1`]
  Rename generationTypeCombo  to generatorTypeCombo
  **Files changed:** Change generatorTypeCombo into an editable combo box., Add generator tag values to combo box items as itemData. Remove GENERATOR_TYPES., Get generator tag value first as itemData and then as entered text if no itemData is found., Add unknown generator types from the NBT data to the combo box., Connect to the combo box's line edit's editingFinished to respond to user-entered generator types., Fixes #113, src/mcedit2/panels/worldinfo.py, src/mcedit2/ui/panels/worldinfo.ui

### 2015-06-11
- **Only import win32api on Windows.** [`474b0f4`]
  **Files changed:** src/mcedit2/util/directories.py

### 2015-06-09
- **Remove some noisy loggers** [`a00a17a`]
  **Files changed:** src/mcedit2/rendering/worldscene.py, src/mcedit2/worldview/worldview.py

### 2015-06-08
- **Add chunkNotPresent to ChunkLoader, WorldView, WorldScene** [`3c56b0f`]
  **Files changed:** src/mcedit2/rendering/chunkloader.py, src/mcedit2/rendering/worldscene.py, src/mcedit2/worldview/cutaway.py, src/mcedit2/worldview/worldview.py

### 2015-06-08
- **Remove recentDirtyChunks. Change ChunkLoader to respond to revisionChanged instead.** [`891bb6d`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/rendering/chunkloader.py, src/mceditlib/worldeditor.py

### 2015-06-08
- **Fix undoBackward returning the wrong RevisionChanges** [`bc50b9c`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-06-08
- **Add chunk-shaped selection box** [`0f7488f`]
  **Files changed:** src/mcedit2/editortools/brush/shapes.py, src/mcedit2/editortools/select.py, src/mcedit2/widgets/shapewidget.py

### 2015-06-08
- **Dirty hack to force chunk rescan after revision change** [`29b7406`]
  Should inspect changes and update instead of rescanning
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-06-08
- **RevisionHistory: fix various functions not respecting deadChunks/deadFiles** [`278966a`]
  chunkPositions now removes dead chunks from the returned chunks
  **Files changed:** readChunkBytes raises ChunkNotPresent for dead chunks, readFile raises IOError for dead files, src/mceditlib/revisionhistory.py

### 2015-06-08
- **Quit app when main window is closed** [`cca35e3`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-06-08
- **Add chunk menu and implement chunk delete command** [`ce7c652`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-06-07
- **createShapedSelection now has the current dimension as an argument** [`5a5d09c`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/brush/modes.py, src/mcedit2/editortools/brush/shapes.py, src/mcedit2/editortools/select.py

### 2015-06-07
- **Always log info about obtained GL context** [`8812e41`]
  The more info, the better.
  **Files changed:** src/mcedit2/util/qglcontext.py

### 2015-06-07
- **Update readme - install pyzmq using pip** [`b10de6f`]
  **Files changed:** README.md

### 2015-06-07
- **Log selection in FillBlocksOperation** [`9e383d4`]
  **Files changed:** src/mceditlib/operations/block_fill.py

### 2015-06-07
- **Add deleted chunks to recentDirtyChunks** [`aeb8744`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-06-07
- **Replace Blocks now respects the "In Selection" checkbox** [`5f94173`]
  **Files changed:** src/mcedit2/editorcommands/find_replace.py

### 2015-06-07
- **Selection highlight now updates after the world is edited.** [`d3187b2`]
  No more selection hanging around after blocks are deleted.
  **Files changed:** src/mcedit2/editortools/select.py, src/mcedit2/rendering/selection.py

### 2015-06-06
- **EditorSession.revisionChanged is now emitted with a RevisionChanges object instead of the revision ID** [`1d9c2c6`]
  **Files changed:** src/mcedit2/editorsession.py, src/mceditlib/anvil/adapter.py, src/mceditlib/worldeditor.py

### 2015-06-06
- **Fix crash when changing selection shape** [`ef520d7`]
  **Files changed:** src/mceditlib/selection/__init__.py

### 2015-06-06
- **Catch errors while calling generator's getPreviewNode** [`c79c851`]
  TODO: better error dialog!
  **Files changed:** src/mcedit2/editortools/generate.py

### 2015-06-06
- **WorkplaneNode can now be oriented to any axis** [`2ce9faa`]
  **Files changed:** src/mcedit2/rendering/workplane.py

### 2015-06-06
- **Fix selection boxes occasionally being super hard to resize.** [`ac495f1`]
  Box was using the wrong plane as the drag reference plane
  **Files changed:** src/mcedit2/handles/boxhandle.py

### 2015-06-06
- **Fix selection renderer rendering anything when selection is zero sized.** [`5de661c`]
  IntersectionBox had the wrong logic for one of its components returning None from box_mask
  **Files changed:** All CombinationBoxes have been adjusted., src/mceditlib/selection/__init__.py

### 2015-06-06
- **Allow bresenham to be reloaded** [`7ae713e`]
  **Files changed:** src/mcedit2/synth/l_system.py

### 2015-06-05
- **Change sys.executable to GetModuleFileNameW** [`8789408`]
  Currently does nothing, but when PyInstaller is patched to use unicode filenames, GMFNW won't return an SFN any more.
  **Files changed:** src/mcedit2/util/directories.py

### 2015-06-05
- **validateGLContext doesn't need to return anything** [`97d6aea`]
  Was getting a weird error like "PySide.QGLContext has no attribute setData" in some logging call...
  **Files changed:** src/mcedit2/util/qglcontext.py

### 2015-06-04
- **Fix lag between moving mouse and view updating.** [`208069b`]
  On mouse move, redraw view after calling view actions, not before.
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-06-04
- **Add a comment in geometry.py** [`65a17d9`]
  **Files changed:** src/mceditlib/geometry.py

### 2015-06-04
- **Fix "jitter" when moving cursor across block edges.** [`8207d12`]
  Use the maximum depth buffer value when converting from a screen position to a 3D ray to increase precision.
  **Files changed:** Not sure why it wasn't the maximum before., src/mcedit2/worldview/worldview.py

### 2015-06-03
- **Add basic workplane control.** [`817d42b`]
  Only Y-axis right now. In the future, maybe a tool for creating one workplane for each axis?
  **Files changed:** src/mcedit2/rendering/vertexarraybuffer.py, src/mcedit2/rendering/workplane.py, src/mcedit2/worldview/camera.py

### 2015-06-03
- **Fix chunk loading origin not updating after changing dimensions** [`4a54d0f`]
  Offscreen views were being added to chunkLoader clients and controlling the load order...
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/worldview/worldview.py, src/mceditlib/worldeditor.py

### 2015-06-03
- **Fix moving left/right while looking down being very slow.** [`0c897f3`]
  Needed to normalize the 'left' vector.
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-06-02
- **Add ParabolicDome brush shape** [`0d956c6`]
  **Files changed:** src/mcedit2/editortools/brush/shapes.py

### 2015-06-02
- **Brush's "Hover" option is now implemented.** [`814a40b`]
  TODO: Button to switch hover to half of object height, or half of object size along axis given by face under cursor
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mceditlib/faces.py

### 2015-06-02
- **Rework brush shapes a bit** [`4e284e6`]
  ShapedSelection -> ShapeFuncSelection
  **Files changed:** BrushShape now has createShapedSelection in addition to shapeFunc, createShapedSelection  is called instead of ShapeFuncSelection, createOptionsWidget added to BrushShape but not yet used..., Move shapeFuncs from mceditlib.selection to brush.shapes, Fix Diamond shape (recenters coordinates), Remove Box shapeFunc - return box from createShapedSelection., src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/brush/masklevel.py, src/mcedit2/editortools/brush/modes.py, src/mcedit2/editortools/brush/shapes.py, src/mcedit2/editortools/select.py, src/mcedit2/test/time_selectionrender.py, src/mceditlib/selection/__init__.py

### 2015-06-02
- **Add cylinder shape.** [`a0bac1c`]
  Todo: axis setting
  **Files changed:** src/mcedit2/editortools/brush/shapes.py

### 2015-06-01
- **Fix bug in modelmesh causing negative y coordinates to roll over** [`b511ce9`]
  **Files changed:** src/mcedit2/rendering/modelmesh.pyx

### 2015-06-01
- **Rework createSelectionMask** [`b12d4ff`]
  Move createSelectionMask into ShapedSelection.box_mask
  **Files changed:** Remove "hollow" and "chance" args - use composed selections for this instead, Don't recenter coordinates in box_mask, Recenter coordinates in SphereShape instead, DiamondShape is now broken., src/mceditlib/selection/__init__.py

### 2015-06-01
- **xxx show wireframe box around brush cursor** [`5635597`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py

### 2015-06-01
- **Allow brush shapes to have no icon.** [`251c999`]
  **Files changed:** src/mcedit2/widgets/shapewidget.py

### 2015-06-01
- **Add some comments and notes** [`49e5533`]
  **Files changed:** src/mcedit2/editortools/brush/masklevel.py, src/mcedit2/editortools/brush/modes.py, src/mcedit2/rendering/chunkloader.py, src/mcedit2/rendering/chunkupdate.py, src/mceditlib/selection/__init__.py

### 2015-05-31
- **Main chunk loading timer can now idle again.** [`8500d6a`]
  ChunkLoader.next now reraises StopIteration to signal caller that all chunks are loaded.
  **Files changed:** src/mcedit2/rendering/chunkloader.py

### 2015-05-31
- **Pull masklevel.py, modes.py, shapes.py out of brush/__init__.py** [`b482e8d`]
  Move shapes out of shapewidget.py, too.
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/brush/masklevel.py, src/mcedit2/editortools/brush/modes.py, src/mcedit2/editortools/brush/shapes.py, src/mcedit2/editortools/select.py, src/mcedit2/widgets/shapewidget.py

### 2015-05-31
- **Add Alek to supporters list** [`b420e29`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-05-30
- **Minimap viewing outline now uses a ray cast to determine the height at which to slice the frustum.** [`c53528c`]
  The outline now grows and shrinks according to how far away the object in the center of the screen is.
  **Files changed:** src/mcedit2/worldview/camera.py, src/mcedit2/worldview/minimap.py

### 2015-05-30
- **Fix minimap's viewing area outline.** [`3772d5d`]
  Check for intersection with eight of the frustum's edges, not just four.
  **Files changed:** src/mcedit2/worldview/minimap.py, src/mcedit2/worldview/worldview.py

### 2015-05-29
- **Use exhaust() in some preview loaders to exhaust iterators.** [`c583635`]
  **Files changed:** src/mcedit2/editortools/generate.py, src/mcedit2/rendering/selection.py

### 2015-05-29
- **Add progress bars to world save and undo revision close.** [`d74ebcf`]
  Tempted to write a progress manager type class the next time this comes up.
  **Files changed:** Progress counts are a little bit off., src/mcedit2/command.py, src/mcedit2/editorsession.py, src/mceditlib/anvil/adapter.py, src/mceditlib/revisionhistory.py, src/mceditlib/schematic.py, src/mceditlib/util/__init__.py, src/mceditlib/worldeditor.py

### 2015-05-29
- **Add __len__ to lru_cache_object** [`3861f7f`]
  **Files changed:** src/mceditlib/cachefunc.py

### 2015-05-29
- **Region repair: Don't put overlapping chunks in lost and found.** [`d1a51ec`]
  They are probably unreadable anyway.
  **Files changed:** src/mceditlib/pc/regionfile.py

### 2015-05-27
- **Fix AttributeError in RegionFile.repair after renaming writeChunk to writeChunkBytes** [`4deae44`]
  **Files changed:** src/mceditlib/pc/regionfile.py

### 2015-05-27
- **Change `assert VERSION_ANVIL` to a LevelFormatError** [`51babcd`]
  LFE can be caught by world list, etc. Having it as an assert just caused the app to exit.
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-05-25
- **Fix crash when switching back to Koch Snowflake plugin** [`ac856a0`]
  Options widget was being recreated. When the previous widget is deleted, it deletes all of its children, including self.iterationsSlider.
  **Files changed:** Maybe make sure getOptionsWidget is only called once and cache its result in GeneratePlugin, src/plugins/koch.py

### 2015-05-24
- **Remove debug print from mcedit2.spec** [`1045da3`]
  **Files changed:** mcedit2.spec

### 2015-05-24
- **Correctly remove pluginModule from sys.modules, as it is a dict and not a list.** [`2244705`]
  **Files changed:** src/mcedit2/plugins.py

### 2015-05-24
- **Close session panels before setting worldEditor to None** [`87c6f45`]
  Panels expect worldEditor to not be None and this was spamming exceptions from one of the list models.
  **Files changed:** src/mcedit2/editorsession.py

### 2015-05-24
- **EditorSession.WorldInfoPanel -> worldInfoPanel** [`9d7adf1`]
  oops...
  **Files changed:** src/mcedit2/editorsession.py

### 2015-05-24
- **Add every pyfile under src/mcedit2 and src/mceditlib to the pyi build.** [`9496914`]
  This brings in synth.l_system even though it isn't imported, and brings in anything else that's only provided for plugins and isn't found by modulefinder.
  **Files changed:** mcedit2.spec

### 2015-05-24
- **Move run_regression_test.py into mceditlib/test** [`6a8d95b`]
  **Files changed:** src/mceditlib/test/run_regression_test.py

### 2015-05-24
- **Remove unused mcedit2/util/scanmodules.py** [`72c85ef`]
  **Files changed:** src/mcedit2/util/scanmodules.py

### 2015-05-24
- **Remove unused mcedit2/util/geometry.py** [`9599097`]
  **Files changed:** src/mcedit2/util/geometry.py

### 2015-05-24
- **Remove unused files in mcedit2/prefs** [`bed69d9`]
  **Files changed:** src/mcedit2/prefs/__init__.py, src/mcedit2/prefs/prefswindow.py, src/mcedit2/prefs/raw.py

### 2015-05-24
- **Remove __init__.py from mcedit2/ui (not a package)** [`3d536c6`]
  **Files changed:** src/mcedit2/ui/__init__.py

### 2015-05-24
- **GenerateTool doesn't call boundsChanged if no currentGenerator** [`519b213`]
  **Files changed:** src/mcedit2/editortools/generate.py

### 2015-05-24
- **Update guidelines with new error log locations** [`15cb5e0`]
  **Files changed:** CONTRIBUTING.md

### 2015-05-24
- **Add a note about not reading the guidelines to the issue guidelines.** [`580af9b`]
  **Files changed:** CONTRIBUTING.md

### 2015-05-24
- **Use a more sensible default view distance** [`2438efd`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-05-24
- **Koch Snowflake plugin now uses boundsChanged to limit the max iterations, and uses glColor to color the lines** [`23fe46c`]
  **Files changed:** src/plugins/koch.py

### 2015-05-24
- **Line's GL color can now be specified** [`11ac62f`]
  **Files changed:** src/mcedit2/synth/l_system.py

### 2015-05-24
- **Add a boundsChanged method to GeneratePlugin** [`60b1361`]
  **Files changed:** src/mcedit2/editortools/generate.py

### 2015-05-24
- **Actually reselect the previous generator plugin after it was reloaded.** [`cc06555`]
  **Files changed:** src/mcedit2/editortools/generate.py

### 2015-05-24
- **Need to use iteritems to iterate registered classes** [`f78039f`]
  **Files changed:** src/mcedit2/widgets/inspector.py, src/mceditlib/anvil/entities.py

### 2015-05-24
- **Generate tool now responds to plugin classes being loaded and unloaded.** [`3a8453a`]
  Adds/removes the plugin class to/from the generator type box
  **Files changed:** Chooses a different generator type when the current type is unloaded, Switches back to the unloaded generator type if the plugin is loaded again, src/mcedit2/editortools/generate.py

### 2015-05-24
- **For automatic unregistration, key plugin classes by the module fullpath.** [`dfa172e`]
  Can't key them by the module itself because once the module is loaded, classes may already be registered.
  **Files changed:** Also, checkTimestamps now returns the correct answer., src/mcedit2/plugins.py

### 2015-05-23
- **When in developer mode, reload modified plugins when app is brought to foreground** [`b5c8b41`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-05-23
- **Add "Developer Mode" toggle to Options menu, remove -debug argument** [`d2cd797`]
  **Files changed:** src/mcedit2/appsettings.py, src/mcedit2/editorapp.py, src/mcedit2/main.py, src/mcedit2/ui/main_window.ui

### 2015-05-23
- **Add function to record and check timestamps to PluginRef** [`ae83f9e`]
  **Files changed:** src/mcedit2/plugins.py

### 2015-05-23
- **Validate GL format only when creating a QGLWidget.** [`355a9a4`]
  QGLContext cannot be created on its own without using deprecated APIs to bind its output to a widget (or an offscreen render buffer, or a texture in an existing context...). So, allow QGLWidget to create the context and then validate it afterward.
  **Files changed:** This also sets the default QGLFormat to require OpenGL 1.3 and hardware rendering (called "direct rendering" in QGLFormat), src/mcedit2/editorapp.py, src/mcedit2/util/qglcontext.py, src/mcedit2/worldview/worldview.py

### 2015-05-22
- **Disable line ending conversion in .gitattributes** [`747e936`]
  **Files changed:** .gitattributes

### 2015-05-22
- **Make currentViewSetting into a settingsOption, cleanup, auto-format, add notes** [`369b4e3`]
  **Files changed:** src/mcedit2/dialogs/plugins_dialog.py, src/mcedit2/editorapp.py, src/mcedit2/editorsession.py

### 2015-05-22
- **Attempt to validate OpenGL capabilities on startup.** [`1337312`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/util/qglcontext.py

### 2015-05-22
- **City: The Random instance is now a parameter instead of a global.** [`d7aa323`]
  Since it is a parameter, it will be passed to replaced symbols through the `**kw=self.parameters` when constructing symbols.
  **Files changed:** src/plugins/city.py

### 2015-05-22
- **Add KeyedVectorAttr, make adapter.metadata accessible through WorldEditor** [`168bbfa`]
  Add AnvilWorldMetadata.Spawn
  **Files changed:** Add KeyedVectorAttr, used for Spawn and TileEntity Position, Remove get/setWorldSpawnPosition, src/mcedit2/editorsession.py, src/mcedit2/panels/worldinfo.py, src/mcedit2/worldlist.py, src/mceditlib/anvil/adapter.py, src/mceditlib/anvil/entities.py, src/mceditlib/minecraft_server.py, src/mceditlib/nbtattr.py, src/mceditlib/worldeditor.py

### 2015-05-22
- **edit_metadata.png -> edit_worldinfo.png** [`123b4ea`]
  **Files changed:** src/mcedit2/assets/mcedit2/icons/edit_worldinfo.png, src/mcedit2/panels/worldinfo.py

### 2015-05-22
- **worldmeta.ui -> worldinfo.ui** [`8327071`]
  **Files changed:** src/mcedit2/panels/worldinfo.py, src/mcedit2/ui/panels/worldinfo.ui

### 2015-05-22
- **WorldMetaPanel -> WorldInfoPanel** [`54f310a`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/panels/worldinfo.py

### 2015-05-22
- **Merge pull request #92 from Rubisk/worldmetadeta** [`2add2c2`]
  Added World-Metadeta

### 2015-05-17
- **Fix Translation for World Info Panel** [`4a6cc5a`]
  **Files changed:** src/mcedit2/panels/worldmeta.py

### 2015-05-17
- **Updated World Info Panel** [`bad40be`]
  **Files changed:** src/mcedit2/assets/mcedit2/clock/dawn.png, src/mcedit2/assets/mcedit2/clock/evening.png, src/mcedit2/assets/mcedit2/clock/night.png, src/mcedit2/assets/mcedit2/clock/noon.png, src/mcedit2/assets/mcedit2/icons/edit_metadata.png, src/mcedit2/panels/worldmeta.py, src/mcedit2/ui/panels/worldmeta.ui, src/mceditlib/anvil/adapter.py

### 2015-05-12
- **Added WorldMetaPanel** [`914e59f`]
  I need to make it somewhat functional still, but wanted to checkout the
  **Files changed:** branch for now, I'll stash this commit with the next WorldMetaPanel one., src/mcedit2/assets/mcedit2/icons/edit_metadata.png, src/mcedit2/editorsession.py, src/mcedit2/panels/player.py, src/mcedit2/panels/worldmeta.py, src/mcedit2/ui/panels/worldmeta.ui, src/mceditlib/anvil/adapter.py

### 2015-05-15
- **Put a stern warning about imports in main.py** [`355346d`]
  And make sure the shebang line comes first
  **Files changed:** src/mcedit2/main.py

### 2015-05-15
- **Call QCoreApplication.quit instead of raising SystemExit** [`6850314`]
  Not sure it's needed, but it might trigger some cleanup code? Who knows.
  **Files changed:** src/mcedit2/editorapp.py

### 2015-05-15
- **Revise the introduction to L-systems** [`3f245f0`]
  **Files changed:** src/mcedit2/synth/l_system.py

### 2015-05-15
- **Add Adrian's City plugin as an example** [`5663ad9`]
  Could flesh this out and add all kinds of parameters like MINSIZE as options
  **Files changed:** src/plugins/city.py

### 2015-05-15
- **Add LSystemPlugin subclass for Koch Snowflake system** [`41ea863`]
  **Files changed:** src/plugins/koch.py

### 2015-05-15
- **Make plugin rows selectable and not editable** [`71722a1`]
  **Files changed:** src/mcedit2/dialogs/plugins_dialog.py, src/mcedit2/ui/plugins.ui

### 2015-05-15
- **Remove displayName from LSystemPlugin, document displayName in GeneratePlugin** [`a34957a`]
  Add class name as fallback for missing displayName
  **Files changed:** src/mcedit2/editortools/generate.py, src/mcedit2/synth/l_system_plugin.py

### 2015-05-15
- **LSystemPlugin is now a core component and not a plugin.** [`23c2746`]
  Provides a minimal implementation of GeneratePlugin suitable for L-systems.
  **Files changed:** getOptionsWidget and createInitialSymbol are the only required methods to implement., Kindly ignore the 'getInputsList' for now, I'm still not sure if it's going to be implemented., src/mcedit2/synth/l_system_plugin.py, src/plugins/l_system_plugin.py

### 2015-05-15
- **GeneratePlugin: Wrap and adjust docstrings, remove wonky TreeGen** [`4bb58c1`]
  **Files changed:** src/mcedit2/editortools/generate.py

### 2015-05-15
- **GenerateTool: Toggling Block or GL Preview no longer updates the other.** [`39da111`]
  **Files changed:** src/mcedit2/editortools/generate.py

### 2015-05-15
- **Rewrote plugin finding code, added PluginRefs and Plugins dialog** [`65b18f7`]
  getAllPlugins returns all PluginRefs found so far
  **Files changed:** detectPlugin tries to find a plugin and returns a PluginRef, findNewPluginsInDir stores a PluginRef for each plugin in the dir, Each PluginRef can be loaded and unloaded, remembers its 'enabled' setting, and provides a displayName and info about loading/unloading errors., On startup, `findNewPluginsInDir` is called., Found plugins are retrieved using getAllPlugins and any enabled plugins are loaded., Plugins dialog lists plugins from getAllPlugins and allows to enable/disable each one., Reloading is not yet implemented., src/mcedit2/assets/mcedit2/reload.png, src/mcedit2/assets_raw/reload.svg, src/mcedit2/dialogs/__init__.py, src/mcedit2/dialogs/plugins_dialog.py, src/mcedit2/editorapp.py, src/mcedit2/plugins.py, src/mcedit2/ui/main_window.ui, src/mcedit2/ui/plugins.ui

### 2015-05-15
- **Use MCESettings.getNameSpace in camera.py** [`ddd6c49`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-05-15
- **Add supporters to About Box as promised in Patreon rewards.** [`70a5bd0`]
  Anyone who donated at least $20 since MCEdit's inception is credited.
  **Files changed:** src/mcedit2/editorapp.py

### 2015-05-12
- **Fixed a bug with the Edit Player button** [`eb8e722`]
  Fixed a bug causing the Edit Player button to stay looking pressed if
  **Files changed:** the red X in the top-right got pressed., src/mcedit2/panels/player.py

### 2015-05-14
- **Keep track of which plugin module is loading plugin classes.** [`ac5e560`]
  When the plugin module is unloaded, unregister all of its classes.
  **Files changed:** Plugin modules are also allowed `register()` and `unregister()` functions to use for e.g. monkey-patching MCEdit's internals and other unspeakable things., src/mcedit2/editorapp.py, src/mcedit2/editortools/__init__.py, src/mcedit2/editortools/generate.py, src/mcedit2/plugins.py, src/mcedit2/util/load_ui.py, src/mcedit2/widgets/inspector.py, src/mceditlib/anvil/entities.py

### 2015-05-14
- **Don't pass an `itertools.chain` to `nbt.walk`** [`c5f1cf4`]
  nbt.walk only accepts TAG_List and TAG_Compound, not arbitrary iterables.
  **Files changed:** src/mceditlib/schematic.py

### 2015-05-13
- **Use catchalls to skip over errors while centering views on players** [`cbd35c1`]
  Avoids crashes on badly-formed player data. Should tighten this up to only catch errors in getting the player's position. Should also add a validate function to AnvilPlayerRef (and every other ref, too?)
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/worldlist.py

### 2015-05-13
- **Add raw asset for compass overlay** [`d10c644`]
  **Files changed:** src/mcedit2/assets_raw/compass.svg

### 2015-05-13
- **GenerateTool handles an empty generatorTypes and a None currentGenerator.** [`b22bbcb`]
  Hopefully this should never happen.
  **Files changed:** src/mcedit2/editortools/generate.py

### 2015-05-13
- **Write app version to log file.** [`aaefc96`]
  Duh.
  **Files changed:** src/mcedit2/main.py

### 2015-05-13
- **Actually abort creating vertex arrays when models are not cooked.** [`addfa3e`]
  **Files changed:** src/mcedit2/rendering/modelmesh.pyx

### 2015-05-13
- **Encoding pathnames with sys.getfilesystemencoding is always wrong.** [`4c66033`]
  On Windows this encodes with the current codepage, which often fails for characters not in the codepage.
  **Files changed:** On Windows, FS functions accept 'unicode' and encode as UTF-16 for WinAPI, On Mac, FS functions accept 'unicode' and encode as UTF-8 for FS API, On Linux, filenames are byte strings and encoding is only a convention. FS functions encode 'unicode' according to locale. On Linux, it is possible to have files whose names cannot be decoded in any character set!, src/mceditlib/minecraft_server.py

### 2015-05-13
- **Line draws GL lines with endpoints at block centers** [`d330a22`]
  **Files changed:** src/mcedit2/synth/l_system.py

### 2015-05-13
- **Line now has a constructor Line(p1, p2)** [`c285151`]
  **Files changed:** src/mcedit2/synth/l_system.py

### 2015-05-13
- **Fill now has a constructor Fill(box, blocktype)** [`9a440c9`]
  **Files changed:** src/mcedit2/synth/l_system.py

### 2015-05-13
- **applyReplacements correctly handles symbols without a 'replace'** [`60a2a83`]
  **Files changed:** src/mcedit2/synth/l_system.py

### 2015-05-13
- **Convenience added to GenerateTool** [`d203639`]
  GL preview is enabled by default
  **Files changed:** Undoing a Generate returns the bounding box to the tool, generateInSchematic is provided with the original bounding box, clearSchematic does not remove schematicBounds (should be called generateBounds or something), src/mcedit2/editortools/generate.py

### 2015-05-13
- **Auto-format analyze.py and analyze.py** [`d67f115`]
  Increase default size of analyze dialog
  **Files changed:** Remove dead code, Improve comments, src/mcedit2/editorcommands/analyze.py, src/mcedit2/ui/analyze.ui, src/mceditlib/operations/analyze.py

### 2015-05-13
- **Merge pull request #85 from Rubisk/develop** [`6d0e89f`]
  Updated Analyze UI

### 2015-05-13
- **Add an experimental plugin to edit items in StorageDrawers via the Block Inspector.** [`66f8c17`]
  Handles exactly one type of drawer, so not very useful at the moment.
  **Files changed:** src/plugins/storagedrawers.py

### 2015-05-13
- **Add a somewhat flaky Generate plugin for L-systems that currently only runs the Koch Snowflake system.** [`4e9a020`]
  This plugin will probably not live for very long as it seems better to make Generate plugins directly for different L-systems.
  **Files changed:** src/plugins/koch.py, src/plugins/l_system_plugin.py

### 2015-05-13
- **Add what appears to be an L-system library for 3D objects** [`16460f6`]
  Objects can be rendered either as Minecraft block placement commands or as OpenGL rendering commands in the form of scenegraph Nodes.
  **Files changed:** The huge block of text at the top probably doesn't do much to explain the value of the system, so examples and tutorials will be coming soon., src/mcedit2/synth/__init__.py, src/mcedit2/synth/l_system.py

### 2015-05-13
- **Add plugins.py with several registration points for plugin classes to be inserted.** [`793fb44`]
  **Files changed:** src/mcedit2/editortools/__init__.py, src/mcedit2/editortools/generate.py, src/mcedit2/plugins.py, src/mcedit2/widgets/inspector.py, src/mcedit2/worldview/worldview.py

### 2015-05-13
- **Skip files in mods dir that are not files.** [`6b83537`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2015-05-12
- **Remove same size check in generateNextSchematic** [`f9a6dba`]
  This was stopping generator options from triggering a regen. Come back to this when generated object previews can be moved.
  **Files changed:** src/mcedit2/editortools/generate.py

### 2015-05-12
- **Add TreeGen back in so GenerateTool doesn't crash on zero generator classes.** [`1be1d81`]
  xxx allow zero generator classes
  **Files changed:** src/mcedit2/editortools/generate.py

### 2015-05-12
- **Load plugins from a "plugins" folder when frozen or the src/plugins folder when running from source.** [`cd7b75d`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/util/directories.py

### 2015-05-12
- **ItemType.name was changed to displayName previously** [`3477b59`]
  **Files changed:** src/mceditlib/blocktypes/itemtypes.py

### 2015-05-12
- **Added a whole bunch of variations on Bresenham's algorithm and a few tests.** [`fe64ea6`]
  The tests check if any of the variations change the algorithm's output to see if I broke anything while making the 3D and fixed-point/scaled variants.
  **Files changed:** src/mcedit2/util/bresenham.py

### 2015-05-12
- **Fleshed out the Generate tool quite a bit.** [`01e08a2`]
  Generate plugins may now provide a scene node for OpenGL previewing instead of Minecraft block previewing
  **Files changed:** Generate plugins may now generate directly into a world instead of via an intermediate schematic, Documented the functions of the GeneratePlugin class, TreeGen is now broken., Added "Live Preview", "Block Preview" and "GL Preview" checkboxes., Added an updatePreview method for plugins to call, e.g. when plugin options change., Exceptions while running a generator are now caught, Exceptions during Live Preview will disable it., src/mcedit2/editortools/generate.py

### 2015-05-12
- **Split QuadVertexArrayBuffer off of VertexArrayBuffer** [`89e01a8`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/chunkmeshes/lowdetail.py, src/mcedit2/rendering/chunkmeshes/terrainpop.py, src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/rendering/selection.py, src/mcedit2/rendering/vertexarraybuffer.py

### 2015-05-12
- **Made analyze file writing support unicode** [`39c85d7`]
  (and stopped it from crashing)
  **Files changed:** src/mcedit2/editorcommands/analyze.py

### 2015-05-12
- **Added option to export analysation results** [`b35830a`]
  **Files changed:** src/mcedit2/editorcommands/analyze.py, src/mcedit2/editorsession.py, src/mceditlib/operations/analyze.py

### 2015-05-12
- **Fixed some small issues with the Analyze Output Panel** [`74c6db1`]
  **Files changed:** src/mcedit2/editorcommands/analyze.py

### 2015-05-12
- **Updated analyze UI** [`eed2c52`]
  Implement all of CW's feedback/change requests, and updated the analyze
  **Files changed:** UI., Next up is export buttons., .gitignore, src/mcedit2/editorcommands/analyze.py, src/mcedit2/editorsession.py, src/mcedit2/ui/analyze.ui, src/mceditlib/operations/analyze.py, src/mceditlib/worldeditor.py

### 2015-05-11
- **Basic Analyze Tool** [`fa65763`]
  Just some first things.
  **Files changed:** src/mcedit2/editorcommands/analyze.py, src/mcedit2/editorsession.py, src/mcedit2/ui/analyze.ui, src/mceditlib/operations/analyze.py, src/mceditlib/worldeditor.py

### 2015-05-10
- **Fixed an issue causing the fill tool to crash.** [`fde3d16`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2015-05-11
- **Monkeypatch codecs.getwriter to not attempt decoding bytes written to stdout/stderr** [`7cb73da`]
  **Files changed:** src/mcedit2/main.py

### 2015-05-11
- **Remove junk from old dynamically loaded tools** [`e2ce7f1`]
  **Files changed:** src/mcedit2/editortools/__init__.py

### 2015-05-11
- **QComboBox.textChanged was renamed to editTextChanged in Qt4** [`8429a8d`]
  Apparently there is compatibility in place for my version of PySide, but not for some others.
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2015-05-11
- **Fix AttributeError in BlockTypeButton after changing textureAtlas to editorSession** [`b2c63b4`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2015-05-11
- **Fold createToolWidget into SelectBlockTool.__init__** [`103a5d9`]
  **Files changed:** src/mcedit2/editortools/select_block.py

### 2015-05-11
- **More documentation to Vector** [`3e2b004`]
  **Files changed:** src/mceditlib/geometry.py

### 2015-05-11
- **showProgress displays the dialog after 0.5 seconds instead of after 8 iterations** [`699143d`]
  showProgress only accepts a tuple as a status result
  **Files changed:** src/mcedit2/util/showprogress.py

### 2015-05-11
- **Document geometry.Vector, change __repr__ to return something that can be evaluated** [`ff619ec`]
  **Files changed:** src/mceditlib/geometry.py

### 2015-05-11
- **Generate tool now has a rudimentary plugin API and can actually apply a generated object to the world.** [`ffc803e`]
  Add a liveUpdate option
  **Files changed:** Catch any errors while running the generator and disable liveUpdate if one is caught., src/mcedit2/editortools/generate.py

### 2015-05-11
- **Add setBlock function to WorldEditor** [`4e507be`]
  Combines the functions of setBlockID and setBlockData. Takes a BlockType or any value convertible to a BlockType
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-05-11
- **Fix calls to os.path.expanduser with unicode strings.** [`a2c9093`]
  expanduser does not handle unicode strings correctly, tries to decode using ASCII instead of FS encoding. Only workaround is to pass bytestrings
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/main.py

### 2015-05-11
- **Fail hard when sys.executable does not exist.** [`1961997`]
  To help diagnose a problem with sys.executable not having a useful path when the app is in a non-ASCII folder. The user data folder can end up in a completely different location as a different series of folders is created.
  **Files changed:** src/mcedit2/util/directories.py

### 2015-05-09
- **Use a lenient encoder for stdin/out/err to avoid encoding errors when printing to a Windows console.** [`30f1ad3`]
  **Files changed:** src/mcedit2/main.py

### 2015-05-09
- **Disable profiling in blockmodels.pyx to avoid a bug with cython0.22+memoryviews+MSVC** [`e0ed1b5`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-05-09
- **Add note to readme about updating setuptools** [`1cd59bc`]
  **Files changed:** README.md

### 2015-05-08
- **Schematics are now exported with an ItemIDs mapping and an itemStackVersion value.** [`346f5c7`]
  Remove and comment out some dead/unused code. INVEditChest shouldn't be important now that we have an inventory editor.
  **Files changed:** src/mceditlib/schematic.py

### 2015-05-08
- **Get selection highlight to display again by connecting to editorSession.dimensionChanged** [`839ae3c`]
  **Files changed:** src/mcedit2/editortools/select.py

### 2015-05-08
- **Document nbt.walk** [`608940a`]
  **Files changed:** src/mceditlib/nbt.pyx

### 2015-05-08
- **BlockTypes return default values for blocks without jsons** [`3991cb0`]
  **Files changed:** src/mceditlib/blocktypes/__init__.py

### 2015-05-08
- **extractZipSchematic is dead, for now.** [`19ed34f`]
  **Files changed:** src/mceditlib/export.py

### 2015-05-08
- **Move walkNBT to nbt.walk** [`45c8a97`]
  **Files changed:** src/mcedit2/editorcommands/find_replace.py, src/mceditlib/nbt.pyx

### 2015-05-08
- **Move dead itemstack conversion code to entities.py and revive it. Use it later for world conversion?** [`7f6e9bb`]
  **Files changed:** src/mceditlib/anvil/adapter.py, src/mceditlib/anvil/entities.py

### 2015-05-08
- **NBTEditorWidget now emits tagValueChanged when a value is changed. More signals soon, maybe?** [`69f7f36`]
  **Files changed:** src/mcedit2/widgets/inventory.py, src/mcedit2/widgets/nbttree/nbteditor.py, src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2015-05-08
- **Change "no model found" to a debuglog to remove spam** [`ef30293`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-05-08
- **Add display name label to inventory editor. Rename "name" to "displayName" in data files. Add fallback for items without a defined displayName.** [`30cf6c4`]
  xxx add unlocalizedName and load Minecraft translation files?
  **Files changed:** src/mcedit2/widgets/inventory.py, src/mcedit2/widgets/itemtype_list.py, src/mceditlib/blocktypes/itemtypes.py, src/mceditlib/blocktypes/tmp_itemblocks.json, src/mceditlib/blocktypes/tmp_items.json

### 2015-05-08
- **Note about BlockTypeSet vs ItemTypeSet** [`b474a8d`]
  **Files changed:** src/mceditlib/blocktypes/itemtypes.py

### 2015-05-08
- **Start working on createItemInSlot as a way of getting pre-parented ItemStacks** [`9e9402c`]
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-05-08
- **Changing the data in one of the item's fields updates all the others, including the NBT Editor.** [`d64b33d`]
  ...updating the NBT editor doesn't update the fields...
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2015-05-08
- **rawIDInput is now a spinbox with min and max** [`4b6633d`]
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2015-05-08
- **Don't return None for all data roles when the itemType can't be found - it's only needed for the icon** [`492fbca`]
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2015-05-08
- **Typing an unmapped internalName for a 1.7 ItemStack no longer raises an error** [`12aa394`]
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2015-05-08
- **Clicking an item in the itemtype list now changes the current itemstack's itemtype** [`dab82c9`]
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2015-05-08
- **Remove spacer below player Inventory box for now** [`392fa77`]
  **Files changed:** src/mcedit2/ui/panels/player.ui

### 2015-05-08
- **Hide the raw ID fields for 1.8 inventories, since the only ID is the internalName** [`91a0b95`]
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2015-05-08
- **Select Block is no longer undoable** [`18e0563`]
  **Files changed:** src/mcedit2/editortools/select_block.py

### 2015-05-08
- **InventoryView slot buttons now highlight when clicked** [`f12859e`]
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2015-05-08
- **ItemStackRef now raises NoParentError when trying to set the internalName of a 1.7 stack or the numeric ID of a 1.8 stack.** [`13554ee`]
  A parent is needed to find the parent world's itemTypes in order to convert the ID.
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-05-08
- **Do not try to auto-convert ItemStacks. This goes against the principle of preserving as much of the unknown parts of the save file as possible.** [`b1cbaf3`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-05-08
- **NBTEditor now operates on NBTCompound/ListRefs, which will propagate the 'dirty' flag up to their containing chunk.** [`e5aa872`]
  The silly editWasMade signal is now gone.
  **Files changed:** src/mcedit2/editortools/edit_chunk.py, src/mcedit2/panels/player.py, src/mcedit2/widgets/inspector.py, src/mcedit2/widgets/inventory.py, src/mcedit2/widgets/nbttree/nbteditor.py, src/mceditlib/nbtattr.py

### 2015-05-08
- **Close all panels when closing EditorSession** [`e0a7133`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-05-07
- **Don't make edits to the itemstack when a different stack is clicked** [`59b1448`]
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2015-05-07
- **Itemtype list is now searchable** [`0dd435c`]
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2015-05-07
- **ItemTypeList now has data roles for internal name and damage** [`71366ff`]
  **Files changed:** src/mcedit2/widgets/itemtype_list.py

### 2015-05-07
- **Fix ItemStackRef.id comparing the tagID to the tag class instead of the ID constant** [`3b6c8d3`]
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-05-07
- **Fix ItemType.repr trying to make None into digits** [`80dd2d2`]
  **Files changed:** src/mceditlib/blocktypes/itemtypes.py

### 2015-05-07
- **Inventory edits are now undoable** [`842bf33`]
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2015-05-06
- **Don't check isinstance(value, refClass) because refClass may not be a class (???)** [`3a50f07`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-05-06
- **Inventories are now editable** [`3a6e680`]
  **Files changed:** src/mcedit2/widgets/inventory.py

### 2015-05-05
- **Set debug=True for the pyinstaller exe to get more info about launch failures** [`93be64f`]
  **Files changed:** mcedit2.spec

### 2015-05-05
- **Add Item IDs from FML tag** [`7e1c7b7`]
  **Files changed:** src/mceditlib/anvil/adapter.py, src/mceditlib/blocktypes/itemtypes.py

### 2015-05-05
- **Make chests look like door-boxes for now. Chest graphics are kept as an entity model with the texture as a model sheet...** [`722f7ad`]
  **Files changed:** src/mceditlib/blocktypes/minecraft.json

### 2015-05-05
- **Inspector now has editor-widget classes registered for different tile entities** [`366aba8`]
  Add editors for Chest, Dispenser, Hopper
  **Files changed:** Add TileEntityRefs for above, Change InventoryEditor to accept a slotLayout, Move player slotLayout to player panel, Remove 'slotCount' from InventoryItemModel, which is no longer a ListModel because it freaks out when rowCount is 0, xxx move slotLayout to InventoryItemModel, src/mcedit2/panels/player.py, src/mcedit2/tileentities/__init__.py, src/mcedit2/tileentities/chest.py, src/mcedit2/ui/inspector.ui, src/mcedit2/widgets/inspector.py, src/mcedit2/widgets/inventory.py, src/mceditlib/anvil/entities.py

### 2015-05-02
- **BlockTypeButton is now able to respond to the editorSession's signal configuredBlocksChanged** [`460a6f1`]
  Changed textureAtlas back to editorSession
  **Files changed:** src/mcedit2/editorcommands/fill.py, src/mcedit2/editorcommands/find_replace.py, src/mcedit2/editorsession.py, src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/flood_fill.py, src/mcedit2/widgets/blockpicker.py

### 2015-05-02
- **Failure to load a item's block texture is no longer fatal** [`c1b59f5`]
  **Files changed:** src/mcedit2/widgets/itemtype_list.py

### 2015-05-02
- **Show both single-player and multiplayer entries for a player, if present.** [`d694afb`]
  **Files changed:** src/mcedit2/panels/player.py

### 2015-05-02
- **Add explicit "return None" to getItemInSlot** [`77f2e33`]
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-05-02
- **Players panel now embeds an InventoryEditor for the player's inventory.** [`948e1da`]
  **Files changed:** src/mcedit2/panels/player.py, src/mcedit2/ui/panels/player.ui

### 2015-05-02
- **Rough draft of inventory editor** [`222b49c`]
  **Files changed:** src/mcedit2/widgets/inventory.py, src/mcedit2/widgets/itemtype_list.py

### 2015-05-02
- **BlockTypePixmap now accepts a size arg** [`a648344`]
  **Files changed:** src/mcedit2/widgets/blocktype_list.py

### 2015-05-02
- **AnvilPlayerRef's Inventory is now a SlottedInventoryAttr** [`4e06ac9`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-05-02
- **AnvilPlayerRef's blockTypes aliases the adapter's** [`610225b`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-05-02
- **ItemTypeSet: handle "texture" being a list, fix __str__ after copying it from BlockType, add __len__** [`468b7fb`]
  **Files changed:** src/mceditlib/blocktypes/itemtypes.py

### 2015-05-02
- **Players panel now stays on top of main window** [`65bc6ab`]
  **Files changed:** src/mcedit2/panels/player.py

### 2015-05-02
- **Corrections to item jsons** [`f62bca5`]
  **Files changed:** src/mceditlib/blocktypes/tmp_itemblocks.json, src/mceditlib/blocktypes/tmp_items.json

### 2015-04-29
- **Display version info in world list** [`9a4aa12`]
  **Files changed:** src/mcedit2/worldlist.py

### 2015-04-29
- **AnvilWorldAdapter auto-converts item stacks to the detected world format.** [`95d0d63`]
  May be a bad idea, but I checked all of the item stacks in a well-played, heavily modded world and found nothing that this would wreck.
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-04-29
- **Make refClass mandatory for EntityListProxy** [`11ae0d6`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-04-29
- **Add ItemStackRef class and supporting elements to PC[Tile]EntityRef** [`62f4855`]
  EntityRefs now try to know their blockTypes. This mainly allows 1.7 worlds to return an item's internalName for its ID when accessed. With the caveat that an item created outside of a world and assigned a 1.7 ID will return a 1.7 ID until it is parented to a world. I can live with that.
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-04-29
- **AnvilWorldAdapter now detects from the level.dat whether the world is in 1.7 format or 1.8** [`66d6852`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-04-29
- **AnvilChunkData's Entities, TileEntities, and TileTicks now alias the corresponding tags in its rootTag** [`0ad4111`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-04-29
- **BlockTypeSet now remembers the item stack version for its world.** [`b5c8f7f`]
  **Files changed:** src/mceditlib/blocktypes/__init__.py

### 2015-04-29
- **WorldEditor uses a proxy list to avoid creating Tile/EntityRefs for each entity up front.** [`72e1f6c`]
  The Ref existing needs to by definition keep the chunk alive, so the chunk can't reference them.
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-04-29
- **Remove named and global blocktypes. Only create a new one with each new world adapter.** [`1cdc438`]
  Caching the .json files offers most of the benefits of a global. Now you are forced to get the WorldEditor's blocktypes, as you should.
  **Files changed:** And comment out InvEditChest and ZipSchematic until they are redone..., src/mceditlib/anvil/adapter.py, src/mceditlib/blocktypes/__init__.py, src/mceditlib/schematic.py

### 2015-04-29
- **lru_cache_object.should_decache now takes the cache key as input, for a very marginal speed gain** [`a8a91cd`]
  **Files changed:** src/mceditlib/cachefunc.py, src/mceditlib/worldeditor.py

### 2015-04-29
- **Chunks that don't unload during a cache miss are treated as hits so they won't immediately be tried next time.** [`4e2ef97`]
  **Files changed:** src/mceditlib/cachefunc.py

### 2015-04-29
- **Messed around with time_loadsave until I found out (duh) that the [Tile]EntityRefs are keeping the chunk alive indefinitely.** [`b0c26c1`]
  **Files changed:** src/mceditlib/test/time_loadsave.py

### 2015-04-29
- **NBTListProxy now wraps its elements in a proxy class that allows direct access to tag values, rather than to the tags themselves.** [`f0af0ef`]
  NBTCompoundListAttr also uses this proxy, wrapping the elements in a specified NBTCompoundRef subclass.
  **Files changed:** These allow NBTAttrs to be defined hierarchically., src/mceditlib/nbtattr.py

### 2015-04-29
- **Catch exception when loading missing/damaged resource pack** [`664ea46`]
  catch-all, eww
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2015-04-29
- **Pin versions of pyside and numpy.** [`1023d56`]
  PySide 1.2 changed to new-style signal mechanics
  **Files changed:** NumPy 1.9.0 heavily optimized array indexing, requirements.txt

### 2015-04-29
- **lazyprop.py -> mceditlib/util** [`b122cc9`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/__init__.py, src/mcedit2/panels/player.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/util/profiler.py, src/mcedit2/widgets/nbttree/nbteditor.py, src/mcedit2/worldview/camera.py, src/mcedit2/worldview/viewaction.py, src/mceditlib/util/lazyprop.py

### 2015-04-27
- **Ignore any exception while getting world info for the world list.** [`5608db1`]
  **Files changed:** src/mcedit2/worldlist.py

### 2015-04-27
- **Go back to fixed far plane for camera perspective to show more of the loadable chunks area** [`2fd2dd7`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-04-27
- **Fix "File Not Found" when listing contents of nonexistent resourcepacks dir** [`c173671`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2015-04-25
- **raycast: Add bounds check to fix FPS drop when casting out of bounds** [`bf47a41`]
  Remove currentChunk since WorldEditor finally has recentChunks
  **Files changed:** src/mcedit2/util/raycast.py

### 2015-04-25
- **Add tagClass property to TAG_List** [`10eec0e`]
  Returns the TAG_Value subclass appropriate for this list.
  **Files changed:** src/mceditlib/nbt.pyx

### 2015-04-25
- **Add ItemTypeSet class, add itemTypes attr to BlockTypeSet, add item jsons stolen from Unified.** [`f630bff`]
  Move json loading stuff for block/itemtypes to its own file
  **Files changed:** src/mceditlib/blocktypes/__init__.py, src/mceditlib/blocktypes/itemtypes.py, src/mceditlib/blocktypes/json_resources.py, src/mceditlib/blocktypes/tmp_itemblocks.json, src/mceditlib/blocktypes/tmp_items.json, src/mceditlib/items.py

### 2015-04-25
- **Cleanup** [`8ddfe26`]
  **Files changed:** src/mcedit2/util/load_ui.py

### 2015-04-25
- **WorldList: Tweak font size of Edit button, remove questionable properties** [`5a37172`]
  **Files changed:** src/mcedit2/ui/world_list.ui

### 2015-04-25
- **Allow find/replace to locate all entities and/or tile entities in the selection, if the searchName and searchValue checkboxes are unchecked and the target IDs fields are empty.** [`1074708`]
  **Files changed:** src/mcedit2/editorcommands/find_replace.py

### 2015-04-24
- **Add traces to MCEditApp startup to diagnose startup errors** [`5ff44bf`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-04-20
- **Zooming to found entities from NBT results works now.** [`21dab1e`]
  Zooming to tile entities worked, but entities were never tested!
  **Files changed:** src/mcedit2/editorcommands/find_replace.py, src/mceditlib/nbtattr.py, src/mceditlib/util/__init__.py

### 2015-04-20
- **Fix errors when getting repr for array types.** [`6e5952b`]
  Change tags to repr names using %r
  **Files changed:** src/mceditlib/nbt.pyx

### 2015-04-19
- **Biome brush cursor now uses the selected biome for its grass color!** [`e47592a`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py

### 2015-04-19
- **ShapedSelections can now return its positions as an iterator of tuples** [`1a0a7fb`]
  Allows non-optimized algorithms to use `selection.positions`
  **Files changed:** src/mceditlib/operations/__init__.py, src/mceditlib/selection/__init__.py

### 2015-04-19
- **Fix infinite loop when updateHeightmap calls setBlocks, which calls updateLights...** [`f625d1f`]
  setBlocks won't update lights if not asked to change blocks (duh)
  **Files changed:** src/mceditlib/multi_block.py

### 2015-04-19
- **Add Biome brush** [`1673b7f`]
  BrushModes create their options widgets
  **Files changed:** BrushModes return additional options that are added to brushTool's common options, BrushModes return their own bounding boxes instead of BrushTool, BrushModes create the level to be used for the brush cursor, Current BrushMode is saved in settings, src/mcedit2/editortools/brush/__init__.py, src/mcedit2/ui/editortools/brush.ui

### 2015-04-19
- **BlockTypeButton sets its new blocks before emitting blocksChanged** [`de6a39c`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2015-04-19
- **Move getSelectedResourceLoader to MCEditApp and have it use settings options in minecraftinstall** [`824553b`]
  Add settings options for current install, version, and resource pack.
  **Files changed:** Connect the combo boxes on WorldListWidget to these options, Fix a dumb bug that caused the default install to never be found., src/mcedit2/editorapp.py, src/mcedit2/util/minecraftinstall.py, src/mcedit2/worldlist.py

### 2015-04-18
- **Several fixes to minecraft installs** [`215dffd`]
  WorldList doesn't crash if no vanilla installs are present
  **Files changed:** WorldList asks EditorApp for a resource loader when previewing worlds (move this somewhere else?), MCInstallGroup only checks if a valid 1.8 install is present and doesn't require a vanilla install, MCInstallGroup can return a default ResourceLoader for the 1.8 install, Removed all traces of the bad-smelling "IVP" thing, replacing it with ResourceLoaders, src/mcedit2/editorapp.py, src/mcedit2/util/minecraftinstall.py, src/mcedit2/worldlist.py

### 2015-04-18
- **Fix stupid bug when putting biome name in status bar** [`deede41`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-04-18
- **Remove biome loggers from modelmesh** [`0ffaeb0`]
  **Files changed:** src/mcedit2/rendering/modelmesh.pyx

### 2015-04-18
- **ModelMesh now renders blocks with biome coloring** [`eac18e6`]
  Blocks need to be marked with biomeTintType in minecraft.json to use this.
  **Files changed:** src/mcedit2/rendering/blockmodels.pxd, src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/rendering/worldscene.py, src/mceditlib/blocktypes/__init__.py, src/mceditlib/blocktypes/minecraft.json

### 2015-04-18
- **Don't try to save changes when loading level.dat_old - fails when opened read-only** [`26a07a8`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-04-17
- **FakeBrushChunk now has a fake Biomes.** [`51c0abc`]
  Maybe someday we'll proxy the world's Biomes here and update them as the cursor moves?  Naaaah, too much mesh rebuilding.
  **Files changed:** src/mcedit2/editortools/brush/__init__.py

### 2015-04-17
- **Editor status bar now shows Biome name and ID** [`4bdd1ee`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py

### 2015-04-17
- **Add some new biome IDs from an NEI dump** [`db9fc62`]
  **Files changed:** src/mceditlib/anvil/biome_types.py, src/mceditlib/anvil/biomes.csv

### 2015-04-17
- **Add get/setBiomeID to WorldEditor, fix dumb typo in setBlockID** [`1830a1c`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-04-17
- **Need to catch NBTFormatError when loading level.dat** [`22abaed`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-04-17
- **Add a zip/mod/jarfile chooser to texture picker. Add a filter proxy to the texture picker and connect the search box.** [`e16ae10`]
  **Files changed:** src/mcedit2/resourceloader.py, src/mcedit2/ui/configure_blocks_dialog.ui, src/mcedit2/widgets/configureblocksdialog.py

### 2015-04-17
- **Add a "Remove" button to Configure Blocks** [`4533ce5`]
  **Files changed:** src/mcedit2/ui/configure_blocks_dialog.ui, src/mcedit2/widgets/configureblocksdialog.py

### 2015-04-17
- **Return a stupid value from AnvilPlayerRef.dimName instead of raising ValueError, need to fix this...** [`8833815`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-04-17
- **Fix a dumb bug in listing chunk positions that should have come up sooner** [`3c5448f`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-04-17
- **Fix changed TextureAtlas/BlockModels not being propagated to renderers** [`7d7de07`]
  **Files changed:** src/mcedit2/rendering/rendergraph.py, src/mcedit2/rendering/worldscene.py

### 2015-04-17
- **For some reason 'pos' can be a string here... need to figure that out** [`515e074`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-04-16
- **ConfigureBlocksDialog: All fields in the main block list (meta, opacity...) are now editable.** [`caa5e91`]
  **Files changed:** src/mcedit2/widgets/configureblocksdialog.py

### 2015-04-16
- **EditorSession now recreates the BlockModels and TextureAtlas whenever configured blocks are changed.** [`d951970`]
  Emit a configuredBlocks signal and connect it to EditorTab to update the world views.
  **Files changed:** BlockModels and TextureAtlas are created in setConfiguredBlocks now., src/mcedit2/editorsession.py, src/mcedit2/rendering/rendergraph.py, src/mcedit2/rendering/scenegraph.py, src/mcedit2/rendering/textureatlas.py, src/mcedit2/rendering/worldscene.py, src/mcedit2/worldview/cutaway.py, src/mcedit2/worldview/worldview.py

### 2015-04-16
- **Configured blocks are skipped when the internalName isn't mapped to an ID.** [`26bf820`]
  Configured blocks are added to blocktypes using a fakeState made from the meta value
  **Files changed:** src/mcedit2/editorsession.py

### 2015-04-16
- **FML loaded blocks are allowed to override and replace Vanilla blocks.** [`056a859`]
  This allows 1.8 blocks to be overridden. Still not allowed to remap Vanilla blocks to another ID.
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-04-16
- **Fix variant rotations rotating in the wrong direction** [`9ac8354`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-04-16
- **Fix blocks with no defined model using the wrong model** [`41cbbcc`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-04-16
- **EditorSession reads the configured blocks from ConfigureBlocksDialog on loading** [`c54a40c`]
  Changing configured blocks after loading still doesn't work - need to reload TextureAtlas, blocktypes, BlockModels for all views and emit a signal
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py, src/mcedit2/widgets/configureblocksdialog.py

### 2015-04-16
- **ConfigureBlocksDialog correctly selects the configured model name when a block is selected** [`037292e`]
  **Files changed:** src/mcedit2/widgets/configureblocksdialog.py

### 2015-04-16
- **BlockModels uses  the forcedModel, forcedModelTextures and forcedModelRotation for configured blocks.** [`200c649`]
  Only warns about missing states files for Vanilla blocks
  **Files changed:** Handles non-loaded textures and unbound texture vars by substituting UNKNOWN_BLOCK, UNKNOWN_MODEL is now a constant, src/mcedit2/rendering/blockmodels.pyx

### 2015-04-16
- **Make ResourceLoader.blockTexturePaths only return each path once.** [`0ef4458`]
  Having a 1.7 and a 1.8 jar in the path returns paths twice, and a resource pack returns them again.
  **Files changed:** src/mcedit2/resourceloader.py

### 2015-04-16
- **Add fake blockState with meta value for FML blocks** [`2589b07`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-04-16
- **Add default values to BlockType used for rendering. Remove special case for resourcePath (it should only point to valid states files or be None)** [`157e3d0`]
  **Files changed:** src/mceditlib/blocktypes/__init__.py

### 2015-04-16
- **Add a weird workaround for parented dialogs not positioning correctly** [`783909f`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-04-16
- **Use an item model for the texture image list for massive decrease in load times.** [`85e8665`]
  **Files changed:** src/mcedit2/ui/configure_blocks_dialog.ui, src/mcedit2/widgets/configureblocksdialog.py

### 2015-04-16
- **Don't add "minecraft:" to block names unless they obviously don't have a prefix** [`ac3bf2a`]
  **Files changed:** src/mceditlib/blocktypes/__init__.py

### 2015-04-15
- **Rough draft of configure blocks/items dialog.** [`47c3be1`]
  Allows adding unknown blocks detected via FML mapping, configuring their vital stats and assigning models and textures.
  **Files changed:** This data is currently unused by EditorSession, but is loaded from and saved to a config file, src/mcedit2/editorapp.py, src/mcedit2/ui/configure_blocks_dialog.ui, src/mcedit2/widgets/configureblocksdialog.py, src/mcedit2/widgets/prefsdialog.py

### 2015-04-15
- **Add blockTexturePaths to ResourceLoader** [`4de268e`]
  Searches for probable block textures and iterates over them.
  **Files changed:** src/mcedit2/resourceloader.py

### 2015-04-15
- **blocktype_list: Split TexturePixmap off of BlockTypePixmap** [`a324505`]
  Move this to another file?
  **Files changed:** src/mcedit2/widgets/blocktype_list.py

### 2015-04-15
- **Create a ResourceLoader for an EditorSession using its associated installation or instance** [`0984ff8`]
  EditorApp creates the ResourceLoader for an EditorSession before creating it.
  **Files changed:** EditorApp finds the install or instance and calls getResourceLoader on it, MMCInstance now has getResourceLoader, MMCInstance's getResourceLoader returns a loader with all installed mods in its search path. Not sure whether they should go before or after the MC jar(s).  (todo: add installed mods for vanilla installs, for homecooked mod packs/installs?), MultiMCInstall now has versions., MCInstallGroup is now responsible for finding a v1.8 jar, and searches all installs and MMC installs for one., ensureValidInstall checks for v1.8 and displays an appropriate dialog if it isn't found., All of this will make it easier to hook in a "Minecraft Assets Pack" as a separate download, and makes it possible to load assets from any installed mods, src/mcedit2/editorapp.py, src/mcedit2/editorsession.py, src/mcedit2/util/minecraftinstall.py

### 2015-04-15
- **Don't spam "Could not get blockstates resource" except for Vanilla blocks.** [`be2db03`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-04-15
- **Add 'unknown' flag to BlockType attributes and set it to True for FML-loaded types. Add unknownBlocks() to EditorSession** [`4c86ec5`]
  **Files changed:** src/mcedit2/editorsession.py, src/mceditlib/anvil/adapter.py, src/mceditlib/blocktypes/__init__.py

### 2015-04-15
- **Add function to ResourceLoader for listing all block models** [`03eb008`]
  xxx only lists Vanilla models. haven't looked at mods with models yet.
  **Files changed:** src/mcedit2/resourceloader.py

### 2015-04-15
- **Remove missing files from the recent files list when scanning it for world info. xxxx maybe not the right place for this...** [`c0910dd`]
  **Files changed:** src/mcedit2/worldlist.py

### 2015-04-15
- **Catch missing texture errors when creating pixmaps for textures (e.g. for blocktype list/picker)** [`3c4336e`]
  **Files changed:** src/mcedit2/widgets/blocktype_list.py

### 2015-04-15
- **Catch errors while loading the texture atlas for the debug widget that shows the atlas image.** [`9c91985`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-04-15
- **Make the editor app available as 'self' for the -eval argument** [`8b0d426`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-04-15
- **Cook quads after loading atlas textures, not immediately before using block models** [`5874818`]
  xxx get the order of initialization right. TextureAtlas needs a GL context to get the maximum texture size. WorldView wants a texture atlas in its constructor for no apparent reason. We'll need to make WorldView have changeable TextureAtlases so get that out of the constructor.
  **Files changed:** src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/rendering/textureatlas.py

### 2015-04-15
- **Change BlockModels/ModelMesh/TextureAtlas to use full paths to texture files** [`a1699c5`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pxd, src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/rendering/textureatlas.py

### 2015-04-14
- **Change ResourceLoader.openStream to use a full path** [`d12b09a`]
  Anticipating textures loaded from mods
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/textureatlas.py, src/mcedit2/resourceloader.py

### 2015-04-14
- **Begin working on Configure Blocks/Items dialog** [`ee5665a`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/ui/configure_blocks_dialog.ui, src/mcedit2/widgets/configureblocksdialog.py, src/mcedit2/widgets/prefsdialog.py

### 2015-04-14
- **Add removeEntities to WorldEditor and use it in RemoveEntitiesOperation** [`53606be`]
  Fixes a problem where EntityRefs were removed from a WorldEditorChunk without removing the underlying tags in the AnvilChunk[Data]
  **Files changed:** src/mceditlib/operations/entity.py, src/mceditlib/worldeditor.py

### 2015-04-14
- **Make raycast ignore non-air blocks found before the first air block.** [`a726923`]
  Gives more sensible behavior when the camera is inside solid blocks.
  **Files changed:** src/mcedit2/util/raycast.py

### 2015-04-14
- **Don't show [tile]entities behind walls, to reduce clutter.** [`a7d582e`]
  xxx relative polygon offsets, how?
  **Files changed:** src/mcedit2/rendering/renderstates.py

### 2015-04-14
- **Open the world starting in the single-player's current dimension, like in MCEdit 1** [`8d0310b`]
  **Files changed:** src/mcedit2/editorsession.py, src/mceditlib/anvil/adapter.py, src/mceditlib/worldeditor.py

### 2015-04-13
- **Fix rendering bug where chunks don't appear to fully update after undo.** [`0020362`]
  Make a copy of chunkNode.children to iterate while removing children.
  **Files changed:** This SHOULD have raised an error related to modifying a list while iterating it., src/mcedit2/rendering/worldscene.py

### 2015-04-13
- **Camera view distance and perspective options are saved.** [`19b0fde`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-04-13
- **Add convenience function to MCESettingsOption to connect a callback and immediately call it.** [`4d39928`]
  **Files changed:** src/mcedit2/util/settings.py

### 2015-04-13
- **Enable only the Blocks layer for MinimapWorldView** [`a43b41a`]
  This was hairy. Find a better way to control visible layers.
  **Files changed:** src/mcedit2/worldview/minimap.py, src/mcedit2/worldview/worldview.py

### 2015-04-13
- **Add chunk coords to pos on status bar** [`3b71c93`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-04-13
- **Remove ChunkNode.layers. Match layers using the ChunkNode's children's .layerName** [`3b430d7`]
  **Files changed:** src/mcedit2/rendering/chunknode.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/worldscene.py

### 2015-04-12
- **ChunkRenderInfo -> chunkupdate.py** [`4e6e074`]
  **Files changed:** src/mcedit2/rendering/chunknode.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/worldscene.py

### 2015-04-12
- **Add Options menu, implement "Enable Lighting Updates" setting, leave Preferences and Configure Blocks/Items unfinished.** [`9bf9a9c`]
  **Files changed:** src/mcedit2/appsettings.py, src/mcedit2/editorapp.py, src/mcedit2/ui/main_window.ui, src/mcedit2/ui/preferences_dialog.ui, src/mcedit2/widgets/prefsdialog.py, src/mceditlib/relight.py

### 2015-04-10
- **Remove nonstandard short array from tag types menu.** [`510e5d7`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbteditor.py

### 2015-04-10
- **Fix NameError in import dialog, set file type for export dialog.** [`a2b1858`]
  Add more export commands for different export formats? Via plugins?
  **Files changed:** src/mcedit2/editorsession.py

### 2015-04-10
- **WorldList is non-modal and does not block closing MCEdit.** [`0328b80`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/worldlist.py

### 2015-04-10
- **WorldView keeps its overlayNode through dimension changes** [`1a6aeed`]
  Ugh, tools need to connect to dimensionChanged and reset their overlays...
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-04-10
- **Get version number from git or _version.py (created by build system)** [`0b6bf64`]
  Display version number in title bar and about box.
  **Files changed:** src/mcedit2/__init__.py, src/mcedit2/editorapp.py, src/mcedit2/editorsession.py

### 2015-04-03
- **Fix blockpicker selecting multiple blocks while searching in single select mode** [`c487fc7`]
  Need to figure out the lag when searching by ID
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2015-04-03
- **Dimension changing is barely working.** [`1b7e709`]
  Still need to connect a few things to dimensionChanged, such as the inspector, and figure out what's wrong with the minimap
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py, src/mcedit2/worldview/worldview.py

### 2015-04-03
- **Catch ValueError when getting string form of LastPlayed time, to catch times before 1970** [`bb87a87`]
  **Files changed:** src/mcedit2/worldlist.py

### 2015-04-03
- **Restore "indiscriminate" option to flood fill** [`49f7ce5`]
  xxx add an API for telling flood fill that two block IDs are the same block in indiscriminate mode (e.g. grass and dirt)
  **Files changed:** src/mcedit2/editortools/flood_fill.py

### 2015-04-03
- **Fix copy-paste(?) bug in revisionhistory.copyToFolder** [`554137d`]
  **Files changed:** src/mceditlib/revisionhistory.py

### 2015-04-03
- **Deque does not support slice assignment** [`ff4424f`]
  too much numpy...
  **Files changed:** src/mceditlib/cachefunc.py

### 2015-04-03
- **Fix KeyError in region position cache, add set() as default value** [`0053f7e`]
  **Files changed:** src/mceditlib/anvil/worldfolder.py

### 2015-04-02
- **ResourceLoader wraps BadZipfile in an IOError so the try/catch around editor creation can catch it** [`5cbdd3a`]
  I'm so bad at error handling.
  **Files changed:** src/mcedit2/resourceloader.py

### 2015-04-02
- **Basic MultiMC integration** [`d184ff0`]
  MultiMC installs can be configured in the same window as MC installs.
  **Files changed:** Saves folders of instances from all MMC installs are added to the "Folder" popup., Also, the StackedWidget uses a blank widget to hide error messages and/or white GL widgets during world changes, src/mcedit2/ui/minecraft_installs.ui, src/mcedit2/ui/world_list.ui, src/mcedit2/util/minecraftinstall.py, src/mcedit2/worldlist.py

### 2015-04-01
- **lru_cache: Fix key being added to queue even when user_function raises an exception** [`c1d5d0b`]
  Also change try/catch to get(key, sentinel) because exceptions are more expensive and misses are common for my use-case
  **Files changed:** src/mceditlib/cachefunc.py

### 2015-04-01
- **lru_cache: Fix key being added to queue even when user_function raises an exception** [`694e39b`]
  Also change try/catch to get(key, sentinel) because exceptions are more expensive and misses are common for my use-case
  **Files changed:** src/mceditlib/cachefunc.py

### 2015-04-01
- **Some fixes to MCInstallDialog after previous work** [`c7a744d`]
  MCInstallGroup gains addInstall and removeInstall
  **Files changed:** Use the new "json" option type for options, src/mcedit2/util/minecraftinstall.py

### 2015-04-01
- **Show progress dialog while opening a world.** [`b592cc4`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py

### 2015-04-01
- **Fix duplicate items in version and resource pack lists after configuring installs** [`2001e8e`]
  **Files changed:** src/mcedit2/worldlist.py

### 2015-03-31
- **Move minecraftinstall.py globals into a singleton** [`1879499`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/test/time_loadmodels.py, src/mcedit2/util/minecraftinstall.py, src/mcedit2/worldlist.py

### 2015-03-30
- **Dumped map colors for all block states. Shows colors of wool and stained clay in minimap correctly.** [`4ef93f0`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/lowdetail.py, src/mceditlib/blocktypes/__init__.py, src/mceditlib/blocktypes/blockdumper/1.8/BlockDumper.java, src/mceditlib/blocktypes/minecraft_raw.json

### 2015-03-30
- **cachefuncs now iterate their keys instead of values** [`43e73ae`]
  **Files changed:** src/mceditlib/cachefunc.py, src/mceditlib/test/cache_test.py, src/mceditlib/worldeditor.py

### 2015-03-30
- **invalidLayers is a set. Don't replace it with something else.** [`11d1301`]
  **Files changed:** src/mcedit2/rendering/worldscene.py

### 2015-03-30
- **cachefuncs now do nothing if asked to decache a non-cached key** [`3c72a69`]
  **Files changed:** src/mceditlib/cachefunc.py

### 2015-03-30
- **Chunk meshes now return SceneNodes instead of VertexArrayBuffers** [`9a73b13`]
  This will allow them to return their own rendering commands instead of being limited to using VertexNodes.
  **Files changed:** src/mcedit2/rendering/blockmeshes.py, src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/chunkmeshes/lowdetail.py, src/mcedit2/rendering/chunkmeshes/terrainpop.py, src/mcedit2/rendering/chunkmeshes/tileticks.py, src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/rendering/scenegraph.py, src/mcedit2/rendering/worldscene.py, src/mceditlib/anvil/adapter.py

### 2015-03-30
- **Restore TileTicks accessor and renderer** [`ae7a9e1`]
  **Files changed:** src/mceditlib/anvil/adapter.py, src/mceditlib/worldeditor.py

### 2015-03-29
- **Entities, TileEntities etc can now be toggled on and off** [`ba53617`]
  Restored another MCEdit1 feature!
  **Files changed:** src/mcedit2/rendering/chunknode.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/layers.py, src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/rendering/scenegraph.py, src/mcedit2/rendering/worldscene.py, src/mcedit2/worldview/camera.py, src/mcedit2/worldview/cutaway.py, src/mcedit2/worldview/worldview.py

### 2015-03-29
- **Fix handling of boolean typed settings** [`88d7f61`]
  **Files changed:** src/mcedit2/util/settings.py

### 2015-03-29
- **Push reopened recent files to the top of the list.** [`a58ea07`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-03-29
- **Fix dumb bug in adding recent file** [`121fd99`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-03-29
- **lru_cache: Remove key from self.queue on decache** [`3fc4644`]
  **Files changed:** src/mceditlib/cachefunc.py

### 2015-03-29
- **Start working on show/hide view layers** [`c59d48c`]
  These small commits are mostly for testing the buildbot scheduler.
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-03-29
- **Bring camera's near plane closer, to match minecraft's** [`69e39bd`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-03-29
- **Exclude some IPython assets and modules from ipy spec. Finally exclude Tkinter for real.** [`cf6c724`]
  **Files changed:** mcedit2.spec

### 2015-03-29
- **Exclude secondary cython outputs from pyi spec** [`85605ab`]
  **Files changed:** hook-mcedit2.py

### 2015-03-26
- **zmq/libzmq.pyd can't find MSVCR90.dll because it isn't in the same directory as itself or in the current directory.** [`6b8cfad`]
  Just chdir to the pyinstaller temp dir until I fix the libzmq linkage in pyinstaller. Every other pyd is in the same directory as MSVCR.
  **Files changed:** src/mcedit2/main.py

### 2015-03-26
- **Remove hard-coded 'pathex' from mcedit2.spec - if `setup.py develop` is run, then these modules will be on the search path with built .pyds.** [`cfb71df`]
  xxx make sure `setup.py develop` is run before `pyinstaller mcedit2.spec`
  **Files changed:** mcedit2.spec

### 2015-03-23
- **Fix item clicks in NBT widget not using the sort/filter proxy.** [`09cc768`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbteditor.py

### 2015-03-23
- **Inspector handles edits properly (find something better than the editMade signal. NBTCompoundRef?)** [`52674af`]
  **Files changed:** src/mcedit2/widgets/inspector.py

### 2015-03-23
- **Fix type errors in _matchTag, fix walkNBT not actually recursing, fix copy-paste error in targetTileEntityIDs** [`00c0683`]
  **Files changed:** src/mcedit2/editorcommands/find_replace.py

### 2015-03-22
- **WorldList no longer reloads the world if the selected world is clicked again** [`28839b6`]
  **Files changed:** src/mcedit2/worldlist.py

### 2015-03-22
- **Fix a stupid bug in removing clients** [`eec86d3`]
  It was removing all clients except the one...
  **Files changed:** src/mcedit2/rendering/chunkloader.py

### 2015-03-22
- **Cache block ID and property .jsons, assuming they won't ever change since they are packaged with the app.** [`b224392`]
  The editor can amend a newly-created BlockTypeSet later for user-configured blocks, etc...
  **Files changed:** src/mceditlib/blocktypes/__init__.py

### 2015-03-22
- **Add "Recent Worlds" popup to world list widget** [`2aa6cd0`]
  **Files changed:** src/mcedit2/ui/world_list.ui, src/mcedit2/worldlist.py

### 2015-03-22
- **Row and Column accept numeric values as specifying fixed-width spacers** [`818aebd`]
  **Files changed:** src/mcedit2/widgets/layout.py

### 2015-03-22
- **Move RecentFilesSetting to appsettings.py, change MCESettingsOption to accept "json" as a type.** [`1b29350`]
  RecentFilesSetting now has a default value
  **Files changed:** src/mcedit2/appsettings.py, src/mcedit2/editorapp.py, src/mcedit2/util/settings.py

### 2015-03-21
- **Render the world list in WorldListWidget using a list view with an item delegate** [`d3e1f4c`]
  I'm getting the hang of this model-view-delegate thing (again)!
  **Files changed:** src/mcedit2/rendering/chunkloader.py, src/mcedit2/styles/mcedit2.qcss, src/mcedit2/ui/world_list.ui, src/mcedit2/worldlist.py

### 2015-03-21
- **Remove duplicate exceptions** [`effde4d`]
  **Files changed:** src/mceditlib/exceptions.py, src/mceditlib/pc/regionfile.py

### 2015-03-19
- **Fix worldlist editing the wrong world because its selection index is cleared when it closes** [`048bc03`]
  **Files changed:** src/mcedit2/worldlist.py

### 2015-03-19
- **levelbase.py -> fakechunklevel.py** [`c3dbb98`]
  **Files changed:** doc/mceditlib.rst, src/mceditlib/fakechunklevel.py, src/mceditlib/java.py, src/mceditlib/multi_block.py, src/mceditlib/schematic.py

### 2015-03-19
- **Remove dead code** [`30ad14e`]
  **Files changed:** src/mceditlib/levelbase.py

### 2015-03-19
- **Re-add blocktype conversion. Store block IDs in schematic files.** [`5477bd5`]
  This allows proper transfer of mod-added blocks (not items) between worlds saved by MinecraftForge 1.7. Items require (intricate) special handling, since they can be literally anywhere. As an added bonus, when items are handled correctly, items can be transferred between Minecraft 1.7 and 1.8, since 1.7 uses numeric item IDs while 1.8 uses textual ones.
  **Files changed:** Only block IDs are converted. In the past, block meta conversion was needed for Pocket Edition worlds (wool specifically) but since block IDs in MCPE are converging on PC edition IDs this may not be needed. In any case, we'll burn the MCPE bridge when we come to it., src/mceditlib/block_copy.py, src/mceditlib/blocktypes/__init__.py, src/mceditlib/levelbase.py, src/mceditlib/schematic.py, src/mceditlib/test/editing_test.py

### 2015-03-19
- **Fix [Tile]Entities not getting exported to schematics** [`34285d3`]
  Because nobody was really sure where they were being stored.
  **Files changed:** src/mceditlib/block_copy.py, src/mceditlib/levelbase.py, src/mceditlib/schematic.py

### 2015-03-19
- **Fix asterisk error when passing positions to BoundingBox constructor.** [`31dc9d4`]
  Why did this go undetected for so long!?
  **Files changed:** src/mceditlib/selection/__init__.py

### 2015-03-19
- **Catch rendering errors per-meshclass instead of aborting the entire chunk.** [`6395118`]
  **Files changed:** src/mcedit2/rendering/chunkupdate.py

### 2015-03-19
- **Add Import/Export menu and commands, start to get them working (finally)** [`d9236e6`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/move.py, src/mcedit2/library.py, src/mcedit2/util/directories.py, src/mceditlib/worldeditor.py

### 2015-03-19
- **Add Library to Windows menu** [`3ce14fd`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-03-19
- **Show first 8 elements of array types in NBT trees.** [`8d800bf`]
  Maybe later we'll add a hex editor...
  **Files changed:** src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2015-03-19
- **Adjust starting point up to player's eye-level (again...)** [`f2df2eb`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-03-18
- **NBT Replace converts string input to the appropriate type, and marks the [tile]entity ref dirty.** [`cf97cac`]
  **Files changed:** src/mcedit2/editorcommands/find_replace.py

### 2015-03-18
- **Add UUID field to PCEntityRef, add dirty() to PCEntityRef and PCTileEntityRef** [`ad5fe02`]
  Ugh... still need to decide whether a PC[Tile]EntityRef (and ItemRef and so on) refers to an entity in any revision (and can sometimes be invalid), or only a single revison (and can be read-only most of the time)
  **Files changed:** src/mceditlib/anvil/entities.py

### 2015-03-18
- **Clear tileEntity inspector when no tile entity, use correct type for entity UUID label** [`6f0deec`]
  **Files changed:** src/mcedit2/widgets/inspector.py

### 2015-03-18
- **Skip players with unparseable UUIDs** [`09b2884`]
  **Files changed:** src/mcedit2/panels/player.py

### 2015-03-18
- **THIS LINE apparently causes a crash when an EditorSession with any commands in its QUndoStack is garbage-collected.** [`087f6e1`]
  Probably related to Qt's object ownership rules. The QUndoStack owns any commands put into it.
  **Files changed:** src/mcedit2/editorapp.py

### 2015-03-18
- **Add "Collect Garbage" to debug menu** [`f9a00d9`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-03-18
- **Fix recent files menu only opening the last world in the menu (oops)** [`e0878ce`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-03-18
- **NBTEditor uses its sorting proxy model again. Now to find out what was so wrong with it that it was removed.** [`c28f8b9`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbteditor.py

### 2015-03-18
- **Clicking a result in the NBT find results will zoom to that entity or tileEntity** [`d753361`]
  **Files changed:** src/mcedit2/editorcommands/find_replace.py, src/mcedit2/editorsession.py

### 2015-03-18
- **When loading a world, start from the single-player's viewpoint like in MCEdit 1** [`ec5d658`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/worldview/fourup.py, src/mcedit2/worldview/iso.py, src/mcedit2/worldview/worldview.py

### 2015-03-18
- **After changing tag names, update the results view. Really ugly, need to do it through the model and not the results** [`5abd935`]
  **Files changed:** src/mcedit2/editorcommands/find_replace.py

### 2015-03-18
- **Implement "Replace All" function for NBT search** [`83826f7`]
  Add replacement inputs to results widget and synchronize them
  **Files changed:** Add default value to MCESettingsOption, src/mcedit2/editorcommands/find_replace.py, src/mcedit2/ui/find_replace_nbt.ui, src/mcedit2/ui/find_replace_nbt_results.ui, src/mcedit2/util/settings.py

### 2015-03-18
- **Started work on InspectorWidget** [`891649d`]
  (doot-do-doot-do-doot doot doot, woo woo)
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/select_block.py, src/mcedit2/ui/inspector.ui, src/mcedit2/widgets/inspector.py, src/mceditlib/worldeditor.py

### 2015-03-18
- **Add "Find again..." button to NBT results** [`9d3ba92`]
  **Files changed:** src/mcedit2/editorcommands/find_replace.py, src/mcedit2/ui/find_replace.ui, src/mcedit2/ui/find_replace_nbt_results.ui

### 2015-03-18
- **Begin separating the Select Block and Select Entity tools apart** [`8d295eb`]
  **Files changed:** src/mcedit2/assets/mcedit2/toolicons/edit_block.png, src/mcedit2/assets_raw/icons.svg, src/mcedit2/editorsession.py, src/mcedit2/editortools/__init__.py, src/mcedit2/editortools/select_block.py, src/mcedit2/editortools/select_entity.py, src/mcedit2/ui/editortools/select_block.ui, src/mcedit2/ui/editortools/select_entity.ui, src/mcedit2/ui/inspector.ui, src/mcedit2/widgets/inspector.py

### 2015-03-17
- **PlayersPanel doesn't error when a player doesn't have a UUID (for older worlds)** [`f2131a3`]
  **Files changed:** src/mcedit2/panels/player.py

### 2015-03-17
- **More work on NBT find/replace** [`e483424`]
  Find/replace settings are saved and loaded
  **Files changed:** Checkboxes are sync'd with field contents, Find results are shown in a separate dock widget, Result entries unambiguously point to an entity or tile entity, src/mcedit2/editorcommands/find_replace.py, src/mcedit2/editorsession.py, src/mcedit2/ui/find_replace_nbt.ui, src/mcedit2/ui/find_replace_nbt_results.ui

### 2015-03-17
- **Create a settings namespace object to group related settings** [`ae0e1be`]
  **Files changed:** src/mcedit2/util/settings.py

### 2015-03-17
- **xxx BlockPicker changed to need textureAtlas and not editorSession** [`f4b620d`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2015-03-17
- **Move several selection-related commands from SelectionTool's options panel to the Select menu in EditorSession** [`402bdb5`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/select.py

### 2015-03-17
- **Ensure that the map view gets cleaned up when the WorldListWidget is closed/hidden/rejected** [`5bacc8b`]
  Seems a bit redundant.
  **Files changed:** src/mcedit2/worldlist.py

### 2015-03-17
- **EditorTab weakly references EditorSession** [`864907a`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-03-17
- **Don't try to read Forge 1.6 "ID" mapping. These store Java class names and not textual block IDs. Worry about this much later, if at all.** [`1c50a30`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-03-17
- **In FML for MC 1.6, 'ordinal' is not the block/item's "meta" - I still don't know what it's for.** [`d1fd573`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-03-17
- **Remove the session's undoStack from the app's undoGroup when the session is closed.** [`a644802`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-03-17
- **Core ViewActions no longer reference the EditorSession, and weakly reference its EditorTab** [`e9de29b`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/worldview/viewaction.py

### 2015-03-17
- **NBTEditorWidget weakly references EditorSession** [`74f4c27`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbteditor.py

### 2015-03-17
- **PlayersPanel weakly references EditorSession** [`9de48d2`]
  **Files changed:** src/mcedit2/panels/player.py

### 2015-03-17
- **Update recent files on startup** [`33b1669`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-03-17
- **Only add actual block IDs from FML mapping (worry about items later)** [`c11fa41`]
  For some reason this required adding two new ID->name mappings to BlockTypeSet
  **Files changed:** src/mceditlib/anvil/adapter.py, src/mceditlib/blocktypes/__init__.py

### 2015-03-17
- **EditorTool is now responsible for creating its toolbar action and providing a signal for EditorSession to connect.** [`53099af`]
  EditorTool weakly references EditorSession.
  **Files changed:** EditorSession does not connect loader.allChunksDone to a lambda any more, src/mcedit2/editorsession.py, src/mcedit2/editortools/__init__.py

### 2015-03-17
- **ChunkLoader weakly references its clients, so as not to keep them alive and not require them to be unregistered on destruction** [`27c1fad`]
  **Files changed:** src/mcedit2/rendering/chunkloader.py

### 2015-03-16
- **Don't set mainWindow as parent of PlayerPanel** [`cd4a8aa`]
  Doing so keeps the editorSession alive as a side effect.
  **Files changed:** src/mcedit2/panels/player.py

### 2015-03-16
- **sessionDidChange now handles switching to a None session (no sessions open, etc)** [`9390d9e`]
  Clears panels and tools toolbars and removes session dockwidgets.
  **Files changed:** src/mcedit2/editorapp.py

### 2015-03-16
- **objgraphwidget: filter common primitive types out, change showBackrefs to have more useful output** [`53ab8b1`]
  **Files changed:** src/mcedit2/util/objgraphwidget.py

### 2015-03-16
- **Block button/picker no longer needs an EditorSession, just a TextureAtlas** [`dec908d`]
  **Files changed:** src/mcedit2/editorcommands/fill.py, src/mcedit2/editorcommands/find_replace.py, src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/flood_fill.py, src/mcedit2/rendering/textureatlas.py, src/mcedit2/widgets/blockpicker.py

### 2015-03-16
- **Destroy WorldView's renderGraph to ensure GL resources are released** [`11a5f19`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-03-16
- **WorldView.viewportMoved does pass the view as its only argument, so don't pretend it doesn't.** [`b8a3512`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/worldview/fourup.py, src/mcedit2/worldview/worldview.py

### 2015-03-16
- **objgraphwidget remembers its input field** [`3482bae`]
  also fix double argument in showBackrefs
  **Files changed:** src/mcedit2/util/objgraphwidget.py

### 2015-03-16
- **weakrefprop handles setting to None** [`6dea864`]
  **Files changed:** src/mcedit2/util/lazyprop.py

### 2015-03-16
- **weakrefprop can auto-assign its instance variable name** [`50ae15c`]
  **Files changed:** src/mcedit2/util/lazyprop.py

### 2015-03-16
- **Recent worlds submenu is back in action** [`4fdda2b`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/ui/main_window.ui

### 2015-03-16
- **destroyLists -> destroy, explicit None checks in scene/rendergraph** [`92de187`]
  **Files changed:** src/mcedit2/rendering/rendergraph.py, src/mcedit2/rendering/scenegraph.py

### 2015-03-16
- **objgraphwidget honors the width/depth for all graphs, handles aborted/failed graphs calmly** [`422f2c2`]
  **Files changed:** src/mcedit2/util/objgraphwidget.py

### 2015-03-16
- **Add a property descriptor for weakref'd members** [`dbe57e9`]
  **Files changed:** src/mcedit2/util/lazyprop.py

### 2015-03-16
- **Paste at current mouse position** [`80fe8f5`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-03-14
- **Add default maxsize for lfu_cache_object** [`50f333f`]
  **Files changed:** src/mceditlib/cachefunc.py

### 2015-03-14
- **Increase raycast distance to 2000, remove depth buffer read, add default distance for raycasts exceeding bounds (should it be 2000?)** [`bac501d`]
  I need to keep reminding myself that the depth buffer read will catch the cursor preview for brushes!
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-03-14
- **Fix cursor getting stuck on edge of world bounds when looking inward from outside the bounds.** [`01882cb`]
  **Files changed:** src/mcedit2/util/raycast.py

### 2015-03-14
- **Cache recently used WorldEditorChunks in a deque. Speeds up getBlock/setBlock by at least double.** [`9478bda`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-03-14
- **Get time_getsetblocks working again.** [`2dfe908`]
  setBlocks accepts single values for Blocks/Data
  **Files changed:** src/mceditlib/multi_block.py, src/mceditlib/test/time_getsetblocks.py

### 2015-03-14
- **WorldEditor now uses the newly modified lru_cache_object to cache the ChunkData it gets from the world adapter.** [`ff1a085`]
  **Files changed:** src/mceditlib/levelbase.py, src/mceditlib/worldeditor.py

### 2015-03-14
- **Modify functions in cachefunc.py for use with WorldEditor.** [`8c0739f`]
  **Files changed:** src/mceditlib/cachefunc.py

### 2015-03-14
- **Quick cache thrashing test** [`b059d93`]
  **Files changed:** src/mceditlib/test/cache_test.py

### 2015-03-14
- **Temporarily disable lighting** [`945c41b`]
  **Files changed:** src/mceditlib/relight.py

### 2015-03-14
- **Remove special handling for odd-shaped edge sections of odd-shaped worlds** [`1128532`]
  Odd-shaped worlds will not be allowed and schematics will provide full sized sections.
  **Files changed:** src/mceditlib/operations/block_fill.py

### 2015-03-14
- **Add a dummy syncToDisk so tests on schematics can run** [`251d632`]
  **Files changed:** src/mceditlib/schematic.py

### 2015-03-14
- **Fix blocktypes in testFill()** [`d92ad6e`]
  **Files changed:** src/mceditlib/test/editing_test.py

### 2015-03-13
- **Add sphinx extension to use non-underscore names in built html, so GH pages doesn't exclude them.** [`f0b3f79`]
  **Files changed:** doc/conf.py, doc/extensions/sphinx_nounderscore.py

### 2015-03-13
- **apidoc skeletons.** [`622dd47`]
  **Files changed:** doc/formats.rst, doc/index.rst, doc/mce.rst, doc/mcedit2.editorcommands.rst, doc/mcedit2.editortools.brush.rst, doc/mcedit2.editortools.rst, doc/mcedit2.handles.rst, doc/mcedit2.panels.rst, doc/mcedit2.prefs.rst, doc/mcedit2.rendering.chunkmeshes.rst, doc/mcedit2.rendering.rst, doc/mcedit2.rst, doc/mcedit2.ui.rst, doc/mcedit2.util.rst, doc/mcedit2.widgets.nbttree.rst, doc/mcedit2.widgets.rst, doc/mcedit2.worldview.rst, doc/mceditlib.anvil.rst, doc/mceditlib.blocktypes.rst, doc/mceditlib.operations.rst, doc/mceditlib.pc.rst, doc/mceditlib.rst, doc/mceditlib.selection.rst, doc/mceditlib.test.rst, doc/mceditlib.util.rst, doc/modules.rst, doc/storage.rst, doc/support.rst

### 2015-03-13
- **entitiesOnRay checks the distance from the (displayed) entity's center instead of its lower left. Increase checking distance.** [`640eec4`]
  **Files changed:** src/mcedit2/editortools/edit_entity.py

### 2015-03-13
- **NBT find/replace just barely works now. Separate NBT tab out of find_replace.ui into its own ui file.** [`7c30807`]
  **Files changed:** src/mcedit2/editorcommands/find_replace.py, src/mcedit2/ui/find_replace.ui, src/mcedit2/ui/find_replace_nbt.ui

### 2015-03-13
- **Make selection face hover have a thick outline, and make it cut into terrain. Change selection color to be different from unknown block.** [`e0e83cf`]
  Remove dead code.
  **Files changed:** src/mcedit2/editortools/select.py, src/mcedit2/rendering/selection.py

### 2015-03-10
- **BlockTypeSet accepts namePrefixes other than "minecraft:"** [`51d8cbf`]
  **Files changed:** src/mceditlib/blocktypes/__init__.py

### 2015-03-10
- **Correctly preserve selected blocks across searches, don't remove custom blocks** [`f5348df`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2015-03-10
- **Several fixes to (multi-)BlockPicker** [`6471064`]
  ID:meta searches are possible again, and use regex for better detection
  **Files changed:** Proxy model is used for the list of selected items on the right, Selected items correctly persist when the search box is used, Selected block(s) are displayed on the bottom using a BlockTypesItemWidget, Layout tweaks, src/mcedit2/ui/block_picker.ui, src/mcedit2/ui/block_picker_multiple.ui, src/mcedit2/widgets/blockpicker.py

### 2015-03-10
- **Fix BlockTypePicker init arguments** [`3045d94`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2015-03-09
- **Remove now-pointless BlockTypePicker singleton** [`0cc3bf4`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2015-03-09
- **Clean up Edit menu creation** [`e2c4959`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-03-09
- **Model-based blocktype list is more fully functional, uses QSortFilterProxyModel for searches** [`267f77c`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2015-03-09
- **Move replace command into to new find/replace dialog, begin work on NBT find/replace** [`99c6a18`]
  xxx FindReplaceDialog
  **Files changed:** src/mcedit2/editorcommands/find_replace.py, src/mcedit2/editorcommands/replace.py, src/mcedit2/editorsession.py, src/mcedit2/editortools/select.py, src/mcedit2/ui/find_replace.ui

### 2015-03-05
- **Begin converting BlockTypeListWidget to use a model and delegate instead of itemWidgets.** [`c49db92`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2015-03-05
- **Don't use numpy at all in cookQuads - compute array elements directly** [`e7b30cd`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-05
- **Static defs in buildBoxQuads** [`f4c997a`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-05
- **Static defs and common subexprs in BlockModels.__init__** [`ecf57c0`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-05
- **Don't uselessly create FloatBoxes, add static types in buildBoxQuads** [`81f35b8`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-05
- **Fix incorrect face used for shading in rotated variants (e.g. stairs)** [`9f1163f`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-05
- **Don't create a new ndarray for each getBlockFaceVertices call** [`ca58a60`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-05
- **Unwrap box and uv before putting them into FaceInfo, unwrap texCoords in getBlockFaceVertices** [`f412461`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-05
- **import numpy ->np, cnp, internalize faces.py, add FaceInfo class to replace big tuples, precalculate element rotation matrix, write out matrix multiplies, use array initializers in  getBlockFaceVertices** [`48241e0`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-04
- **Strings should be unicode, as those from json data also are** [`35eafa1`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-03
- **Add static types in cookQuads** [`ab70a16`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-03
- **Cache results of npRotate** [`f11115d`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-03
- **Compute variant rotation matrix only once for a variant, instead of for each element face** [`9901135`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-03
- **Add isList and isCompound to NBT tags, fix an earlier bad rename** [`d4aa289`]
  **Files changed:** src/mceditlib/nbt.pyx

### 2015-03-01
- **Fold storeQuads into cookQuads to avoid calling it a billion times for the unknown blocks. Sacrifice the cookedModels dict for now.** [`69380c9`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-03
- **Enable profiling?** [`ed75d29`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-03-03
- **Repair time_loadmodels after changes to minecraftinstall** [`c764599`]
  **Files changed:** src/mcedit2/test/time_loadmodels.py

### 2015-02-24
- **Multiple select block picker is now double column (needs checkboxes, better highlighting for left column)** [`08290ce`]
  **Files changed:** src/mcedit2/editorcommands/replace.py, src/mcedit2/ui/block_picker_multiple.ui, src/mcedit2/widgets/blockpicker.py

### 2015-02-24
- **Better entity stats in copyBlocks** [`ce2e67f`]
  **Files changed:** src/mceditlib/block_copy.py

### 2015-02-24
- **Add selection menu with just "Select All" for now** [`d9606b9`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/select.py

### 2015-02-18
- **Fix entity box rendering by disabling textures** [`5f83e97`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/entitymesh.py

### 2015-02-18
- **Edit entity properly saves changes by connecting to nbtEditor.editMade (why???)** [`4d4dfb0`]
  **Files changed:** src/mcedit2/editortools/edit_entity.py

### 2015-02-18
- **Improve log message in block_fill** [`fadc81f`]
  **Files changed:** src/mceditlib/operations/block_fill.py

### 2015-02-18
- **Overhead view has camera vector** [`9f15c42`]
  **Files changed:** src/mcedit2/worldview/overhead.py

### 2015-02-18
- **Catch SessionLockLost when saving a world** [`85ae144`]
  Display a message and close the world.
  **Files changed:** src/mcedit2/editorapp.py

### 2015-02-18
- **WorldEditorChunk now maintains a list of [Tile]EntityRefs instead of AnvilChunkData** [`fb64391`]
  **Files changed:** src/mceditlib/anvil/adapter.py, src/mceditlib/anvil/entities.py, src/mceditlib/schematic.py, src/mceditlib/worldeditor.py

### 2015-02-11
- **Allow findVersion1_8 to accept (1, 8, ".2")** [`e0f27e5`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2015-02-11
- **Excepthook override needs the logging module to work, so setup logging first.** [`8d416b7`]
  **Files changed:** src/mcedit2/main.py

### 2015-02-08
- **Mousewheel binding works, cutaway view shows view controls** [`57f6991`]
  **Files changed:** src/mcedit2/worldview/cutaway.py, src/mcedit2/worldview/viewaction.py, src/mcedit2/worldview/viewcontrols.py, src/mcedit2/worldview/worldview.py

### 2015-02-08
- **showProgress does eight iterations before showing the progress dialog** [`97d4cb0`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/util/showprogress.py, src/mcedit2/util/worldloader.py

### 2015-02-08
- **Only warn about unusable installs when disabling them** [`c8c577f`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2015-02-06
- **Try to handle worlds that have no players** [`a7436d7`]
  **Files changed:** src/mcedit2/panels/player.py

### 2015-02-06
- **findVersion1_8 doesn't take modded or prerelease versions** [`e17f7af`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2015-02-06
- **Fix minecraft installs dialog not opening when no installs are found** [`a7cf8b5`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2015-02-06
- **spacing** [`9cd98a5`]
  **Files changed:** mcedit2.spec

### 2015-02-04
- **Block picker allows ID:meta input** [`34d1e30`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2015-02-04
- **Add button to world list for choosing any world** [`c82507d`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/ui/world_list.ui, src/mcedit2/worldlist.py

### 2015-02-04
- **Show IDs in str(BlockType)** [`5a105ad`]
  **Files changed:** src/mceditlib/blocktypes/__init__.py

### 2015-02-02
- **ResourceLoader raises ResourceNotFound, log more info about resource loaders** [`091a869`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/textureatlas.py, src/mcedit2/resourceloader.py, src/mcedit2/util/minecraftinstall.py

### 2015-02-02
- **Set currentImport after removing a pending import, do some cleanup...** [`9899964`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-02-02
- **use absolute import in modelmesh to quell 'missing import' warning** [`699783e`]
  **Files changed:** src/mcedit2/rendering/modelmesh.pyx

### 2015-02-02
- **Changelog?** [`d93b3e8`]
  **Files changed:** CHANGES.rst, version.txt

### 2015-02-02
- **Read version from version.txt, note how to run mcedit2.spec** [`537e217`]
  **Files changed:** mcedit2.spec, setup.py, version.txt

### 2015-02-02
- **Return None for child items out of list/compound bounds - may be called when deleting the last item** [`b4683d5`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2015-02-02
- **beginInsertRows doesn't update the view unless the parent index's column is 0** [`eb89e99`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2015-02-02
- **internal pointers nonsense didn't solve anything** [`4087c9a`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2015-02-02
- **nbttreeview.py->nbteditor.py** [`e075fab`]
  **Files changed:** src/mcedit2/widgets/nbttree/__init__.py, src/mcedit2/widgets/nbttree/nbteditor.py

### 2015-02-01
- **More work on NBT editor** [`817c3a2`]
  Adding to Compounds is possible, showing a tag type menu.
  **Files changed:** Adding to an empty list uses the menu too, setModel changed to setRootTag, tries to keep tree expand state when model changes (e.g. due to revision change), chunk editor treeView->nbtEditor, src/mcedit2/editortools/edit_chunk.py, src/mcedit2/editortools/edit_entity.py, src/mcedit2/panels/player.py, src/mcedit2/ui/editortools/select_entity.ui, src/mcedit2/widgets/nbttree/nbttreemodel.py, src/mcedit2/widgets/nbttree/nbttreeview.py

### 2015-02-01
- **Only emit revisionChanged if the revision actually changed** [`1361389`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-02-01
- **Remove old terrain pngs (why are they even still here)** [`ad4ece2`]
  **Files changed:** src/mcedit2/assets/mcedit2/textures/terrain-classic.png, src/mcedit2/assets/mcedit2/textures/terrain-pocket.png, src/mcedit2/assets/mcedit2/textures/terrain.png

### 2015-02-01
- **NBT editor can add/remove from lists, displays root item as root instead of its children** [`e07cc96`]
  NBTTreeView -> NBTEditorWidget
  **Files changed:** editor is a QWidget again, added add/remove buttons, expands first column when child is expanded, removed vertical borders from tree views, items have isCompound and isList, src/mcedit2/editortools/edit_chunk.py, src/mcedit2/panels/player.py, src/mcedit2/styles/mcedit2.qcss, src/mcedit2/ui/editortools/edit_chunk.ui, src/mcedit2/ui/panels/player.ui, src/mcedit2/widgets/nbttree/nbttreemodel.py, src/mcedit2/widgets/nbttree/nbttreeview.py

### 2015-02-01
- **NBT tree allows value editing, Players list allows undo for NBT value changes, remove lines from tree branch icons for now** [`19a8c01`]
  **Files changed:** src/mcedit2/panels/player.py, src/mcedit2/styles/mcedit2.qcss, src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2015-01-30
- **Don't override model()** [`37943a0`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbttreeview.py

### 2015-01-30
- **PropertyList correctly emits dataChanged** [`cae00bb`]
  **Files changed:** src/mcedit2/widgets/propertylist.py

### 2015-01-30
- **NBTTreeView now inherits QTreeView and is used in place of QTreeView in several places.** [`a2329f5`]
  **Files changed:** src/mcedit2/editortools/edit_chunk.py, src/mcedit2/editortools/edit_entity.py, src/mcedit2/ui/editortools/edit_chunk.ui, src/mcedit2/ui/panels/player.ui, src/mcedit2/widgets/nbttree/nbttreeview.py

### 2015-01-30
- **Set NBT tree view with correct proxy model (oops)** [`17c9256`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbttreeview.py

### 2015-01-30
- **Extract NBT property list widget from players tool, change it to use a model+view+delegate combo.** [`dfc497e`]
  **Files changed:** src/mcedit2/panels/player.py, src/mcedit2/ui/panels/player.ui, src/mcedit2/widgets/__init__.py, src/mcedit2/widgets/propertylist.py

### 2015-01-30
- **Fix arguments to rowCount** [`97baf03`]
  **Files changed:** src/mcedit2/widgets/nbttree/nbttreemodel.py

### 2015-01-30
- **QTreeView borders, like in Qt Designer** [`bd0ac55`]
  **Files changed:** src/mcedit2/styles/mcedit2.qcss

### 2015-01-30
- **Capt_World's patron skin** [`2cbc356`]
  **Files changed:** src/mcedit2/assets_raw/playerskins/capt_world.png

### 2015-01-30
- **centerWidgetInScreen only optionally resizes the widget to a fraction of screen size** [`92377f3`]
  **Files changed:** src/mcedit2/util/screen.py, src/mcedit2/worldlist.py

### 2015-01-30
- **Unload cached players and metadata when changing revisions. (Move metadata up a level to WorldEditor?)** [`6541e45`]
  **Files changed:** src/mceditlib/anvil/adapter.py, src/mceditlib/worldeditor.py

### 2015-01-29
- **Emit revisionChanged signal from EditorSession** [`3710339`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-01-29
- **Even completely unknown blocks will render as question marks** [`7e50ea7`]
  **Files changed:** src/mcedit2/rendering/worldscene.py, src/mceditlib/blocktypes/__init__.py

### 2015-01-29
- **Factor out function centerWidgetInScreen** [`7163ac2`]
  **Files changed:** src/mcedit2/util/screen.py, src/mcedit2/worldlist.py

### 2015-01-26
- **Get rid of "No texture" spam** [`c1f4112`]
  **Files changed:** src/mcedit2/widgets/blocktype_list.py

### 2015-01-26
- **Add rendering for water and lava** [`f3df53e`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pxd, src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/chunknode.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/rendering/worldscene.py

### 2015-01-26
- **Model renderer has lighting (finally)** [`793ca4b`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pxd, src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx

### 2015-01-26
- **Move NBT tree widget stuff under widgets/** [`3022747`]
  **Files changed:** src/mcedit2/editortools/edit_chunk.py, src/mcedit2/editortools/edit_entity.py, src/mcedit2/panels/player.py, src/mcedit2/widgets/__init__.py, src/mcedit2/widgets/nbttree/__init__.py, src/mcedit2/widgets/nbttree/nbttreemodel.py, src/mcedit2/widgets/nbttree/nbttreeview.py

### 2015-01-26
- **Don't try to import folders from the schematic library** [`1dd9eef`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-01-26
- **Show the unknown block texture in block pickers and buttons** [`3beb641`]
  **Files changed:** src/mcedit2/widgets/blocktype_list.py

### 2015-01-25
- **Don't show progress bar for small brushes** [`50087e7`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py

### 2015-01-25
- **idmapping override for torches, since MC uses meta=5 for upright torches** [`f477a2b`]
  **Files changed:** src/mceditlib/blocktypes/__init__.py, src/mceditlib/blocktypes/idmapping.json

### 2015-01-25
- **Remove stray loggers in multi_block** [`e211a0d`]
  **Files changed:** src/mceditlib/multi_block.py

### 2015-01-25
- **Add question mark texture (and "model") for unknown blocks.** [`673689f`]
  **Files changed:** src/mcedit2/assets/mcedit2/block_unknown.png, src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/textureatlas.py, src/mceditlib/blocktypes/__init__.py, src/mceditlib/blocktypes/idmapping_raw.json

### 2015-01-25
- **Don't default to pc_blocktypes in WorldEditor, use adapter's types. (wtf)** [`e9f18b1`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-01-25
- **Default to meta=0 when getting blocktypes** [`ea7f17d`]
  **Files changed:** src/mceditlib/blocktypes/__init__.py

### 2015-01-25
- **Load internal names from FML name mapping. Can't do much besides name the blocks, though.** [`1dc9290`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-01-25
- **Show IDs next to internal name in status bar** [`c6f11a6`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-01-25
- **Start work on pluggable Generate tool** [`35a0883`]
  **Files changed:** src/mcedit2/editortools/generate.py, src/mcedit2/editortools/move.py

### 2015-01-24
- **Fix crash switching away from chunk tool** [`4508387`]
  **Files changed:** src/mcedit2/editortools/edit_chunk.py

### 2015-01-24
- **setBlocks now uses array broadcasting on its input arrays** [`6ac442a`]
  **Files changed:** src/mceditlib/multi_block.py

### 2015-01-24
- **Allow world adapter to not implement createChunk** [`bb89a78`]
  **Files changed:** src/mceditlib/worldeditor.py

### 2015-01-24
- **Add flag to world adapter to disable lighting updates** [`115362e`]
  **Files changed:** src/mceditlib/anvil/adapter.py, src/mceditlib/levelbase.py, src/mceditlib/worldeditor.py

### 2015-01-23
- **We have a createSchematic function, use it.** [`2b3a33c`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py, src/mceditlib/export.py, src/mceditlib/schematic.py, src/mceditlib/test/schematic_test.py, src/mceditlib/worldeditor.py

### 2015-01-23
- **Fix crash when adding new import** [`97f9e17`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-01-23
- **Move BoxHandle to its own file, move boxFaceUnderCursor to selection.py, remove findBlockFace as it is superseded by rayCast** [`cbd2b0d`]
  **Files changed:** src/mcedit2/editortools/move.py, src/mcedit2/editortools/select.py, src/mcedit2/handles/__init__.py, src/mcedit2/handles/boxhandle.py, src/mcedit2/rendering/selection.py, src/mcedit2/worldview/cutaway.py, src/mcedit2/worldview/worldview.py

### 2015-01-23
- **Move selection drag and resize logic into a BoxHandleNode class for reuse** [`c40e290`]
  **Files changed:** src/mcedit2/editortools/select.py, src/mcedit2/rendering/selection.py

### 2015-01-22
- **BlockTypeButton doesn't expand vertically by default, like a regular button** [`3db1cbb`]
  **Files changed:** src/mcedit2/widgets/blockpicker.py

### 2015-01-22
- **Combine a spin box and a slider into a SpinSlider widget. Use it in the brush tool.** [`97d9453`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/ui/editortools/brush.ui, src/mcedit2/widgets/spinslider.py

### 2015-01-22
- **Fix crash when tool has no cursorNode** [`07cdd46`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-01-21
- **Double clicking a pending import zooms to its center** [`93bd771`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/move.py, src/mceditlib/selection/__init__.py

### 2015-01-21
- **Move tool allows multiple pending imports** [`1878917`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/edit_chunk.py, src/mcedit2/editortools/move.py, src/mcedit2/editortools/select.py, src/mcedit2/rendering/selection.py

### 2015-01-21
- **Fix ObjectInspector's reload not working when a missing object reappears** [`883907a`]
  **Files changed:** src/mcedit2/widgets/objectinspector.py

### 2015-01-21
- **Encapsulate pending import info, preparing for multiple imports** [`f571965`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/move.py

### 2015-01-21
- **Change error handler to actually crash.** [`b4de6e2`]
  **Files changed:** src/mcedit2/main.py

### 2015-01-21
- **Begin work on schematic browser** [`abe03a4`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py, src/mcedit2/library.py

### 2015-01-20
- **Remove stray log from viewAction work** [`3d64f30`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-01-20
- **Profile augmentEvent** [`54c4ffa`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-01-20
- **Force view redraw when center pos changes** [`7c46cfa`]
  Updates minimap when turning camera
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-01-20
- **Fix zero division in profilerui** [`66e941e`]
  **Files changed:** src/mcedit2/util/profilerui.py

### 2015-01-20
- **Reduce distance rayCast advances through chunks from 2000 to a more reasonable maxDistance * 4** [`ecd796d`]
  Reduces lag when aiming at the sky
  **Files changed:** src/mcedit2/util/raycast.py

### 2015-01-20
- **Unify view actions to accept either mouse or keyboard bindings. Bindings are now saved to settings.** [`d94c07d`]
  To do: Mouse wheel bindings, get rid of the second binding popup
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/util/settings.py, src/mcedit2/worldview/camera.py, src/mcedit2/worldview/cutaway.py, src/mcedit2/worldview/fourup.py, src/mcedit2/worldview/iso.py, src/mcedit2/worldview/overhead.py, src/mcedit2/worldview/viewaction.py, src/mcedit2/worldview/viewcontrols.py, src/mcedit2/worldview/worldview.py

### 2015-01-20
- **Event focus set on world view when session is opened.** [`908cdb3`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py

### 2015-01-19
- **Put log file in user data folder** [`31af416`]
  **Files changed:** src/mcedit2/main.py

### 2015-01-19
- **Put data folder in ./ instead of ./src/mcedit when running from source (xxx work on this)** [`fe7e841`]
  **Files changed:** src/mcedit2/util/directories.py

### 2015-01-13
- **Disable tool shortcuts. Find out why they override view controls.** [`49e88fa`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-01-13
- **Camera view has WASD controls (again)** [`a1e3f48`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-01-13
- **WorldView doesn't update if centerPoint is called with the same value** [`474b7b1`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-01-13
- **WorldView accepts keyboard focus** [`a974465`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-01-13
- **More work on worldview keybinding editor - accepts keypresses including lone modifier keys** [`814fbfc`]
  **Files changed:** src/mcedit2/worldview/viewcontrols.py

### 2015-01-13
- **Add keypress action handlers to worldview** [`e2c81be`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-01-12
- **Keep profiler enabled for now** [`0f0c6a4`]
  **Files changed:** src/mcedit2/util/profiler.py

### 2015-01-11
- **SelectionScene is transparent again, now excludes air blocks using a composed selection** [`73806f9`]
  **Files changed:** src/mcedit2/editortools/select.py, src/mcedit2/rendering/selection.py

### 2015-01-11
- **WorldView mouseover handles ChunkNotPresent more sensibly** [`fb2ddf3`]
  **Files changed:** src/mcedit2/worldview/worldview.py

### 2015-01-11
- **ChunkGroupNode now implements containsChunkNode** [`cc8f475`]
  **Files changed:** src/mcedit2/rendering/chunknode.py

### 2015-01-11
- **readChunk now propagates ChunkNotPresent correctly** [`72619a8`]
  **Files changed:** src/mceditlib/anvil/adapter.py

### 2015-01-11
- **Move chunkPositions and sectionPositions to SelectionBox** [`a1c6e32`]
  Now requires min/max cx/cy/cz to be implemented by subclasses
  **Files changed:** src/mceditlib/selection/__init__.py

### 2015-01-11
- **VertexRenderNode no longer assumes anything about the enable state of GL_TEXTURE_2D on GL_TEXTURE0.** [`ecec87c`]
  It still assumes GL_TEXTURE1 is enabled if lightcoords are present.
  **Files changed:** src/mcedit2/rendering/rendergraph.py

### 2015-01-11
- **Camera view skips chunks outside the view distance (chunks that would be offered because the minimap loaded them)** [`aeac1b1`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-01-11
- **iterateChunks has a radius parameter, not diameter** [`ff17731`]
  **Files changed:** src/mcedit2/worldview/iso.py, src/mcedit2/worldview/worldview.py

### 2015-01-11
- **Increase camera view distance, ensure view distance changes update the scene** [`494c992`]
  **Files changed:** src/mcedit2/worldview/camera.py

### 2015-01-11
- **Add benchmark for SelectionScene** [`3d8e524`]
  **Files changed:** src/mcedit2/test/time_selectionrender.py

### 2015-01-11
- **Add a few more profiler calls** [`52b7261`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/rendering/chunkloader.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/selection.py, src/mcedit2/rendering/worldscene.py, src/mcedit2/util/worldloader.py, src/mcedit2/worldview/worldview.py

### 2015-01-11
- **Profiler widget shows time not taken by children in a "self" column, instead of as an (other) node.** [`8ad5823`]
  Zero div error in ProfilerWidget
  **Files changed:** src/mcedit2/util/profilerui.py

### 2015-01-11
- **Render small selections immediately** [`dbfdd44`]
  **Files changed:** src/mcedit2/rendering/selection.py

### 2015-01-11
- **Don't stupidly recalculate renderType lookup table for each section** [`641f0b3`]
  **Files changed:** src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/worldscene.py

### 2015-01-11
- **Profiler widget has alternating colors** [`af1b889`]
  **Files changed:** src/mcedit2/util/profilerui.py

### 2015-01-11
- **Remove some dead code** [`9b458c3`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/rendering/blockmeshes.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/util/profiler.py, src/mceditlib/worldeditor.py

### 2015-01-11
- **Fix error when changing shape with no selection** [`50425f3`]
  **Files changed:** src/mcedit2/editortools/select.py

### 2015-01-11
- **ShapeWidget buttons now toggle exclusively** [`bc3b186`]
  **Files changed:** src/mcedit2/widgets/shapewidget.py

### 2015-01-11
- **Whoops, ZeroBox is actually used** [`eab84b7`]
  **Files changed:** src/mceditlib/selection/__init__.py

### 2015-01-10
- **BoundingBox -> mceditlib.selection** [`68ea8b8`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/edit_entity.py, src/mcedit2/editortools/move.py, src/mcedit2/editortools/select.py, src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/selection.py, src/mcedit2/util/raycast.py, src/mcedit2/worldview/cutaway.py, src/mcedit2/worldview/worldview.py, src/mceditlib/anvil/adapter.py, src/mceditlib/block_copy.py, src/mceditlib/export.py, src/mceditlib/geometry.py, src/mceditlib/levelbase.py, src/mceditlib/schematic.py, src/mceditlib/selection/__init__.py, src/mceditlib/test/anvil_test.py, src/mceditlib/test/editing_test.py, src/mceditlib/test/extended_id_test.py, src/mceditlib/test/schematic_test.py, src/mceditlib/test/server_test.py, src/mceditlib/test/time_getsetblocks.py, src/mceditlib/worldeditor.py

### 2015-01-10
- **Select tool creates shaped selections.** [`44f601a`]
  Move brush shapes to mceditlib.selection
  **Files changed:** BrushShapeWidget -> mcedit2.widgets.shapewidget.ShapeWidget, New class SelectionScene renders selections as opaque white cubes, Change text of resize/deselect history commands, BoundingBox compares against None without crashing, has sensible repr again, src/mcedit2/assets/mcedit2/icons/shapes/diamond.png, src/mcedit2/assets/mcedit2/icons/shapes/round.png, src/mcedit2/assets/mcedit2/icons/shapes/square.png, src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/edit_chunk.py, src/mcedit2/editortools/move.py, src/mcedit2/editortools/select.py, src/mcedit2/rendering/chunknode.py, src/mcedit2/rendering/rendergraph.py, src/mcedit2/rendering/selection.py, src/mcedit2/ui/editortools/brush.ui, src/mcedit2/widgets/__init__.py, src/mcedit2/widgets/shapewidget.py, src/mceditlib/geometry.py, src/mceditlib/operations/block_fill.py, src/mceditlib/selection/__init__.py

### 2015-01-10
- **VertexArrayBuffer correctly computes its element offsets instead of using the weird guesses in rendering.slices** [`78ae056`]
  **Files changed:** src/mcedit2/rendering/rendergraph.py, src/mcedit2/rendering/vertexarraybuffer.py

### 2015-01-09
- **Clear undo block before saving, adjust comments** [`b743217`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-01-09
- **Add property list to player editor (xxx still needs undo, so does chunk property editor)** [`85cf180`]
  **Files changed:** src/mcedit2/panels/player.py, src/mcedit2/ui/panels/player.ui

### 2015-01-09
- **Move tool moves "things"** [`1cf8079`]
  **Files changed:** src/mcedit2/editortools/move.py

### 2015-01-08
- **Multi-command paste and move operations - Start, Move, Finish are recorded in history** [`b4e1c43`]
  ...and add some type info
  **Files changed:** src/mcedit2/command.py, src/mcedit2/editorsession.py, src/mcedit2/editortools/move.py, src/mcedit2/util/undostack.py, src/mcedit2/worldview/worldview.py, src/mceditlib/geometry.py, src/mceditlib/worldeditor.py

### 2015-01-08
- **Move undo block logic to new class MCEUndoStack, change Edit menu to use stack-provided actions** [`98ff85b`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/util/undostack.py

### 2015-01-08
- **Schematic adapter fakes Biomes array at the correct size** [`dcc326f`]
  **Files changed:** src/mceditlib/schematic.py

### 2015-01-08
- **Add NBTUUIDAttr class, add UUID attribute to player ref** [`318c1b1`]
  **Files changed:** src/mceditlib/anvil/adapter.py, src/mceditlib/nbtattr.py

### 2015-01-08
- **Hide hovers when selection tool is inactive** [`1d6b65f`]
  **Files changed:** src/mcedit2/editortools/select.py

### 2015-01-08
- **Non-NBT chunk editor (is this really necessary)** [`993d348`]
  **Files changed:** src/mcedit2/editortools/edit_chunk.py, src/mcedit2/panels/player.py, src/mcedit2/ui/editortools/edit_chunk.ui, src/mceditlib/anvil/adapter.py

### 2015-01-08
- **Player Tool is now a Panel** [`a206ab5`]
  **Files changed:** src/mcedit2/assets/mcedit2/icons/edit_player.png, src/mcedit2/editorapp.py, src/mcedit2/editorsession.py, src/mcedit2/editortools/__init__.py, src/mcedit2/editortools/edit_player.py, src/mcedit2/panels/__init__.py, src/mcedit2/panels/player.py, src/mcedit2/ui/main_window.ui, src/mcedit2/ui/panels/player.ui

### 2015-01-06
- **resourcePath finds stuff relative to parent dir of mcedit2 module (src/), not current dir** [`a83977d`]
  allows mcedit2 script to run from any dir in source installs
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/util/resources.py

### 2015-01-06
- **Get pyinstaller working again w/new install instructions** [`e0438af`]
  **Files changed:** hook-mcedit2.py, mcedit2.spec

### 2015-01-06
- **Move translation folder under src/mcedit2** [`559ffd4`]
  **Files changed:** src/mcedit2/i18n/en_US.ts

### 2015-01-06
- **Remove testing junk from replace.py** [`7cc2876`]
  **Files changed:** src/mcedit2/editorcommands/replace.py

### 2015-01-06
- **BlockTypePixmap shows textures again. BlockTypeSet[] prepends namePrefix again.** [`069001d`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/widgets/blocktype_list.py, src/mceditlib/blocktypes/__init__.py

### 2015-01-06
- **enable/disable Edit menu commands according to undo stack state and selection state** [`e0128c9`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-01-06
- **Only emit SelectionCoordinateWidget.boxChanged when the user changes the inputs** [`5adf245`]
  **Files changed:** src/mcedit2/editortools/select.py

### 2015-01-06
- **Add getBlock, returning a BlockType, and use it in findBlockFace (wait, isn't this replaced by raycast?)** [`ff8922f`]
  **Files changed:** src/mcedit2/worldview/worldview.py, src/mceditlib/worldeditor.py

### 2015-01-06
- **organize editorapp.py** [`29b5fa2`]
  **Files changed:** src/mcedit2/editorapp.py

### 2015-01-06
- **Move currentSelection and selectionChanged to EditorSession** [`de969c0`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/select.py

### 2015-01-06
- **session.selectionBox -> currentSelection** [`2074faa`]
  **Files changed:** src/mcedit2/editorcommands/fill.py, src/mcedit2/editorcommands/replace.py, src/mcedit2/editorsession.py, src/mcedit2/editortools/move.py, src/mcedit2/editortools/select.py

### 2015-01-05
- **EditorSession now provides menus, so it can toggle menuAction.enabled as needed** [`767a966`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py, src/mcedit2/ui/main_window.ui

### 2015-01-05
- **Tighten up margins in EditorTab** [`4c5b818`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-01-05
- **Check margin keyword to Row/Column is not None** [`244f9ad`]
  **Files changed:** src/mcedit2/widgets/layout.py

### 2015-01-05
- **Remove pyuic testing junk** [`ea730d0`]
  **Files changed:** src/mcedit2/ui/py/__init__.py, src/mcedit2/ui/py/ui_block_picker.py

### 2015-01-05
- **CONTRIBUTING.md: mcedit 1.x issues** [`757a16d`]
  **Files changed:** CONTRIBUTING.md

### 2015-01-05
- **LICENSE.txt -> LICENSE.md** [`c9b6a97`]
  **Files changed:** LICENSE.md

### 2015-01-04
- **Colorize leaves, grass, herbs, redstone, etc.  Disable cython profiling. Change offsets to size_t just in case.** [`48b615a`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx

### 2015-01-04
- **...and just disable it entirely for now. lots of things don't look right until the alpha is fixed.** [`7c87049`]
  **Files changed:** src/mcedit2/rendering/textureatlas.py

### 2015-01-04
- **check bool(GL.glGenerateMipmap) xxxx don't use it at all, generate mips w/numpy** [`fb85782`]
  **Files changed:** src/mcedit2/rendering/textureatlas.py, src/mcedit2/util/glutils.py

### 2015-01-04
- **Destroy lists when removing children from rendergraph, make parent link a weakref to avoid cyclic refs/gc** [`3806d4b`]
  **Files changed:** src/mcedit2/rendering/rendergraph.py, src/mcedit2/rendering/scenegraph.py

### 2015-01-04
- **cullface is an int, compare with None** [`bdb8233`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-01-04
- **updateStatusLabel with None when no block is found** [`238e0a1`]
  **Files changed:** src/mcedit2/editorsession.py

### 2015-01-04
- **Store cooked models as structs instead of list of tuples - now the important loops are all white (C code) but it leaks memory** [`801307e`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pxd, src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx

### 2015-01-04
- **Only cook quads when needed - speeds up world list** [`8649904`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/rendering/textureatlas.py

### 2015-01-03
- **ignore nbt.html** [`cd632c6`]
  **Files changed:** .gitignore

### 2015-01-03
- **cookedModelsByID is now an object array instead of a dict** [`62c15ac`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx

### 2015-01-03
- **set xyzuvs coords by adding ndarray, not tuple** [`1eab140`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx

### 2015-01-03
- **cdef section.Data** [`a4c6ae6`]
  **Files changed:** src/mcedit2/editortools/brush/__init__.py, src/mcedit2/rendering/modelmesh.pyx

### 2015-01-03
- **fix uv scaling for animated (non-square) textures** [`b0e84c9`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-01-03
- **Profile pyx** [`e64508e`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx

### 2015-01-03
- **Don't cook quads if testing without GL** [`d200e31`]
  **Files changed:** src/mcedit2/rendering/textureatlas.py

### 2015-01-03
- **disable bounds checking** [`472f248`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx

### 2015-01-03
- **rotate textures without looping** [`af03a74`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-01-03
- **cdef several int/float variables** [`1e80460`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx, src/mceditlib/blocktypes/__init__.py

### 2015-01-03
- **store cooked models by id, meta. remove face from quad tuples** [`c23cad6`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx

### 2015-01-03
- **Break apart loops into cythonizable ones** [`d997a44`]
  **Files changed:** src/mcedit2/rendering/modelmesh.pyx

### 2015-01-03
- **Allow modelMesh.createVertexArrays to optionally return an iterator** [`cd52c59`]
  **Files changed:** src/mcedit2/rendering/chunkupdate.py

### 2015-01-03
- **extract method rotateVertices** [`c39f2c1`]
  xxx extract method
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-01-03
- **extract method buildBoxQuads** [`5e2b792`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-01-03
- **cache blockstate jsons** [`1b766e5`]
  **Files changed:** src/mcedit2/rendering/blockmodels.pyx

### 2015-01-03
- **move block models to cython** [`e63ced7`]
  **Files changed:** .gitignore, setup.py, src/mcedit2/rendering/blockmodels.pyx, src/mcedit2/rendering/modelmesh.pyx, src/mcedit2/rendering/textureatlas.py, src/mcedit2/test/time_loadmodels.py, src/mcedit2/util/minecraftinstall.py, src/mcedit2/util/objgraphwidget.py

### 2015-01-02
- **Remove pywin32 from requirements** [`009ea2f`]
  **Files changed:** README.md, requirements.txt

### 2015-01-02
- **Merge branch 'pr/n8_MasterEjay'** [`bd74574`]

### 2015-01-02
- **Add more detail to the Linux / OSX instructions** [`97d37c8`]
  **Files changed:** README.md

### 2015-01-02
- **Proffread README.md** [`080a8b6`]
  **Files changed:** README.md

### 2015-01-02
- **Progress logs when loading models** [`3b63df5`]
  **Files changed:** src/mcedit2/rendering/blockmodels.py

### 2015-01-02
- **Fix error in low detail when any column height=0 (still displays height=1 as empty)** [`4ccd17e`]
  **Files changed:** src/mcedit2/rendering/chunkmeshes/lowdetail.py

### 2015-01-02
- **Pass None when creating GL_PROXY_TEXTURE_2D in the hopes it will be interpreted as a null pointer** [`caf8ef6`]
  **Files changed:** src/mcedit2/rendering/textureatlas.py

### 2015-01-02
- **Handle element rotation, texture rotation, variant rotation, correct texture alignment problems and shading values** [`4f2e649`]
  **Files changed:** src/mcedit2/rendering/blockmodels.py, src/mceditlib/anvil/adapter.py, src/mceditlib/blocktypes/__init__.py, src/mceditlib/geometry.py

### 2015-01-02
- **Enable face culling for textureatlas nodes** [`0ac2511`]
  **Files changed:** src/mcedit2/rendering/rendergraph.py

### 2015-01-02
- **Move Player command works, use player's rotation when opening first view** [`636934b`]
  **Files changed:** src/mcedit2/editorsession.py, src/mcedit2/editortools/edit_player.py, src/mceditlib/anvil/adapter.py, src/mceditlib/worldeditor.py

### 2015-01-02
- **Status bar shows blockState under the cursor** [`f8025c8`]
  **Files changed:** src/mcedit2/editorapp.py, src/mcedit2/editorsession.py

### 2015-01-01
- **TAG_COMPOUND -> ID_COMPOUND et al** [`997178e`]
  **Files changed:** src/mcedit2/nbt_treemodel.py, src/mceditlib/nbt.pyx

### 2015-01-01
- **dump renderType as int, not string, handle maxLOD=0 in textureAtlas** [`cac8d30`]
  **Files changed:** src/mcedit2/rendering/blockmodels.py, src/mcedit2/rendering/textureatlas.py, src/mceditlib/blocktypes/minecraft_raw.json

### 2015-01-01
- **BlockModelMesh -> modelmesh.py** [`bcf904c`]
  **Files changed:** src/mcedit2/rendering/blockmodels.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/modelmesh.py

### 2015-01-01
- **dump resourceVariants from minecraft** [`8ce6571`]
  **Files changed:** src/mcedit2/rendering/blockmodels.py, src/mceditlib/blocktypes/blockdumper/1.8/BlockDumper.java, src/mceditlib/blocktypes/minecraft_raw.json

### 2014-12-31
- **Models have directional shading, texture rotation is observed** [`3f9c56c`]
  **Files changed:** src/mcedit2/rendering/blockmodels.py, src/mcedit2/rendering/chunkupdate.py

### 2014-12-31
- **Remove all old block renderers, read block models from minecraft.jar, update minecraft_raw.json and idmapping.json** [`ee22c24`]
  BlockTypeSet is indexed with internalName, blockState as well as ID, meta
  **Files changed:** blockData -> meta, BoundingBox init with maximum=, src/mcedit2/editorsession.py, src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/flood_fill.py, src/mcedit2/rendering/blockmeshes.py, src/mcedit2/rendering/blockmeshes_old/__init__.py, src/mcedit2/rendering/blockmeshes_old/crossedsquares.py, src/mcedit2/rendering/blockmeshes_old/emptysections.py, src/mcedit2/rendering/blockmeshes_old/fence.py, src/mcedit2/rendering/blockmeshes_old/ladder.py, src/mcedit2/rendering/blockmeshes_old/minecarttrack.py, src/mcedit2/rendering/blockmeshes_old/redstonedust.py, src/mcedit2/rendering/blockmeshes_old/stairs.py, src/mcedit2/rendering/blockmeshes_old/standard.py, src/mcedit2/rendering/blockmeshes_old/torch.py, src/mcedit2/rendering/blockmeshes_old/vine.py, src/mcedit2/rendering/blockmeshes_old/water.py, src/mcedit2/rendering/blockmodels.py, src/mcedit2/rendering/chunkmeshes/__init__.py, src/mcedit2/rendering/chunkmeshes/entitymesh.py, src/mcedit2/rendering/chunkmeshes/lowdetail.py, src/mcedit2/rendering/chunkmeshes/terrainpop.py, src/mcedit2/rendering/chunkmeshes/tileticks.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/textureatlas.py, src/mcedit2/rendering/worldscene.py, src/mcedit2/widgets/blockpicker.py, src/mcedit2/widgets/blocktype_list.py, src/mcedit2/worldlist.py, src/mcedit2/worldview/worldview.py, src/mceditlib/blocktypes/__init__.py, src/mceditlib/blocktypes/blockdumper/BlockDumper.java, src/mceditlib/blocktypes/idmapping.json, src/mceditlib/blocktypes/legacy_ids.json, src/mceditlib/blocktypes/minecraft.json, src/mceditlib/blocktypes/minecraft_old.json, src/mceditlib/blocktypes/minecraft_raw.json, src/mceditlib/blocktypes/named_ids.py, src/mceditlib/blocktypes/rendertypes.py, src/mceditlib/faces.py, src/mceditlib/geometry.py, src/mceditlib/operations/block_fill.py, src/mceditlib/test/editing_test.py, src/mceditlib/test/time_fill.py

### 2014-12-30
- **Move old minecraft.json away** [`0bc2fc5`]
  **Files changed:** src/mceditlib/blocktypes/minecraft_old.json

### 2014-12-29
- **move old blockmeshes away** [`8a6c75e`]
  **Files changed:** src/mcedit2/rendering/blockmeshes_old/__init__.py, src/mcedit2/rendering/blockmeshes_old/blockmesh.py, src/mcedit2/rendering/blockmeshes_old/crossedsquares.py, src/mcedit2/rendering/blockmeshes_old/emptysections.py, src/mcedit2/rendering/blockmeshes_old/entitymesh.py, src/mcedit2/rendering/blockmeshes_old/fence.py, src/mcedit2/rendering/blockmeshes_old/ladder.py, src/mcedit2/rendering/blockmeshes_old/lowdetail.py, src/mcedit2/rendering/blockmeshes_old/minecarttrack.py, src/mcedit2/rendering/blockmeshes_old/redstonedust.py, src/mcedit2/rendering/blockmeshes_old/stairs.py, src/mcedit2/rendering/blockmeshes_old/standard.py, src/mcedit2/rendering/blockmeshes_old/terrainpop.py, src/mcedit2/rendering/blockmeshes_old/tileticks.py, src/mcedit2/rendering/blockmeshes_old/torch.py, src/mcedit2/rendering/blockmeshes_old/vine.py, src/mcedit2/rendering/blockmeshes_old/water.py

### 2014-12-31
- **minecraftinstall matches 1.8 with no minor rev** [`fa3b03a`]
  **Files changed:** src/mcedit2/util/minecraftinstall.py

### 2015-01-02
- **Developer setup instructions, fix entry points in setup.py, fix requirements.txt** [`2fe930e`]
  **Files changed:** .gitignore, README.md, requirements.txt, setup.py

### 2015-01-02
- **Make objgraph optional** [`c5a30d1`]
  **Files changed:** src/mcedit2/util/objgraphwidget.py

### 2015-01-02
- **resourcePath raises an error with the requested and full paths if the file does not exist.** [`0684400`]
  **Files changed:** src/mcedit2/util/resources.py

### 2014-12-29
- **todo.txt -> GH Issue** [`eb15c54`]
  **Files changed:** notes/todo.txt

### 2015-01-01
- **get `setup.py build_ext` working again** [`ee8ed74`]
  **Files changed:** setup.py

### 2014-12-28
- **Add README, CONTRIBUTING** [`8fdd19f`]
  and some other stuff...
  **Files changed:** CONTRIBUTING.md, LICENSE.txt, README.md, notes/todo.txt, src/mcedit2/worldview/cutaway.py, src/mceditlib/anvil/adapter.py, src/mceditlib/nbtattr.py, src/mceditlib/worldeditor.py

### 2014-12-27
- **Bury skeletons** [`a25c0ab`]
  **Files changed:** .gitattributes, .gitignore, LICENSE.txt, doc/Makefile, doc/conf.py, doc/formats.rst, doc/index.rst, doc/make.bat, doc/mce.rst, doc/storage.rst, doc/support.rst, hook-mcedit2.py, i18n/en_US.ts, mcedit2.spec, mcediticon.ico, notes/chunk.txt, notes/todo.txt, requirements-mceditlib.txt, requirements.txt, setup.py, src/mcedit2/__init__.py, src/mcedit2/assets/mcedit2/dialogicons/dialog-error-7.png, src/mcedit2/assets/mcedit2/dialogicons/dialog-information-3.png, src/mcedit2/assets/mcedit2/dialogicons/dialog-warning-2.png, src/mcedit2/assets/mcedit2/dialogicons/dialog-warning-4.png, src/mcedit2/assets/mcedit2/icons/add.png, src/mcedit2/assets/mcedit2/icons/remove.png, src/mcedit2/assets/mcedit2/mcediticon.png, src/mcedit2/assets/mcedit2/mcediticonbig.png, src/mcedit2/assets/mcedit2/nbticons/LICENSE.txt, src/mcedit2/assets/mcedit2/nbticons/array.png, src/mcedit2/assets/mcedit2/nbticons/byte.png, src/mcedit2/assets/mcedit2/nbticons/compound.png, src/mcedit2/assets/mcedit2/nbticons/double.png, src/mcedit2/assets/mcedit2/nbticons/float.png, src/mcedit2/assets/mcedit2/nbticons/int.png, src/mcedit2/assets/mcedit2/nbticons/list.png, src/mcedit2/assets/mcedit2/nbticons/long.png, src/mcedit2/assets/mcedit2/nbticons/short.png, src/mcedit2/assets/mcedit2/nbticons/text.png, src/mcedit2/assets/mcedit2/textures/compass.png, src/mcedit2/assets/mcedit2/textures/compass_small.png, src/mcedit2/assets/mcedit2/textures/terrain-classic.png, src/mcedit2/assets/mcedit2/textures/terrain-pocket.png, src/mcedit2/assets/mcedit2/textures/terrain.png, src/mcedit2/assets/mcedit2/toolicons/brush.png, src/mcedit2/assets/mcedit2/toolicons/edit_chunk.png, src/mcedit2/assets/mcedit2/toolicons/edit_entity.png, src/mcedit2/assets/mcedit2/toolicons/edit_player.png, src/mcedit2/assets/mcedit2/toolicons/flood_fill.png, src/mcedit2/assets/mcedit2/toolicons/generate.png, src/mcedit2/assets/mcedit2/toolicons/move.png, src/mcedit2/assets/mcedit2/toolicons/select_blocks.png, src/mcedit2/assets_raw/icons.svg, src/mcedit2/command.py, src/mcedit2/editorapp.py, src/mcedit2/editorcommands/__init__.py, src/mcedit2/editorcommands/fill.py, src/mcedit2/editorcommands/replace.py, src/mcedit2/editorsession.py, src/mcedit2/editortools/__init__.py, src/mcedit2/editortools/brush/__init__.py, src/mcedit2/editortools/edit_chunk.py, src/mcedit2/editortools/edit_entity.py, src/mcedit2/editortools/edit_player.py, src/mcedit2/editortools/flood_fill.py, src/mcedit2/editortools/generate.py, src/mcedit2/editortools/move.py, src/mcedit2/editortools/select.py, src/mcedit2/main.py, src/mcedit2/nbt_treemodel.py, src/mcedit2/prefs/__init__.py, src/mcedit2/prefs/prefswindow.py, src/mcedit2/prefs/raw.py, src/mcedit2/rendering/__init__.py, src/mcedit2/rendering/blockmeshes/__init__.py, src/mcedit2/rendering/blockmeshes/blockmesh.py, src/mcedit2/rendering/blockmeshes/crossedsquares.py, src/mcedit2/rendering/blockmeshes/emptysections.py, src/mcedit2/rendering/blockmeshes/entitymesh.py, src/mcedit2/rendering/blockmeshes/fence.py, src/mcedit2/rendering/blockmeshes/ladder.py, src/mcedit2/rendering/blockmeshes/lowdetail.py, src/mcedit2/rendering/blockmeshes/minecarttrack.py, src/mcedit2/rendering/blockmeshes/redstonedust.py, src/mcedit2/rendering/blockmeshes/stairs.py, src/mcedit2/rendering/blockmeshes/standard.py, src/mcedit2/rendering/blockmeshes/terrainpop.py, src/mcedit2/rendering/blockmeshes/tileticks.py, src/mcedit2/rendering/blockmeshes/torch.py, src/mcedit2/rendering/blockmeshes/vine.py, src/mcedit2/rendering/blockmeshes/water.py, src/mcedit2/rendering/chunkloader.py, src/mcedit2/rendering/chunknode.py, src/mcedit2/rendering/chunkupdate.py, src/mcedit2/rendering/compass.py, src/mcedit2/rendering/cubes.py, src/mcedit2/rendering/depths.py, src/mcedit2/rendering/frustum.py, src/mcedit2/rendering/geometrycache.py, src/mcedit2/rendering/layers.py, src/mcedit2/rendering/lightmap.py, src/mcedit2/rendering/loadablechunks.py, src/mcedit2/rendering/rendergraph.py, src/mcedit2/rendering/renderstates.py, src/mcedit2/rendering/scenegraph.py, src/mcedit2/rendering/sky.py, src/mcedit2/rendering/slices.py, src/mcedit2/rendering/textureatlas.py, src/mcedit2/rendering/vertexarraybuffer.py, src/mcedit2/rendering/worldscene.py, src/mcedit2/resourceloader.py, src/mcedit2/styles/mcedit2.qcss, src/mcedit2/test/time_raycast.py, src/mcedit2/ui/Makefile, src/mcedit2/ui/__init__.py, src/mcedit2/ui/block_picker.ui, src/mcedit2/ui/blocktype_list.ui, src/mcedit2/ui/coord_widget.ui, src/mcedit2/ui/editortools/brush.ui, src/mcedit2/ui/editortools/edit_chunk.ui, src/mcedit2/ui/editortools/edit_player.ui, src/mcedit2/ui/editortools/images/brush_diamond.png, src/mcedit2/ui/editortools/images/brush_round.png, src/mcedit2/ui/editortools/images/brush_square.png, src/mcedit2/ui/editortools/select_entity.ui, src/mcedit2/ui/fill.ui, src/mcedit2/ui/images/config.png, src/mcedit2/ui/images/query.png, src/mcedit2/ui/images/update.png, src/mcedit2/ui/log_view.ui, src/mcedit2/ui/main_window.ui, src/mcedit2/ui/mcedit2.qrc, src/mcedit2/ui/minecraft_installs.ui, src/mcedit2/ui/py/__init__.py, src/mcedit2/ui/py/ui_block_picker.py, src/mcedit2/ui/replace.ui, src/mcedit2/ui/selection_coord_widget.ui, src/mcedit2/ui/world_list.ui, src/mcedit2/util/__init__.py, src/mcedit2/util/bresenham.py, src/mcedit2/util/bugfixes.py, src/mcedit2/util/custom_traceback.py, src/mcedit2/util/dialogs.py, src/mcedit2/util/directories.py, src/mcedit2/util/geometry.py, src/mcedit2/util/glutils.py, src/mcedit2/util/ipython_widget.py, src/mcedit2/util/lazyprop.py, src/mcedit2/util/load_png.py, src/mcedit2/util/load_ui.py, src/mcedit2/util/mceaction.py, src/mcedit2/util/minecraftinstall.py, src/mcedit2/util/objgraphwidget.py, src/mcedit2/util/profiler.py, src/mcedit2/util/profilerui.py, src/mcedit2/util/raycast.py, src/mcedit2/util/resources.py, src/mcedit2/util/scanmodules.py, src/mcedit2/util/settings.py, src/mcedit2/util/showprogress.py, src/mcedit2/util/worldloader.py, src/mcedit2/widgets/__init__.py, src/mcedit2/widgets/blockpicker.py, src/mcedit2/widgets/blocktype_list.py, src/mcedit2/widgets/flowlayout.py, src/mcedit2/widgets/infopanel.py, src/mcedit2/widgets/layout.py, src/mcedit2/widgets/log_view.py, src/mcedit2/widgets/nbttreeview.py, src/mcedit2/widgets/objectinspector.py, src/mcedit2/worldlist.py, src/mcedit2/worldview/__init__.py, src/mcedit2/worldview/camera.py, src/mcedit2/worldview/cutaway.py, src/mcedit2/worldview/fourup.py, src/mcedit2/worldview/iso.py, src/mcedit2/worldview/minimap.py, src/mcedit2/worldview/overhead.py, src/mcedit2/worldview/viewcontrols.py, src/mcedit2/worldview/worldruler.py, src/mcedit2/worldview/worldview.py, src/mceditlib/__init__.py, src/mceditlib/anvil/__init__.py, src/mceditlib/anvil/adapter.py, src/mceditlib/anvil/biome_types.py, src/mceditlib/anvil/entities.py, src/mceditlib/anvil/worldfolder.py, src/mceditlib/block_copy.py, src/mceditlib/blockrotation.py, src/mceditlib/blocktypes/__init__.py, src/mceditlib/blocktypes/legacy_ids.json, src/mceditlib/blocktypes/minecraft.json, src/mceditlib/blocktypes/minecraft_raw.json, src/mceditlib/blocktypes/named_ids.py, src/mceditlib/blocktypes/rendertypes.py, src/mceditlib/cachefunc.py, src/mceditlib/directories.py, src/mceditlib/exceptions.py, src/mceditlib/export.py, src/mceditlib/faces.py, src/mceditlib/findadapter.py, src/mceditlib/geometry.py, src/mceditlib/heightmaps.py, src/mceditlib/items.py, src/mceditlib/items.txt, src/mceditlib/java.py, src/mceditlib/levelbase.py, src/mceditlib/minecraft_server.py, src/mceditlib/multi_block.py, src/mceditlib/nbt.pyx, src/mceditlib/nbtattr.py, src/mceditlib/operations/__init__.py, src/mceditlib/operations/block_fill.py, src/mceditlib/operations/entity.py, src/mceditlib/pc/__init__.py, src/mceditlib/pc/regionfile.py, src/mceditlib/pocket.py, src/mceditlib/relight.py, src/mceditlib/revisionhistory.py, src/mceditlib/run_regression_test.py, src/mceditlib/schematic.py, src/mceditlib/test/__init__.py, src/mceditlib/test/anvil_test.py, src/mceditlib/test/editing_test.py, src/mceditlib/test/entity_test.py, src/mceditlib/test/extended_id_test.py, src/mceditlib/test/nbt_test.py, src/mceditlib/test/relight_test.py, src/mceditlib/test/revisionhistory_test.py, src/mceditlib/test/schematic_test.py, src/mceditlib/test/server_test.py, src/mceditlib/test/session_lock_test.py, src/mceditlib/test/templevel.py, src/mceditlib/test/time_exportimport.py, src/mceditlib/test/time_fill.py, src/mceditlib/test/time_getsetblocks.py, src/mceditlib/test/time_loadsave.py, src/mceditlib/test/time_nbt.py, src/mceditlib/test/time_relight.py, src/mceditlib/test/time_storagechain.py, src/mceditlib/util/__init__.py, src/mceditlib/util/unique_nd.py, src/mceditlib/worldeditor.py, test_files/AnvilWorld/level.dat, test_files/AnvilWorld/region/r.-1.-1.mca, test_files/AnvilWorld/region/r.-1.0.mca, test_files/AnvilWorld/region/r.0.-1.mca, test_files/AnvilWorld/region/r.0.0.mca, test_files/AnvilWorld_1.8/data/Mineshaft.dat, test_files/AnvilWorld_1.8/data/Village.dat, test_files/AnvilWorld_1.8/data/villages.dat, test_files/AnvilWorld_1.8/data/villages_end.dat, test_files/AnvilWorld_1.8/data/villages_nether.dat, test_files/AnvilWorld_1.8/level.dat, test_files/AnvilWorld_1.8/level.dat_mcr, test_files/AnvilWorld_1.8/level.dat_old, test_files/AnvilWorld_1.8/playerdata/a1f04ccd-e535-4a34-ae5f-b05084e5888f.dat, test_files/AnvilWorld_1.8/region/r.-1.0.mca, test_files/AnvilWorld_1.8/region/r.0.0.mca, test_files/AnvilWorld_1.8/stats/a1f04ccd-e535-4a34-ae5f-b05084e5888f.json, test_files/Floating.schematic, test_files/PocketWorld.zip, test_files/Station.schematic, test_files/TileTicks.nbt, test_files/city_256_256_128.dat, test_files/indev.mclevel, test_files/station.txt, test_files/uncompressed.nbt, test_requirements.txt
