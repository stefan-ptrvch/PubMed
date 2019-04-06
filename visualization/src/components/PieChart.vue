<template>
  <div class="bk-root" id="325e65cd-6bb6-473b-ab37-d125f950a2d0" data-root-id="1002"></div>
</template>

<script>
export default {
  mounted() {
(function() {
    var fn = function() {
      Bokeh.safely(function() {
        (function(root) {
          function embed_document(root) {

          var docs_json = '{"0eebe9be-af5c-4226-ab88-6c52fd6c66ad":{"roots":{"references":[{"attributes":{},"id":"1013","type":"BasicTicker"},{"attributes":{"axis_label":null,"formatter":{"id":"1034","type":"BasicTickFormatter"},"plot":{"id":"1002","subtype":"Figure","type":"Plot"},"ticker":{"id":"1013","type":"BasicTicker"},"visible":false},"id":"1012","type":"LinearAxis"},{"attributes":{},"id":"1010","type":"LinearScale"},{"attributes":{"callback":null},"id":"1006","type":"DataRange1d"},{"attributes":{"items":[{"id":"1039","type":"LegendItem"}],"plot":{"id":"1002","subtype":"Figure","type":"Plot"}},"id":"1038","type":"Legend"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"1022","type":"HoverTool"}]},"id":"1023","type":"Toolbar"},{"attributes":{},"id":"1008","type":"LinearScale"},{"attributes":{"callback":null,"data":{"angle":{"__ndarray__":"gsEp3hUeE0Ch2uqUFKvcPzQhFVbqIcs/P1AxLM4byj9ZrmnYlQ/IP6Ha6pQUq7w/uTgjQdyeuj8FU8xFM3q0PwVTzEUzerQ/EYLoGxd0sz8=","dtype":"float64","shape":[10]},"color":["#3182bd","#6baed6","#9ecae1","#c6dbef","#e6550d","#fd8d3c","#fdae6b","#fdd0a2","#31a354","#74c476"],"country":["United States","France","China","Australia","Germany","Austria","United Kingdom","Spain","Sweden","Japan"],"index":[44,23,37,20,40,43,6,22,24,47],"value":[1195,112,53,51,47,28,26,20,20,19]},"selected":{"id":"1046","type":"Selection"},"selection_policy":{"id":"1045","type":"UnionRenderers"}},"id":"1027","type":"ColumnDataSource"},{"attributes":{},"id":"1034","type":"BasicTickFormatter"},{"attributes":{"callback":null,"start":-0.5},"id":"1004","type":"Range1d"},{"attributes":{"end_angle":{"expr":{"id":"1026","type":"CumSum"},"units":"rad"},"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"radius":{"units":"data","value":0.4},"start_angle":{"expr":{"id":"1025","type":"CumSum"},"units":"rad"},"x":{"value":0},"y":{"value":1}},"id":"1030","type":"Wedge"},{"attributes":{"end_angle":{"expr":{"id":"1026","type":"CumSum"},"units":"rad"},"fill_color":{"field":"color"},"line_color":{"value":"white"},"radius":{"units":"data","value":0.4},"start_angle":{"expr":{"id":"1025","type":"CumSum"},"units":"rad"},"x":{"value":0},"y":{"value":1}},"id":"1029","type":"Wedge"},{"attributes":{},"id":"1018","type":"BasicTicker"},{"attributes":{"callback":null,"tooltips":"@country: @value"},"id":"1022","type":"HoverTool"},{"attributes":{"field":"angle","include_zero":true},"id":"1025","type":"CumSum"},{"attributes":{"label":{"field":"country"},"renderers":[{"id":"1031","type":"GlyphRenderer"}]},"id":"1039","type":"LegendItem"},{"attributes":{"below":[{"id":"1012","type":"LinearAxis"}],"left":[{"id":"1017","type":"LinearAxis"}],"plot_height":350,"renderers":[{"id":"1012","type":"LinearAxis"},{"id":"1016","type":"Grid"},{"id":"1017","type":"LinearAxis"},{"id":"1021","type":"Grid"},{"id":"1038","type":"Legend"},{"id":"1031","type":"GlyphRenderer"}],"title":{"id":"1001","type":"Title"},"toolbar":{"id":"1023","type":"Toolbar"},"toolbar_location":null,"x_range":{"id":"1004","type":"Range1d"},"x_scale":{"id":"1008","type":"LinearScale"},"y_range":{"id":"1006","type":"DataRange1d"},"y_scale":{"id":"1010","type":"LinearScale"}},"id":"1002","subtype":"Figure","type":"Plot"},{"attributes":{"grid_line_color":{"value":null},"plot":{"id":"1002","subtype":"Figure","type":"Plot"},"ticker":{"id":"1013","type":"BasicTicker"}},"id":"1016","type":"Grid"},{"attributes":{"dimension":1,"grid_line_color":{"value":null},"plot":{"id":"1002","subtype":"Figure","type":"Plot"},"ticker":{"id":"1018","type":"BasicTicker"}},"id":"1021","type":"Grid"},{"attributes":{},"id":"1036","type":"BasicTickFormatter"},{"attributes":{"plot":null,"text":"Number of Papers Published by Countries in Clinical NLP"},"id":"1001","type":"Title"},{"attributes":{"data_source":{"id":"1027","type":"ColumnDataSource"},"glyph":{"id":"1029","type":"Wedge"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1030","type":"Wedge"},"selection_glyph":null,"view":{"id":"1032","type":"CDSView"}},"id":"1031","type":"GlyphRenderer"},{"attributes":{},"id":"1045","type":"UnionRenderers"},{"attributes":{},"id":"1046","type":"Selection"},{"attributes":{"axis_label":null,"formatter":{"id":"1036","type":"BasicTickFormatter"},"plot":{"id":"1002","subtype":"Figure","type":"Plot"},"ticker":{"id":"1018","type":"BasicTicker"},"visible":false},"id":"1017","type":"LinearAxis"},{"attributes":{"source":{"id":"1027","type":"ColumnDataSource"}},"id":"1032","type":"CDSView"},{"attributes":{"field":"angle"},"id":"1026","type":"CumSum"}],"root_ids":["1002"]},"title":"Bokeh Application","version":"1.0.4"}}';
          var render_items = [{"docid":"0eebe9be-af5c-4226-ab88-6c52fd6c66ad","roots":{"1002":"325e65cd-6bb6-473b-ab37-d125f950a2d0"}}];
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
