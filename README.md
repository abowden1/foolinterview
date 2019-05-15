**Installation:** <br />
****
1. `mkdir <dir_name>`
2. `cd <dir_name>`
3. Create a Python3 virtual environment. Ex. (using virtualenvwrapper): `mkvirtualenv -p python3 <env_name>`
4. Start vitualenv: `workon env_name`
5. `git clone https://github.com/abowden1/foolinterview.git`
6. `cd foolinterview`
7. Run build.sh **note: you may need to alter permissions to execute build.sh depending on your environment:** <br /> 
   If needed run `chmod +x build.sh` <br/>
   Run `./build.sh`
8. Navigate to the URL output by the `runserver` command (Ex. `http://127.0.0.1:8000/`)

****
**Usage**
****
On the home screen there will be a featured article displayed, based on the slug value provided to 
`foolinterview/settings.py: FEATURED_ARTICLE_SLUG`

There will be additional articles displayed below the featured. You can adjust the number displayed by editing 
the value in `foolinterview/settings.py: SECONDARY_ARTICLE_COUNT`

Selecing **"Read More"** will take you to the article.

In the article page sidebar, stock quotes are listed. You can edit the number displayed by editing
the value in `foolinterview/settings.py: QUOTE_TABLE_COUNT`

Since the quotes are currently stored in JSON, they may not be up to date. To see
an up-to-date quote, click the link in the listed Stock Value.

Load different quotes by selecting the **"Shuffle Quotes"** button.

Anonymous comments are also displayed on the sidebar. You can add a comment in the **"Add Comment"** field and
click on **"Submit"**
****
**Additional Configurations**
****
Have a new content file? Change `foolinterview/settings.py: CONTENT_FILE` to use that to populate the articles.

Have a new quotes file? Change `foolinterview/settings.py: QUTES_FILE` to use that to populate the quotes.
****
**Future Considerations**
****
Maintain more articles by loading `content_api.json` to the database. Use articles stored there to populate the site.

Add the ability to create user accounts and restrict comments to only be submitted by the users.

Adjust the design of the site to have better branding.
 
 
