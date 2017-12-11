// var main_page = ["Dashboard", "Settings", "Logout"];

// var course_page = ["Course Notes", "Assignment", "Inbox", "Logout"];

 var start = 100;
var mid = 145;
var end = 250;
var width = 20;
var leftX = start;
var leftY = start;
var rightX = mid - (width / 2.7);
var rightY = mid + (width / 2.7);
var animationSpeed = 20;

var ctx = document.getElementsByTagName('canvas')[0].getContext('2d');
ctx.lineWidth = width;
ctx.strokeStyle = 'rgba(0, 150, 0, 1)';

for (i = start; i < mid; i++) {
  var drawLeft = window.setTimeout(function() {
    ctx.beginPath();
    ctx.moveTo(start, start);
    ctx.lineTo(leftX, leftY);
    ctx.stroke();
    leftX++;
    leftY++;
  }, 1 + (i * animationSpeed) / 3);
}

for (i = mid; i < end; i++) {
  var drawRight = window.setTimeout(function() {
    ctx.beginPath();
    ctx.moveTo(leftX, leftY);
    ctx.lineTo(rightX, rightY);
    ctx.stroke();
    rightX++;
    rightY--;
  }, 1 + (i * animationSpeed) / 3);
}

//js for file upload




