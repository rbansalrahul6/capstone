django-project-skeleton
=======================

**django-project-skeleton** is my skeleton for Django projects. It provides a
directory structure for Django projects during development and deployment.


Meta
----

Author:
    Mischback

Status:
    maintained, in development

Version:
    1.1

Django Version:
    1.8



Usage
-----

To use this repository just use the ``template`` option of `django-admin
<https://docs.djangoproject.com/en/1.8/ref/django-admin/#startproject-projectname-destination>`_::

    $ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/development.zip [projectname]

If you wish to automagically fill the ``apache2_vhost.sample`` the command is::

    $ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/development.zip --name apache2_vhost.sample [projectname]


Documentation
-------------

You can see the documentation over at **Read the Docs**: `django-project-skeleton
<http://django-project-skeleton.readthedocs.org/en/latest/>`_
