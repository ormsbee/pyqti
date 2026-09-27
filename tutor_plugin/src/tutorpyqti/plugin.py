"""
Tutor plugin for running pyqti's XBlock in ``tutor dev``.

    tutor plugins enable pyqti
    tutor mounts add /path/to/pyqti
    tutor images build openedx-dev
"""

from tutor import hooks

# Tutor only bind-mounts a directory from `tutor mounts add` into the openedx images
# and the lms/cms containers if its name matches one of these regexes. re.match only
# anchors the start, so without "$" a sibling checkout like pyqti-revamp would match.
hooks.Filters.MOUNTED_DIRECTORIES.add_item(("openedx", r"pyqti$"))

# Tutor installs mounted packages with a plain `pip install -e /mnt/pyqti`, which
# ignores extras. Re-install with [xblock] at the end of the openedx-dev build. The
# guard keeps the build working when this plugin is enabled but pyqti isn't mounted.
hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-dev-dockerfile-post-python-requirements",
        """{% if "pyqti" in iter_mounted_directories(MOUNTS, "openedx") %}
RUN $PIP_COMMAND install -e "/mnt/pyqti[xblock]"
{% endif %}""",
    )
)
