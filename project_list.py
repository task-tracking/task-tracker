# Please add your project to the list below.  In order, include:
# * the name of your project, so we can label it in the meta-tracker
# * the label that your project uses to indicate design issues
# * the owner and name of your repository, for instance "owner/myrepository"

import collections

Project = collections.namedtuple('Project', 'name label url')

projects = [
    Project(name="?", label="?", url="?")
]

