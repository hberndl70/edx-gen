
# Settings for Components

Below is a list of the settings that can be specified for each type of component.


## Common Settings For Components

For components, the heading above the settings must starts with `# COMPONENT`.

The settings differ for each componet. However, there are certain common settings. 

One important setting is called `type`, which defines the type of component being defined.

Possible values of 'type' are as follows:
- `type="text"`
- `type="video"`
- `type="problem-checkboxes"`

At the moment, for problems, only 'problem-checkboxes' are implemented.
- problem-checkboxes: A problem where the learner needs to answer checkbox questions (with one or multiple right answers).

Other common setting for all components  are as follows:

_Required_
- `display_name="unit name"`

_Optional_
- `visible_to_staff_only+"true"`
- `start="2019-08-18T10:00:00+00:00"`

The `display_name` is not displayed to the user in the edX interface.


## Text

Additional text settings are as follows:

NIL


## Video

Additional video settings are as follows:

_Required_  (either one of the two)
- `youtube_id_1_0="3_yD_cEKoCk"`
- `video_filename="my_video.mp4"`

_Optional_
- `download_video="false"`
- ... and many more


## Problem - Checkboxes

Additional checkboxes problem settings are as follows:

_Optional_
- `max_attempts: "2"`
- `weight: "1.0"`
- `showanswer: "finished"`
- `group_access: "{}"`
- `rerandomize: "always"` or `"never"` or ...
- `attempts_before_showanswer_button: "1"`


