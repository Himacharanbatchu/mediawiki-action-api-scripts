# MediaWiki Action API Scripts

This repository contains easy-to-use Python scripts for interacting with the MediaWiki Action API. These scripts are intended to assist editors by automating common tasks, such as retrieving page content, listing categories, and monitoring recent changes.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)

## Scripts

Each script interacts with the MediaWiki Action API to perform a specific task. Replace placeholders in the script (like page titles or usernames) with your desired values.

### Script Descriptions

1. **search_keyword.py** - Searches for pages with a specific keyword or phrase.

2. **get_page_content.py** - Retrieves the full content of a specified page.

3. **list_page_categories.py** - Lists all categories that a page belongs to.

4. **list_category_pages.py** - Lists all pages in a given category.

5. **list_page_links.py** - Lists all internal links on a specified page.

6. **list_page_images.py** - Lists all images used on a specified page.

7. **list_recent_changes.py** - Displays recent changes on the wiki, useful for monitoring activity.

8. **list_page_templates.py** - Lists all templates used on a specified page.

9. **get_user_contributions.py** - Retrieves recent contributions by a specific user.

10. **get_page_views.py** - Displays page view statistics for a specified page.

## Usage

Run each script independently. For example:

```bash
python scripts/search_keyword.py
```

Each script prints its output to the console.

## License
This project is open-source and available under the MIT License.
