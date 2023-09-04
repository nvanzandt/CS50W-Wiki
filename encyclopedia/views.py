from django.shortcuts import render
import markdown
import random
from . import util


""" 
Converts markdown to html and returns the html content
"""
def convert_md_to_html(title): 
    md_content = util.get_entry(title) 
    markdowner = markdown.Markdown()
    if md_content is None: 
        return None
    else:
        return markdowner.convert(md_content)


"""
Displays the home page
"""
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


"""
Displays the content of the entry in html format
"""
def show_entry(request, title): 
    html_content = convert_md_to_html(title) 
    if html_content is not None: 
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })
    else: 
         return render(request, "encyclopedia/error.html", {"message": "This entry does not exist" 
        })
        

"""
Displays the search results
"""
def search_entry(request): 
    if request.method == "POST":
        title = request.POST['q']
        html_content = convert_md_to_html(title)
        if html_content is not None: 
            return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })
        else: 
            allEntries = util.list_entries() 
            results = []
            for entry in allEntries: 
                if title.lower() in entry.lower(): 
                    results.append(entry)
            return render(request, "encyclopedia/search.html", {
                "results": results
            })


"""
Creates a new entry
"""    
def new_entry(request):
    if request.method == "GET": 
        return render(request, "encyclopedia/new.html")
    else: 
        title = request.POST['title'] 
        content = request.POST['content']

        existingContent = util.get_entry(title) 
        if existingContent is not None: 
            return render(request, "encyclopedia/error.html", {
                "message": "Entry page already exists"
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html",{
                "title": title, 
                "content": html_content
            })


"""
Edits an existing entry
"""
def edit_entry(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title, 
            "content": content
        })


"""
Saves the edited entry
""" 
def save_entry(request):
    if request.method == 'POST': 
        title = request.POST['title'] 
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html",{
            "title": title, 
            "content": html_content
        })
    

"""
Displays a random entry
"""
def random_entry(request):
    allEntries = util.list_entries()
    random_entry = random.choice(allEntries)
    html_content = convert_md_to_html(random_entry)
    return render(request, "encyclopedia/entry.html",{
        "title": random_entry, 
        "content": html_content
    })


