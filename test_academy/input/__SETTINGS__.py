## S3 settings
S3_MOOC_FOLDER = 'pricing'
S3_BUCKET = "mooc-test"
S3_VIDEOS_FOLDER = "videos"
S3_ANSWERS_FOLDER =  'mob_answers'
S3_EXAMPLES_FOLDER =  'mob_examples'
#S3_LINKS_URL = 'https://mooc-test.s3-ap-southeast-1.amazonaws.com/' # must end in '/'
S3_LINKS_URL = 'https://sos-de-fra-1.exo.io/'

# edx settings
EDX_EXTERNAL_GRADER_QUEUENAME = 'spatial_computational_thinking'
EDX_ASSET_FILE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'pdf', 'srt'] 

# SETTINGS FOR MOBIUS FILES
MOB_ANSWER_FILENAMES = ['_ans.mob'] # files that are answers should end with this
MOB_EXAMPLE_FILENAMES = ['_exp.mob']# files that are examples should end with this
MOB_URL = 'https://design-automation.github.io/mobius-parametric-modeller-dev' # the dev version
#MOB_URL = 'https://mobius.design-automation.net/' # the stable version

# LANGUAGES
# available languages: ['us', 'uk', 'pt', 'es', 'zh', 'fr', 'de', 'nl']
LANGUAGES = ['en']
ALL_LANGUAGES = {
    'en': 'English',
    'zh': 'Mandarin',
    'pt': 'Portuguese',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'nl': 'Dutch'
} 
