<template>
  <div>
    <h5>Network of Cooperation Between Cities</h5>
    <canvas id="network" width="1000" height="600"></canvas>
  </div>
</template>

<script>
export default {
  mounted() {

    // Some global variables, relatin to infrastructure
    var canvas = d3.select("#network")
    var width = canvas.attr("width")
    var height = canvas.attr("height")
    var ctx = canvas.node().getContext("2d")
    var r = 10
    var color = d3.scaleOrdinal(d3.schemeCategory20)
    var simulation = d3.forceSimulation()
      .force("x", d3.forceX(width/2))
      .force("y", d3.forceY(height/2))
      .force("collide", d3.forceCollide(r))
      .force("charge", d3.forceManyBody()
        .strength(-200))
      .force("link", d3.forceLink()
        .id(function (d) { return d.name })
        .strength(0.2))

    d3.json("./cities.json", function (err, graph) {
      if (err) throw err

      simulation.nodes(graph.nodes)
      simulation.force("link")
        .links(graph.links)
      simulation.on("tick", update)

      canvas
        .call(d3.drag()
          .container(canvas.node())
          .subject(dragsubject)
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended))

      function update() {
        ctx.clearRect(0, 0, width, height)

        ctx.beginPath()
        ctx.globalAlpha = 0.5
        graph.links.forEach(drawLink)
        ctx.stroke()


        ctx.globalAlpha = 1.0
        graph.nodes.forEach(drawNode)
      }

      function dragsubject() {
        return simulation.find(d3.event.x, d3.event.y)
      }

    })

    function dragstarted() {
      if (!d3.event.active) simulation.alphaTarget(0.3).restart()
      d3.event.subject.fx = d3.event.subject.x
      d3.event.subject.fy = d3.event.subject.y
      console.log(d3.event.subject)
    }

    function dragged() {
      d3.event.subject.fx = d3.event.x
      d3.event.subject.fy = d3.event.y
    }

    function dragended() {
      if (!d3.event.active) simulation.alphaTarget(0)
      d3.event.subject.fx = null
      d3.event.subject.fy = null
    }

    function drawNode(d) {
      const SCALE_FACTOR = 3
      ctx.beginPath()
      ctx.fillStyle = color(d.party)
      ctx.moveTo(d.x, d.y)
      ctx.arc(d.x, d.y, Math.log2(d.num_pub)*SCALE_FACTOR, 0, Math.PI*2)
      ctx.fill()

      var style = ctx.fillStyle
      ctx.fillStyle = "#FFA500"
      ctx.font = "bold 15px Arial";
      ctx.fillText(d.name, d.x, d.y);
      ctx.fillStyle = style
    }

    function drawLink(l) {
      ctx.moveTo(l.source.x, l.source.y)
      ctx.lineTo(l.target.x, l.target.y)
    }
  }
}
</script>
