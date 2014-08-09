ckanext-appckan
===============

Plugin that adds a button to register the apps (CKAN) integrate with AppCKAN http://appckan.com

Installation
===============

First, install the appckan CKAN extension in your Python virtual environment. Make sure that your virtualenv is activated, then do:

<pre><code>. /usr/lib/ckan/default/bin/activate</code></pre>

<pre><code>pip install -e  git+https://github.com/lerao/ckanext-appckan.git#egg=ckanext-appckan</code></pre>

Then <code>cd</code> into the <code>ckanext-appckan</code> directory and run:

<pre><code>python setup.py develop</code></pre>

Finally, enable the extension. Edit your CKAN ini file (e.g. development.ini, production.ini), find the <code>plugins =</code> line and add the appckan plugin:

<pre><code>plugins = appckan</code></pre>

After, restart apache2 and nginx:

<pre><code>sudo service apache2 restart
sudo service nginx restart
</code></pre>