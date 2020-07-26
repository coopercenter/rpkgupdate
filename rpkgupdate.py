"""
@file rpkgupdate.py
@author David Hill, Jr.
@brief This script will scan all repos that use the R programming language
       in the cooper center organization, collect all r packages used and and install them locally on your machine.
"""

from github import Github
import sys
import getpass
import stdiomask


"""
@brief this method gets all the repos from the cooper center organization
"""
def setup():
    # login
    user = input("Github Username: ")
    password = stdiomask.getpass("Github Password: ")

    try:
        g = Github(user, password) 
    except:
        print("Username or Password incorrect.")
        return
    
    # get cooper center organization
    try:
        org = g.get_organization("coopercenter")
    except:
        print("Could not get organization or it does not exist.")
        return

    # get all repos of organization
    org_repos = org.get_repos('all')

    return org_repos

def GetDeps(file):
    return

def main():
    r_repos = []
    r_packages = set()
    content_files = []
    r_files = []

    # get all repos from setup
    repos = setup()

    if repos:
        # gets all R repos
        for repo in repos:
            if repo.language == 'R':
                r_repos.append(repo)

        # get all files from all R repos
        for repo in r_repos:
            contents = repo.get_contents("")
            while contents:
                file_content = contents.pop(0)
                if file_content.type == "dir":
                    contents.extend(repo.get_contents(file_content.path))
                else:
                    content_files.append(file_content)

        # get all r and rmd files
        for file in content_files:
            if file.name.endswith('.R') or file.name.endswith('.Rmd'):
                r_files.append(file)


    else:
        exit()
    


if __name__ == "__main__":
    main()