    function Countdown(then, id) {
     
	    this.then = then;
            this.id = id;
	    
	    function setElement(id, value) {
		    value = (value < 10) ? "0" + value: + value;
		    getElementById(id).innerHTML = value;
	    }
	    
	    function countdown() {
		    now  		  = new Date();
		    diff		  = new Date(this.then - now);
		    
		    seconds_left  = Math.floor(diff.valueOf() / 1000);
	    
		    seconds  = Math.floor(seconds_left / 1) % 60;
		    minutes  = Math.floor(seconds_left / 60) % 60;
		    hours    = Math.floor(seconds_left / 3600) % 24;
		    days     = Math.floor(seconds_left / 86400) % 86400;
		    
		    setElement('countdown-days', days);
		    setElement('countdown-hours', hours);
		    setElement('countdown-minutes', minutes);
		    setElement('countdown-seconds', seconds);
                    console.debug(days);
                    console.debug(hours);
		    
		    countdown.timer = setTimeout(countdown, 1000);
	    }
	    
		    
	    function start() {
		    this.timer = setTimeout(countdown, 1000);
	    }
	    
	    start(then);	
     }
