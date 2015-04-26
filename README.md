This is a simple python script that allows you to collect issues of a given
type from across github.  It was created for the fine folks of
[Open Source Design](https://github.com/opensourcedesign) but can be used for
any given label (documentation, translation, etc).

To run the script:

* Set up a tracker repository where issues will be collected
* Include that information, along with your username and password, in config.py
* Add projects to project_list.py.  Make sure you have their permission, as 
Github currently does not let you opt out of issue references, so participating
in the tracker will leave issue references.
* run "python bot.py"

Currently you need to run the script manually to scrape new issues.
