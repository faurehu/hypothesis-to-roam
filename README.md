I use this script to fetch annotations from [Hypothes.is](https://hypothes.is) and format it into a pasteable format for [Roam](https://roamresearch.com)

Caveats:

* Will remove square brackets `[]` from highlights and notes
* Will remove line breaks from highlights and notes

Use:

* Get your API token from https://hypothes.is/account/developer
* Get the url of the site you want to get annotations from
* Call `python3 <API-TOKEN> <url> <optional>`
    * Insert any third argument for blockquote output
* The results will be written to file `output.txt` in the same directory