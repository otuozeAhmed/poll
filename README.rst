Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

You will need to have the following installed:

- Python 3.1+ - https://python.org
- Git - https://git-scm.com/


~~~~~~~~~~~~~

**Step - 1. Download The Project.**
~~~~~~~~~~~~~

   .. code:: sh

        git clone https://github.com/otuozeAhmed/poll.git
***

**Step - 2.**
~~~~~~~~~~~~~

   .. code:: sh

       cd pm

***
 
**Step 3a - Activate Virtual Environment - (Git Bash Terminal)**
~~~~~~~~~~~~~
   .. code:: sh

       source venv/Scripts/activate
***

**Step 3b - Activate Virtual Environment - (Command Prompt).**
~~~~~~~~~~~~~

   .. code:: sh

       .\venv\Scripts\activate
***

**Step 4 - Run Development Server.**
~~~~~~~~~~~~~

   .. code:: sh

       waitress-serve --listen=127.0.0.1:8000 core.wsgi:application
***
