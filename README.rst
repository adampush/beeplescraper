beeplescraper
=============

Here are a couple of scripts to scrape beeple.tumblr.com using :code:`requests`
and :code:`beautifulsoup4`. The intended usage is:

.. code:: bash

    $ python beeplescraper.py

Then, after the script exits, run the next script:

.. code:: bash

    $ python beepledownloader.py

:code:`beeplescraper.py` will find all the "high res" image urls and write them to a
file, :code:`image-urls.txt` in the current working directory. Then,
:code:`beepledownloader.py` reads the URLs from the :code:`image-urls.txt` and
downloads each image, saving them to a directory :code:`beeple_images/` in the
current working directory.

There are some "configuration constants" which are named :code:`IN_ALL_CAPS`,
e.g. :code:`MAX_PAGES` in :code:`beeplescraper.py` which are pretty
self-explanatory and offer some amount of control over the operation of the
scripts.
