# Regenie Corpus

Regenie is Regen Network's advanced AI chatbot which is trained on an open source corpus of content
which is managed in this repository. If you are using Regenie and discover that it is missing a key
piece of information that it should know about, please contribute to this repository by suggesting
new URLs that it should scan.

Each piece of content that Regenie consumes should be hosted on a public URL so that Regenie can
reference those URLs as sources for its answers. The lists of URLs are contained in CSV files in this
repository where each line in the CSV file represents one URL.

URLs which are automatically discovered by our [web crawler script](update-urls.py) are stored in
the [managed-urls](./managed-urls) folder. Please try to first update the crawler script to crawl
URLs that it missed if the content should have been discoverable but was missed. URLs that must
be manually added should be tracked in the [manual-urls](./manual-urls) folder.
