I use this script to fetch annotations from [Hypothes.is](https://hypothes.is) and format it into a pasteable format for [Roam](https://roamresearch.com)

Caveats:

* Will remove square brackets `[]` from highlights and notes
* Will remove line breaks from highlights and notes

Use:

* Get your API token from https://hypothes.is/account/developer
* Create a file `secret.txt` and in a single line paste your API token
* Get the url of the site you want to get annotations from
* Call `python3 <url> <optional>`
    * Insert any second argument for blockquote output
* The results will be written to file `output.txt` in the same directory