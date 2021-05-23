# CMS

This is a very basic content management system written in django. It is still in works. I have put the basic idea below.

Administration page
====================
Django provides a very good admin page so there is no need to reinvent the wheel. I have used the admin page and have applied some modifications for filtering and sorting. 
The articles have 4 status possible (Pending, Needs Approval, Published, Archived). The administrator can see all of these objects and can sort, create and change status of
the articles accordingly. The articles are written in markdown and converted to constant HTML content which cannot be edited by the admin to reduce invalid HTML errors popping up 
here and there.

User page
=========
The home page (/cms/) lists all content. Only published and archived content are available to the end users. It also has a very basic search functionality.

This project needs a lot more work as of now like a login page and marking users as admins, etc. Will continue improving on it when time permits. Also need to add some frontend
content in JS, CSS or React if possible.
