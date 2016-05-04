# python_lib_sphinx

[![Build Status](https://travis-ci.org/saun4app/python_lib_sphinx.svg?branch=master)](https://travis-ci.org/saun4app/python_lib_sphinx)
[![codecov.io](https://codecov.io/github/hbetts/orbitalpy/coverage.svg?branch=master)](https://codecov.io/github/saun4app/python_lib_sphinx?branch=master)

This is a supplemental example for [`generator-python-lib`](https://github.com/hbetts/generator-python-lib) to crate a Python library with documentation using [`Sphinx`](https://pypi.python.org/pypi/Sphinx).

## Install python-lib & housekeeping

Run:
```bash
$ npm install -g yo
$ npm install -g generator-python-lib
$ pip install virtualenv
$ virtualenv --python=python3 venv
$ source ./venv/bin/activate
```

## Setup new library

Run:
```bash
$ mkdir python_lib_sphinx
$ cd python_lib_sphinx
$ yo python-lib
```

Follow the instructions of `yo python-lib`.

Add `Sphinx`, `docutils`, `Jinja2` to `requirements-dev.txt`

`requirements-dev.txt`:

```
codecov==2.0.3
coverage==4.0.3
pluggy==0.3.1
py==1.4.31
requests==2.10.0
tox==2.3.1
virtualenv==15.0.1
Sphinx==1.4.1
docutils==0.12
Jinja2==2.8
```

Run:
```bash
$ python setup.py test
$ python setup.py install
```

## Setup `sphinx`

Run:
```bash
$ mkdir docs
$ cd docs
$ sphinx-quickstart
```

Follow the instructions of `sphinx-quickstart`.

Add `sys.path.insert(0, os.path.abspath('../..'))` to `conf.py` after `sphinx-quickstart` is finished,

Run:

```bash
$ sphinx-apidoc -f -o source/ ../python_lib_sphinx/
$ make html
```

The generated documentation page is located at `docs/_build/html/index.html`.

### `utils` module document looks like the following:


<span id="python-lib-sphinx-utils-module"></span><h2>python_lib_sphinx.utils module<a class="headerlink" href="#module-python_lib_sphinx.utils" title="Permalink to this headline">¶</a></h2>
<p>General purpose utility library..</p>
<dl class="class">
<dt id="python_lib_sphinx.utils.Constants">
<em class="property">class </em><code class="descclassname">python_lib_sphinx.utils.</code><code class="descname">Constants</code><a class="headerlink" href="#python_lib_sphinx.utils.Constants" title="Permalink to this definition">¶</a></dt>
<dd><p>Bases: <a class="reference external" href="https://docs.python.org/library/functions.html#object" title="(in Python v2.7)"><code class="xref py py-class docutils literal"><span class="pre">object</span></code></a></p>
<p>Constants.</p>
<dl class="class">
<dt id="python_lib_sphinx.utils.Constants.Earth">
<em class="property">class </em><code class="descname">Earth</code><a class="headerlink" href="#python_lib_sphinx.utils.Constants.Earth" title="Permalink to this definition">¶</a></dt>
<dd><p>Bases: <a class="reference external" href="https://docs.python.org/library/functions.html#object" title="(in Python v2.7)"><code class="xref py py-class docutils literal"><span class="pre">object</span></code></a></p>
<p>Earth constants.</p>
<dl class="attribute">
<dt id="python_lib_sphinx.utils.Constants.Earth.GRAVITY">
<code class="descname">GRAVITY</code><em class="property"> = 9.80665</em><a class="headerlink" href="#python_lib_sphinx.utils.Constants.Earth.GRAVITY" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

</dd></dl>

<dl class="class">
<dt id="python_lib_sphinx.utils.Constants.Mars">
<em class="property">class </em><code class="descclassname">Constants.</code><code class="descname">Mars</code><a class="headerlink" href="#python_lib_sphinx.utils.Constants.Mars" title="Permalink to this definition">¶</a></dt>
<dd><p>Bases: <a class="reference external" href="https://docs.python.org/library/functions.html#object" title="(in Python v2.7)"><code class="xref py py-class docutils literal"><span class="pre">object</span></code></a></p>
<p>Mars constants.</p>
<dl class="attribute">
<dt id="python_lib_sphinx.utils.Constants.Mars.GRAVITY">
<code class="descname">GRAVITY</code><em class="property"> = 9</em><a class="headerlink" href="#python_lib_sphinx.utils.Constants.Mars.GRAVITY" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

</dd></dl>

</dd></dl>

<dl class="function">
<dt id="python_lib_sphinx.utils.circumference">
<code class="descclassname">python_lib_sphinx.utils.</code><code class="descname">circumference</code><span class="sig-paren">(</span><em>radius</em><span class="sig-paren">)</span><a class="headerlink" href="#python_lib_sphinx.utils.circumference" title="Permalink to this definition">¶</a></dt>
<dd><p>Calculate the circumference of an object.</p>
<p>2*pi*r</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">math</span> <span class="k">import</span> <span class="o">*</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">round</span><span class="p">(</span><span class="n">circumference</span><span class="p">(</span><span class="mi">600000</span><span class="p">),</span> <span class="mi">3</span><span class="p">)</span>
<span class="go">3769911.184</span>
</pre></div>
</div>
</dd></dl>

<dl class="function">
<dt id="python_lib_sphinx.utils.orbital_period">
<code class="descclassname">python_lib_sphinx.utils.</code><code class="descname">orbital_period</code><span class="sig-paren">(</span><em>planet</em>, <em>planatary_radius</em>, <em>altitude</em><span class="sig-paren">)</span><a class="headerlink" href="#python_lib_sphinx.utils.orbital_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Calculate the orbital period of an object.</p>
<p>d = v*t</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">math</span> <span class="k">import</span> <span class="o">*</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">round</span><span class="p">(</span><span class="n">orbital_period</span><span class="p">(</span><span class="n">Constants</span><span class="o">.</span><span class="n">Earth</span><span class="p">,</span> <span class="mi">600000</span><span class="p">,</span> <span class="mi">70</span><span class="p">),</span> <span class="mi">3</span><span class="p">)</span>
<span class="go">1554.43</span>
</pre></div>
</div>
</dd></dl>

<dl class="function">
<dt id="python_lib_sphinx.utils.orbital_speed">
<code class="descclassname">python_lib_sphinx.utils.</code><code class="descname">orbital_speed</code><span class="sig-paren">(</span><em>planet</em>, <em>planatary_radius</em>, <em>altitude</em><span class="sig-paren">)</span><a class="headerlink" href="#python_lib_sphinx.utils.orbital_speed" title="Permalink to this definition">¶</a></dt>
<dd><p>Calculate the orbital speed of an object.</p>
<p>v = R*sqrt(g/(R+h))</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">math</span> <span class="k">import</span> <span class="o">*</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">round</span><span class="p">(</span><span class="n">orbital_speed</span><span class="p">(</span><span class="n">Constants</span><span class="o">.</span><span class="n">Earth</span><span class="p">,</span> <span class="mi">600000</span><span class="p">,</span> <span class="mi">70</span><span class="p">),</span> <span class="mi">3</span><span class="p">)</span>
<span class="go">2425.552</span>
</pre></div>
</div>
</dd></dl>




## References

- [generator-python-lib](https://github.com/hbetts/generator-python-lib)
- [Sphinx for Python documentation](http://gisellezeno.com/tutorials/sphinx-for-python-documentation.html)


Read [CONTRIBUTING](CONTRIBUTING.md).
