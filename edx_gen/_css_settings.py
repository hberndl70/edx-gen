#--------------------------------------------------------------------------------------------------
# Settings for figures

FIGURE_CSS = 'margin:20px;'

FIGCAPTION_CSS = ';'.join([
    'width:400px',
    'display:block',
    'margin-left:auto',
    'margin-right:auto',
    'margin-top:8px',
    'text-align:center',
    'font-style:italic'
    ])

IMAGE_MODAL_CSS = ';'.join([
    'width:400px',
    'display:block',
    'margin-left:auto',
    'margin-right:auto',
    'border-style:solid',
    'border-width:1px'
    ])

IMAGE_CSS = ';'.join([
    'display:block',
    'margin-left:auto',
    'margin-right:auto',
    'border-style:solid',
    'border-width:1px'
    ])
#--------------------------------------------------------------------------------------------------
# Settings for the language buttons
# These are the buttons that appear under each video

LANG_BUTTON_CSS = ';'.join([
    'padding:2px',
    'margin:1px',
    'border-style:solid',
    'border-width:1px',
    'display:inline',
    'cursor:pointer'
    ])

SELECT_LANG_SCRIPT = '''
function myFunction(lang) {
  document.getElementById('chinese').style="display:none";
  document.getElementById('french').style="display:none";
  if (lang !== 'none') {
    document.getElementById(lang).style="display:block";
  }
}
'''
#--------------------------------------------------------------------------------------------------
# Settings for Mobius Iframes
# These are the embedded Mobius models

MOB_IFRAME_WIDTH = '100%'
MOB_IFRAME_HEIGHT ='600px'

MOB_MINI_IFRAME_WIDTH = '80%'
MOB_MINI_IFRAME_HEIGHT ='400px'

MOB_IFRAME_STYLE = ';'.join([
    'display:block',
    'margin-left:auto',
    'margin-right:auto',
    'border-style:solid',
    'border-width:1px'
    ])


#--------------------------------------------------------------------------------------------------
