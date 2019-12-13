// https://www.w3schools.com/
// Adapted from https://www.youtube.com/watch?v=f6Bf3gl4hWY
(function() {
	var canvas = document.querySelector("#canvas");
	var context = canvas.getContext("2d");
	// Set canvas dimensions
	canvas.width = 280;
	canvas.height = 280;
	// set mouse
	var Mouse = { x: 0, y: 0 };
	var lastMouse = { x: 0, y: 0 };
	// canvas colour
	context.fillStyle = "black";
	// Draws a filled rectangle in black (default)
	context.fillRect(0, 0, canvas.width, canvas.height);
	// paint stroke colour
	context.color = "white";
	// stroke size
	context.lineWidth = 15;
	// Creates a rounded edge when two lines meet and draws a line with rounded end caps
	context.lineJoin = context.lineCap = "round";
	
	clearCanvas();
	  
	/** EVENT LISTENERS */  
  	canvas.addEventListener( "mousemove",
	function(e) { 	
	  lastMouse.x = Mouse.x;
	  lastMouse.y = Mouse.y;
	  Mouse.x = e.pageX - this.offsetLeft;
	  Mouse.y = e.pageY - this.offsetTop;
	  }, false);
  	canvas.addEventListener("mousedown",
	function(e) {
	  canvas.addEventListener("mousemove", onPaint, false);
  	}, false);
  	canvas.addEventListener("mouseup",
	function() {
	  canvas.removeEventListener("mousemove", onPaint, false);
  	}, false);
	  
	/** PAINT FUNCTION */  
  	var onPaint = function() {
	context.lineWidth = context.lineWidth;
	context.lineJoin = "round";
	context.lineCap = "round";
	context.strokeStyle = context.color;
	context.beginPath();
	context.moveTo(lastMouse.x, lastMouse.y);
	context.lineTo(Mouse.x, Mouse.y);
	context.closePath();
	context.stroke();
  	};
  	/* CLEAR CANVAS FUNCTION */
  	function clearCanvas() {
	var clearButton = $("#clearButton");
	clearButton.on("click", function() {
	  context.clearRect(0, 0, 280, 280);
	  context.fillStyle = "black";
	  context.fillRect(0, 0, canvas.width, canvas.height);
  	});
  	}})();
	