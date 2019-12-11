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
	context.fillRect(0, 0, canvas.width, canvas.height);
	// paint stroke colour
	context.color = "white";
	context.lineWidth = 15;
	context.lineJoin = context.lineCap = "round";

	clearCanvas();
	  
  	canvas.addEventListener( "mousemove",
	function(e) { 
	  lastMouse.x = Mouse.x;
	  lastMouse.y = Mouse.y;
	  Mouse.x = e.pageX - this.offsetLeft;
	  Mouse.y = e.pageY - this.offsetTop;
	  }, false);
	/** EVENT LISTENERS */  
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
  	/* CLEAR BUTTON */
  	function clearCanvas() {
	var clearButton = $("#clearButton");
	clearButton.on("click", function() {
	  context.clearRect(0, 0, 280, 280);
	  context.fillStyle = "black";
	  context.fillRect(0, 0, canvas.width, canvas.height);
  	});
  	}})();
	