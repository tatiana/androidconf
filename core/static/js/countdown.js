function Countdown(start, stop) {
    function changeStyle(elementId, property, value) {
        document.getElementById(elementId).style[property] = value;
    }
    function twoDigits(n) {
        return (n < 10) ? "0" + n : n;
    }

    function getDifference(now, then) {
        diff = new Date(then - now);
        seconds_left = Math.floor(diff.valueOf() / 1000);
        return seconds_left;
    }

    function updateCountdown(start, stop, now) {
        seconds_left_to_start = getDifference(now, start);
        seconds_left_to_finish = getDifference(now, stop);
        if (seconds_left_to_finish <= 0) {
            changeStyle('conference-running', 'display', 'none');
            changeStyle('conference-finished', 'display', 'block');
            changeStyle('countdown', 'display', 'none');
        }
        else if (seconds_left_to_start <= 0) {
            changeStyle('conference-running', 'display', 'block');
            changeStyle('conference-finished', 'display', 'none');
            changeStyle('countdown', 'display', 'none');
        }
        else {
            seconds = twoDigits(seconds_left % 60);
            minutes = twoDigits(Math.floor(seconds_left_to_start / 60) % 60);
            hours = twoDigits(Math.floor(seconds_left_to_start / 3600) % 24);
            days = twoDigits(Math.floor(seconds_left_to_start / 86400) % 86400);

            document.getElementById('countdown-days').innerHTML = days;
            document.getElementById('countdown-hours').innerHTML = hours;
            document.getElementById('countdown-minutes').innerHTML = minutes;
            document.getElementById('countdown-seconds').innerHTML = seconds;

            changeStyle('conference-running', 'display', 'none');
            changeStyle('conference-finished', 'display', 'none');
            changeStyle('countdown', 'display', 'block');
        }
    }
    updateCountdown(start, stop, new Date());
}
startDateAsString = 'new Date("Nov 26 2011 08:00:00 GMT-2")';
endDateAsString = 'new Date("Nov 26 2011 19:00:00 GMT-2")';
setInterval('Countdown(' + startDateAsString + ', ' + endDateAsString + ');',
            1000);
