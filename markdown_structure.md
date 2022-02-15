# Markdown Structure

The markdown files for the generator need to be structured in a specific way.

There are two type of markdown content.

* _Folder Settings_: This markdown specifies the settings for each folder. 

* _Unit Content_: This markdown specifies the actual cotent of each unit, as a series of components.

## Folder Settings

Folder settings are specified at the top of all markdown files in the same way. These files containing the settings specify the configuration for the folder. So, for example, the .md file in the 'course' folder `_course.md` specifies the settings for the `course` part. 

Here is a snippet of an example of some settings for the folder `course` in the file `_course.md`.

```
# COURSE
{:
    display_name="STARTER"
    cert_html_view_enabled="true"
    course_image="EXO100.png"
    graceperiod="900 seconds"
    invitation_only="true"
    language="en"
    learning_info="[]"
    minimum_grade_credit="0.8"
    wiki_slug="Exoscale.EXO100.R2021"
}
```

Things to note:

* The settings start with a heading. This heading must be created at the first line of the file.
* The heading text should be in upper case, and should start with the type of folder it is in:
  * `# ROOT`, `# COURSE`, `# SECTION`, `# SUBSECTION`, `# UNIT`
  * Note that you can add additional text. The requirement is just that the text starts with these specififc characters. For example, you may like some separators '===' to make the document visually clearer.
* The settings are enclosed in curly braces, like this `{: }`. Note the colon, it is important.
* The `{: }` settings must immediatley following the heading. There can be now blank lines.
* Inside the  `{: }` settings container, each setting consists of a key-value pair, `key="value"`. The key-value pairs can be on different lines, but there can be no spaces around the `=` sign. So `key = "value"` will not work.

The files for all these folders only contain settings except the `unit` folders, there is the strcutured content of the course.  So there should be nothing in the file after the settings. (If there is more text below, it will be ignored.)

For more information on the settings that can be specified for folders:

* See [Settings for Folders](markdown_settings_folders.md)

## Unit Content

The unit content is added to the markdown files in the unit folders, under the settings. The markdown defines a sequence of components, each of which has its own settings.

Here is a snippet of an example of some settings and content for a unit.

~~~~~~~~~~~~~~~~~~~~~~~~~~~
# UNIT ==========
{:
    display_name="Ungraded Quiz"
}

# COMPONENT ==========
{:
    type="problem-checkboxes"
    display_name="A Checkboxes Test Problem"
}

Here is the text for this question. What is the question?

![This is the alt text.](edx_image.png "A test image.")

===

[x] a correct answer

[ ] an incorrect answer

[x] another correct answer

[x] yet another correct answer

===

Some feedback about the correct answer.

Some more feedback in a seperate paragraph.

# COMPONENT ==========
{:
    type="problem-submit"
    display_name="A Problem with File Submission"
    attempts_before_showanswer_button="1" 
    max_attempts="1"
    showanswer="finished"
    weight="1.0"
    answer="answer.txt"
}

This is a submit problem, where a file needs to be uploaded that will be autograded by an external grader.

===

The text describes the solution to the problem.

~~~~~~~~~~~~~~~~~~~~~~~~~~~

Things to note:

* This file specifies the settings for the unit and the settings for two components:
  * a checkboxes problem, and 
  * a submit problem.
* The settings for the unit follow the same rules as those described above. Note that the text `# UNIT` must appear on the first line.
* Follwoing the settings for the unit, each component starts with a heading `# COMPONENT`
* Follwoing the heading, the `{: }` settings define settings specific to that component.
* One important required setting is the `type="xxx"` setting. Valid values are:
  * `type="html"`, `type="problem-checkboxes"`, `type="problem-submit"`, `type="video"`, 
* The actual content of the component is specifid after the settings. This can be specified in normal markdown.
* Note that all the blank lines are significant.

For  'problem-checkboxes' and 'problem-submit' components, it is necessary to divide the content into different parts. This is done using the `===` characters (with blank lines above and below).

The 'problem-checkboxes' has three parts, so the content must include two `===` splitters:

* Top: The problem description.
* `===`
* Middle: The checkbox choices.
* `===`
* Bottom: The problem solution, only displayed to the learner after certain conditions are met (as specified in the settings).

For checkboxes choices, the correct and incorrect choices are specified by starting with `[ ]` or `[x]` (small `x`, is important). Each choice must be seperated by an empty line.

The 'problem-submit' has two parts, so the content must include one `===` splitter:

* Top: The problem description.
* `===`
* Bottom: The problem solution, only displayed to the learner after certain conditions are met (as specified in the settings).

For more information on the settings that can be specified for components:

* See [Settings for Components](markdown_settings_components.md)