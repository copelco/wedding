// usage: log('inside coolFunc', this, arguments);
// paulirish.com/2009/log-a-lightweight-wrapper-for-consolelog/
window.log = function f(){ log.history = log.history || []; log.history.push(arguments); if(this.console) { var args = arguments, newarr; try { args.callee = f.caller } catch(e) {}; newarr = [].slice.call(args); if (typeof console.log === 'object') log.apply.call(console.log, console, newarr); else console.log.apply(console, newarr);}};

// make it safe to use console.log always
(function(a){function b(){}for(var c="assert,count,debug,dir,dirxml,error,exception,group,groupCollapsed,groupEnd,info,log,markTimeline,profile,profileEnd,time,timeEnd,trace,warn".split(","),d;!!(d=c.pop());){a[d]=a[d]||b;}})
(function(){try{console.log();return window.console;}catch(a){return (window.console={});}}());


// place any jQuery/helper plugins in here, instead of separate, slower script files.


function toggle_regrets() {
    var party_select = $('#id_party_size');
    var date_select = $('#id_arrival_date');
    var date_wrapper = $(date_select).parent().parent();
    var size = $(party_select).val();
    if (size == 0) {
        date_wrapper.hide()
        date_select.val('');
    } else {
        date_wrapper.show();
        date_select.val('2012-11-03');
    }
}


(function() {
    $('#id_party_size').change(toggle_regrets);
    toggle_regrets();
})(jQuery);
