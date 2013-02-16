

function blowCloud() {

	'use strict';
	
	var cloud;
	cloud = document.createElement('div');
	cloud.setAttribute('class', 'cloud');

	var path = 50, // Size of the path to move.
    	velocity = 0.005+Math.random()*0.005,
    	time = path/velocity,
    	way = Math.random()>0.5?'-':'+'; // Choose direction (left or right).

	$(cloud).css({
		left: Math.random()*(window.innerWidth-path-100)+'px', // starting position (-100 for height)
		top: Math.random()*(window.innerHeight-path-100)+'px', // starting position (-100 for width)
		opacity: 0,
	});

	$(cloud).addClass('cloud'+(~~(Math.random()*4)+1));
	
	if (!$("#troposphere")[0])
		$(document.body).prepend("<div id='troposphere'></div>");
	$('#troposphere').append(cloud);

	function precipitate () {
		$(cloud).stop().fadeOut(500, function() {
			$(cloud).remove()
			blowCloud(); // Blow a new one.
		});
	}
	
	$(cloud).animate({opacity: 1}, 1000);
	$(cloud).click(precipitate);
	$(cloud).animate(
		{left: way+'='+path}, time, "linear", precipitate
	);
}

$(document).ready(function () {
	for (var i=0; i<5; i++) {
		blowCloud();
	}
});