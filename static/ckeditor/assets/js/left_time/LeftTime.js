/*
    Please don't CHANGE the IDes! Declare them in your HTML code. you have to declare timespan (this.timespan)
    to calculate the time need to be done.
    
    Also need `JQuery` and `Toastify JS`
*/


class LeftTime {
    
    timespan = 0;
    left_hour = $('#left_hour');
    left_minute = $('#left_minute');
    left_second = $('#left_second');
    text = 'زمان شما به پایان رسیده است!';
    time = 3;
    h = null;
    min = null;
    sec = null;
    
    constructor(timespan, showTime, text) {
        this.timespan = timespan;
        if (showTime)
            this.time = showTime;
        if (text)
            this.text = text;
    }
    
    run() {
        if (this.timespan) {
            this.h = Math.floor(this.timespan / 3600);
            this.min = this.timespan % 3600 === 0 ? 0 : Math.floor((this.timespan - (this.h * 3600)) / 60);
            this.sec = this.timespan % 60 === 0 ? 0 : this.timespan - (this.h * 3600) - (this.min * 60);
            this.timespan--;
            this.left_hour.html(this.h);
            this.left_minute.html(this.min);
            this.left_second.html(this.sec);
        } else if (this.sec === 1) {
            this.left_second.html(0);
            this.sec = 0;
            Toastify({
                text: this.text,
                duration: this.time * 1000,
                newWindow: true,
                close: true,
                gravity: 'top', // `top` or `bottom`
                position: 'center', // `left`, `center` or `right`
                stopOnFocus: true, // Prevents dismissing of toast on hover
                style: {
                    background: 'rgb(108,95,252)',
                },
            }).showToast();
        }
    }
}
