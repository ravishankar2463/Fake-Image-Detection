// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
  var data = google.visualization.arrayToDataTable([
  ['Task', 'Hours per Day'],
  ['Confident', 8],
  ['Not Confident', 2],
]);

  // Optional; add a title and set the width and height of the chart
  var options = {'title':'Confidence In The Analysis',
                 'width':550, 
                 'height':400,
                 'colors':['green','red'],
                 animation: {
                    duration: 1000,
                    easing: 'in',
                    startup: true
                  }
                };

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
  var percent = 0;
  // start the animation loop
  var handler = setInterval(function() {
    // values increment
    percent += 1;
    // apply new values
    data.setValue(0, 1, percent);
    data.setValue(1, 1, 100 - percent);
    // update the pie
    chart.draw(data, options);
    // check if we have reached the desired value
    if (percent >= 90)
      // stop the loop
      clearInterval(handler);
  }, 15);
}