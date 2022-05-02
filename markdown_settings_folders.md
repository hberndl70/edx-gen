
# Settings for Folders

Below is a list of the settings that can be specified for each type of folder and each type of component.


## Root Folder Settings

The heading must starts with `# ROOT`.

Additional edX course metadata is as follows:

_Required_ (example)
- `org="Exoscale"`
- `course="EXO100"`
- `url_name="R2021"`


NOTE: _The values must match the values on edX. If they do not match, import of the .tar.gz file into edX will fail._


## Common Settings For Folders

Common setting folders (except the top level ROOT folder) are as follows:

_Required_
- `display_name="Welcome"` 

_Optional_
- `visible_to_staff_only="true"`
- `start="&quot;2019-08-18T10:00:00+00:00&quot;"`

The display_name is the name that will be displayed to the user in the edX interface.


## Course Folder Settings

The heading must starts with `# COURSE`.

Additional course metadata is as follows:

_Optional_
- `cert_html_view_enabled="true"`
- `course_image="course_image.jpg"`
- `graceperiod="900 seconds"`
- `invitation_only="true"`
- `language="en"`
- `learning_info="[]"`
- `minimum_grade_credit="0.8"`
- `wiki_slug="Exoscale.EXO100.R2021"`


## Section Folder Settings

The heading must starts with `# SECTION`.

Additional section metadata is as follows:

NIL


## Subsection Folder Settings

The heading must starts with `# SUBSECTION`.

Additional subsection metadata is as follows:

_Optional_
- `format="Assignment"`
- `graded="true"`
- `due="2019-08-25T10:00:00+00:00"`
- `hide_after_due="true"`


## Unit Folder Settings

The heading must starts with `# UNIT`.

NIL
