<template>
  <div class="bk-root" id="62ea92a9-6e04-4eaf-8053-29cfd8bc3a4f" data-root-id="1076"></div>
</template>
<script>
export default {
  mounted() {
  (function() {
    var fn = function() {
      Bokeh.safely(function() {
        (function(root) {
          function embed_document(root) {

          var docs_json = '{"72c61fe4-9c5c-4ecb-be7d-15b1c9dd682f":{"roots":{"references":[{"attributes":{"grid_line_color":{"value":null},"plot":{"id":"1076","subtype":"Figure","type":"Plot"},"ticker":{"id":"1087","type":"BasicTicker"}},"id":"1090","type":"Grid"},{"attributes":{"fill_color":{"value":"#1f77b4"},"line_color":{"value":"#1f77b4"},"top":{"field":"Count"},"width":{"value":0.9},"x":{"field":"Year"}},"id":"1101","type":"VBar"},{"attributes":{"formatter":{"id":"1108","type":"BasicTickFormatter"},"plot":{"id":"1076","subtype":"Figure","type":"Plot"},"ticker":{"id":"1092","type":"BasicTicker"}},"id":"1091","type":"LinearAxis"},{"attributes":{"callback":null,"data":{"Count":[83,130,248,167,179,113,69,81,73,141,48,43,35,22,19,14,8,13,14,13,17,12,8,24,6,3,6,4,1,2],"Year":[2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,1994,2001,2000,1999,1998,1997,1996,1995,1993,1992,1991,1990,1989,1988],"index":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]},"selected":{"id":"1111","type":"Selection"},"selection_policy":{"id":"1110","type":"UnionRenderers"}},"id":"1099","type":"ColumnDataSource"},{"attributes":{"plot":null,"text":"Yearly Published Clinical NLP Papers"},"id":"1075","type":"Title"},{"attributes":{},"id":"1092","type":"BasicTicker"},{"attributes":{"data_source":{"id":"1099","type":"ColumnDataSource"},"glyph":{"id":"1101","type":"VBar"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1102","type":"VBar"},"selection_glyph":null,"view":{"id":"1104","type":"CDSView"}},"id":"1103","type":"GlyphRenderer"},{"attributes":{"dimension":1,"plot":{"id":"1076","subtype":"Figure","type":"Plot"},"ticker":{"id":"1092","type":"BasicTicker"}},"id":"1095","type":"Grid"},{"attributes":{"callback":null},"id":"1078","type":"DataRange1d"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"top":{"field":"Count"},"width":{"value":0.9},"x":{"field":"Year"}},"id":"1102","type":"VBar"},{"attributes":{},"id":"1108","type":"BasicTickFormatter"},{"attributes":{"source":{"id":"1099","type":"ColumnDataSource"}},"id":"1104","type":"CDSView"},{"attributes":{"callback":null,"start":0},"id":"1080","type":"DataRange1d"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1096","type":"HoverTool"}]},"id":"1097","type":"Toolbar"},{"attributes":{"callback":null,"tooltips":"\\n        &lt;div&gt;\\n          Year: @Year &lt;br&gt;\\n          Publications: @Count\\n        &lt;/div&gt;\\n        "},"id":"1096","type":"HoverTool"},{"attributes":{},"id":"1110","type":"UnionRenderers"},{"attributes":{},"id":"1082","type":"LinearScale"},{"attributes":{"below":[{"id":"1086","type":"LinearAxis"}],"left":[{"id":"1091","type":"LinearAxis"}],"plot_height":350,"renderers":[{"id":"1086","type":"LinearAxis"},{"id":"1090","type":"Grid"},{"id":"1091","type":"LinearAxis"},{"id":"1095","type":"Grid"},{"id":"1103","type":"GlyphRenderer"}],"title":{"id":"1075","type":"Title"},"toolbar":{"id":"1097","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"1078","type":"DataRange1d"},"x_scale":{"id":"1082","type":"LinearScale"},"y_range":{"id":"1080","type":"DataRange1d"},"y_scale":{"id":"1084","type":"LinearScale"}},"id":"1076","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"1111","type":"Selection"},{"attributes":{},"id":"1084","type":"LinearScale"},{"attributes":{},"id":"1106","type":"BasicTickFormatter"},{"attributes":{"formatter":{"id":"1106","type":"BasicTickFormatter"},"plot":{"id":"1076","subtype":"Figure","type":"Plot"},"ticker":{"id":"1087","type":"BasicTicker"}},"id":"1086","type":"LinearAxis"},{"attributes":{},"id":"1087","type":"BasicTicker"}],"root_ids":["1076"]},"title":"Bokeh Application","version":"1.0.4"}}';
          var render_items = [{"docid":"72c61fe4-9c5c-4ecb-be7d-15b1c9dd682f","roots":{"1076":"62ea92a9-6e04-4eaf-8053-29cfd8bc3a4f"}}];
          root.Bokeh.embed.embed_items(docs_json, render_items);

          }
          if (root.Bokeh !== undefined) {
            embed_document(root);
          } else {
            var attempts = 0;
            var timer = setInterval(function(root) {
              if (root.Bokeh !== undefined) {
                embed_document(root);
                clearInterval(timer);
              }
              attempts++;
              if (attempts > 100) {
                console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                clearInterval(timer);
              }
            }, 10, root)
          }
        })(window);
      });
    };
    if (document.readyState != "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  })()
  }
}
</script>
