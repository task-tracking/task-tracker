import requests, json, csv

from project_list import projects
from config import user, password, post_url

# Import list of indexed issues from csv file
with open('issues.csv') as csv_file:
    reader = csv.reader(csv_file)
    issue_IDs = [int(row[0]) for row in reader]

for project in projects:

    # Gets open issues from each project
    scrape_params = {'labels': project.label}
    scrape_url = "https://api.github.com/repos/" + project.url + "/issues"
    scrape_request = requests.get(scrape_url, auth = (user, password), 
        params = scrape_params)
    issues = json.loads(scrape_request.text)

    for issue in issues:

        # Check that this issue is new
        if issue['id'] not in issue_IDs:

            issue_body = ("<strong>To work on this task, go to <a href='" +
                issue['html_url'] + "'>the original issue</a>.</strong>\r\n\r\n" + 
                issue['body'])

            post_data = {'labels': [project.name], 'title': issue['title'], 
                'body': issue_body}

            post_request = requests.post(post_url, auth = (user, password),
                data = json.dumps(post_data))

            # Save new issue to csv index file
            with open('issues.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)                
                writer.writerow([issue['id']])    
        
