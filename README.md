# checkoutbot

A python selenium checkout bot based on the SNKRS website.

# Dependencies:

# Setup:

replacing cdc_ string in Chromedriver using Vim to avoid detection:

`sudo vim /path/to/chromedriver`

After running the line above, do the following:

Replace all instances of cdc_ with dog_ by typing 

`:%s/cdc_/dog_/g`

dog_ is just an example. You can choose anything as long as it has the same amount of characters as the search string (e.g., cdc_), otherwise the chromedriver will fail.
To save the changes and quit, type :wq! and press return.


