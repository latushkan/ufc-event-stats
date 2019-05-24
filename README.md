# UFC STATISTICS 

##  Description:
This program downloads statistics on all UFC fights from 'ufc-stats.com' for statistical analysis.  

## Packages
1. **[Python](https://docs.python.org/3/)** for data wrangling  
	1. **[Requests](https://2.python-requests.org/en/master/)** for web scraping  
	2. **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)** for parsing    
	3. **[LXML](https://lxml.de/3.4/lxmldoc-3.4.4.pdf)** parser for BS4
	4. **[Pandas](https://pandas.pydata.org/pandas-docs/stable/)** for data frame via [Anaconda](https://docs.anaconda.com/anaconda/), a cross platform distribution for data analysis and scientific computing  
2. **[R](https://www.rdocumentation.org/taskviews#Bayesian)** for data visualization and analysis  
## Package Installers
[Pip](https://pip.pypa.io/en/stable/installing/)  
[Pipenv](https://docs.pipenv.org/en/latest/)  for **Requests**


## GitHub
### Starting a New Project
 create new repository on GitHub    
`mkdir <new-repository>` to make local repository    
`git init` to make GitHub "see" the working directory  
`git remote add origin <link>`  links local repository to GitHub equivalent   
`git pull origin master` fetches copy of master branch, pulls over license   
`touch README.md` makes a new files  
`git status` to check for untracked or changed files  
`git add README.txt` to stage files before commiting  
`git commit -m "log message"` creates log that describes changes in the commit  
`git push -u origin master` pushes commit to the master branch.   
### Making a New Branch
`git pull` to make sure master is "clean"
`git checkout -b 01-scrape-and-parse` create local branch or switch to another branch
`git push origin 01-scrape-and-parse` push branch onto github
`remote` vs `upstream` 







