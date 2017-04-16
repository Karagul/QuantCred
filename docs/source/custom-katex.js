window.onload = function() {
  var inlineMath = document.getElementsByClassName("math inline");
  for (var i=0; i < inlineMath.length; i++) {
    var texText = inlineMath[i].firstChild
    katex.render(texText.data, inlineMath[i])
  }
  var displayMath = document.getElementsByClassName("math display");
  for (var i=0; i < displayMath.length; i++) {
    var texText = displayMath[i].firstChild
    katex.render(texText.data, displayMath[i], {displayMode: true})
  }
}
