#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : urllib check jira merged but don't change status on jira
"""
from urllib.request import urlopen, Request
import base64
import json

STASH_FILE_CONTENT_URL = 'http://sw-stash.freescale.net/rest/api/1.0/projects/{0}/repos/{1}/commits?until={2}&&limit={3}'
# {0} project name
# {1} repository name
# {2} commit
# {3} nr. of commits

JIRA_FILE_CONTENT_URL = 'http://sw-jira.freescale.net/rest/api/2/search?jql=project={0}%20AND%20status="{1}"&maxResults={2}'
# {0} project name
# {1} issue's state
# {2} number of issues

def get_jira(uri):
    req = Request(uri)
    req.add_header('Authorization', 'Basic U1ZDX0RFVlRFQ0g6OWhtN1gzbUpSOG5HNGgy')
    return urlopen(req)

def get_stash(uri):
    req = Request(uri)
    req.add_header('Authorization', 'Basic U1ZDX0RFVlRFQ0g6bmhSOXAzMmFXOA==')
    return urlopen(req)

def get(uri, user, password):
    """
    Run a Get rest call
    :param uri: Rest Uri
    :param user: Rest server user name
    :param password: Rest server password
    :return: Rest call response object
    """
    req = Request(uri)
    auth = base64.b64encode('{0}:{1}'.format(user, password).encode())
    req.add_header('Authorization', 'Basic {0}'.format(auth.decode()))
    return urlopen(req)

def get_issues_in_state(proj_name, state, number_of_issues):
    state = state.replace(' ', '%20')
    uri = JIRA_FILE_CONTENT_URL.format(proj_name, state, number_of_issues)
    response = get_jira(uri)
    data = json.loads(response.read())
    issues = data['issues']
    issues_in_state = []

    if (len(issues) < number_of_issues):
        number_of_issues = len(issues)
    
    for i in range(number_of_issues):
        issues_in_state.append(issues[i]['key'])
        
    return issues_in_state

def get_merged_issues(proj_name, repo_name, commit, commits_count):
    uri = STASH_FILE_CONTENT_URL.format(proj_name, repo_name, commit, commits_count)
    response = get_stash(uri)
    data = json.loads(response.read())
    values = data['values']
    issues_set = set()
    issues_list = []

    if (len(values) < commits_count):
        commits_count = len(values)

    for i in range(commits_count):
        try:
            keys = values[i]['properties']['jira-key']
            j = 0
            for j in range(len(keys)):
                issues_set.add(keys[j])
            issues_list = list(issues_set)
        except:
            continue

    return issues_list

if __name__ == '__main__':
    in_state = get_issues_in_state('ASDK', 'In Progress', 500)
    issues_list = get_merged_issues('ASDK', 'SDK_Codebase', '', 1000)
    state_issues = [val for val in in_state if val in issues_list]

    print(state_issues)
    print(len(state_issues))
    print('Done')
