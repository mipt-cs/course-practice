Документация по pygame.draw
##############################

:date: 2020-09-28 09:00
:summary: Документация по pygame.draw.
:status: draft

.. default-role:: code
.. contents:: Содержание


Документация по pygame.draw
===========================

.. raw:: html

   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

   <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
       <meta http-equiv="X-UA-Compatible" content="IE=Edge" />
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       <title>pygame.draw &#8212; pygame v2.0.0.dev7 documentation</title>
       <link rel="stylesheet" href="../images/lab5/pygame.css" type="text/css" />
       <link rel="stylesheet" href="../images/lab5/pygments.css" type="text/css" />
       <script type="text/javascript" id="documentation_options" data-url_root="../" src="../images/lab5/documentation_options.js"></script>
       <script type="text/javascript" src="../images/lab5/jquery.js"></script>
       <script type="text/javascript" src="../images/lab5/underscore.js"></script>
       <script type="text/javascript" src="../images/lab5/doctools.js"></script>
       <script type="text/javascript" src="../images/lab5/language_data.js"></script>
       <link rel="shortcut icon" href="../images/lab5/pygame.ico"/>
       <link rel="index" title="Index" href="../genindex.html" />
       <link rel="search" title="Search" href="../search.html" />
       <link rel="next" title="pygame.event" href="event.html" />
       <link rel="prev" title="pygame.display" href="display.html" />
     </head><body>

       <div class="document">

     <div class="header">
       <table>
         <tr>
      <td class="logo">
        <a href="https://www.pygame.org/">
          <img src="../images/lab5/pygame_tiny.png"/>
        </a>
        <h5>pygame documentation</h5>
      </td>
      <td class="pagelinks">
        <div class="top">
          <a href="https://www.pygame.org/">Pygame Home</a> ||
          <a href="../index.html">Help Contents</a> ||
          <a href="../genindex.html">Reference Index</a>

           <form action="../search.html" method="get" style="display:inline;float:right;">
             <input name="q" value="" type="text">
             <input value="search" type="submit">
           </form>
        </div>
        <hr style="color:black;border-bottom:none;border-style: dotted;border-bottom-style:none;">
        <p class="bottom"><b>Most useful stuff</b>:
          <a href="color.html">Color</a> |
          <a href="display.html">display</a> |
          <a href="draw.html">draw</a> |
          <a href="event.html">event</a> |
          <a href="font.html">font</a> |
          <a href="image.html">image</a> |
          <a href="key.html">key</a> |
          <a href="locals.html">locals</a> |
          <a href="mixer.html">mixer</a> |
          <a href="mouse.html">mouse</a> |
          <a href="rect.html">Rect</a> |
          <a href="surface.html">Surface</a> |
          <a href="time.html">time</a> |
          <a href="music.html">music</a> |
          <a href="pygame.html">pygame</a>
        </p>

        <p class="bottom"><b>Advanced stuff</b>:
          <a href="cursors.html">cursors</a> |
          <a href="joystick.html">joystick</a> |
          <a href="mask.html">mask</a> |
          <a href="sprite.html">sprite</a> |
          <a href="transform.html">transform</a> |
          <a href="bufferproxy.html">BufferProxy</a> |
          <a href="freetype.html">freetype</a> |
          <a href="gfxdraw.html">gfxdraw</a> |
          <a href="midi.html">midi</a> |
          <a href="overlay.html">Overlay</a> |
          <a href="pixelarray.html">PixelArray</a> |
          <a href="pixelcopy.html">pixelcopy</a> |
          <a href="sndarray.html">sndarray</a> |
          <a href="surfarray.html">surfarray</a> |
          <a href="math.html">math</a>
        </p>

        <p class="bottom"><b>Other</b>:
          <a href="camera.html">camera</a> |
          <a href="cdrom.html">cdrom</a> |
          <a href="examples.html">examples</a> |
          <a href="fastevent.html">fastevent</a> |
          <a href="scrap.html">scrap</a> |
          <a href="tests.html">tests</a> |
          <a href="touch.html">touch</a> |
          <a href="pygame.html#module-pygame.version">version</a>
        </p>
      </td>
         </tr>
       </table>
     </div>

         <div class="documentwrapper">
             <div class="body" role="main">

   <div class="section" id="module-pygame.draw">
   <span id="pygame-draw"></span><dl class="definition module">
   <dt class="title module">
   <code class="docutils literal notranslate"><span class="pre">pygame.draw</span></code></dt>
   <dd><div class="line-block">
   <div class="line"><span class="summaryline">pygame module for drawing shapes</span></div>
   </div>
   <table border="1" class="toc docutils">
   <colgroup>
   <col width="23%" />
   <col width="1%" />
   <col width="76%" />
   </colgroup>
   <tbody valign="top">
   <tr class="row-odd"><td><a class="toc reference external" href="draw.html#pygame.draw.rect">pygame.draw.rect</a></td>
   <td>—</td>
   <td>draw a rectangle</td>
   </tr>
   <tr class="row-even"><td><a class="toc reference external" href="draw.html#pygame.draw.polygon">pygame.draw.polygon</a></td>
   <td>—</td>
   <td>draw a polygon</td>
   </tr>
   <tr class="row-odd"><td><a class="toc reference external" href="draw.html#pygame.draw.circle">pygame.draw.circle</a></td>
   <td>—</td>
   <td>draw a circle</td>
   </tr>
   <tr class="row-even"><td><a class="toc reference external" href="draw.html#pygame.draw.ellipse">pygame.draw.ellipse</a></td>
   <td>—</td>
   <td>draw an ellipse</td>
   </tr>
   <tr class="row-odd"><td><a class="toc reference external" href="draw.html#pygame.draw.arc">pygame.draw.arc</a></td>
   <td>—</td>
   <td>draw an elliptical arc</td>
   </tr>
   <tr class="row-even"><td><a class="toc reference external" href="draw.html#pygame.draw.line">pygame.draw.line</a></td>
   <td>—</td>
   <td>draw a straight line</td>
   </tr>
   <tr class="row-odd"><td><a class="toc reference external" href="draw.html#pygame.draw.lines">pygame.draw.lines</a></td>
   <td>—</td>
   <td>draw multiple contiguous straight line segments</td>
   </tr>
   <tr class="row-even"><td><a class="toc reference external" href="draw.html#pygame.draw.aaline">pygame.draw.aaline</a></td>
   <td>—</td>
   <td>draw a straight antialiased line</td>
   </tr>
   <tr class="row-odd"><td><a class="toc reference external" href="draw.html#pygame.draw.aalines">pygame.draw.aalines</a></td>
   <td>—</td>
   <td>draw multiple contiguous straight antialiased line segments</td>
   </tr>
   </tbody>
   </table>
   <p>Draw several simple shapes to a surface. These functions will work for
   rendering to any format of surface. Rendering to hardware surfaces will be
   slower than regular software surfaces.</p>
   <p>Most of the functions take a width argument to represent the size of stroke
   (thickness) around the edge of the shape. If a width of 0 is passed the shape
   will be filled (solid).</p>
   <p>All the drawing functions respect the clip area for the surface and will be
   constrained to that area. The functions return a rectangle representing the
   bounding area of changed pixels. This bounding rectangle is the 'minimum'
   bounding box that encloses the affected area.</p>
   <p>All the drawing functions accept a color argument that can be one of the
   following formats:</p>
   <blockquote>
   <div><ul class="simple">
   <li>a <a class="tooltip reference internal" href="color.html#pygame.Color" title=""><code class="xref py py-mod docutils literal notranslate"><span class="pre">pygame.Color</span></code><span class="tooltip-content">pygame object for color representations</span></a> object</li>
   <li>an <code class="docutils literal notranslate"><span class="pre">(RGB)</span></code> triplet (tuple/list)</li>
   <li>an <code class="docutils literal notranslate"><span class="pre">(RGBA)</span></code> quadruplet (tuple/list)</li>
   <li>an integer value that has been mapped to the surface's pixel format
   (see <a class="tooltip reference internal" href="surface.html#pygame.Surface.map_rgb" title=""><code class="xref py py-func docutils literal notranslate"><span class="pre">pygame.Surface.map_rgb()</span></code><span class="tooltip-content">convert a color into a mapped color value</span></a> and <a class="tooltip reference internal" href="surface.html#pygame.Surface.unmap_rgb" title=""><code class="xref py py-func docutils literal notranslate"><span class="pre">pygame.Surface.unmap_rgb()</span></code><span class="tooltip-content">convert a mapped integer color value into a Color</span></a>)</li>
   </ul>
   </div></blockquote>
   <p>A color's alpha value will be written directly into the surface (if the
   surface contains pixel alphas), but the draw function will not draw
   transparently.</p>
   <p>These functions temporarily lock the surface they are operating on. Many
   sequential drawing calls can be sped up by locking and unlocking the surface
   object around the draw calls (see <a class="tooltip reference internal" href="surface.html#pygame.Surface.lock" title=""><code class="xref py py-func docutils literal notranslate"><span class="pre">pygame.Surface.lock()</span></code><span class="tooltip-content">lock the Surface memory for pixel access</span></a> and
   <a class="tooltip reference internal" href="surface.html#pygame.Surface.unlock" title=""><code class="xref py py-func docutils literal notranslate"><span class="pre">pygame.Surface.unlock()</span></code><span class="tooltip-content">unlock the Surface memory from pixel access</span></a>).</p>
   <div class="admonition note">
   <p class="first admonition-title">Note</p>
   <p class="last">See the <a class="tooltip reference internal" href="gfxdraw.html#module-pygame.gfxdraw" title=""><code class="xref py py-mod docutils literal notranslate"><span class="pre">pygame.gfxdraw</span></code><span class="tooltip-content">pygame module for drawing shapes</span></a> module for alternative draw methods.</p>
   </div>
   <dl class="definition function">
   <dt class="title" id="pygame.draw.rect">
   <code class="descclassname">pygame.draw.</code><code class="descname">rect</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pygame.draw.rect" title="Permalink to this definition">¶</a></dt>
   <dd><div class="line-block">
   <div class="line"><span class="summaryline">draw a rectangle</span></div>
   <div class="line"><span class="signature">rect(surface, color, rect) -&gt; Rect</span></div>
   <div class="line"><span class="signature">rect(surface, color, rect, width=0, border_radius=0, border_radius=-1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1) -&gt; Rect</span></div>
   </div>
   <p>Draws a rectangle on the given surface.</p>
   <table class="docutils field-list" frame="void" rules="none">
   <col class="field-name" />
   <col class="field-body" />
   <tbody valign="top">
   <tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
   <li><strong>surface</strong> (<a class="reference internal" href="surface.html#pygame.Surface" title="pygame.Surface"><em>Surface</em></a>) -- surface to draw on</li>
   <li><strong>color</strong> (<a class="reference internal" href="color.html#pygame.Color" title="pygame.Color"><em>Color</em></a><em> or </em><em>int</em><em> or </em><em>tuple</em><em>(</em><em>int</em><em>, </em><em>int</em><em>, </em><em>int</em><em>, </em><em>[</em><em>int</em><em>]</em><em>)</em>) -- color to draw with, the alpha value is optional if using a
   tuple <code class="docutils literal notranslate"><span class="pre">(RGB[A])</span></code></li>
   <li><strong>rect</strong> (<a class="reference internal" href="rect.html#pygame.Rect" title="pygame.Rect"><em>Rect</em></a>) -- rectangle to draw, position and dimensions</li>
   <li><strong>width</strong> (<em>int</em>) -- <p>(optional) used for line thickness or to indicate that
   the rectangle is to be filled (not to be confused with the width value
   of the <code class="docutils literal notranslate"><span class="pre">rect</span></code> parameter)</p>
   <blockquote>
   <div><div class="line-block">
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">width</span> <span class="pre">==</span> <span class="pre">0</span></code>, (default) fill the rectangle</div>
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">width</span> <span class="pre">&gt;</span> <span class="pre">0</span></code>, used for line thickness</div>
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">width</span> <span class="pre">&lt;</span> <span class="pre">0</span></code>, nothing will be drawn</div>
   <div class="line"><br /></div>
   </div>
   <div class="admonition note">
   <p class="first admonition-title">Note</p>
   <p class="last">When using <code class="docutils literal notranslate"><span class="pre">width</span></code> values <code class="docutils literal notranslate"><span class="pre">&gt;</span> <span class="pre">1</span></code>, the edge lines will grow
   outside the original boundary of the rect. For more details on
   how the thickness for edge lines grow, refer to the <code class="docutils literal notranslate"><span class="pre">width</span></code> notes
   of the <a class="tooltip reference internal" href="#pygame.draw.line" title=""><code class="xref py py-func docutils literal notranslate"><span class="pre">pygame.draw.line()</span></code><span class="tooltip-content">draw a straight line</span></a> function.</p>
   </div>
   </div></blockquote>
   </li>
   <li><strong>border_radius</strong> (<em>int</em>) -- (optional) used for drawing rectangle with rounded corners.
   The supported range is [0, min(height, width) / 2], with 0 representing a rectangle
   without rounded corners.</li>
   <li><strong>border_top_left_radius</strong> (<em>int</em>) -- (optional) used for setting the value of top left
   border. If you don't set this value, it will use the border_radius value.</li>
   <li><strong>border_top_right_radius</strong> (<em>int</em>) -- (optional) used for setting the value of top right
   border. If you don't set this value, it will use the border_radius value.</li>
   <li><strong>border_bottom_left_radius</strong> (<em>int</em>) -- (optional) used for setting the value of bottom left
   border. If you don't set this value, it will use the border_radius value.</li>
   <li><strong>border_bottom_right_radius</strong> (<em>int</em>) -- <p>(optional) used for setting the value of bottom right
   border. If you don't set this value, it will use the border_radius value.</p>
   <blockquote>
   <div><div class="line-block">
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">border_radius</span> <span class="pre">&lt;</span> <span class="pre">1</span></code> it will draw rectangle without rounded corners</div>
   <div class="line">if any of border radii has the value <code class="docutils literal notranslate"><span class="pre">&lt;</span> <span class="pre">0</span></code> it will use value of the border_radius</div>
   <div class="line">If sum of radii on the same side of the rectangle is greater than the rect size the radii</div>
   <div class="line">will get scaled</div>
   </div>
   </div></blockquote>
   </li>
   </ul>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first">a rect bounding the changed pixels, if nothing is drawn the
   bounding rect's position will be the position of the given <code class="docutils literal notranslate"><span class="pre">rect</span></code>
   parameter and its width and height will be 0</p>
   </td>
   </tr>
   <tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body"><p class="first last"><a class="reference internal" href="rect.html#pygame.Rect" title="pygame.Rect">Rect</a></p>
   </td>
   </tr>
   </tbody>
   </table>
   <div class="admonition note">
   <p class="first admonition-title">Note</p>
   <p class="last">The <a class="tooltip reference internal" href="surface.html#pygame.Surface.fill" title=""><code class="xref py py-func docutils literal notranslate"><span class="pre">pygame.Surface.fill()</span></code><span class="tooltip-content">fill Surface with a solid color</span></a> method works just as well for drawing
   filled rectangles and can be hardware accelerated on some platforms with
   both software and hardware display modes.</p>
   </div>
   <div class="versionchanged">
   <p><span class="versionmodified">Changed in pygame 2.0.0: </span>Added support for keyword arguments.</p>
   </div>
   <div class="versionchanged">
   <p><span class="versionmodified">Changed in pygame 2.0.0.dev8: </span>Added support for border radius.</p>
   </div>
   </dd></dl>

   <dl class="definition function">
   <dt class="title" id="pygame.draw.polygon">
   <code class="descclassname">pygame.draw.</code><code class="descname">polygon</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pygame.draw.polygon" title="Permalink to this definition">¶</a></dt>
   <dd><div class="line-block">
   <div class="line"><span class="summaryline">draw a polygon</span></div>
   <div class="line"><span class="signature">polygon(surface, color, points) -&gt; Rect</span></div>
   <div class="line"><span class="signature">polygon(surface, color, points, width=0) -&gt; Rect</span></div>
   </div>
   <p>Draws a polygon on the given surface.</p>
   <table class="docutils field-list" frame="void" rules="none">
   <col class="field-name" />
   <col class="field-body" />
   <tbody valign="top">
   <tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
   <li><strong>surface</strong> (<a class="reference internal" href="surface.html#pygame.Surface" title="pygame.Surface"><em>Surface</em></a>) -- surface to draw on</li>
   <li><strong>color</strong> (<a class="reference internal" href="color.html#pygame.Color" title="pygame.Color"><em>Color</em></a><em> or </em><em>int</em><em> or </em><em>tuple</em><em>(</em><em>int</em><em>, </em><em>int</em><em>, </em><em>int</em><em>, </em><em>[</em><em>int</em><em>]</em><em>)</em>) -- color to draw with, the alpha value is optional if using a
   tuple <code class="docutils literal notranslate"><span class="pre">(RGB[A])</span></code></li>
   <li><strong>points</strong> (<em>tuple</em><em>(</em><em>coordinate</em><em>) or </em><em>list</em><em>(</em><em>coordinate</em><em>)</em>) -- a sequence of 3 or more (x, y) coordinates that make up the
   vertices of the polygon, each <em>coordinate</em> in the sequence must be a
   tuple/list/<a class="tooltip reference internal" href="math.html#pygame.math.Vector2" title=""><code class="xref py py-class docutils literal notranslate"><span class="pre">pygame.math.Vector2</span></code><span class="tooltip-content">a 2-Dimensional Vector</span></a> of 2 ints/floats,
   e.g. <code class="docutils literal notranslate"><span class="pre">[(x1,</span> <span class="pre">y1),</span> <span class="pre">(x2,</span> <span class="pre">y2),</span> <span class="pre">(x3,</span> <span class="pre">y3)]</span></code></li>
   <li><strong>width</strong> (<em>int</em>) -- <p>(optional) used for line thickness or to indicate that
   the polygon is to be filled</p>
   <blockquote>
   <div><div class="line-block">
   <div class="line">if width == 0, (default) fill the polygon</div>
   <div class="line">if width &gt; 0, used for line thickness</div>
   <div class="line">if width &lt; 0, nothing will be drawn</div>
   <div class="line"><br /></div>
   </div>
   <div class="admonition note">
   <p class="first admonition-title">Note</p>
   <p class="last">When using <code class="docutils literal notranslate"><span class="pre">width</span></code> values <code class="docutils literal notranslate"><span class="pre">&gt;</span> <span class="pre">1</span></code>, the edge lines will grow
   outside the original boundary of the polygon. For more details on
   how the thickness for edge lines grow, refer to the <code class="docutils literal notranslate"><span class="pre">width</span></code> notes
   of the <a class="tooltip reference internal" href="#pygame.draw.line" title=""><code class="xref py py-func docutils literal notranslate"><span class="pre">pygame.draw.line()</span></code><span class="tooltip-content">draw a straight line</span></a> function.</p>
   </div>
   </div></blockquote>
   </li>
   </ul>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first">a rect bounding the changed pixels, if nothing is drawn the
   bounding rect's position will be the position of the first point in the
   <code class="docutils literal notranslate"><span class="pre">points</span></code> parameter (float values will be truncated) and its width and
   height will be 0</p>
   </td>
   </tr>
   <tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body"><p class="first"><a class="reference internal" href="rect.html#pygame.Rect" title="pygame.Rect">Rect</a></p>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Raises:</th><td class="field-body"><ul class="first last simple">
   <li><strong>ValueError</strong> -- if <code class="docutils literal notranslate"><span class="pre">len(points)</span> <span class="pre">&lt;</span> <span class="pre">3</span></code> (must have at least 3 points)</li>
   <li><strong>TypeError</strong> -- if <code class="docutils literal notranslate"><span class="pre">points</span></code> is not a sequence or <code class="docutils literal notranslate"><span class="pre">points</span></code> does not
   contain number pairs</li>
   </ul>
   </td>
   </tr>
   </tbody>
   </table>
   <div class="admonition note">
   <p class="first admonition-title">Note</p>
   <p class="last">For an aapolygon, use <a class="reference internal" href="#pygame.draw.aalines" title="pygame.draw.aalines"><code class="xref py py-func docutils literal notranslate"><span class="pre">aalines()</span></code></a> with <code class="docutils literal notranslate"><span class="pre">closed=True</span></code>.</p>
   </div>
   <div class="versionchanged">
   <p><span class="versionmodified">Changed in pygame 2.0.0: </span>Added support for keyword arguments.</p>
   </div>
   </dd></dl>

   <dl class="definition function">
   <dt class="title" id="pygame.draw.circle">
   <code class="descclassname">pygame.draw.</code><code class="descname">circle</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pygame.draw.circle" title="Permalink to this definition">¶</a></dt>
   <dd><div class="line-block">
   <div class="line"><span class="summaryline">draw a circle</span></div>
   <div class="line"><span class="signature">circle(surface, color, center, radius) -&gt; Rect</span></div>
   <div class="line"><span class="signature">circle(surface, color, center, radius, width=0, draw_top_right=None, draw_top_left=None, draw_bottom_left=None, draw_bottom_right=None) -&gt; Rect</span></div>
   </div>
   <p>Draws a circle on the given surface.</p>
   <table class="docutils field-list" frame="void" rules="none">
   <col class="field-name" />
   <col class="field-body" />
   <tbody valign="top">
   <tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
   <li><strong>surface</strong> (<a class="reference internal" href="surface.html#pygame.Surface" title="pygame.Surface"><em>Surface</em></a>) -- surface to draw on</li>
   <li><strong>color</strong> (<a class="reference internal" href="color.html#pygame.Color" title="pygame.Color"><em>Color</em></a><em> or </em><em>int</em><em> or </em><em>tuple</em><em>(</em><em>int</em><em>, </em><em>int</em><em>, </em><em>int</em><em>, </em><em>[</em><em>int</em><em>]</em><em>)</em>) -- color to draw with, the alpha value is optional if using a
   tuple <code class="docutils literal notranslate"><span class="pre">(RGB[A])</span></code></li>
   <li><strong>center</strong> (<em>tuple</em><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>) or
   </em><em>list</em><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>) or </em><a class="reference internal" href="math.html#pygame.math.Vector2" title="pygame.math.Vector2"><em>Vector2</em></a><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>)</em>) -- center point of the circle as a sequence of 2 ints/floats,
   e.g. <code class="docutils literal notranslate"><span class="pre">(x,</span> <span class="pre">y)</span></code></li>
   <li><strong>radius</strong> (<em>int</em><em> or </em><em>float</em>) -- radius of the circle, measured from the <code class="docutils literal notranslate"><span class="pre">center</span></code> parameter,
   nothing will be drawn if the <code class="docutils literal notranslate"><span class="pre">radius</span></code> is less than 1</li>
   <li><strong>width</strong> (<em>int</em>) -- <p>(optional) used for line thickness or to indicate that
   the circle is to be filled</p>
   <blockquote>
   <div><div class="line-block">
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">width</span> <span class="pre">==</span> <span class="pre">0</span></code>, (default) fill the circle</div>
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">width</span> <span class="pre">&gt;</span> <span class="pre">0</span></code>, used for line thickness</div>
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">width</span> <span class="pre">&lt;</span> <span class="pre">0</span></code>, nothing will be drawn</div>
   <div class="line"><br /></div>
   </div>
   <div class="admonition note">
   <p class="first admonition-title">Note</p>
   <p class="last">When using <code class="docutils literal notranslate"><span class="pre">width</span></code> values <code class="docutils literal notranslate"><span class="pre">&gt;</span> <span class="pre">1</span></code>, the edge lines will only grow
   inward.</p>
   </div>
   </div></blockquote>
   </li>
   <li><strong>draw_top_right</strong> (<em>bool</em>) -- (optional) if this is set to True than the top right corner
   of the circle will be drawn</li>
   <li><strong>draw_top_left</strong> (<em>bool</em>) -- (optional) if this is set to True than the top left corner
   of the circle will be drawn</li>
   <li><strong>draw_bottom_left</strong> (<em>bool</em>) -- (optional) if this is set to True than the bottom left corner
   of the circle will be drawn</li>
   <li><strong>draw_bottom_right</strong> (<em>bool</em>) -- <p>(optional) if this is set to True than the bottom right corner
   of the circle will be drawn</p>
   <blockquote>
   <div><div class="line-block">
   <div class="line">if any of the draw_circle_part is True than it will draw all circle parts that have the True</div>
   <div class="line">value, otherwise it will draw the entire circle.</div>
   </div>
   </div></blockquote>
   </li>
   </ul>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first">a rect bounding the changed pixels, if nothing is drawn the
   bounding rect's position will be the <code class="docutils literal notranslate"><span class="pre">center</span></code> parameter value (float
   values will be truncated) and its width and height will be 0</p>
   </td>
   </tr>
   <tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body"><p class="first"><a class="reference internal" href="rect.html#pygame.Rect" title="pygame.Rect">Rect</a></p>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Raises:</th><td class="field-body"><ul class="first last simple">
   <li><strong>TypeError</strong> -- if <code class="docutils literal notranslate"><span class="pre">center</span></code> is not a sequence of two numbers</li>
   <li><strong>TypeError</strong> -- if <code class="docutils literal notranslate"><span class="pre">radius</span></code> is not a number</li>
   </ul>
   </td>
   </tr>
   </tbody>
   </table>
   <div class="versionchanged">
   <p><span class="versionmodified">Changed in pygame 2.0.0: </span>Added support for keyword arguments.
   Nothing is drawn when the radius is 0 (a pixel at the <code class="docutils literal notranslate"><span class="pre">center</span></code> coordinates
   used to be drawn when the radius equaled 0).
   Floats, and Vector2 are accepted for the <code class="docutils literal notranslate"><span class="pre">center</span></code> param.
   The drawing algorithm was improved to look more like a circle.</p>
   </div>
   <div class="versionchanged">
   <p><span class="versionmodified">Changed in pygame 2.0.0.dev8: </span>Added support for drawing circle quadrants.</p>
   </div>
   </dd></dl>

   <dl class="definition function">
   <dt class="title" id="pygame.draw.ellipse">
   <code class="descclassname">pygame.draw.</code><code class="descname">ellipse</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pygame.draw.ellipse" title="Permalink to this definition">¶</a></dt>
   <dd><div class="line-block">
   <div class="line"><span class="summaryline">draw an ellipse</span></div>
   <div class="line"><span class="signature">ellipse(surface, color, rect) -&gt; Rect</span></div>
   <div class="line"><span class="signature">ellipse(surface, color, rect, width=0) -&gt; Rect</span></div>
   </div>
   <p>Draws an ellipse on the given surface.</p>
   <table class="docutils field-list" frame="void" rules="none">
   <col class="field-name" />
   <col class="field-body" />
   <tbody valign="top">
   <tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
   <li><strong>surface</strong> (<a class="reference internal" href="surface.html#pygame.Surface" title="pygame.Surface"><em>Surface</em></a>) -- surface to draw on</li>
   <li><strong>color</strong> (<a class="reference internal" href="color.html#pygame.Color" title="pygame.Color"><em>Color</em></a><em> or </em><em>int</em><em> or </em><em>tuple</em><em>(</em><em>int</em><em>, </em><em>int</em><em>, </em><em>int</em><em>, </em><em>[</em><em>int</em><em>]</em><em>)</em>) -- color to draw with, the alpha value is optional if using a
   tuple <code class="docutils literal notranslate"><span class="pre">(RGB[A])</span></code></li>
   <li><strong>rect</strong> (<a class="reference internal" href="rect.html#pygame.Rect" title="pygame.Rect"><em>Rect</em></a>) -- rectangle to indicate the position and dimensions of the
   ellipse, the ellipse will be centered inside the rectangle and bounded
   by it</li>
   <li><strong>width</strong> (<em>int</em>) -- <p>(optional) used for line thickness or to indicate that
   the ellipse is to be filled (not to be confused with the width value
   of the <code class="docutils literal notranslate"><span class="pre">rect</span></code> parameter)</p>
   <blockquote>
   <div><div class="line-block">
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">width</span> <span class="pre">==</span> <span class="pre">0</span></code>, (default) fill the ellipse</div>
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">width</span> <span class="pre">&gt;</span> <span class="pre">0</span></code>, used for line thickness</div>
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">width</span> <span class="pre">&lt;</span> <span class="pre">0</span></code>, nothing will be drawn</div>
   <div class="line"><br /></div>
   </div>
   <div class="admonition note">
   <p class="first admonition-title">Note</p>
   <p class="last">When using <code class="docutils literal notranslate"><span class="pre">width</span></code> values <code class="docutils literal notranslate"><span class="pre">&gt;</span> <span class="pre">1</span></code>, the edge lines will only grow
   inward from the original boundary of the <code class="docutils literal notranslate"><span class="pre">rect</span></code> parameter.</p>
   </div>
   </div></blockquote>
   </li>
   </ul>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first">a rect bounding the changed pixels, if nothing is drawn the
   bounding rect's position will be the position of the given <code class="docutils literal notranslate"><span class="pre">rect</span></code>
   parameter and its width and height will be 0</p>
   </td>
   </tr>
   <tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body"><p class="first last"><a class="reference internal" href="rect.html#pygame.Rect" title="pygame.Rect">Rect</a></p>
   </td>
   </tr>
   </tbody>
   </table>
   <div class="versionchanged">
   <p><span class="versionmodified">Changed in pygame 2.0.0: </span>Added support for keyword arguments.</p>
   </div>
   </dd></dl>

   <dl class="definition function">
   <dt class="title" id="pygame.draw.arc">
   <code class="descclassname">pygame.draw.</code><code class="descname">arc</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pygame.draw.arc" title="Permalink to this definition">¶</a></dt>
   <dd><div class="line-block">
   <div class="line"><span class="summaryline">draw an elliptical arc</span></div>
   <div class="line"><span class="signature">arc(surface, color, rect, start_angle, stop_angle) -&gt; Rect</span></div>
   <div class="line"><span class="signature">arc(surface, color, rect, start_angle, stop_angle, width=1) -&gt; Rect</span></div>
   </div>
   <p>Draws an elliptical arc on the given surface.</p>
   <p>The two angle arguments are given in radians and indicate the start and stop
   positions of the arc. The arc is drawn in a counterclockwise direction from
   the <code class="docutils literal notranslate"><span class="pre">start_angle</span></code> to the <code class="docutils literal notranslate"><span class="pre">stop_angle</span></code>.</p>
   <table class="docutils field-list" frame="void" rules="none">
   <col class="field-name" />
   <col class="field-body" />
   <tbody valign="top">
   <tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
   <li><strong>surface</strong> (<a class="reference internal" href="surface.html#pygame.Surface" title="pygame.Surface"><em>Surface</em></a>) -- surface to draw on</li>
   <li><strong>color</strong> (<a class="reference internal" href="color.html#pygame.Color" title="pygame.Color"><em>Color</em></a><em> or </em><em>int</em><em> or </em><em>tuple</em><em>(</em><em>int</em><em>, </em><em>int</em><em>, </em><em>int</em><em>, </em><em>[</em><em>int</em><em>]</em><em>)</em>) -- color to draw with, the alpha value is optional if using a
   tuple <code class="docutils literal notranslate"><span class="pre">(RGB[A])</span></code></li>
   <li><strong>rect</strong> (<a class="reference internal" href="rect.html#pygame.Rect" title="pygame.Rect"><em>Rect</em></a>) -- rectangle to indicate the position and dimensions of the
   ellipse which the arc will be based on, the ellipse will be centered
   inside the rectangle</li>
   <li><strong>start_angle</strong> (<em>float</em>) -- start angle of the arc in radians</li>
   <li><strong>stop_angle</strong> (<em>float</em>) -- <p>stop angle of the arc in
   radians</p>
   <blockquote>
   <div><div class="line-block">
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">start_angle</span> <span class="pre">&lt;</span> <span class="pre">stop_angle</span></code>, the arc is drawn in a
   counterclockwise direction from the <code class="docutils literal notranslate"><span class="pre">start_angle</span></code> to the
   <code class="docutils literal notranslate"><span class="pre">stop_angle</span></code></div>
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">start_angle</span> <span class="pre">&gt;</span> <span class="pre">stop_angle</span></code>, tau (tau == 2 * pi) will be added
   to the <code class="docutils literal notranslate"><span class="pre">stop_angle</span></code>, if the resulting stop angle value is greater
   than the <code class="docutils literal notranslate"><span class="pre">start_angle</span></code> the above <code class="docutils literal notranslate"><span class="pre">start_angle</span> <span class="pre">&lt;</span> <span class="pre">stop_angle</span></code> case
   applies, otherwise nothing will be drawn</div>
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">start_angle</span> <span class="pre">==</span> <span class="pre">stop_angle</span></code>, nothing will be drawn</div>
   <div class="line"><br /></div>
   </div>
   </div></blockquote>
   </li>
   <li><strong>width</strong> (<em>int</em>) -- <p>(optional) used for line thickness (not to be confused
   with the width value of the <code class="docutils literal notranslate"><span class="pre">rect</span></code> parameter)</p>
   <blockquote>
   <div><div class="line-block">
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">width</span> <span class="pre">==</span> <span class="pre">0</span></code>, nothing will be drawn</div>
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">width</span> <span class="pre">&gt;</span> <span class="pre">0</span></code>, (default is 1) used for line thickness</div>
   <div class="line">if <code class="docutils literal notranslate"><span class="pre">width</span> <span class="pre">&lt;</span> <span class="pre">0</span></code>, same as <code class="docutils literal notranslate"><span class="pre">width</span> <span class="pre">==</span> <span class="pre">0</span></code></div>
   </div>
   <div class="admonition note">
   <p class="first admonition-title">Note</p>
   <p class="last">When using <code class="docutils literal notranslate"><span class="pre">width</span></code> values <code class="docutils literal notranslate"><span class="pre">&gt;</span> <span class="pre">1</span></code>, the edge lines will only grow
   inward from the original boundary of the <code class="docutils literal notranslate"><span class="pre">rect</span></code> parameter.</p>
   </div>
   </div></blockquote>
   </li>
   </ul>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first">a rect bounding the changed pixels, if nothing is drawn the
   bounding rect's position will be the position of the given <code class="docutils literal notranslate"><span class="pre">rect</span></code>
   parameter and its width and height will be 0</p>
   </td>
   </tr>
   <tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body"><p class="first last"><a class="reference internal" href="rect.html#pygame.Rect" title="pygame.Rect">Rect</a></p>
   </td>
   </tr>
   </tbody>
   </table>
   <div class="versionchanged">
   <p><span class="versionmodified">Changed in pygame 2.0.0: </span>Added support for keyword arguments.</p>
   </div>
   </dd></dl>

   <dl class="definition function">
   <dt class="title" id="pygame.draw.line">
   <code class="descclassname">pygame.draw.</code><code class="descname">line</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pygame.draw.line" title="Permalink to this definition">¶</a></dt>
   <dd><div class="line-block">
   <div class="line"><span class="summaryline">draw a straight line</span></div>
   <div class="line"><span class="signature">line(surface, color, start_pos, end_pos, width) -&gt; Rect</span></div>
   <div class="line"><span class="signature">line(surface, color, start_pos, end_pos, width=1) -&gt; Rect</span></div>
   </div>
   <p>Draws a straight line on the given surface. There are no endcaps. For thick
   lines the ends are squared off.</p>
   <table class="docutils field-list" frame="void" rules="none">
   <col class="field-name" />
   <col class="field-body" />
   <tbody valign="top">
   <tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
   <li><strong>surface</strong> (<a class="reference internal" href="surface.html#pygame.Surface" title="pygame.Surface"><em>Surface</em></a>) -- surface to draw on</li>
   <li><strong>color</strong> (<a class="reference internal" href="color.html#pygame.Color" title="pygame.Color"><em>Color</em></a><em> or </em><em>int</em><em> or </em><em>tuple</em><em>(</em><em>int</em><em>, </em><em>int</em><em>, </em><em>int</em><em>, </em><em>[</em><em>int</em><em>]</em><em>)</em>) -- color to draw with, the alpha value is optional if using a
   tuple <code class="docutils literal notranslate"><span class="pre">(RGB[A])</span></code></li>
   <li><strong>start_pos</strong> (<em>tuple</em><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>) or
   </em><em>list</em><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>) or </em><a class="reference internal" href="math.html#pygame.math.Vector2" title="pygame.math.Vector2"><em>Vector2</em></a><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>)</em>) -- start position of the line, (x, y)</li>
   <li><strong>end_pos</strong> (<em>tuple</em><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>) or
   </em><em>list</em><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>) or </em><a class="reference internal" href="math.html#pygame.math.Vector2" title="pygame.math.Vector2"><em>Vector2</em></a><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>)</em>) -- end position of the line, (x, y)</li>
   <li><strong>width</strong> (<em>int</em>) -- <p>(optional) used for line thickness</p>
   <div class="line-block">
   <div class="line">if width &gt;= 1, used for line thickness (default is 1)</div>
   <div class="line">if width &lt; 1, nothing will be drawn</div>
   <div class="line"><br /></div>
   </div>
   <div class="admonition note">
   <p class="first admonition-title">Note</p>
   <p>When using <code class="docutils literal notranslate"><span class="pre">width</span></code> values <code class="docutils literal notranslate"><span class="pre">&gt;</span> <span class="pre">1</span></code>, lines will grow as follows.</p>
   <p>For odd <code class="docutils literal notranslate"><span class="pre">width</span></code> values, the thickness of each line grows with the
   original line being in the center.</p>
   <p class="last">For even <code class="docutils literal notranslate"><span class="pre">width</span></code> values, the thickness of each line grows with the
   original line being offset from the center (as there is no exact
   center line drawn). As a result, lines with a slope &lt; 1
   (horizontal-ish) will have 1 more pixel of thickness below the
   original line (in the y direction). Lines with a slope &gt;= 1
   (vertical-ish) will have 1 more pixel of thickness to the right of
   the original line (in the x direction).</p>
   </div>
   </li>
   </ul>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first">a rect bounding the changed pixels, if nothing is drawn the
   bounding rect's position will be the <code class="docutils literal notranslate"><span class="pre">start_pos</span></code> parameter value (float
   values will be truncated) and its width and height will be 0</p>
   </td>
   </tr>
   <tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body"><p class="first"><a class="reference internal" href="rect.html#pygame.Rect" title="pygame.Rect">Rect</a></p>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Raises:</th><td class="field-body"><p class="first last"><strong>TypeError</strong> -- if <code class="docutils literal notranslate"><span class="pre">start_pos</span></code> or <code class="docutils literal notranslate"><span class="pre">end_pos</span></code> is not a sequence of
   two numbers</p>
   </td>
   </tr>
   </tbody>
   </table>
   <div class="versionchanged">
   <p><span class="versionmodified">Changed in pygame 2.0.0: </span>Added support for keyword arguments.</p>
   </div>
   </dd></dl>

   <dl class="definition function">
   <dt class="title" id="pygame.draw.lines">
   <code class="descclassname">pygame.draw.</code><code class="descname">lines</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pygame.draw.lines" title="Permalink to this definition">¶</a></dt>
   <dd><div class="line-block">
   <div class="line"><span class="summaryline">draw multiple contiguous straight line segments</span></div>
   <div class="line"><span class="signature">lines(surface, color, closed, points) -&gt; Rect</span></div>
   <div class="line"><span class="signature">lines(surface, color, closed, points, width=1) -&gt; Rect</span></div>
   </div>
   <p>Draws a sequence of contiguous straight lines on the given surface. There are
   no endcaps or miter joints. For thick lines the ends are squared off.
   Drawing thick lines with sharp corners can have undesired looking results.</p>
   <table class="docutils field-list" frame="void" rules="none">
   <col class="field-name" />
   <col class="field-body" />
   <tbody valign="top">
   <tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
   <li><strong>surface</strong> (<a class="reference internal" href="surface.html#pygame.Surface" title="pygame.Surface"><em>Surface</em></a>) -- surface to draw on</li>
   <li><strong>color</strong> (<a class="reference internal" href="color.html#pygame.Color" title="pygame.Color"><em>Color</em></a><em> or </em><em>int</em><em> or </em><em>tuple</em><em>(</em><em>int</em><em>, </em><em>int</em><em>, </em><em>int</em><em>, </em><em>[</em><em>int</em><em>]</em><em>)</em>) -- color to draw with, the alpha value is optional if using a
   tuple <code class="docutils literal notranslate"><span class="pre">(RGB[A])</span></code></li>
   <li><strong>closed</strong> (<em>bool</em>) -- if <code class="docutils literal notranslate"><span class="pre">True</span></code> an additional line segment is drawn between
   the first and last points in the <code class="docutils literal notranslate"><span class="pre">points</span></code> sequence</li>
   <li><strong>points</strong> (<em>tuple</em><em>(</em><em>coordinate</em><em>) or </em><em>list</em><em>(</em><em>coordinate</em><em>)</em>) -- a sequence of 2 or more (x, y) coordinates, where each
   <em>coordinate</em> in the sequence must be a
   tuple/list/<a class="tooltip reference internal" href="math.html#pygame.math.Vector2" title=""><code class="xref py py-class docutils literal notranslate"><span class="pre">pygame.math.Vector2</span></code><span class="tooltip-content">a 2-Dimensional Vector</span></a> of 2 ints/floats and adjacent
   coordinates will be connected by a line segment, e.g. for the
   points <code class="docutils literal notranslate"><span class="pre">[(x1,</span> <span class="pre">y1),</span> <span class="pre">(x2,</span> <span class="pre">y2),</span> <span class="pre">(x3,</span> <span class="pre">y3)]</span></code> a line segment will be drawn
   from <code class="docutils literal notranslate"><span class="pre">(x1,</span> <span class="pre">y1)</span></code> to <code class="docutils literal notranslate"><span class="pre">(x2,</span> <span class="pre">y2)</span></code> and from <code class="docutils literal notranslate"><span class="pre">(x2,</span> <span class="pre">y2)</span></code> to <code class="docutils literal notranslate"><span class="pre">(x3,</span> <span class="pre">y3)</span></code>,
   additionally if the <code class="docutils literal notranslate"><span class="pre">closed</span></code> parameter is <code class="docutils literal notranslate"><span class="pre">True</span></code> another line segment
   will be drawn from <code class="docutils literal notranslate"><span class="pre">(x3,</span> <span class="pre">y3)</span></code> to <code class="docutils literal notranslate"><span class="pre">(x1,</span> <span class="pre">y1)</span></code></li>
   <li><strong>width</strong> (<em>int</em>) -- <p>(optional) used for line thickness</p>
   <div class="line-block">
   <div class="line">if width &gt;= 1, used for line thickness (default is 1)</div>
   <div class="line">if width &lt; 1, nothing will be drawn</div>
   <div class="line"><br /></div>
   </div>
   <div class="admonition note">
   <p class="first admonition-title">Note</p>
   <p class="last">When using <code class="docutils literal notranslate"><span class="pre">width</span></code> values <code class="docutils literal notranslate"><span class="pre">&gt;</span> <span class="pre">1</span></code> refer to the <code class="docutils literal notranslate"><span class="pre">width</span></code> notes
   of <a class="reference internal" href="#pygame.draw.line" title="pygame.draw.line"><code class="xref py py-func docutils literal notranslate"><span class="pre">line()</span></code></a> for details on how thick lines grow.</p>
   </div>
   </li>
   </ul>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first">a rect bounding the changed pixels, if nothing is drawn the
   bounding rect's position will be the position of the first point in the
   <code class="docutils literal notranslate"><span class="pre">points</span></code> parameter (float values will be truncated) and its width and
   height will be 0</p>
   </td>
   </tr>
   <tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body"><p class="first"><a class="reference internal" href="rect.html#pygame.Rect" title="pygame.Rect">Rect</a></p>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Raises:</th><td class="field-body"><ul class="first last simple">
   <li><strong>ValueError</strong> -- if <code class="docutils literal notranslate"><span class="pre">len(points)</span> <span class="pre">&lt;</span> <span class="pre">2</span></code> (must have at least 2 points)</li>
   <li><strong>TypeError</strong> -- if <code class="docutils literal notranslate"><span class="pre">points</span></code> is not a sequence or <code class="docutils literal notranslate"><span class="pre">points</span></code> does not
   contain number pairs</li>
   </ul>
   </td>
   </tr>
   </tbody>
   </table>
   <div class="versionchanged">
   <p><span class="versionmodified">Changed in pygame 2.0.0: </span>Added support for keyword arguments.</p>
   </div>
   </dd></dl>

   <dl class="definition function">
   <dt class="title" id="pygame.draw.aaline">
   <code class="descclassname">pygame.draw.</code><code class="descname">aaline</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pygame.draw.aaline" title="Permalink to this definition">¶</a></dt>
   <dd><div class="line-block">
   <div class="line"><span class="summaryline">draw a straight antialiased line</span></div>
   <div class="line"><span class="signature">aaline(surface, color, start_pos, end_pos) -&gt; Rect</span></div>
   <div class="line"><span class="signature">aaline(surface, color, start_pos, end_pos, blend=1) -&gt; Rect</span></div>
   </div>
   <p>Draws a straight antialiased line on the given surface.</p>
   <table class="docutils field-list" frame="void" rules="none">
   <col class="field-name" />
   <col class="field-body" />
   <tbody valign="top">
   <tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
   <li><strong>surface</strong> (<a class="reference internal" href="surface.html#pygame.Surface" title="pygame.Surface"><em>Surface</em></a>) -- surface to draw on</li>
   <li><strong>color</strong> (<a class="reference internal" href="color.html#pygame.Color" title="pygame.Color"><em>Color</em></a><em> or </em><em>int</em><em> or </em><em>tuple</em><em>(</em><em>int</em><em>, </em><em>int</em><em>, </em><em>int</em><em>, </em><em>[</em><em>int</em><em>]</em><em>)</em>) -- color to draw with, the alpha value is optional if using a
   tuple <code class="docutils literal notranslate"><span class="pre">(RGB[A])</span></code></li>
   <li><strong>start_pos</strong> (<em>tuple</em><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>) or
   </em><em>list</em><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>) or </em><a class="reference internal" href="math.html#pygame.math.Vector2" title="pygame.math.Vector2"><em>Vector2</em></a><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>)</em>) -- start position of the line, (x, y)</li>
   <li><strong>end_pos</strong> (<em>tuple</em><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>) or
   </em><em>list</em><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>) or </em><a class="reference internal" href="math.html#pygame.math.Vector2" title="pygame.math.Vector2"><em>Vector2</em></a><em>(</em><em>int</em><em> or </em><em>float</em><em>, </em><em>int</em><em> or </em><em>float</em><em>)</em>) -- end position of the line, (x, y)</li>
   <li><strong>blend</strong> (<em>int</em>) -- (optional) if non-zero (default) the line will be blended
   with the surface's existing pixel shades, otherwise it will overwrite them</li>
   </ul>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first">a rect bounding the changed pixels, if nothing is drawn the
   bounding rect's position will be the <code class="docutils literal notranslate"><span class="pre">start_pos</span></code> parameter value (float
   values will be truncated) and its width and height will be 0</p>
   </td>
   </tr>
   <tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body"><p class="first"><a class="reference internal" href="rect.html#pygame.Rect" title="pygame.Rect">Rect</a></p>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Raises:</th><td class="field-body"><p class="first last"><strong>TypeError</strong> -- if <code class="docutils literal notranslate"><span class="pre">start_pos</span></code> or <code class="docutils literal notranslate"><span class="pre">end_pos</span></code> is not a sequence of
   two numbers</p>
   </td>
   </tr>
   </tbody>
   </table>
   <div class="versionchanged">
   <p><span class="versionmodified">Changed in pygame 2.0.0: </span>Added support for keyword arguments.</p>
   </div>
   </dd></dl>

   <dl class="definition function">
   <dt class="title" id="pygame.draw.aalines">
   <code class="descclassname">pygame.draw.</code><code class="descname">aalines</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pygame.draw.aalines" title="Permalink to this definition">¶</a></dt>
   <dd><div class="line-block">
   <div class="line"><span class="summaryline">draw multiple contiguous straight antialiased line segments</span></div>
   <div class="line"><span class="signature">aalines(surface, color, closed, points) -&gt; Rect</span></div>
   <div class="line"><span class="signature">aalines(surface, color, closed, points, blend=1) -&gt; Rect</span></div>
   </div>
   <p>Draws a sequence of contiguous straight antialiased lines on the given
   surface.</p>
   <table class="docutils field-list" frame="void" rules="none">
   <col class="field-name" />
   <col class="field-body" />
   <tbody valign="top">
   <tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
   <li><strong>surface</strong> (<a class="reference internal" href="surface.html#pygame.Surface" title="pygame.Surface"><em>Surface</em></a>) -- surface to draw on</li>
   <li><strong>color</strong> (<a class="reference internal" href="color.html#pygame.Color" title="pygame.Color"><em>Color</em></a><em> or </em><em>int</em><em> or </em><em>tuple</em><em>(</em><em>int</em><em>, </em><em>int</em><em>, </em><em>int</em><em>, </em><em>[</em><em>int</em><em>]</em><em>)</em>) -- color to draw with, the alpha value is optional if using a
   tuple <code class="docutils literal notranslate"><span class="pre">(RGB[A])</span></code></li>
   <li><strong>closed</strong> (<em>bool</em>) -- if <code class="docutils literal notranslate"><span class="pre">True</span></code> an additional line segment is drawn between
   the first and last points in the <code class="docutils literal notranslate"><span class="pre">points</span></code> sequence</li>
   <li><strong>points</strong> (<em>tuple</em><em>(</em><em>coordinate</em><em>) or </em><em>list</em><em>(</em><em>coordinate</em><em>)</em>) -- a sequence of 2 or more (x, y) coordinates, where each
   <em>coordinate</em> in the sequence must be a
   tuple/list/<a class="tooltip reference internal" href="math.html#pygame.math.Vector2" title=""><code class="xref py py-class docutils literal notranslate"><span class="pre">pygame.math.Vector2</span></code><span class="tooltip-content">a 2-Dimensional Vector</span></a> of 2 ints/floats and adjacent
   coordinates will be connected by a line segment, e.g. for the
   points <code class="docutils literal notranslate"><span class="pre">[(x1,</span> <span class="pre">y1),</span> <span class="pre">(x2,</span> <span class="pre">y2),</span> <span class="pre">(x3,</span> <span class="pre">y3)]</span></code> a line segment will be drawn
   from <code class="docutils literal notranslate"><span class="pre">(x1,</span> <span class="pre">y1)</span></code> to <code class="docutils literal notranslate"><span class="pre">(x2,</span> <span class="pre">y2)</span></code> and from <code class="docutils literal notranslate"><span class="pre">(x2,</span> <span class="pre">y2)</span></code> to <code class="docutils literal notranslate"><span class="pre">(x3,</span> <span class="pre">y3)</span></code>,
   additionally if the <code class="docutils literal notranslate"><span class="pre">closed</span></code> parameter is <code class="docutils literal notranslate"><span class="pre">True</span></code> another line segment
   will be drawn from <code class="docutils literal notranslate"><span class="pre">(x3,</span> <span class="pre">y3)</span></code> to <code class="docutils literal notranslate"><span class="pre">(x1,</span> <span class="pre">y1)</span></code></li>
   <li><strong>blend</strong> (<em>int</em>) -- (optional) if non-zero (default) each line will be blended
   with the surface's existing pixel shades, otherwise the pixels will be
   overwritten</li>
   </ul>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first">a rect bounding the changed pixels, if nothing is drawn the
   bounding rect's position will be the position of the first point in the
   <code class="docutils literal notranslate"><span class="pre">points</span></code> parameter (float values will be truncated) and its width and
   height will be 0</p>
   </td>
   </tr>
   <tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body"><p class="first"><a class="reference internal" href="rect.html#pygame.Rect" title="pygame.Rect">Rect</a></p>
   </td>
   </tr>
   <tr class="field-even field"><th class="field-name">Raises:</th><td class="field-body"><ul class="first last simple">
   <li><strong>ValueError</strong> -- if <code class="docutils literal notranslate"><span class="pre">len(points)</span> <span class="pre">&lt;</span> <span class="pre">2</span></code> (must have at least 2 points)</li>
   <li><strong>TypeError</strong> -- if <code class="docutils literal notranslate"><span class="pre">points</span></code> is not a sequence or <code class="docutils literal notranslate"><span class="pre">points</span></code> does not
   contain number pairs</li>
   </ul>
   </td>
   </tr>
   </tbody>
   </table>
   <div class="versionchanged">
   <p><span class="versionmodified">Changed in pygame 2.0.0: </span>Added support for keyword arguments.</p>
   </div>
   </dd></dl>

   <div class="figure" id="id1">
   <a class="reference internal image-reference" href="../images/lab5/draw_module_example.png"><img alt="draw module example" src="../images/lab5/draw_module_example.png" style="width: 200.0px; height: 165.0px;" /></a>
   <p class="caption"><span class="caption-text">Example code for draw module.</span></p>
   </div>
   <div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="c1"># Import a library of functions called &#39;pygame&#39;</span>
   <span class="kn">import</span> <span class="nn">pygame</span>
   <span class="kn">from</span> <span class="nn">math</span> <span class="k">import</span> <span class="n">pi</span>

   <span class="c1"># Initialize the game engine</span>
   <span class="n">pygame</span><span class="o">.</span><span class="n">init</span><span class="p">()</span>

   <span class="c1"># Define the colors we will use in RGB format</span>
   <span class="n">BLACK</span> <span class="o">=</span> <span class="p">(</span>  <span class="mi">0</span><span class="p">,</span>   <span class="mi">0</span><span class="p">,</span>   <span class="mi">0</span><span class="p">)</span>
   <span class="n">WHITE</span> <span class="o">=</span> <span class="p">(</span><span class="mi">255</span><span class="p">,</span> <span class="mi">255</span><span class="p">,</span> <span class="mi">255</span><span class="p">)</span>
   <span class="n">BLUE</span> <span class="o">=</span>  <span class="p">(</span>  <span class="mi">0</span><span class="p">,</span>   <span class="mi">0</span><span class="p">,</span> <span class="mi">255</span><span class="p">)</span>
   <span class="n">GREEN</span> <span class="o">=</span> <span class="p">(</span>  <span class="mi">0</span><span class="p">,</span> <span class="mi">255</span><span class="p">,</span>   <span class="mi">0</span><span class="p">)</span>
   <span class="n">RED</span> <span class="o">=</span>   <span class="p">(</span><span class="mi">255</span><span class="p">,</span>   <span class="mi">0</span><span class="p">,</span>   <span class="mi">0</span><span class="p">)</span>

   <span class="c1"># Set the height and width of the screen</span>
   <span class="n">size</span> <span class="o">=</span> <span class="p">[</span><span class="mi">400</span><span class="p">,</span> <span class="mi">300</span><span class="p">]</span>
   <span class="n">screen</span> <span class="o">=</span> <span class="n">pygame</span><span class="o">.</span><span class="n">display</span><span class="o">.</span><span class="n">set_mode</span><span class="p">(</span><span class="n">size</span><span class="p">)</span>

   <span class="n">pygame</span><span class="o">.</span><span class="n">display</span><span class="o">.</span><span class="n">set_caption</span><span class="p">(</span><span class="s2">&quot;Example code for the draw module&quot;</span><span class="p">)</span>

   <span class="c1">#Loop until the user clicks the close button.</span>
   <span class="n">done</span> <span class="o">=</span> <span class="kc">False</span>
   <span class="n">clock</span> <span class="o">=</span> <span class="n">pygame</span><span class="o">.</span><span class="n">time</span><span class="o">.</span><span class="n">Clock</span><span class="p">()</span>

   <span class="k">while</span> <span class="ow">not</span> <span class="n">done</span><span class="p">:</span>

       <span class="c1"># This limits the while loop to a max of 10 times per second.</span>
       <span class="c1"># Leave this out and we will use all CPU we can.</span>
       <span class="n">clock</span><span class="o">.</span><span class="n">tick</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>

       <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">pygame</span><span class="o">.</span><span class="n">event</span><span class="o">.</span><span class="n">get</span><span class="p">():</span> <span class="c1"># User did something</span>
           <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">type</span> <span class="o">==</span> <span class="n">pygame</span><span class="o">.</span><span class="n">QUIT</span><span class="p">:</span> <span class="c1"># If user clicked close</span>
               <span class="n">done</span><span class="o">=</span><span class="kc">True</span> <span class="c1"># Flag that we are done so we exit this loop</span>

       <span class="c1"># All drawing code happens after the for loop and but</span>
       <span class="c1"># inside the main while done==False loop.</span>

       <span class="c1"># Clear the screen and set the screen background</span>
       <span class="n">screen</span><span class="o">.</span><span class="n">fill</span><span class="p">(</span><span class="n">WHITE</span><span class="p">)</span>

       <span class="c1"># Draw on the screen a GREEN line from (0, 0) to (50, 30) </span>
       <span class="c1"># 5 pixels wide.</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">line</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">GREEN</span><span class="p">,</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span> <span class="p">[</span><span class="mi">50</span><span class="p">,</span><span class="mi">30</span><span class="p">],</span> <span class="mi">5</span><span class="p">)</span>

       <span class="c1"># Draw on the screen 3 BLACK lines, each 5 pixels wide.</span>
       <span class="c1"># The &#39;False&#39; means the first and last points are not connected.</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">lines</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">BLACK</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="p">[[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">80</span><span class="p">],</span> <span class="p">[</span><span class="mi">50</span><span class="p">,</span> <span class="mi">90</span><span class="p">],</span> <span class="p">[</span><span class="mi">200</span><span class="p">,</span> <span class="mi">80</span><span class="p">],</span> <span class="p">[</span><span class="mi">220</span><span class="p">,</span> <span class="mi">30</span><span class="p">]],</span> <span class="mi">5</span><span class="p">)</span>

       <span class="c1"># Draw on the screen a GREEN line from (0, 50) to (50, 80) </span>
       <span class="c1"># Because it is an antialiased line, it is 1 pixel wide.</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">aaline</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">GREEN</span><span class="p">,</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">50</span><span class="p">],[</span><span class="mi">50</span><span class="p">,</span> <span class="mi">80</span><span class="p">],</span> <span class="kc">True</span><span class="p">)</span>

       <span class="c1"># Draw a rectangle outline</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">rect</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">BLACK</span><span class="p">,</span> <span class="p">[</span><span class="mi">75</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">50</span><span class="p">,</span> <span class="mi">20</span><span class="p">],</span> <span class="mi">2</span><span class="p">)</span>

       <span class="c1"># Draw a solid rectangle</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">rect</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">BLACK</span><span class="p">,</span> <span class="p">[</span><span class="mi">150</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">50</span><span class="p">,</span> <span class="mi">20</span><span class="p">])</span>

       <span class="c1"># Draw a rectangle with rounded corners</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">rect</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">GREEN</span><span class="p">,</span> <span class="p">[</span><span class="mi">115</span><span class="p">,</span> <span class="mi">210</span><span class="p">,</span> <span class="mi">70</span><span class="p">,</span> <span class="mi">40</span><span class="p">],</span> <span class="mi">10</span><span class="p">,</span> <span class="n">border_radius</span><span class="o">=</span><span class="mi">15</span><span class="p">)</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">rect</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">RED</span><span class="p">,</span> <span class="p">[</span><span class="mi">135</span><span class="p">,</span> <span class="mi">260</span><span class="p">,</span> <span class="mi">50</span><span class="p">,</span> <span class="mi">30</span><span class="p">],</span> <span class="mi">0</span><span class="p">,</span> <span class="n">border_radius</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">border_top_left_radius</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
                        <span class="n">border_bottom_right_radius</span><span class="o">=</span><span class="mi">15</span><span class="p">)</span>

       <span class="c1"># Draw an ellipse outline, using a rectangle as the outside boundaries</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">ellipse</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">RED</span><span class="p">,</span> <span class="p">[</span><span class="mi">225</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">50</span><span class="p">,</span> <span class="mi">20</span><span class="p">],</span> <span class="mi">2</span><span class="p">)</span>

       <span class="c1"># Draw an solid ellipse, using a rectangle as the outside boundaries</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">ellipse</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">RED</span><span class="p">,</span> <span class="p">[</span><span class="mi">300</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">50</span><span class="p">,</span> <span class="mi">20</span><span class="p">])</span>

       <span class="c1"># This draws a triangle using the polygon command</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">polygon</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">BLACK</span><span class="p">,</span> <span class="p">[[</span><span class="mi">100</span><span class="p">,</span> <span class="mi">100</span><span class="p">],</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">200</span><span class="p">],</span> <span class="p">[</span><span class="mi">200</span><span class="p">,</span> <span class="mi">200</span><span class="p">]],</span> <span class="mi">5</span><span class="p">)</span>

       <span class="c1"># Draw an arc as part of an ellipse. </span>
       <span class="c1"># Use radians to determine what angle to draw.</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">arc</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">BLACK</span><span class="p">,[</span><span class="mi">210</span><span class="p">,</span> <span class="mi">75</span><span class="p">,</span> <span class="mi">150</span><span class="p">,</span> <span class="mi">125</span><span class="p">],</span> <span class="mi">0</span><span class="p">,</span> <span class="n">pi</span><span class="o">/</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">arc</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">GREEN</span><span class="p">,[</span><span class="mi">210</span><span class="p">,</span> <span class="mi">75</span><span class="p">,</span> <span class="mi">150</span><span class="p">,</span> <span class="mi">125</span><span class="p">],</span> <span class="n">pi</span><span class="o">/</span><span class="mi">2</span><span class="p">,</span> <span class="n">pi</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">arc</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">BLUE</span><span class="p">,</span> <span class="p">[</span><span class="mi">210</span><span class="p">,</span> <span class="mi">75</span><span class="p">,</span> <span class="mi">150</span><span class="p">,</span> <span class="mi">125</span><span class="p">],</span> <span class="n">pi</span><span class="p">,</span><span class="mi">3</span><span class="o">*</span><span class="n">pi</span><span class="o">/</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">arc</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">RED</span><span class="p">,</span>  <span class="p">[</span><span class="mi">210</span><span class="p">,</span> <span class="mi">75</span><span class="p">,</span> <span class="mi">150</span><span class="p">,</span> <span class="mi">125</span><span class="p">],</span> <span class="mi">3</span><span class="o">*</span><span class="n">pi</span><span class="o">/</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="o">*</span><span class="n">pi</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>

       <span class="c1"># Draw a circle</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">circle</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">BLUE</span><span class="p">,</span> <span class="p">[</span><span class="mi">60</span><span class="p">,</span> <span class="mi">250</span><span class="p">],</span> <span class="mi">40</span><span class="p">)</span>

       <span class="c1"># Draw only one circle quadrant</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">circle</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">BLUE</span><span class="p">,</span> <span class="p">[</span><span class="mi">250</span><span class="p">,</span> <span class="mi">250</span><span class="p">],</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">draw_top_right</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">circle</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">RED</span><span class="p">,</span> <span class="p">[</span><span class="mi">250</span><span class="p">,</span> <span class="mi">250</span><span class="p">],</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="n">draw_top_left</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">circle</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">GREEN</span><span class="p">,</span> <span class="p">[</span><span class="mi">250</span><span class="p">,</span> <span class="mi">250</span><span class="p">],</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="n">draw_bottom_left</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">draw</span><span class="o">.</span><span class="n">circle</span><span class="p">(</span><span class="n">screen</span><span class="p">,</span> <span class="n">BLACK</span><span class="p">,</span> <span class="p">[</span><span class="mi">250</span><span class="p">,</span> <span class="mi">250</span><span class="p">],</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="n">draw_bottom_right</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

       <span class="c1"># Go ahead and update the screen with what we&#39;ve drawn.</span>
       <span class="c1"># This MUST happen after all the other drawing commands.</span>
       <span class="n">pygame</span><span class="o">.</span><span class="n">display</span><span class="o">.</span><span class="n">flip</span><span class="p">()</span>

   <span class="c1"># Be IDLE friendly</span>
   <span class="n">pygame</span><span class="o">.</span><span class="n">quit</span><span class="p">()</span>
   </pre></div>
   </div>
   </dd></dl>

   </div>


   <br /><br />
   <hr />
   <a href="https://github.com/pygame/pygame/edit/master/docs/reST/ref/draw.rst" rel="nofollow">Edit on GitHub</a>
             </div>
         </div>
         <div class="clearer"></div>
       </div>
       <div class="related" role="navigation" aria-label="related navigation">
         <h3>Navigation</h3>
         <ul>
           <li class="right" style="margin-right: 10px">
             <a href="../genindex.html" title="General Index"
                accesskey="I">index</a></li>
           <li class="right" >
             <a href="../py-modindex.html" title="Python Module Index"
                >modules</a> |</li>
           <li class="right" >
             <a href="event.html" title="pygame.event"
                accesskey="N">next</a> |</li>
           <li class="right" >
             <a href="display.html" title="pygame.display"
                accesskey="P">previous</a> |</li>
           <li class="nav-item nav-item-0"><a href="../index.html">pygame v2.0.0.dev7 documentation</a> &#187;</li>
       <script type="text/javascript" src="https://www.pygame.org/comment/jquery.plugin.docscomments.js"></script>

         </ul>
       </div>
       <div class="footer" role="contentinfo">
           &#169; Copyright 2011-2019, pygame developers.
       </div>
     </body>
   </html>
