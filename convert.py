import sys
from bs4 import BeautifulSoup

def parse_html_bookmarks(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    bookmarks = {}
    current_folder = None

    for dt in soup.find_all('dt'):
        if dt.find('h3'):  # This is a folder
            current_folder = dt.find('h3').get_text()
            bookmarks[current_folder] = []
        elif dt.find('a'):  # This is a bookmark
            bookmark = dt.find('a')
            bookmarks[current_folder].append({'name': bookmark.get_text(), 'url': bookmark['href']})

    return bookmarks

def bookmarks_to_markdown(bookmarks, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for folder, links in bookmarks.items():
            if folder:  # Avoid NoneType folders
                file.write(f"## {folder}\n")
            for link in links:
                file.write(f"- [{link['name']}]({link['url']})\n")
            file.write("\n")

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py [input_html_file] [output_markdown_file]")
        sys.exit(1)

    html_file = sys.argv[1]
    output_file = sys.argv[2]

    bookmarks = parse_html_bookmarks(html_file)
    bookmarks_to_markdown(bookmarks, output_file)
    print(f"Bookmarks exported to {output_file}")

if __name__ == "__main__":
    main()
