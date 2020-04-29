eel.start_file()
function generateQRCode() {
	eel.ELA()
	document.getElementById("qr").src = "temp/temp.jpg"
	document.getElementById("ela").src = "temp/diff.jpg"
}

function sendresults()	{
	window.location.href = "results.html";
	eel.generateResults()
}


function dispresults(){
    var JSONdata = JSON.parse(data);
    console.log(JSONdata[0].class);
    console.log(JSONdata[0].prob);
    if (JSONdata[0].class == "0"){
	document.getElementById("res").innerText = "Fake"
	} else {
	document.getElementById("res").innerText = "Real"
	}
	google.charts.load('current', {'packages':['corechart']});
	google.charts.setOnLoadCallback(drawChart);
	// Draw the chart and set the chart values
	function drawChart() {
	  var data = google.visualization.arrayToDataTable([
	  ['Label', 'Value'],
	  ['Confident',	JSONdata[0].prob*100],
	  ['Doubtful', 100- JSONdata[0].prob*100],
	]);

	  // Optional; add a title and set the width and height of the chart
	  var options = {'title':'Confidence In The Analysis',
	                 'width':550, 
	                 'height':400,
	                 'colors':['#00FF00','#DC143C']
	                };

	  // Display the chart inside the <div> element with id="piechart"
	  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
	  chart.draw(data, options);}
	//   var percent = 0;
	//   // start the animation loop
	//   var handler = setInterval(function() {
	//     // values increment
	//     percent += 1;
	//     // apply new values
	//     data.setValue(0, 1, percent);
	//     data.setValue(1, 1, 100 - percent);
	//     // update the pie
	//     chart.draw(data, options);
	//     // check if we have reached the desired value
	//     if (percent >= JSONdata[0].prob*100)
	//       // stop the loop
	//       clearInterval(handler);
	//   }, 15);
	// }
}

